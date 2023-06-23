Proyecto Appium con Python

1.- Clonar el repositorio

2.- Abrir el proyecto con pycharm

3.- Descagar los requerimientos con el comando (asegurarse que los requerimientos se hayan descargado e instalado correctamente):
	
	pip install -r requirements.txt

4.- Iniciar de manera manual appium

5.- Verificar que se tenga iniciado el emulador de Android, en caso de utilizar un dispositivo físico asegurarse de que esté conectado.
	Nota: Es necesario solo tener el emulador o el dispositivo conectado.

6.- Para correr las pruebas es necesario ejecutar el comando:
	
	pytest TestLogin.py