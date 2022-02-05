
LIBRERÍA DE NÚMEROS COMPLEJOS

En la librería encontrará las herramientas para llevar a cabo operaciones básicas con números complejos tales como la suma, producto, resta, división, módulo, conjugado, conversión de representaciones polares y cartesianas, y la fase.

Para obtener una copia del proyecto es necesario dirigirse al link del repositorio (https://github.com/leoncico/ProyectCNYT) y descargar todos los archivos publicados.

Pre-requisitos.
Es necesario descargar el entorno de desarrollo PyCharm o el lenguaje de programación Python.
Así mismo obtener una copia de la librería publicada en el repositorio.
Si aún no cuenta con alguno de los anteriores, siga los siguientes pasos:

Descargar e Instalar PyCharm.
1. Dirijase al siguiente link: https://www.jetbrains.com/es-es/pycharm/
2. Haga clic en el botón “Descargar”, es azul y está ubicado en la esquina superior derecha de la web.
3. A continuación elija su sistema operativo; ya sea Windows, macOS o Linux.
4. Haga clic en Descargar, bajo el titular “Community”.
5. Luego se iniciará la descarga y deberá esperar.
6. Una vez completada la descarga, abra el instalador, presione “siguiente” en los pasos posteriores y acepte los términos y condiciones de la aplicación.

Descargar e Instalar Python.
1. Diríjase al siguiente link: https://www.python.org/downloads/
2. Haga clic en el botón “Download Python”, si es necesario elija la versión para macOS o Linux.
3. Luego se iniciará la descarga y deberá esperar.
4. Una vez completada la descarga, abra el instalador, presione “siguiente” en los pasos posteriores y acepte los términos y condiciones de la aplicación.

Instalación.	
Obtener una copia del Proyecto.
1. Dijirase al link del repositorio: https://github.com/leoncico/ProyectCNYT
2. Pulse el botón “Code” de color verde.
3. Seleccione la opción “Download ZIP”
4. Descomprima el .ZIP y ejecute el archivo .py

Ejecutando las pruebas.
Si desea realizar pruebas en la librería abra el archivo “TestLib1.py”, allí podrá probar cada una de las operaciones con los números que desee de la siguiente manera:

Luego del texto “self.assertEqual” se indica la operación a realizar, en los dos siguientes pares de vectores indique los complejos que desee operar (primer valor para real, segundo valor para imaginario), luego de la coma deberá ingresar el resultado que debería obtener), por ejemplo:

    def test_sumacplx(self):
        self.assertEqual(lc.sumacplx((3,-1),(1 , 4)), (4,3))
Donde (3,-1), (1,4) son los complejos que se desean sumar, (4,3) es el resultado a comprobar.

También podrá utilizar el archivo “Libreria1.py” para realizar las operaciones cuando lo necesite.
 
Construido con
PyCharm Community Edition

Autores
David Leonardo Piñeros – Programador.
Luis Daniel Benavides – Tutor y Revisor.
