# Playground Final Project: Blog de Eventos
Este proyecto implementa todos los requisitos base de la consigna: En forma individual, crearás una aplicación web estilo blog programada en Python en Django. Esta web tendrá admin, perfiles, registro, páginas y formularios.
- Modelos creados: `Evento` (modelo principal), `Ubicacion`, `Profile`, `Chat` y `Mensaje`.
- Autenticación: Vistas de Login, Registro, Logout y edición de Perfil.
- Vistas: Uso de mínimo 2 CBV y Mixins para gestión del Blog.
- Acceso visible a la vista de "Acerca de mí" donde se contará acerca del dueño de la página manejado en el route `about/`.
- Acceso visible a la vista de blogs que debe alojarse en el route `pages/`.
- Acceso a una pantalla que contendrá las páginas. Al clickear en “Leer más” debe navegar al detalle de la page mediante un route `pages/`.
- Cuando no existe ninguna página se muestra un "No se encontraron eventos."
- Para editar o borrar pages debes estar logueado.


## Descripción
Aplicación web desarrollada en **Python/Django** como proyecto final. 

La app permite a los usuarios registrarse, iniciar sesión, crear y administrar eventos (con título, descripción enriquecida, imagen y fechas), así como editar su perfil personal.

`Proyecto desarrollado en Septiembre/Octubre 2025 con Python, Django + Bootstrap`

## Tecnologías Aplicadas
- Python 3
- Django Framework
- SQLite3
- HTML5 (Herencia de Templates)
- CSS3 / Bootstrap 5
- Git/GitHub (con .gitignore)

## Funcionalidades principales
- **Home** con acceso a sección principal.
- **Sobre Mi** en `/about/`, con información sobre el autor del proyecto.
- **Eventos (BlogEventos)**:
  - **Listado de eventos** en `/pages/` con buscador por nombre.
  - **Detalle de evento** en `/pages/<id>/` mostrando:
    - Nombre, descripción (rich text con CKEditor5), resumen
    - Fechas de inicio y fin
    - Organizador y ubicación
    - Imagen del evento
  - **CRUD de eventos** (solo para usuarios logueados)
    - Crear evento: `/pages/crear/`
    - Editar evento: `/pages/<id>/editar/`
    - Eliminar evento: `/pages/<id>/eliminar/`
- **Ubicaciones (Ubicacion)**:
  - **Listado de ubicaciones** en `/ubicacion/`.
    - Campos: nombre, dirección, ciudad, país.
  - **CRUD de ubicaciones** (solo para usuarios logueados)
    - Crear ubicación: `/ubicacion/crear/`
    - Editar ubicación: `/ubicacion/<id>/editar/`
    - Eliminar ubicación: `/ubicacion/<id>/eliminar/`
- **Usuarios (Accounts)**:
  - **Registro de usuario** con campos `username`, `email`, `password`, `nombre` y `apellido`.
  - **Login y Logout** con redirección a la página de perfil para usuarios ya autenticados.
  - **Perfil de usuario** con: Nombre, Apellido, Email, Avatar (imagen de perfil), Bio y sitio web
  - **Edición de perfil** para modificar los datos de su usuario y de perfil (avatar, bio, website).
  - **Cambio de contraseña** con vistas integradas de Django.
- **Mensajería (Mensajeria)**:
  - Comunicación 1 a 1 entre usuarios registrados.
  - Lista de chats del usuario con últimos mensajes y estado de lectura.
  - Vista de detalle del chat mostrando mensajes enviados y recibidos al estilo “chat”.
  - Mensajes propios muestran si fueron leídos por el otro usuario.
  - Avatar del usuario visible junto a los mensajes recibidos.
  - Posicionamiento automático al último mensaje al abrir un chat.
  - Creación de nuevos chats con cualquier usuario registrado.
- **Admin Django** con gestión de todos los modelos.

## Tecnologías usadas y versiones:
- **Python 3.10.10**
- **Django 5.2.6**
- **django-ckeditor-5** (para texto enriquecido)
- **Pillow 11.3.0** (para manejo de imágenes)
- **Bootstrap 5.3.7** (para estilos en templates)

## Estructura básica del proyecto
```
proyecto_final/
├── accounts/ # App de Gestión de usuarios
├── blogeventos/ # App principal: eventos y ubicaciones
├── mensajeria/ # App de Chat
├── templates/ # Template para herencia desde base.html
├── static/ # Archivos estáticos (CSS, imágenes fijas)
├── media/ # Archivos subidos por usuarios (no incluida en el repo)
├── db.sqlite3 # Base de datos local (no incluida en el repo)
├── requirements.txt # todas las librerías y/o paquetes con sus versiones para que el proyecto funcione correctamente
└── README.md
```

## Instalación y ejecución
1. Clonar el repositorio:
```
   git clone https://github.com/ygh86/proyectoFinal_Hermida
   cd proyectoFinal_Hermida
```

2. Crear y activar entorno virtual:
```
python -m venv venv
# Windows
.\.venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Instalar dependencias:
```
pip install -r requirements.txt
```

4. Crear la base de datos y aplicar migraciones:
```
python manage.py migrate
python manage.py createsuperuser  # crear usuario admin
```

5. Ejecutar el servidor:
```
python manage.py runserver
```

6. Acceder a la app en:
```
http://127.0.0.1:8000/
```

## Usuario de prueba
Para registrarte ingresar directamente en `/accounts/registro/` O usar el admin en `/admin/` para crear usuarios.

## Video de demostración
Acceso al video de muestra -> https://drive.google.com/file/d/1tx6twPSrGeJpsjKncoNdPs2tmIUJQg0y/view?usp=sharing

## Licencia
Proyecto académico – uso educativo.
