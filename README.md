MusicWeb
========

Este proyecto almacena toda la información referida a bandas locales con el con el fin de promover sus canciones e historias, compartir su música y más, sin fines de lucro.

Requerimientos
--------------
* django
* django-admin-bootstrapped
* pillow
* django-bootstrap3


Necesitaremos el comando pip para instalar los requerimientos. Para instalarlo:

  En Debian y Ubuntu:
  
  <code>$ sudo apt-get install python-pip</code>
  
  En Fedora:
  
  <code>$ sudo yum install python-pip</code>

También necesitaremos un entorno virtual <code>$ pip install virtualenv</code>

Una vez clonado el repositorio creamos el entorno virtual <code>$ virtualenv venv</code>.

Vamos a la carpeta doc/. Dentro de ella encontraremos un archivo 'requirement.txt' y ejecutamos el comando <code>$ pip install -r requeriments.txt </code>.

Con esto ya deberiamos tener instaladas nuestros requerimientos.


Correr el Servidor
------------------

Estando dentro de nuestro repositorio recién clonado 'MusicWeb/' vamos a la carpeta 'src/' y luego a 'Music/'. Resumido
<code>$ cd src/Music/</code>.
Sincronizamos la base de datos. <code>$ python manage.py syncdb</code> y corremos el servidor <code>$ python manage.py runserver</code>.

Desde cualquier browser (google chrome, firefox, etc) vamos a la url '127.0.0.1:8000' o 'localhost:8000'.
Y ahora ya podemos ver nuestra página web.




