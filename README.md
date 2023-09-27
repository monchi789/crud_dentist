# **Sistema de Reservas y Control de Tratamientos de Citas API**  
![img.png](images%2Fimg.png)
  
Este es un proyecto de API desarrollado en Python utilizando el framework FastAPI y PostgreSQL como gestor de base de datos.   
El objetivo de esta API es proporcionar un sistema robusto para la gestión de reservas y el control de tratamientos de citas  
en clínicas médicas u otros entornos similares.  
  
## **Autor**  
- **Nombre:** Cristian Monzon Guzman  
- **Correo:** cristian-02-@live.com
- **LinkedIn:** [¡Conéctame en LinkedIn!](https://www.linkedin.com/in/cristian-monzon-guzman/)
  
## Caracteristicas Principales  
- Gestión de citas y reservas de pacientes.  
- Seguimiento de tratamientos médicos.  
- Administración de personal médico y de apoyo.  
- Almacenamiento seguro de datos de pacientes y médicos en una base de datos PostgreSQL.  
  
## **Capturas de Pantalla**  
A continuación, se presenta algunas capturas de pantalla que muestra cómo funciona la API en acción:  
  
![img.png](images/json.png)

  
## **Diagrama de la Base de Datos**  
![crud_dentist.jpg](images%2Fcrud_dentist.jpg)
  
## Instalación  
A continuación, se detallan los pasos para configurar y ejecutar el proyecto en tu entorno local.  
  
1. Clona este repositorio en tu maquina local: <br>
```bash
git clone https://github.com/monchi789/crud_dentist.git
```

2. Crea un entorno virtual (recomendado) e instala las dependencias: 
```bash
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3.  Configura las variables de entorno necesarias, como las credenciales de la base de datos PostgreSQL.
4. Inicia la aplicación:
```bash
uvicorn main:app --reload
```

5. Accede a la API en `http://localhost:8000/docs` en tu navegador o herramienta de cliente API.

## Uso
A continuación, se detallan algunos ejemplos de cómo utilizar la API:
- **Endpoint de Users:** Para crear un usuario, realiza una solicitud POST a `/users` con los datos del usuario
```json
[
    {
    "phone_number": "987675645",
    "password": "$2b$12$.iES7ZhtzeqnRU1uRnCK7OV.gcyDHOHSlNz8UlVuz.0zpMlj6eMcm",
    "first_name": "Cristian",
    "email": "monchi@example.com",
    "username": "monchi789",
    "id": 1,
    "last_name": "Monzon Guzman"
    }
    
]
```
- **Endpoint de Consulta de Pacientes**: Para obtener información de un usuario, realiza una solicitud GET a `/users/{id}` donde `{id}` es el ID del usuario.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

### Resumen de la Licencia

MIT License (MIT)

Derechos de autor (c) [2023] [Cristian Monzon Guzman]

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), para tratar el Software sin restricciones, incluidos, entre otros, los derechos de uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta de copias del Software y para permitir a las personas a las que se les proporcione el Software a hacerlo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, YA SEA EXPRESA O IMPLÍCITA, INCLUYENDO, PERO NO LIMITADO A, LAS GARANTÍAS DE COMERCIABILIDAD, APTITUD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS TITULARES DE LOS DERECHOS DE AUTOR O LOS TITULARES DE PATENTES SERÁN RESPONSABLES POR CUALQUIER RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRA MANERA, DERIVADA DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE.