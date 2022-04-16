# dataset-1

El link al repositorio es el siguiente: [ GitHub](https://github.com/migueliiin/dataset-1)

Nuestros sitemap y wireframe estan en este link en figma: [ Figma](https://www.figma.com/file/gZkqWm9Caiq4GtCqs90ncU/Prototipo-web?node-id=0%3A1)


### COMO FUNCIONAN LOS MODELOS DE ANÁLISIS DE DATOS
Para la fase del trabajo en la cual estamos trabajando, es de crucial importancia tener claros los conceptos respecto a lo que es un modelo de análisis de datos y la importancia de este.

Podríamos definirlo como aquella disciplina en la cual se interpreta la información de una determinada institución, de tal forma  que se pueda entender qué es lo que sucede y, en consecuencia, se tenga la capacidad de tomar decisiones que sean beneficiosas para los objetivos establecidos.

Para aclararlo bien , podríamos relacionarlo como la representación técnica de un sistema en específico, la cual  es una representación gráfica donde a través de la misma se comunica y transfiere una información por ejemplo mediante gráficos, siempre representando una información muy clara y precisa.

Para este punto, conviene decir que todas las empresas buscan expandirse. siempre quieren maximizar los beneficios. De esta manera, necesitan tener muy controlado el entorno que les rodea y en el que se manejan.
Pues bien, para conseguirlo, es fundamental conocer la importancia del análisis de datos estadísticos, que te serán de utilidad no solamente para conseguir los objetivos que habías planificado, sino también para superarlos constantemente.

Para tener controlado el entorno es clave controlar todo lo relacionado con la gestión de clientes, una planificación estratégica de cara al futuro, tener clara la organización de los datos…

Este modelo de análisis consta de 4 elementos, los cuales sirven para clasificar principalmente los diferentes diagramas. Además estos con clasificados en elementos de escenario ( Casos de uso, textos diagramas de carril o diagramas de actividad), elementos de flujo(diagramas de flujo de datos, diagramas de flujo de control o narrativas de procesamiento),elementos de clases(diagramas de clases,paquetes de análisis) y elementos de comportamiento( diagramas de estado y diagramas de secuencia).

En el lengua que empleamos, Python, los datos se analizan mediante Pandas estos son una  la librería que se usa para el análisis y tratamiento de datos. Nos proporciona la clase Dataframe, la cual permite almacenar los datos en un objeto similar a una tabla de una base de datos.



### Underfitting y Overfitting

Las principales causas al obtener malos resultados en Machine Learning son el overfitting o el underfitting de los datos. Cuando entrenamos nuestro modelo intentamos “hacer encajar” los datos de entrada entre ellos y con la salida. 

Siempre que creamos una máquina de aprendizaje deberemos tener en cuenta que pueden caer en uno de estos problemas por no poder generalizar correctamente el conocimiento. Underfitting indicará la imposibilidad de identificar o de obtener resultados correctos por carecer de suficientes muestras de entrenamiento o un entrenamiento muy pobre. Overfitting indicará un aprendizaje “excesivo” del conjunto de datos de entrenamiento haciendo que nuestro modelo únicamente pueda producir unos resultados singulares y con la imposibilidad de comprender nuevos datos de entrada.

Underfitting: se produce cuando nuestro modelo no es capaz de identificar patrones. Por lo que tendrá siempre pésimos resultados. Formas de prevenir el underfitting:
* Tratar los datos correctamente, eliminando outliers y variables innecesarias. 
* Utilizar modelos más complejos. 
* Ajustar los parámetros de nuestros modelos.
* Aumentar las iteraciones en los algoritmos iterativos


Overfitting: se produce cuando nuestro modelo se aprende los datos de train perfectamente, por lo que no es capaz de generalizar, y cuando le lleguen nuevos datos obtendrá pésimos resultados. Formas de prevenir el overfitting:
* Dividir nuestros datos en training, validación y testing.
* Obtener un mayor número de datos.
* Ajustar los parámetros de nuestros modelos.
* Utilizar modelos más simples.
* Los datos vienen de distintas distribuciones.
* Bajar el número de iteraciones en los algoritmos iterativos.

Para intentar que estos problemas nos afecten lo menos posible, podemos llevar a cabo diversas acciones:
* Cantidad mínima de muestras tanto para entrenar el modelo como para validarlo.
* Clases variadas y equilibradas en cantidad: En caso de aprendizaje supervisado y suponiendo que tenemos que clasificar diversas clases o categorías, es importante que los datos de entrenamiento estén balanceados. 
* Conjunto de Test de datos. Siempre subdividir nuestro conjunto de datos y mantener una porción del mismo “oculto” a nuestra máquina entrenada. Esto nos permitirá obtener una valoración de aciertos/fallos real del modelo y también nos permitirá detectar fácilmente efectos del overfitting /underfitting.
* Parameter Tunning o Ajuste de Parámetros: deberemos experimentar sobre todo dando más/menos “tiempo/iteraciones” al entrenamiento y su aprendizaje hasta encontrar el equilibrio.
* Cantidad excesiva de Dimensiones (features), con muchas variantes distintas, sin suficientes muestras. A veces conviene eliminar o reducir la cantidad de características que utilizaremos para entrenar el modelo. Una herramienta útil para hacerlo es PCA.


En nuestro caso personal, nuestro mayor problema ha ido de la mano con la cantidad excesiva de dimensiones, ya que tenemos asociado un Dataset de muy grandes dimensiones ( unas 400.000 líneas), lo que nos ha impedido trabajar correctamente. Una buena solución, ha sido eliminar gran parte del contenido, trabajando con el mismo archivo pero muy minimizado. Con 20.000 líneas aún seguía siendo muy difícil trabajar con este, y no ha sido hasta que hemos bajado a las 1000 líneas donde hemos podido trabajar cómodamente y sin fallos ni saturación.






