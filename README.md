
# Sistema Escolar

Este proyecto es una aplicación de escritorio básica para un sistema escolar, implementada en Python utilizando **Tkinter** para la interfaz gráfica de usuario.

## Requisitos

Asegúrate de tener instalado:

- **Python 3.6** o superior
- **Tkinter** (que viene incluido con la mayoría de las distribuciones de Python)

### Instalación de Pillow

Si no tienes Pillow instalado, puedes instalarlo con el siguiente comando o buscar la versión para tu sistema en [Pillow](https://pillow.readthedocs.io/en/stable/installation.html).

```bash
brew install pillow

### Instalación de Python y Tkinter

Si no tienes Python instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).

**Para verificar si tienes Tkinter instalado**, abre un terminal y ejecuta el siguiente comando:

```bash
python3 -m tkinter
```

Si Tkinter está correctamente instalado, verás una pequeña ventana gráfica de prueba.

## Ejecución del Proyecto

Para ejecutar la aplicación, simplemente usa el siguiente comando desde la raíz del proyecto:

```bash
python index.py
```

o puedes utilizar 

```bash
python3 index.py
```

Este comando abrirá la ventana principal de la aplicación donde se puede iniciar sesión con las credenciales predeterminadas.

## Uso de la Aplicación

Al iniciar la aplicación, podrás ver una ventana de inicio de sesión. Usa las siguientes credenciales para acceder:

- **Usuario**: `admin`
- **Contraseña**: `1234`

Si los datos ingresados son correctos, recibirás un mensaje de bienvenida.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura básica:

```
sistema-escolar/
├── src/
│   ├── index.py                  # Archivo principal que ejecuta la aplicación
│   ├── modules/
│       ├── login/
│           ├── Login.py          # Lógica del login y vista
```

## Tecnologías Usadas

- **Python**: Lenguaje de programación principal.
- **Tkinter**: Para la creación de la interfaz gráfica de usuario (GUI).

## Próximas mejoras

- Implementar una funcionalidad para registro de nuevos usuarios.
- Integrar una base de datos para almacenar información de los usuarios.