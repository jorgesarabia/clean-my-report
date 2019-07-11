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

## To do list
- Poner en un archivo index.html links a los reportes generados.