#EXAMEN PARCIAL DICIEMBRE EDA II

En este examen escogí la opción B. 


 - FUNCIÓN __DIVIDIR EN SEGMENTOS__:

En un principio, me aproximé a las solución dividiendo en segmentos los identificadores según si "tipo".
Así se pueden comparar números basándose solo en ciertas partes relevantes de ellos,
siendo lo más cómodo un string del número identificador.


 - FUNCIÓN __CALCULAR SIMILITUD DE SEGMENTOS__:

Después, se calcula la similitud compararndo las dos listas de segmentos y, de manera recursiva,
llamar a la función para que compare los elementos y cada coincidencia la vaya sumando.
Cuando haya recorrido todo el string y haya comparado amabas listas de segmentos,
dividirá las coincidencias entre la longitud de la la lista para así devolver el porcentaje de coincidencias.


 - FUNCIÓN __CLASIFICAR IDENTIFICADOR__:

Es la parte del código que clasifica el identifcador como "similar" o "Nuevo".
Utilizará un número objetivo contra cada número en la lista original
y clasifica si es "similar" a algún número (utilizando el umbral)  o "nuevo". 
la función busca el número que más se parece y si no alcanza el umbral de similitud (determinado por usuario),
se clasifica como nuevo. El umbral controla qué tan parecidos deben de ser los números para considerarse similares.


 - CONFIGURACIÓN INICIAL Y ENTRADA DEL USUSARIO:

Lista original: contiene los identificadores preexistentes. (Esto no es un input)

Tipo de identificador: Se escoge el tipo de identificador a analizar. 
Este es un input y optimiza el código al evitar hacer un bucle para busccar qué tipo de identificador es.

Umbral: Existe la opción de modificar el umbral.
Lo ideal es 0.8 teniendo en cuenta los ejemplos no obstante, ello se puede modificar.


 -  INTERACCIÓN:

Se procesan los números que el usuario ingresa uno por uno y los clasifica.

El ciclo se termina cuando el usuario escribe "salir"

***FIN DEL CÓDIGO


