# clean-my-report
Este pequeño script fue creado para automatizar tareas en el reporte del Code Coverage generado por [Istanbul](https://istanbul.js.org/) en un entorno Angular.

## ¿Por qué fue creado?
El asunto es que es más fácil para el equipo de desarrollo ver los reportes en la web y si es que compartimos esa 
información tal cual la genera el Istanbul, queda expuesto el código fuente del proyecto. 
Esta información viene en los archivos **<nombre_del_script>.ts.html**, por lo que para compartir el reporte 
en un entorno público es mejor suprimir estos archivos.
A su vez, hay que suprimir los links que llevaban a estos archivos que ahora no están disponibles a fin de evitar errores del tipo 404 donde sea que este informe se comparta.
Esta es una tarea muy tediosa incluso para proyectos pequeños, y ese es el motivo de este script.

## Tareas del script
Lo que hace este script es: 
- Copiar en una carpeta los archivos generados por el Istanbul, excepto aquellos que
muestran el código fuente del proyecto.
- Una vez copiados, analiza cada archivo index.html con el fin de reemplazar el href="http://<nombre_archivo>**.ts.html**" por href="#".

# Para probar el script
- Es recomendable clonar el proyecto en un entorno virtual. El script corre con Python 3.

`git clone https://github.com/jorgesarabia/clean-my-report.git`

`source <virtual_env>/bin/activate`

- Configurar el `ORIGIN_PATH` en el archivo [config.py](https://github.com/jorgesarabia/clean-my-report/blob/master/config.py).

`ORIGIN_PATH = "path/al/coverage"`

- Probar el script:

`python main.py`

# To do list
- Poner en un archivo index.html links a los reportes generados.
- Reestructurar el proyecto.