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

2. Instala las dependencias:
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