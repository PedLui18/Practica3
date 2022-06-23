# Practica3

Prueba Automatizada para la pagina Web de Epic Games

Link del documento Low Test Case : https://docs.google.com/document/d/1CPynsAVMaSldz8vySlryF30knSBwtScoA32rAyxyN-U/edit?usp=sharing
Para iniciar el proyecto es necesario contar con una conexion estable a internet y contar con el navegador de Chrome

Pasos:
1) Tener instalado Python a su ultima version
2) Para la instalacion de pip ingresamos al siguiente link https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/
5) Realizar la instalacion de Selenium mediante el comando "pip install -U selenium" 
6) Para continuar con el proyecto es necesario saber la version de nuestro Chrome para esto ingresamos a Chrome en la parte superior derecha  se encuentran un icono con tres puntos,hacer click seleccionar la opcion de ayuda, la cuak se encuentra cerca al final del menu desplegable, hacer click, seleccionar la opcion de Informacion de Google Chrome, se abrira una ventana mostrando la version de nuestro navegador
12) Luego de saber nuestra version de Chrome necesitamos ir a la pagina de:"https://chromedriver.chromium.org/downloads"
13) Seleccionamos la version que se adapte a nuestra version de navegador, en mi caso selecciona la version 102 
14) Al seleccionar la version se nos mostrara los archivos que se pueden descargar, escoger el que sea para el sistema operativo que se este utilizando, en mi caso se usar la version para windows
15) El archivo que se selecciono sera un "rar" es necesario descomprimirlo haciendo click derecho y seleccionando la opcion de "descomprimir en "ejemplo\"" 
16) Realizar el paso anterior nos creara una carpeta con el contenido del rar, el cual sera una ejecutable llamado "chromedriver"
17) Copiamos la ruta en la cual esta nuestro archivo, ejemplo: 'C:\\Users\\Pedro\\Downloads\\chromedriver\\chromedriver.exe' 
18) Abrimos el IDE visual code para comenzar a trabajar
19) abrimos el archivo QA_EpicGames.py
20) buscar dentro el codigo la variable "driver_path = ", añadimos la ruta la donde se encuentra el ejecutable que descargamos anteriormente
21) antes de realizar la ejecucion del archivo abrimos una nueva terminal haciendo click opcion de terminal en el menu de opciones visual code, en el menu despleagable seleccionames la opcion de nueva terminal
22) En la terminal de comandos ingresamos los siguientes comandos: pip3 install -U selenium,
pip3 install webdriver-manager 
23) Para poder ejecutar el archivo hacemos click derecho en alguna de las linea de codigo dentro del editor y seleccionamos la opcion de ejecutar el archivo python en terminal

24) Se ejecutara el archivo "QA_EpicGames.py" esto es lo que sucedera:
25) Se abrira el navegador google chrome 
26) Se mostrara la pagina inicial de Epic Games 
27) Se mostrara una lista de opciones disponibles para iniciar sesion
28) Seleccionara la primera opcion: Iniciar Sesion con Epic Games 
29) Se mostrara un formulario con los campos de correo electronico y contraseña
30) Rellenara los campos con los datos ya dados en el archivo python
31) Ubicara el boton de Iniciar Sesion Ahora y se hara click
35) Se mostrara un captcha, donde esperara un tiempo, luego hara click en el icono de cerrar
38) se imprimira en la terminal un mensaje 

Estudiante Pedro Luis Tarqui Roman
