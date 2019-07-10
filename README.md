# clean-my-report
Este pequeño script fue creado para automatizar tareas en el reporte del Code Coverage generado por [istanbul](https://istanbul.js.org/).

## El problema
Es más fácil para el equipo de desarrollo ver los reportes en la web y si es que queremos compartir esa información
tal cual la genera el istanbul, queda expuesto el código fuente del proyecto.
Lo que hace este script es copiar en una carpeta los archivos generados por el istanbul, excepto aquellos que
muestran el código fuente del proyecto.
Una vez copiados, analiza cada archivo html con el fin de reemplazar el href="http://<nombre_archivo>**.ts.html**" por href="#".

TODO:
Poner en un archivo index.html links a los reportes generados.
