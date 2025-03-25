Application at the service of the global iron comrades community.

## 🤝 Contribuidores
[![Contribuidores](https://contrib.rocks/image?repo=LosCompasDeHierro/lcdh_app)](https://github.com/LosCompasDeHierro/lcdh_app/graphs/contributors)

# Siguientes Pasos
   1. Clona el repositorio: `git clone https://github.com/LosCompasDeHierro/lcdh_app`
   2. Crea un entorno virtual (better practices): `python -m venv lcdh_env`
   3. Activa el entorno virtual: `source lcdh_env/bin/activate`
   4. Instala las dependencias: `pip install -r requirements.txt`
   5. crea las migraciones `python manage.py makemigrations`
   6. Ejecuta las migraciones: `python manage.py migrate`
   7. Inicia el servidor: `python manage.py runserver`


# Estructura del Proyecto y Explicación de Archivos

```
proyecto/
├── src/
│   ├── core/                  # Lógica de negocio
│   ├── infrastructure/        # Implementaciones concretas
│   │   ├── database/
│   │   ├── api/
│   │   └── repositories/
│   ├── application/           # Casos de uso
│   └── shared/                # Utilidades comunes
├── tests/                     # Pruebas
├── docker-compose.yml
├── Dockerfile
├── .env.example
└── package.json
```

russlan
MunecoInfiel1+

charly
MunecoInfiel2+

roger
MunecoInfiel3+

infiel  
MunecoInfiel4+


jazi
MunecoInfiel5+

sudo usermod -aG lcdh roger

sudo mkdir -p /var/www/lcdh
sudo chown root:lcdh /var/www/lcdh
sudo chmod 2775 /var/www/lcdh


1. **lcdh_app/**
   - **models.py**: Define las clases de los modelos que representan las tablas de la base de datos. Por ejemplo, si tienes una clase `User`, esta corresponde a una tabla `User` en la base de datos.
   - **views.py**: Contiene las funciones y clases que manejan las solicitudes HTTP y devuelven respuestas. Por ejemplo, una vista puede obtener datos de los modelos y renderizar una plantilla HTML.
   - **urls.py**: Mapea las URL de la aplicación a las vistas correspondientes. Define las rutas que los usuarios pueden acceder en la aplicación.
   - **admin.py**: Registra los modelos para que aparezcan en la interfaz de administración de Django.

2. **lcdhsite/**
   - **settings.py**: Contiene todas las configuraciones del proyecto, como las bases de datos, aplicaciones instaladas, middleware, configuraciones de seguridad, etc.
   - **urls.py**: Define las rutas principales del proyecto y puede incluir las rutas de las aplicaciones individuales.
   - **wsgi.py** y **asgi.py**: Configuración para desplegar la aplicación en servidores que soportan WSGI/ASGI.

3. **templates/admin/**
   - Contiene archivos HTML que son plantillas para la interfaz de administración de Django.

4. **manage.py**: Es un script de línea de comandos que permite interactuar con el proyecto Django. Se utiliza para tareas administrativas como iniciar el servidor de desarrollo, ejecutar migraciones, crear superusuarios, entre otras.

5. **requirements.txt**: Lista todas las dependencias y paquetes necesarios para que el proyecto funcione. Puedes instalar estas dependencias usando `pip install -r requirements.txt`.

### Diagrama de Estructura
![Diagrama del código](https://assets.digitalocean.com/articles/alligator/boo.svg "a title")
