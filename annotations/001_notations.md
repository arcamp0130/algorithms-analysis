# Noación en los algoritmos

Usamos notación asintótica para denotar la complejidad de un algoritmo; que funcione no significa que sea eficiente.
Se puede medir la velocidad temporal por medio de:
- Crear y ejecutar el algoritmo k veces.
- Medir el tiempo de las k ejecuciones.
- Realizar una gráfica de tendencia.

Existen tres tipos de notación asintóticas:
- **Big O:** Describe el límite superior de complejidad en el peor de los casos.
- **Big Omega:** Describe el límite inferior de complejidad en el mejor de los casos.
- **Big Theta:** Usa ambos límites, superior e inferior, para el mejor y peor de los casos.

Cada ciclo for representa una consulta a la lista, una n para la notación.

```python
for i in range(n):
  something()
```

Al tener p ciclos, se considera que todas las n se multiplican p veces $n^p$

```python
for i in range(n):
  for j in range (n):
    something()

```

## Tipos de complejidad

Existen dos tipos esenciales de complejidad, importantes para saber la verdadera eficiencia de un algoritmo: complejiad temporal y espacial.

Es de suma importancia medir la estabilidad de cualuquier algoritmo, y es por ello que es probable que el algoritmo en cuestión tenga un comportamiento inestable para pequeños conjuntos de datos y se estabilice en grandes conjuntos. Al tomar un punto donde la función no toque las asíntotas, decimos que es un punto n_0 donde el algoritmo se estabiliza.
