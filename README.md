# Creación y sincronización de repositorios con Git y Github
Nombre: *Carlos Armando Muñoz Bustamante*
Matricula: *2630017*
Nombre de la práctica: *Creación y sincronización de repositorios con Git y Github*
Objetivo de la práctica: Crear un repositorio local utilizando Git, sincronizarlo con un repositorio remoto en **GitHub** y comprobar el flujo de trabajo en ambos sentidos:
![vincular git y github](https://hermes.dio.me/articles/cover/e2d8683b-5828-4e74-bf69-1a98690d761e.png)

## Descripción del procedimiento realizado
Cree un un repositorio local, un repositorio remoto, vinculé ambos entre sí y fuí realizando commits modificando los archivos en repetidas ocasiones en ambos repositorios.
## Comandos de git utilizados
- Git init: inicializa un repositorio de Git en el directorio actual.
- Git status: muestra el estado actual del proyecto.
- Git add .: agrega **todos los cambios** de los archivos al área staging.
- Git main branch -M main: cambia el nombre de la rama actual a "***main***".
- Git log: muestra el **historial de commits** del proyecto.
- Git commit -m "texto": guarda los cambios preparados en un **commit**.
- Git remote add origin URL_DEL_REPOSITORIO: conecta el repositorio local con un repositorio remoto (por ejemplo, en Github).
- Git remote -v: muestra las **URLs de los repositorios remotos** que están conectados.
- Git fetch: descarga información y cambios del repositorio remoto **sin modificar los archivos locales**.
- Git push -u origin main: sube los commits de la rama **main** al repositorio remoto llamado **origin**.
- Git pull origin main: descarga y aplica cambios de Github.

## Explicación de cómo se creó el repositorio local
El repositorio local se creó dentro del directorio "practica_git_carlos_muñoz" utilizando el comando **git init**. Después, utilicé **git status** para ver los archivos que estaban en *untracked files*. Luego, usando **git add .**, se añadieron todos los archivos (README.md y datos.txt) a la zona de staging. Finalmente, poniendo **git commit -m "descripción"** para crear el primer commit y así termiando la creación del primer commit.
## Explicación de cómo se vinculó el repositorio local con Github
Primero, cree un repositorio público en Github. Una vez creado copié la URL del repositorio para poder vincularlo con el repositorio local. Utilicé el comando **git remote add origin URL_DEL_REPOSITORIO** y pude vincular ambos repositorios. Después, para verificar que el repositorio remoto se haya agregado correctamente utilicé **git remote -v**.

PD: durante el proceso olvidé crear la llave ssh entonces se me complicó vincular el repositorio local con el repositorio remoto entonces tuve que crear una llave ssh.
## Explicación de la sincronización Local → GitHub 
La sincronización del repositorio local al repositorio remoto (Github) se explica mediante commits, cada que se hace un commit en el local está la opción de subirlo a la nube con el comando git push -u origin main para poder editarlo y tener un respaldo del archivo

## Explicación de la sincronización GitHub → Local
Esto es lo mismo que lo anterior pero a la inversa; una vez que se tienen los archivos en Github, se pueden editar, cambiar la información y enviarlo al repositorio local con el mismo comando (git push -u origin main) para trabajar desde el repositorio local

## Descripción de los archivos contenidos en el repositorio
- Archivo llamado "datos.txt": este archivo (hecho en bloc de notas) solo contiene texto simple y texto modificado desde el repositorio local y remoto.
- Archivo llamado "documento_para_practicar.txt": este archivo (creado en bloc de notas) lo hice simplemente para practicar y hacer commits porque es divertido 
- Archivo markdown: este archivo tipo markdown (también creado en bloc de notas) se creó para hacer esta bitácora
## Conclusión
Personalmente, fue una práctica que me gustó mucho porque pude volver a aprender cosas ya vistas en clases. El video recomendado me ayudó mucho para hacer esta práctica. Hubo momentos en los que me desesperé un poco porque no me salían las cosas o porque había errores imprevistos, pero al final pude resolverlos y me quedo con el enorme aprendizaje que adquirí haciendo esta práctica.
:)
