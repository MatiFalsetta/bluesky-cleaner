# 🦋 Bluesky Like Cleaner

Una herramienta en Python para eliminar todos los likes de tu cuenta de Bluesky usando la API oficial de ATProto.

## ✨ Características

- 🔐 Autenticación segura con la API oficial de Bluesky
- 📊 Muestra estadísticas de tus likes antes de eliminar
- 🔄 Progreso en tiempo real con contador
- ⚠️ Confirmación de seguridad antes de proceder
- 🛡️ Control de errores y rate limiting
- ⏸️ Posibilidad de interrumpir el proceso en cualquier momento

## 📋 Requisitos

- Python 3.10 o superior
- Una cuenta de Bluesky
- Acceso a internet

## 🚀 Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/MatiFalsetta/bluesky-cleaner
cd bluesky-cleaner
```

2. Crear y activar el entorno virtual (Recomendado)
```bash
python -m venv env
.\env\Scripts\Activate.ps1
```

3. Instala las dependencias:
```bash
pip install atproto
```

## 💻 Uso

1. Ejecuta el script:
```bash
python borrar_likes.py
```

2. Ingresa tu handle de Bluesky (ej: `usuario.bsky.social`)
3. Ingresa tu contraseña
4. Revisa las estadísticas mostradas
5. Confirma si quieres proceder con la eliminación

## 💻 Uso

1. **Crear una contraseña de la aplicación** (Obligatorio):
   - Acceder a [https://bsky.app/settings/app-passwords](https://bsky.app/settings/app-passwords)
   - Agregue una nueva contraseña de aplicación para este script con un nombre único
   - No es necesario marcar la casilla de permitir el acceso a tus mensajes directos
   - Guardar la contraseña generada con formato xxxx-xxxx-xxxx-xxxx (la necesitará en el paso 3)

2. Ejecutar el script:
```bash
python delete_likes.py
```

3. Introducir el nombre de usuario de Bluesky (p. ej., `user.bsky.social`)
4. Introducir la **contraseña de la aplicación** (no la contraseña de la cuenta habitual)
5. Revisar las estadísticas mostradas
6. Confirmar si se desea continuar con la eliminación

## 🗑️ Desinstalación

Para eliminar completamente la herramienta del sistema:

1. Borra la carpeta del repositorio:
```bash
# Navega al directorio principal donde clonaste el repositorio
cd ..
# Borra toda la carpeta bluesky-cleaner
rm -rf bluesky-cleaner
```

**Nota**: Esto eliminará permanentemente todos los archivos, incluyendo el script y los registros. Asegúrate de no necesitar ningún archivo de la carpeta antes de borrarla.

## ⚠️ Advertencias importantes

- **Esta acción es IRREVERSIBLE**: Una vez eliminados, los likes no se pueden recuperar
- **Proceso lento**: Con las pausas de seguridad, eliminar miles de likes puede tomar tiempo
- **Requiere credenciales**: Necesitas tu usuario y contraseña de Bluesky

## 🔧 Cómo funciona

1. **Autenticación**: Se conecta a Bluesky usando el SDK oficial de ATProto
2. **Obtención**: Usa `com.atproto.repo.list_records` para obtener todos tus registros de likes
3. **Eliminación**: Elimina cada registro usando `com.atproto.repo.delete_record`
4. **Progreso**: Muestra estadísticas en tiempo real y maneja errores

## 🤝 Contribuir

Las contribuciones son bienvenidas! Si encuentras un bug o tienes una mejora:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## ⚡ FAQ

**¿Es seguro usar mis credenciales?**
Sí, el script usa la biblioteca oficial de ATProto y no almacena tus credenciales.

**¿Puedo interrumpir el proceso?**
Sí, puedes usar Ctrl+C en cualquier momento para detener la ejecución.

**¿Afecta a los posts originales?**
No, solo elimina tus registros de likes, no los posts originales de otros usuarios.

## 🙋‍♂️ Soporte

Si tienes problemas o preguntas, abre un [issue](https://github.com/MatiFalsetta/bluesky-cleaner/issues) en este repositorio.

---

⭐ Si este proyecto te fue útil, ¡dale una estrella!