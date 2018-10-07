## ReplaceSpeed - Clase que te permite buscar y remplazar archivos de forma recursiva

Esta clase fue pensada para automatizar la busqueda y remplazo de recursos otimizados recomendados por **PageSpeed Insights** en nuestro sito web.
Pero puede utilizarse para buscar y remplazar recursivamente desde una carpeta origen a otras detino

###Como funciona:

Buscar archivos de forma recursiva en en muchos directorios destino y lo remplaza por archivos optimizados de una carpeta origen

###Uso:

```python
from replacespeed import ReplaceSpeed

r = ReplaceSpeed(
    optimized_dir='C:\\Users\\joseR\\Downloads\\optimized_contents)',
    find_dirs = ['D:\\develop\workspace\\web\\dist', 'D:\\develop\\workspace\\web\\public\\media'],
    exclude_dirs = ['src']
)

r.apply()
```

