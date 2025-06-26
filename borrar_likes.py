#!/usr/bin/env python3
"""
borrar_likes.py - Elimina todos los likes de tu cuenta de Bluesky

Este script utiliza la API oficial de Bluesky (ATProto) para:
1. Obtener todos los posts que has dado like
2. Eliminar cada like de forma individual
3. Mostrar progreso en tiempo real

Requiere: pip install atproto
"""

import time
import sys
from typing import List, Dict, Any
from atproto import Client, models

def configurar_cliente() -> Client:
    """
    Configura y autentica el cliente de Bluesky
    """
    print("🔐 Configurando conexión a Bluesky...")
    
    # Solicitar credenciales
    handle = input("Ingresa tu handle de Bluesky (ej: usuario.bsky.social): ").strip()
    password = input("Ingresa tu contraseña: ").strip()
    
    try:
        client = Client()
        client.login(handle, password)
        print(f"✅ Autenticado exitosamente como @{handle}")
        return client
    except Exception as e:
        print(f"❌ Error de autenticación: {e}")
        print("Verifica tu handle y contraseña.")
        sys.exit(1)

def obtener_todos_los_likes(client: Client) -> List[Dict[str, Any]]:
    """
    Obtiene todos los registros de likes del usuario (no los posts, sino los registros de like)
    """
    print("\n📋 Obteniendo registros de likes...")
    
    todos_los_likes = []
    cursor = None
    
    try:
        while True:
            # Usar listRecords para obtener los registros de likes directamente
            params = {
                'repo': client.me.did,
                'collection': 'app.bsky.feed.like',  # Colección de likes
                'limit': 100  # Máximo permitido por la API
            }
            
            if cursor:
                params['cursor'] = cursor
            
            response = client.com.atproto.repo.list_records(params=params)
            
            if not response.records:
                break
                
            todos_los_likes.extend(response.records)
            print(f"📦 Obtenidos {len(todos_los_likes)} registros de likes hasta ahora...")
            
            # Verificar si hay más páginas
            if hasattr(response, 'cursor') and response.cursor:
                cursor = response.cursor
            else:
                break
                
            # Pequeña pausa para no sobrecargar la API
            time.sleep(0.1)
            
    except Exception as e:
        print(f"❌ Error obteniendo registros de likes: {e}")
        return todos_los_likes
    
    print(f"✅ Total de registros de likes encontrados: {len(todos_los_likes)}")
    return todos_los_likes

def eliminar_likes(client: Client, likes: List[Dict[str, Any]]) -> None:
    """
    Elimina todos los registros de likes de la lista
    """
    if not likes:
        print("ℹ️  No hay likes para eliminar.")
        return
    
    print(f"\n🗑️  Iniciando eliminación de {len(likes)} registros de likes...")
    
    # Confirmar acción
    confirmacion = input(f"⚠️  ¿Estás seguro de que quieres eliminar {len(likes)} likes? (s/N): ").strip().lower()
    if confirmacion not in ['s', 'si', 'sí', 'y', 'yes']:
        print("❌ Cancelado por el usuario.")
        return
    
    eliminados = 0
    errores = 0
    
    for i, like_record in enumerate(likes, 1):
        try:
            # Extraer la rkey del URI del registro de like
            rkey = like_record.uri.split('/')[-1]
            
            # Usar la sintaxis correcta para delete_record
            from atproto import models
            
            delete_data = models.ComAtprotoRepoDeleteRecord.Data(
                repo=client.me.did,
                collection='app.bsky.feed.like',
                rkey=rkey
            )
            
            client.com.atproto.repo.delete_record(data=delete_data)
            eliminados += 1
            
            # Mostrar progreso
            if i % 10 == 0 or i == len(likes):
                porcentaje = (i / len(likes)) * 100
                print(f"🔄 Progreso: {eliminados} eliminados, {errores} errores ({porcentaje:.1f}%)")
            
            # Pausa para evitar rate limiting
            time.sleep(0.2)
            
        except Exception as e:
            errores += 1
            print(f"⚠️  Error eliminando like #{i}: {e}")
            
            # Si hay muchos errores consecutivos, preguntar si continuar
            if errores > 5 and (errores / i) > 0.1:  # Más del 10% de errores
                continuar = input("❓ Muchos errores. ¿Continuar? (s/N): ").strip().lower()
                if continuar not in ['s', 'si', 'sí', 'y', 'yes']:
                    break
    
    print(f"\n✅ Proceso completado:")
    print(f"   ✓ Likes eliminados: {eliminados}")
    print(f"   ⚠ Errores: {errores}")

def mostrar_estadisticas_previas(likes: List[Dict[str, Any]]) -> None:
    """
    Muestra estadísticas de los registros de likes antes de eliminar
    """
    if not likes:
        return
    
    print(f"\n📊 Estadísticas de tus likes:")
    print(f"   • Total de registros de likes: {len(likes)}")
    
    # Contar likes por fecha aproximada (usando información del registro)
    fechas_recientes = 0
    for like in likes:
        try:
            # Los registros más recientes suelen tener rkeys más altas
            rkey = like.uri.split('/')[-1]
            if rkey and len(rkey) > 10:  # Formato típico de rkey
                fechas_recientes += 1
        except:
            pass
    
    print(f"   • Registros válidos encontrados: {fechas_recientes}")
    print(f"   • Nota: Se eliminarán los registros de likes, no los posts originales")

def main():
    """
    Función principal del programa
    """
    print("🦋 ELIMINADOR DE LIKES DE BLUESKY")
    print("=" * 40)
    print("Este script eliminará TODOS tus likes de Bluesky.")
    print("⚠️  Esta acción NO es reversible.")
    print("=" * 40)
    
    try:
        # Configurar cliente
        client = configurar_cliente()
        
        # Obtener todos los likes
        likes = obtener_todos_los_likes(client)
        
        if not likes:
            print("\n🎉 No tienes likes para eliminar. ¡Tu cuenta ya está limpia!")
            return
        
        # Mostrar estadísticas
        mostrar_estadisticas_previas(likes)
        
        # Eliminar likes
        eliminar_likes(client, likes)
        
        print("\n🎉 ¡Proceso completado! Todos tus likes han sido procesados.")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Proceso interrumpido por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()