# 🚇 Metro CDMX - Búsqueda de Rutas con Grafos (BFS y DFS)

Este repositorio contiene la solución en Python para modelar el mapa del Metro de la Ciudad de México como un **grafo no dirigido**. El objetivo principal es calcular rutas entre estaciones asumiendo un modelo de costo unitario (moverse de una estación a la siguiente cuesta 1 unidad).

## ⚙️ Algoritmos Implementados

Para la búsqueda y cálculo de rutas se implementaron dos algoritmos clásicos:
* **BFS (Búsqueda en Anchura):** Encuentra la ruta óptima. Al ser un grafo sin peso, siempre garantiza la ruta más corta (menor número de estaciones).
* **DFS (Búsqueda en Profundidad):** Encuentra una ruta válida explorando hasta el final de una línea antes de intentar otras opciones, lo que sirve para contrastar su eficiencia contra el BFS.

## 📍 Rutas Calculadas

El programa evalúa y muestra los resultados de ambos algoritmos para las siguientes rutas específicas:
1. Cuatro Caminos ➔ Pantitlán
2. Politécnico ➔ Taxqueña
3. Zapata ➔ Oceanía

## 🧮 Sobre el Cálculo de Costo
El modelo utiliza un esquema de **costo unitario**, lo que significa que avanzar de una estación a su estación vecina inmediata tiene un costo exacto de **1**. 

* No se toman en cuenta distancias físicas en kilómetros ni tiempos promedio de traslado.
* No se aplican costos adicionales (penalizaciones) por realizar transbordos entre diferentes líneas.

Debido a que todas las conexiones valen lo mismo, el algoritmo **BFS** es ideal para este caso, ya que garantiza matemáticamente encontrar la ruta óptima que atraviesa el menor número de estaciones.

## Nota sobre el historial de Commits

El código de este proyecto se desarrolló y probó localmente utilizando Visual Studio Code. Una vez que la solución (con los algoritmos BFS y DFS) estuvo completa y funcional, se procedió a inicializar el repositorio en Git y subir el proyecto a GitHub, razón por la cual se refleja un único commit principal.
