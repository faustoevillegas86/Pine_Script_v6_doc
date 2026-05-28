# Google Apps Script (ES-419) - Complete Content

Generated: 2026-05-27 18:30

## Table of Contents

- [Apps Script](#apps-script) (12)
- [Descripción general de Google Apps Script](#descripción-general-de-google-apps-script) (12)
- [Descripción general de la referencia](#descripción-general-de-la-referencia) (4)
- [Ejemplos de Google Apps Script](#ejemplos-de-google-apps-script) (23)

**Total: 51 items**

---

## Apps Script

### Apps Script

- Página principal
- Google Workspace
- Apps Script
### Automatiza y extiende Google Workspace con código sencillo.
Apps Script es una plataforma de JavaScript basada en la nube y potenciada por Google Drive que te permite integrar y automatizar tareas en los productos de Google.
## Desarrolla soluciones de alta calidad con facilidad
### Automatizaciones
Escriba un código que realice tareas de manera programática en todos los productos de Google. Las automatizaciones se activan mediante menús personalizados, botones, acciones del usuario o una programación basada en el tiempo.
### Funciones personalizadas
Escribe funciones de Hojas de cálculo de Google en Apps Script y llámalas desde tu hoja de cálculo como funciones integradas.
### Complementos
Compila una app que automatice tareas o se conecte a servicios de terceros desde Google Workspace. Comparta su solución con otras personas en Google Workspace Marketplace.
### Apps de chat
Proporciona una interfaz de conversación que permita a los usuarios de Google Chat interactuar con los servicios como si el servicio fuera una persona.
### Potencia tus secuencias de comandos con IA
### Guía de inicio rápido de Vertex AI
### Guía de inicio rápido del agente de ADK
### Guía de inicio rápido del agente A2A
### Analizador de mensajes de Gmail
### Agente de Viajes Concierge
### Función personalizada de verificador de datos
### Guía de inicio rápido del agente de ADK
### Guía de inicio rápido del agente A2A
### Guía de inicio rápido del agente de A2UI
### Servicio de Vertex AI
### Inicio rápido del agente de Gemini Enterprise
### Agentes de Gemini Enterprise
### Agentes de Vertex AI
### Crea un complemento de Gmail con vibe coding
### Notas de la versión
### Asistencia
### API de REST
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-03-03 (UTC)

---

### ¿Qué puede hacer Apps Script?

- Página principal
- Google Workspace
- Apps Script
- Guías
# Descripción general de Google Apps Script Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Apps Script es una plataforma de desarrollo de aplicaciones rápida que permite crear aplicaciones empresariales que se integran con Google Workspace con rapidez. Escribes código en JavaScript moderno y tienes acceso a bibliotecas integradas para aplicaciones de Google Workspace, como Gmail, Calendario de Google, Google Drive y muchas más. No debes instalar nada, ya que te proporcionamos un editor de código incorporado directamente en el navegador para que tu secuencia de comandos se guarde en Drive y se ejecute en los servidores de Google.
Si es la primera vez que usas JavaScript, Codecademy ofrece varios cursos de JavaScript . (Estos cursos no fueron desarrollados por Google ni están asociados con la empresa).
## ¿Qué puede hacer Apps Script?
Apps Script es versátil. Úsala para realizar las siguientes acciones:
- Agregar menús personalizados , y diálogos y barras laterales a Documentos de Google, Hojas de cálculo de Google y Formularios de Google
- Escribir funciones personalizadas y macros para Hojas de cálculo
- Publicar apps web independientes o incorporadas en Google Sites.
- Interactuar con otros servicios de Google , como Google AdSense, Google Analytics, Calendario, Drive, Gmail y Google Maps.
- Compilar complementos livianos add-ons y publicarlos en Google Workspace Marketplace. Si planeas compilar complementos a gran escala, consulta Cómo compilar un complemento de Google Workspace con extremos HTTP .
## Prueba una guía de inicio rápido
Prueba una de las siguientes guías de inicio rápido para ejecutar un proyecto de Apps Script en menos de 5 minutos.
- Guía de inicio rápido de automatización : Compila y ejecuta una automatización que cree un documento de Documentos y te envíe un vínculo a él por correo electrónico.
- Guía de inicio rápido de función personalizada : Crea una función personalizada que calcule el precio de venta de los artículos con descuento.
- Guía de inicio rápido de bot de Google Chat : Crea un bot de Chat al que se le puedan enviar mensajes directamente y que responda repitiendo tus mensajes.
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Automatizaciones

- Página principal
- Google Workspace
- Apps Script
- Guías
# Menús personalizados en Google Workspace Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Las secuencias de comandos pueden extender ciertos productos de Google agregando elementos de la interfaz de usuario que, cuando se hace clic en ellos, ejecutan una función de Google Apps Script. El ejemplo más común es ejecutar una secuencia de comandos desde un elemento de menú personalizado en Documentos, Hojas de cálculo, Presentaciones o Formularios de Google, pero las funciones de secuencias de comandos también se pueden activar haciendo clic en imágenes y dibujos en Hojas de cálculo.
## Menús personalizados en Documentos, Hojas de cálculo, Presentaciones o Formularios
Apps Script puede agregar menús nuevos en Documentos, Hojas de cálculo, Presentaciones o Formularios, con cada elemento de menú vinculado a una función en una secuencia de comandos. (En Formularios, los menús personalizados solo son visibles para un editor que abre el formulario para modificarlo, no para un usuario que lo abre para responder).
Solo las secuencias de comandos vinculadas pueden crear menús. Para mostrar el menú cuando el usuario abre un archivo, escribe el código del menú dentro de una onOpen función.
`onOpen`
En el siguiente ejemplo, se muestra cómo agregar un menú con un elemento, seguido de un separador visual y, luego, un submenú que contiene otro elemento. Cuando el usuario selecciona cualquiera de los elementos de menú, una función correspondiente abre un diálogo de alerta . Para obtener más información sobre los tipos de diálogos que puedes abrir, consulta la guía de diálogos y barras laterales .
```
function
 
onOpen
()
 
{


  
const
 
ui
 
=
 
SpreadsheetApp
.
getUi
();


  
// Or DocumentApp, SlidesApp or FormApp.


  
ui
.
createMenu
(
'Custom Menu'
)


      
.
addItem
(
'First item'
,
 
'menuItem1'
)


      
.
addSeparator
()


      
.
addSubMenu
(
ui
.
createMenu
(
'Sub-menu'
)


          
.
addItem
(
'Second item'
,
 
'menuItem2'
))


      
.
addToUi
();


}



function
 
menuItem1
()
 
{


  
SpreadsheetApp
.
getUi
()
 
// Or DocumentApp, SlidesApp or FormApp.


      
.
alert
(
'You clicked the first menu item!'
);


}



function
 
menuItem2
()
 
{


  
SpreadsheetApp
.
getUi
()
 
// Or DocumentApp, SlidesApp or FormApp.


      
.
alert
(
'You clicked the second menu item!'
);


}
```
Un documento, una hoja de cálculo, una presentación o un formulario solo pueden contener un menú con un nombre determinado. Si la misma secuencia de comandos o cualquier otra agrega un menú con el mismo nombre, el menú nuevo reemplaza al anterior. Los menús no se pueden quitar mientras el archivo está abierto, aunque puedes escribir tu onOpen función para omitir el menú en el futuro si se establece una propiedad determinada.
`onOpen`
Los complementos del editor también pueden tener elementos de menú, pero usan reglas especiales para definir cómo se definen.
## Imágenes y dibujos en los que se puede hacer clic en Hojas de cálculo
También puedes asignar una función de Apps Script a una imagen o un dibujo en Hojas de cálculo, siempre que la secuencia de comandos esté vinculada a la hoja de cálculo. En el siguiente ejemplo, se muestra cómo configurarlo.
- En Hojas de cálculo, selecciona el elemento de menú Extensiones > Apps Script para crear una secuencia de comandos vinculada a la hoja de cálculo.
- Borra cualquier código que haya en el editor de secuencias de comandos y pega el código que se encuentra a continuación.
```
function
 
showMessageBox
()
 
{


  
SpreadsheetApp
.
getUi
().
alert
(
'You clicked it!'
);


}
```
- Vuelve a Hojas de cálculo y selecciona Insertar > Imagen o Insertar > Dibujo para insertar una imagen o un dibujo.
- Después de insertar la imagen o el dibujo, haz clic en él. Aparecerá un pequeño selector de menú desplegable en la esquina superior derecha. Haz clic en él y elige Asignar secuencia de comandos .
- En el diálogo que aparece, escribe el nombre de la función de Apps Script que quieres ejecutar, sin paréntesis. En este caso, showMessageBox . Haz clic en Aceptar .
`showMessageBox`
- Vuelve a hacer clic en la imagen o el dibujo. Ahora se ejecuta la función.
La ejecución de la secuencia de comandos solo se activa cuando se hace clic en la imagen o el dibujo en un navegador web. La secuencia de comandos no se ejecuta si se hace clic en la imagen o el dibujo en un dispositivo móvil.
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Funciones personalizadas

- Página principal
- Google Workspace
- Apps Script
- Guías
# Funciones personalizadas en Hojas de cálculo de Google Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Hojas de cálculo de Google ofrece cientos de funciones integradas , como AVERAGE , SUM y VLOOKUP . Cuando estas no son suficientes para tus necesidades, puedes usar Apps Script para escribir funciones personalizadas y, luego, usarlas en Hojas de cálculo como si fueran funciones integradas.
`AVERAGE`
`SUM`
`VLOOKUP`
Para ver ejemplos de funciones personalizadas, consulta los siguientes instructivos:
- Cómo calcular el precio de venta de los artículos con descuento (guía de inicio rápido)
- Cómo calcular un descuento de precios por niveles
- Cómo calcular la distancia en automóvil y convertir metros a millas
- Resume datos de varias hojas
- Verifica la veracidad de las afirmaciones con un agente de IA del ADK y un modelo de Gemini
## Cómo comenzar
Las funciones personalizadas se crean con JavaScript estándar. Si es la primera vez que usas JavaScript, Codecademy ofrece un curso para principiantes . Este curso no fue desarrollado por Google ni está asociado a la empresa.
Esta es una función personalizada, llamada DOUBLE , que multiplica un valor de entrada por 2:
`DOUBLE`
```
/**


 * Multiplies an input value by 2.


 * @param {number} input The number to double.


 * @return The input multiplied by 2.


 * @customfunction


*/


function
 
DOUBLE
(
input
)
 
{


  
return
 
input
 
*
 
2
;


}
```
Si no sabes cómo escribir código JavaScript y no tienes tiempo para aprender, consulta la tienda de complementos de Google Workspace para ver si alguien más ya creó la función personalizada que necesitas.
### Cómo crear una función personalizada
Para escribir una función personalizada, sigue estos pasos:
- Crea o abre una hoja de cálculo en Hojas de cálculo.
- Selecciona el elemento de menú Extensiones > Apps Script .
- Borra cualquier código que aparezca en el editor de secuencias de comandos. Para la función DOUBLE que se mostró anteriormente, copia y pega el código en el editor de secuencias de comandos.
`DOUBLE`
- En la parte superior, haz clic en Guardar save .
Ahora puedes usar la función personalizada .
### Obtén una función personalizada de Google Workspace Marketplace
Google Workspace Marketplace ofrece varias funciones personalizadas como complementos de Google Workspace para Hojas de cálculo . Para usar o explorar estos complementos, haz lo siguiente:
- Crea o abre una hoja de cálculo en Hojas de cálculo.
- En la parte superior, haz clic en Complementos > Obtener complementos .
- Una vez que se abra Google Workspace Marketplace , haz clic en el cuadro de búsqueda de la esquina superior derecha.
- Escribe "función personalizada" y presiona Intro.
- Si encuentras un complemento de funciones personalizadas que te interese, haz clic en Instalar para instalarlo.
- Es posible que aparezca un diálogo que te indique que el complemento requiere autorización. Si es así, lee atentamente el aviso y, luego, haz clic en Permitir .
- El complemento estará disponible en la hoja de cálculo. Para usar el complemento en otra hoja de cálculo, ábrela y, en la parte superior, haz clic en Complementos > Administrar complementos . Busca el complemento que quieras usar y haz clic en Opciones more_vert > Usar en este documento .
### Usa una función personalizada
Una vez que escribas una función personalizada o instales una desde Google Workspace Marketplace, se usará como una función integrada:
- Haz clic en la celda en la que quieres usar la función.
- Escribe un signo igual ( = ) seguido del nombre de la función y cualquier valor de entrada (por ejemplo, =DOUBLE(A1) ) y presiona Intro.
`=`
`=DOUBLE(A1)`
- La celda muestra Loading... por un momento y, luego, devuelve el resultado.
`Loading...`
## Lineamientos para funciones personalizadas
Antes de escribir tu propia función personalizada, debes conocer algunos lineamientos.
### Nombres de funciones
Además de las convenciones estándar para nombrar funciones de JavaScript, ten en cuenta lo siguiente:
- El nombre de una función personalizada debe ser diferente de los nombres de las funciones integradas , como SUM() .
`SUM()`
- El nombre de una función personalizada no puede terminar con un guion bajo ( _ ), que denota una función privada en Apps Script.
`_`
- El nombre de una función personalizada se debe declarar con la sintaxis function myFunction() , no var myFunction = new Function() .
`function myFunction()`
`var myFunction = new Function()`
- El uso de mayúsculas no importa, aunque los nombres de las funciones de la hoja de cálculo suelen estar en mayúsculas.
### Argumentos
Al igual que una función integrada, una función personalizada puede tomar argumentos como valores de entrada:
- Si llamas a tu función con una referencia a una sola celda como argumento (como =DOUBLE(A1) ), el argumento es el valor de la celda.
`=DOUBLE(A1)`
- Si llamas a tu función con una referencia a un rango de celdas como argumento (como =DOUBLE(A1:B10) ), el argumento es un array bidimensional de los valores de las celdas. Por ejemplo, en la siguiente captura de pantalla, Apps Script interpreta los argumentos en =DOUBLE(A1:B2) como double([[1,3],[2,4]]) . Ten en cuenta que el código de muestra para DOUBLE descrito anteriormente debería modificarse para aceptar un array como entrada .
Si llamas a tu función con una referencia a un rango de celdas como argumento (como =DOUBLE(A1:B10) ), el argumento es un array bidimensional de los valores de las celdas. Por ejemplo, en la siguiente captura de pantalla, Apps Script interpreta los argumentos en =DOUBLE(A1:B2) como double([[1,3],[2,4]]) . Ten en cuenta que el código de muestra para DOUBLE descrito anteriormente debería modificarse para aceptar un array como entrada .
`=DOUBLE(A1:B10)`
`=DOUBLE(A1:B2)`
`double([[1,3],[2,4]])`
`DOUBLE`
- Los argumentos de las funciones personalizadas deben ser determinísticos . Es decir, las funciones integradas de la hoja de cálculo que devuelven un resultado diferente cada vez que se calculan, como NOW() o RAND() , no se permiten como argumentos para una función personalizada. Si una función personalizada intenta devolver un valor basado en una de estas funciones integradas volátiles, se mostrará Loading... de forma indefinida.
Los argumentos de las funciones personalizadas deben ser determinísticos . Es decir, las funciones integradas de la hoja de cálculo que devuelven un resultado diferente cada vez que se calculan, como NOW() o RAND() , no se permiten como argumentos para una función personalizada. Si una función personalizada intenta devolver un valor basado en una de estas funciones integradas volátiles, se mostrará Loading... de forma indefinida.
`NOW()`
`RAND()`
`Loading...`
- Para activar el recálculo, debes pasar una celda o un rango de celdas referenciados directamente como argumento a la función personalizada. De lo contrario, la función personalizada no se vuelve a calcular hasta que edites la función o cambies el valor de una celda a la que se hace referencia. Si usas el método getValue en funciones personalizadas, ten en cuenta que el rango al que se hace referencia no se pasa directamente como argumento a la función personalizada.
Para activar el recálculo, debes pasar una celda o un rango de celdas referenciados directamente como argumento a la función personalizada. De lo contrario, la función personalizada no se vuelve a calcular hasta que edites la función o cambies el valor de una celda a la que se hace referencia. Si usas el método getValue en funciones personalizadas, ten en cuenta que el rango al que se hace referencia no se pasa directamente como argumento a la función personalizada.
`getValue`
### Valores de retorno
Cada función personalizada debe devolver un valor para mostrar, de modo que se cumpla lo siguiente:
- Si una función personalizada devuelve un valor, este se muestra en la celda desde la que se llamó a la función.
- Si una función personalizada devuelve un array bidimensional de valores, estos se desbordan en las celdas adyacentes, siempre y cuando estén vacías. Si esto provocara que el array sobrescriba el contenido existente de las celdas, la función personalizada arrojará un error. Para ver un ejemplo, consulta la sección sobre cómo optimizar funciones personalizadas .
- Una función personalizada no puede afectar a las celdas que no sean aquellas en las que devuelve un valor. En otras palabras, una función personalizada no puede editar celdas arbitrarias, solo las celdas desde las que se llama y sus celdas adyacentes. Para editar celdas arbitrarias, usa un menú personalizado para ejecutar una función.
- Una llamada a función personalizada debe devolver un resultado en un plazo de 30 segundos. De lo contrario, la celda mostrará #ERROR! y la nota de la celda será Exceeded maximum execution time (line 0). .
`#ERROR!`
`Exceeded maximum execution time
(line 0).`
### Tipos de datos
Hojas de cálculo almacena los datos en diferentes formatos según la naturaleza de los datos. Cuando estos valores se usan en funciones personalizadas, Apps Script los trata como el tipo de datos adecuado en JavaScript . Estas son las áreas de confusión más comunes:
- Las horas y las fechas en Hojas de cálculo se convierten en objetos Date en Apps Script. Si la hoja de cálculo y la secuencia de comandos usan zonas horarias diferentes (un problema poco común), la función personalizada debe compensar la diferencia.
- Los valores de duración en Hojas de cálculo también se convierten en objetos Date , pero trabajar con ellos puede ser complicado .
`Date`
- Los valores de porcentaje en Hojas de cálculo se convierten en números decimales en Apps Script. Por ejemplo, una celda con el valor 10% se convierte en 0.1 en Apps Script.
`10%`
`0.1`
### Autocompletar
Hojas de cálculo admite el autocompletado para las funciones personalizadas, al igual que para las funciones integradas . A medida que escribes el nombre de una función en una celda, verás una lista de funciones integradas y personalizadas que coinciden con lo que ingresas.
Las funciones personalizadas aparecen en esta lista si su secuencia de comandos incluye una etiqueta JSDoc @customfunction , como en el ejemplo de DOUBLE() .
`@customfunction`
`DOUBLE()`
```
/**


 * Multiplies the input value by 2.


 *


 * @param {number} input The value to multiply.


 * @return {number} The input multiplied by 2.


 * @customfunction


 */


function
 
DOUBLE
(
input
)
 
{


  
return
 
input
 
*
 
2
;


}
```
## Avanzado
En esta sección, se abordan temas avanzados sobre las funciones personalizadas.
### Usa los servicios de Google Apps Script
Las funciones personalizadas pueden llamar a ciertos servicios de Apps Script para realizar tareas más complejas. Por ejemplo, una función personalizada puede llamar al servicio Language para traducir una frase en inglés al español.
A diferencia de la mayoría de los otros tipos de Apps Scripts, las funciones personalizadas nunca les solicitan a los usuarios que autoricen el acceso a datos personales. Por lo tanto, solo pueden llamar a servicios que no tienen acceso a datos personales, específicamente a los siguientes:
`getUserProperties()`
`get*()`
`set*()`
`SpreadsheetApp.openById()`
`SpreadsheetApp.openByUrl()`
Si tu función personalizada arroja el mensaje de error You do not have permission to call X service. , el servicio requiere autorización del usuario y, por lo tanto, no se puede usar en una función personalizada.
`You do not have permission to
call X service.`
Para usar un servicio que no se encuentre en la lista anterior, crea un menú personalizado que ejecute una función de Apps Script en lugar de escribir una función personalizada. Una función que se activa desde un menú le pide autorización al usuario si es necesario y, en consecuencia, puede usar todos los servicios de Apps Script.
### Comparte funciones personalizadas
Las funciones personalizadas comienzan vinculadas a la hoja de cálculo en la que se crearon. Esto significa que una función personalizada escrita en una hoja de cálculo no se puede usar en otras hojas de cálculo, a menos que uses uno de los siguientes métodos:
- Haz clic en Extensiones > Apps Script para abrir el editor de secuencias de comandos. Luego, copia el texto de la secuencia de comandos de la hoja de cálculo original y pégalo en el editor de secuencias de comandos de otra hoja de cálculo.
- Haz clic en Archivo > Crear una copia para crear una copia de la hoja de cálculo que contiene la función personalizada. Cuando se copia una hoja de cálculo, también se copian las secuencias de comandos adjuntas. Cualquier persona que tenga acceso a la hoja de cálculo puede copiar la secuencia de comandos. (Los colaboradores que solo tienen acceso de lectura no pueden abrir el editor de secuencias de comandos en la hoja de cálculo original. Sin embargo, cuando hacen una copia, se convierten en propietarios de ella y pueden ver la secuencia de comandos.
- Publica la secuencia de comandos como un complemento de editor de Hojas de cálculo.
Todas las secuencias de comandos vinculadas a contenedores comparten las mismas listas de acceso que sus contenedores. Esto significa que cualquier persona con permiso para editar la hoja de cálculo también puede editar cualquier código de Apps Script adjunto a ella. Para obtener más información, consulta acceso a secuencias de comandos vinculadas .
### Optimización
Cada vez que se usa una función personalizada en una hoja de cálculo, Hojas de cálculo realiza una llamada independiente al servidor de Apps Script. Si tu hoja de cálculo contiene docenas (o cientos, o miles) de llamadas a funciones personalizadas, este proceso puede ser lento. Es posible que algunos proyectos con muchas funciones personalizadas o funciones personalizadas complejas experimenten una demora temporal en las ejecuciones.
Por lo tanto, si planeas usar una función personalizada varias veces en un rango grande de datos, considera modificar la función para que acepte un rango como entrada en forma de un array bidimensional y, luego, devuelva un array bidimensional que pueda desbordarse en las celdas correspondientes.
Por ejemplo, la función DOUBLE() que se mostró anteriormente se puede volver a escribir para que acepte una sola celda o un rango de celdas de la siguiente manera:
`DOUBLE()`
```
/**


 * Multiplies the input value by 2.


 *


 * @param {number|Array<Array<number>>} input The value or range of cells


 *     to multiply.


 * @return The input multiplied by 2.


 * @customfunction


 */


function
 
DOUBLE
(
input
)
 
{


  
return
 
Array
.
isArray
(
input
)
 
?


      
input
.
map
(
row
 
=
>
 
row
.
map
(
cell
 
=
>
 
cell
 
*
 
2
))
 
:


      
input
 
*
 
2
;


}
```
Este enfoque usa el método map del objeto Array de JavaScript en el array bidimensional de celdas para obtener cada fila y, luego, para cada fila, vuelve a usar map para devolver el doble del valor de cada celda. Devuelve un array bidimensional que contiene los resultados. De esta manera, puedes llamar a DOUBLE solo una vez, pero hacer que calcule una gran cantidad de celdas a la vez, como se muestra en la siguiente captura de pantalla. Podrías lograr lo mismo con instrucciones if anidadas en lugar de la llamada a map .
`Array`
`map`
`DOUBLE`
`if`
`map`
Del mismo modo, la siguiente función personalizada recupera de manera eficiente contenido en vivo de Internet y usa un array bidimensional para mostrar dos columnas de resultados con una sola llamada a función. Si cada celda requiriera su propia llamada a función, la operación tardaría mucho más, ya que el servidor de Apps Script tendría que descargar y analizar el feed XML cada vez.
```
/**


 * Show the title and date for the first page of posts on the


 * Developer blog.


 *


 * @return Two columns of data representing posts on the


 *     Developer blog.


 * @customfunction


 */


function
 
getBlogPosts
()
 
{


  
var
 
array
 
=
 
[];


  
var
 
url
 
=
 
'https://gsuite-developers.googleblog.com/atom.xml'
;


  
var
 
xml
 
=
 
UrlFetchApp
.
fetch
(
url
).
getContentText
();


  
var
 
document
 
=
 
XmlService
.
parse
(
xml
);


  
var
 
root
 
=
 
document
.
getRootElement
();


  
var
 
atom
 
=
 
XmlService
.
getNamespace
(
'http://www.w3.org/2005/Atom'
);


  
var
 
entries
 
=
 
document
.
getRootElement
().
getChildren
(
'entry'
,
 
atom
);


  
for
 
(
var
 
i
 
=
 
0
;
 
i
 < 
entries
.
length
;
 
i
++
)
 
{


    
var
 
title
 
=
 
entries
[
i
].
getChild
(
'title'
,
 
atom
).
getText
();


    
var
 
date
 
=
 
entries
[
i
].
getChild
(
'published'
,
 
atom
).
getValue
();


    
array
.
push
([
title
,
 
date
]);


  
}


  
return
 
array
;


}
```
Estas técnicas se pueden aplicar a casi cualquier función personalizada que se use repetidamente en una hoja de cálculo, aunque los detalles de implementación varían según el comportamiento de la función.
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-26 (UTC)

---

### Complementos

- Página principal
- Google Workspace
- Complementos
- Add-ons
# Descripción general de los complementos Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Los complementos son aplicaciones personalizadas que extienden las aplicaciones de Google Workspace.
## Agrega nuevas capacidades a Google Workspace
Los complementos ayudan a automatizar tareas o a poner a disposición servicios o información de terceros en Google Workspace. Con los complementos, puedes hacer lo siguiente:
- Crear interfaces de usuario personalizadas que se integren directamente en las aplicaciones de Google Workspace. Estas interfaces pueden mostrar información al usuario y proporcionar controles de usuario.
- Aumentar la eficiencia del flujo de trabajo cuando se trabaja con Google Workspace mediante la automatización o la optimización de tareas.
- Controlar y mover datos entre las aplicaciones de Google.
- Eliminar la necesidad de cambiar de navegador, ya que se le proporciona al usuario todo lo que necesita en Google Workspace.
- Conectarse a servicios que no son de Google dentro de las aplicaciones de Google Workspace, lo que te permite recuperar o subir datos de esos servicios a Google Workspace.
## Tipos de complementos
Hay dos tipos de complementos que puedes compilar: complementos de Google Workspace y complementos del Editor . Para obtener más información, consulta Tipos de complementos .
## API Google Workspace Add-ons
Algunas funciones, como la extensión del menú desplegable de videoconferencias de Google Calendar y las capacidades de iOS, aún no son compatibles con la API de Google Workspace Add-ons.
Con la API de Google Workspace Add-ons, puedes hacer lo siguiente:
- Automatizar pruebas e implementaciones.
- Realizar tareas en segundo plano con el servicio de hosting de tu complemento.
- Crear y administrar implementaciones con herramientas de línea de comandos.
- Administrar permisos de implementación para cuentas de servicio o usuarios habituales con permisos detallados de Cloud IAM.
Para obtener más información sobre la API de Google Workspace Add-ons, consulta la documentación de referencia .
## Prueba una guía de inicio rápido
Para ver cómo funciona la compilación de un complemento, prueba una guía de inicio rápido:
- Guía de inicio rápido del complemento de Google Workspace de Node.js
- Guía de inicio rápido del complemento de Google Workspace de Apps Script
- Guía de inicio rápido del complemento del Editor de Apps Script
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-04 (UTC)

---

### Explora muestras de Apps Script

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Ejemplos de Google Apps Script Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Explora muestras y soluciones de Apps Script que te muestran cómo automatizar tareas, extender las interfaces de usuario de Google Workspace y realizar integraciones en Google y servicios externos.
Consulta las muestras por caso de uso, productos destacados de Google y tipo :
Filtrar por Casos de uso Seleccionar todo Borrar todo Automatización Administración de proyectos de Apps Script Análisis de datos Correo electrónico y comunicación Administración de empleados Planificación de eventos Administración de archivos Administración del tiempo Productos Seleccionar todo Borrar todo Gemini Gmail Consola del administrador de Google Calendario de Google Google Chat Documentos de Google Google Drive Formularios de Google Google Maps Hojas de cálculo de Google Presentaciones de Google VertexAi YouTube expand_less Menos expand_more Más Tipo de muestra Seleccionar todo Borrar todo Guía de inicio rápido Instructivo Codelab GitHub Restablecer Listo filter_list Filtros Planifica viajes con un agente de IA accesible en todo Google Workspace Nivel de programación: Avanzado Duración: 45 minutos Tipo de proyecto: Complemento de Google Workspace que extiende Chat, Gmail, Calendario, Drive y Documentos, Hojas de cálculo y Presentaciones. En este instructivo, se muestra cómo publicar agentes Hojas de cálculo de Google Google Drive Vertex AI Calendario de Google Documentos de Google Presentaciones de Google Gemini Gmail Apps Script Google Workspace Vertex AI Agent Engine Google Chat Complementos de Google Workspace Responde a incidentes con Google Chat, Vertex AI, Apps Script y autenticación de usuarios Respond to incidents in Chat and generate an AI-based summary of the resolution in Docs. Gemini Google Chat Vertex AI Google Workspace Apps Script Consola del administrador Documentos de Google Complementos de Google Workspace Cómo traducir texto en un documento de Documentos de Google En esta guía de inicio rápido, se crea un complemento del Editor de Documentos de Google que traduce el texto seleccionado en un documento. Para usar este ejemplo, debes cumplir con los siguientes requisitos previos: Reemplaza el contenido de cada Documentos de Google Google Workspace Apps Script Enviar correos electrónicos sobre los envíos nuevos de Formularios de Google En esta guía de inicio rápido, se crea un complemento del Editor de Formularios de Google que usa activadores para enviar mensajes de Gmail cuando un usuario responde al formulario. Para usar este ejemplo, debes cumplir con los siguientes Apps Script Formularios de Google Google Workspace Cómo agregar un servicio de conferencias web al Calendario de Google Importante: Este inicio rápido solo es para proveedores de conferencias web. La siguiente guía de inicio rápido del complemento de Google Workspace extiende Calendario de Google para sincronizarlo con un servicio ficticio de conferencias web llamado Google Workspace Apps Script Compila un complemento de Google Workspace con Apps Script En esta guía de inicio rápido, se crea un complemento de Google Workspace que muestra páginas principales, activadores contextuales y cómo conectarse a APIs de terceros. El complemento crea interfaces contextuales y no contextuales en Gmail, Google Drive Google Workspace Apps Script Calendario de Google Gmail Cómo traducir texto desde Presentaciones de Google En esta guía de inicio rápido, se crea un complemento del Editor de Presentaciones de Google que traduce el texto seleccionado en una presentación. Para usar esta muestra, debes cumplir con los siguientes requisitos previos: Reemplaza el contenido de Apps Script Google Workspace Presentaciones de Google Compila una app de Google Chat con Google Apps Script Crea una app de Google Chat con la que puedas enviar mensajes y que responda directamente con la repetición de tus mensajes. En el siguiente diagrama, se muestran la arquitectura y el patrón de mensajería: En el diagrama anterior, un usuario que Google Chat Google Workspace Apps Script Guía de inicio rápido de Google Apps Script Crea una secuencia de comandos de Google Apps Script que realice solicitudes a la API de Google Chat. En las guías de inicio rápido, se explica cómo configurar y ejecutar una app que llama a una API de Google Workspace. En esta guía de inicio rápido, Apps Script Google Workspace Google Chat Programa reuniones desde Google Chat Create Google Calendar events from a Chat space. Apps Script Google Workspace Calendario de Google Google Chat Recopila y administra contactos en Google Chat Help users manage their personal and business contacts by collecting information in card messages and dialogs. Google Workspace Apps Script Google Chat Recibe alertas sobre descuentos en acciones Enumera tus acciones en una hoja de cálculo de Hojas de Google y recibe alertas por correo electrónico si el precio de una acción baja más que su precio de compra. Apps Script Google Workspace Hojas de cálculo de Google Gmail Genera y envía archivos PDF desde Hojas de cálculo de Google Crea y envía PDFs por correo electrónico automáticamente desde Hojas de cálculo de Google con Apps Script. Google Workspace Google Drive Gmail Apps Script Hojas de cálculo de Google Realiza un seguimiento de las vistas y los comentarios de videos de YouTube Hacer un seguimiento del rendimiento de los videos de YouTube en una hoja de cálculo de Hojas de cálculo de Google y recibir notificaciones de Gmail sobre los comentarios nuevos YouTube Gmail Apps Script Hojas de cálculo de Google Google Workspace Propague el calendario de vacaciones del equipo Automatiza un calendario de vacaciones compartido del equipo sincronizando los eventos de ausencia de los calendarios de Google individuales con Google Apps Script. Google Workspace Grupos de Google Apps Script Calendario de Google Crea un corchete de torneo Aprende a usar Apps Script para crear un cuadro de torneo de eliminación simple para hasta 64 participantes. Apps Script Hojas de cálculo de Google Google Workspace Crea un registro para un sitio externo Automatiza los registros de actividades fuera de la oficina creando un formulario para las preferencias de los empleados y relacionándolos con un programa de actividades. Hojas de cálculo de Google Google Workspace Formularios de Google Apps Script Verifica la exactitud de las declaraciones con un agente de IA del ADK y un modelo de Gemini Aprende a crear una función personalizada de Hojas de cálculo de Google para verificar la exactitud de las declaraciones con un agente de Vertex AI y un modelo de Gemini. Vertex AI Google Workspace Hojas de cálculo de Google Apps Script Gemini Complementos de Google Workspace Enviar contenido seleccionado Aprende a usar Formularios de Google para permitir que los usuarios seleccionen contenido y recibirlo automáticamente por correo electrónico. Gmail Documentos de Google Formularios de Google Hojas de cálculo de Google Apps Script Google Workspace Guía de inicio rápido de las funciones personalizadas Crea funciones personalizadas en Google Apps Script y úsalas en Hojas de cálculo de Google como si fueran funciones integradas. Apps Script Hojas de cálculo de Google Google Workspace Complementos de Google Workspace Registra tiempos y actividades en el Calendario de Google y Hojas de cálculo de Google Aprende a hacer un seguimiento del tiempo dedicado a un proyecto en el Calendario de Google y a sincronizarlo con Hojas de cálculo de Google para crear hojas de horas. Apps Script Calendario de Google Hojas de cálculo de Google Google Workspace Compartir recursos con empleados nuevos Automatiza la incorporación de empleados nuevos a un Grupo de Google con Formularios de Google y Apps Script para compartir recursos. Hojas de cálculo de Google Documentos de Google Apps Script Grupos de Google Google Workspace Gmail Formularios de Google Analiza la opinión de los comentarios con la API de Google Cloud Natural Language Aprende a analizar datos de texto y opiniones a gran escala en Hojas de cálculo de Google con Apps Script y la API de Google Cloud Natural Language. Google Workspace Apps Script Hojas de cálculo de Google Guía de inicio rápido: Genera texto con Vertex AI En esta página, se explica cómo usar el servicio avanzado de Vertex AI de Google Apps Script para darle instrucciones al modelo Gemini 2.5 Flash para que genere texto. Para obtener más información sobre el servicio avanzado de Vertex AI, consulta la Apps Script Vertex AI Google Workspace Calcula un descuento de precios por niveles Esta función personalizada facilita el cálculo de los importes de descuento para un sistema de precios por niveles en Hojas de cálculo de Google. Complementos de Google Workspace Google Workspace Hojas de cálculo de Google Apps Script Sube archivos a Google Drive desde Formularios de Google Aprende a usar Apps Script para subir y organizar archivos en Google Drive desde Formularios de Google. Formularios de Google Google Workspace Google Drive Apps Script Calcula la distancia en automóvil y convierte los metros a millas Aprende a usar funciones personalizadas para calcular la distancia en automóvil, convertir metros a millas y agregar instrucciones paso a paso a una hoja. Apps Script Complementos de Google Workspace Hojas de cálculo de Google Google Workspace Google Maps Envía certificados de agradecimiento personalizados a los empleados Automatiza la creación y el envío de certificados personalizados de reconocimiento para empleados combinando datos de Hojas de cálculo de Google con una plantilla de Presentaciones de Google y enviándolos con Gmail. Hojas de cálculo de Google Gmail Presentaciones de Google Google Drive Google Workspace Apps Script Resumir datos de varias hojas Usa una función personalizada para resumir datos con estructuras similares de varias hojas en una hoja de cálculo de Google. Apps Script Google Workspace Hojas de cálculo de Google Complementos de Google Workspace Guía de inicio rápido de la biblioteca Crea una biblioteca de Apps Script que puedas usar para quitar filas duplicadas en los datos de hojas de cálculo. Google Workspace Hojas de cálculo de Google Apps Script expand_less Menos Más expand_more
Filtrar por
### Planifica viajes con un agente de IA accesible en todo Google Workspace
Nivel de programación: Avanzado Duración: 45 minutos Tipo de proyecto: Complemento de Google Workspace que extiende Chat, Gmail, Calendario, Drive y Documentos, Hojas de cálculo y Presentaciones. En este instructivo, se muestra cómo publicar agentes
- Hojas de cálculo de Google
- Google Drive
- Vertex AI
- Calendario de Google
- Documentos de Google
- Presentaciones de Google
- Gemini
- Gmail
- Apps Script
- Google Workspace
- Vertex AI Agent Engine
- Google Chat
- Complementos de Google Workspace
### Responde a incidentes con Google Chat, Vertex AI, Apps Script y autenticación de usuarios
Respond to incidents in Chat and generate an AI-based summary of the resolution in Docs.
- Gemini
- Google Chat
- Vertex AI
- Google Workspace
- Apps Script
- Consola del administrador
- Documentos de Google
- Complementos de Google Workspace
### Cómo traducir texto en un documento de Documentos de Google
En esta guía de inicio rápido, se crea un complemento del Editor de Documentos de Google que traduce el texto seleccionado en un documento. Para usar este ejemplo, debes cumplir con los siguientes requisitos previos: Reemplaza el contenido de cada
- Documentos de Google
- Google Workspace
- Apps Script
### Enviar correos electrónicos sobre los envíos nuevos de Formularios de Google
En esta guía de inicio rápido, se crea un complemento del Editor de Formularios de Google que usa activadores para enviar mensajes de Gmail cuando un usuario responde al formulario. Para usar este ejemplo, debes cumplir con los siguientes
- Apps Script
- Formularios de Google
- Google Workspace
### Cómo agregar un servicio de conferencias web al Calendario de Google
Importante: Este inicio rápido solo es para proveedores de conferencias web. La siguiente guía de inicio rápido del complemento de Google Workspace extiende Calendario de Google para sincronizarlo con un servicio ficticio de conferencias web llamado
- Google Workspace
- Apps Script
### Compila un complemento de Google Workspace con Apps Script
En esta guía de inicio rápido, se crea un complemento de Google Workspace que muestra páginas principales, activadores contextuales y cómo conectarse a APIs de terceros. El complemento crea interfaces contextuales y no contextuales en Gmail,
- Google Drive
- Google Workspace
- Apps Script
- Calendario de Google
- Gmail
### Cómo traducir texto desde Presentaciones de Google
En esta guía de inicio rápido, se crea un complemento del Editor de Presentaciones de Google que traduce el texto seleccionado en una presentación. Para usar esta muestra, debes cumplir con los siguientes requisitos previos: Reemplaza el contenido de
- Apps Script
- Google Workspace
- Presentaciones de Google
### Compila una app de Google Chat con Google Apps Script
Crea una app de Google Chat con la que puedas enviar mensajes y que responda directamente con la repetición de tus mensajes. En el siguiente diagrama, se muestran la arquitectura y el patrón de mensajería: En el diagrama anterior, un usuario que
- Google Chat
- Google Workspace
- Apps Script
### Guía de inicio rápido de Google Apps Script
Crea una secuencia de comandos de Google Apps Script que realice solicitudes a la API de Google Chat. En las guías de inicio rápido, se explica cómo configurar y ejecutar una app que llama a una API de Google Workspace. En esta guía de inicio rápido,
- Apps Script
- Google Workspace
- Google Chat
### Programa reuniones desde Google Chat
Create Google Calendar events from a Chat space.
- Apps Script
- Google Workspace
- Calendario de Google
- Google Chat
### Recopila y administra contactos en Google Chat
Help users manage their personal and business contacts by collecting information in card messages and dialogs.
- Google Workspace
- Apps Script
- Google Chat
### Recibe alertas sobre descuentos en acciones
Enumera tus acciones en una hoja de cálculo de Hojas de Google y recibe alertas por correo electrónico si el precio de una acción baja más que su precio de compra.
- Apps Script
- Google Workspace
- Hojas de cálculo de Google
- Gmail
### Genera y envía archivos PDF desde Hojas de cálculo de Google
Crea y envía PDFs por correo electrónico automáticamente desde Hojas de cálculo de Google con Apps Script.
- Google Workspace
- Google Drive
- Gmail
- Apps Script
- Hojas de cálculo de Google
### Realiza un seguimiento de las vistas y los comentarios de videos de YouTube
Hacer un seguimiento del rendimiento de los videos de YouTube en una hoja de cálculo de Hojas de cálculo de Google y recibir notificaciones de Gmail sobre los comentarios nuevos
- YouTube
- Gmail
- Apps Script
- Hojas de cálculo de Google
- Google Workspace
### Propague el calendario de vacaciones del equipo
Automatiza un calendario de vacaciones compartido del equipo sincronizando los eventos de ausencia de los calendarios de Google individuales con Google Apps Script.
- Google Workspace
- Grupos de Google
- Apps Script
- Calendario de Google
### Crea un corchete de torneo
Aprende a usar Apps Script para crear un cuadro de torneo de eliminación simple para hasta 64 participantes.
- Apps Script
- Hojas de cálculo de Google
- Google Workspace
### Crea un registro para un sitio externo
Automatiza los registros de actividades fuera de la oficina creando un formulario para las preferencias de los empleados y relacionándolos con un programa de actividades.
- Hojas de cálculo de Google
- Google Workspace
- Formularios de Google
- Apps Script
### Verifica la exactitud de las declaraciones con un agente de IA del ADK y un modelo de Gemini
Aprende a crear una función personalizada de Hojas de cálculo de Google para verificar la exactitud de las declaraciones con un agente de Vertex AI y un modelo de Gemini.
- Vertex AI
- Google Workspace
- Hojas de cálculo de Google
- Apps Script
- Gemini
- Complementos de Google Workspace
### Enviar contenido seleccionado
Aprende a usar Formularios de Google para permitir que los usuarios seleccionen contenido y recibirlo automáticamente por correo electrónico.
- Gmail
- Documentos de Google
- Formularios de Google
- Hojas de cálculo de Google
- Apps Script
- Google Workspace
### Guía de inicio rápido de las funciones personalizadas
Crea funciones personalizadas en Google Apps Script y úsalas en Hojas de cálculo de Google como si fueran funciones integradas.
- Apps Script
- Hojas de cálculo de Google
- Google Workspace
- Complementos de Google Workspace
### Registra tiempos y actividades en el Calendario de Google y Hojas de cálculo de Google
Aprende a hacer un seguimiento del tiempo dedicado a un proyecto en el Calendario de Google y a sincronizarlo con Hojas de cálculo de Google para crear hojas de horas.
- Apps Script
- Calendario de Google
- Hojas de cálculo de Google
- Google Workspace
### Compartir recursos con empleados nuevos
Automatiza la incorporación de empleados nuevos a un Grupo de Google con Formularios de Google y Apps Script para compartir recursos.
- Hojas de cálculo de Google
- Documentos de Google
- Apps Script
- Grupos de Google
- Google Workspace
- Gmail
- Formularios de Google
### Analiza la opinión de los comentarios con la API de Google Cloud Natural Language
Aprende a analizar datos de texto y opiniones a gran escala en Hojas de cálculo de Google con Apps Script y la API de Google Cloud Natural Language.
- Google Workspace
- Apps Script
- Hojas de cálculo de Google
### Guía de inicio rápido: Genera texto con Vertex AI
En esta página, se explica cómo usar el servicio avanzado de Vertex AI de Google Apps Script para darle instrucciones al modelo Gemini 2.5 Flash para que genere texto. Para obtener más información sobre el servicio avanzado de Vertex AI, consulta la
- Apps Script
- Vertex AI
- Google Workspace
### Calcula un descuento de precios por niveles
Esta función personalizada facilita el cálculo de los importes de descuento para un sistema de precios por niveles en Hojas de cálculo de Google.
- Complementos de Google Workspace
- Google Workspace
- Hojas de cálculo de Google
- Apps Script
### Sube archivos a Google Drive desde Formularios de Google
Aprende a usar Apps Script para subir y organizar archivos en Google Drive desde Formularios de Google.
- Formularios de Google
- Google Workspace
- Google Drive
- Apps Script
### Calcula la distancia en automóvil y convierte los metros a millas
Aprende a usar funciones personalizadas para calcular la distancia en automóvil, convertir metros a millas y agregar instrucciones paso a paso a una hoja.
- Apps Script
- Complementos de Google Workspace
- Hojas de cálculo de Google
- Google Workspace
- Google Maps
### Envía certificados de agradecimiento personalizados a los empleados
Automatiza la creación y el envío de certificados personalizados de reconocimiento para empleados combinando datos de Hojas de cálculo de Google con una plantilla de Presentaciones de Google y enviándolos con Gmail.
- Hojas de cálculo de Google
- Gmail
- Presentaciones de Google
- Google Drive
- Google Workspace
- Apps Script
### Resumir datos de varias hojas
Usa una función personalizada para resumir datos con estructuras similares de varias hojas en una hoja de cálculo de Google.
- Apps Script
- Google Workspace
- Hojas de cálculo de Google
- Complementos de Google Workspace
### Guía de inicio rápido de la biblioteca
Crea una biblioteca de Apps Script que puedas usar para quitar filas duplicadas en los datos de hojas de cálculo.
- Google Workspace
- Hojas de cálculo de Google
- Apps Script
### Acerca de los tipos de muestras
A continuación, se proporciona una explicación de cada tipo de muestra:
Las muestras de inicio rápido ofrecen muestras de código rápidas de prueba de concepto para que comiences a trabajar con Apps Script en menos de cinco minutos. Las guías de inicio rápido están disponibles para la mayoría de los tipos de proyectos de Apps Script.
Encuentra guías de inicio rápido organizadas por tipo de proyecto a la izquierda en Samples by project type o prueba esta automatización sencilla que crea un documento de Google y te envía un vínculo a él por correo electrónico.
Las muestras de soluciones son proyectos de Apps Script completamente funcionales. Las soluciones abordan problemas comerciales realistas y muestran cómo puedes automatizar flujos de trabajo en Google Workspace. A menudo, puedes implementar soluciones sin necesidad de editar o actualizar el código.
Encuentra soluciones organizadas por tipo de proyecto a la izquierda, en Samples by project type o prueba esta solución popular de combinación de correo electrónico .
Los codelabs son instructivos técnicos interactivos paso a paso. Combinan explicaciones, código de muestra de prácticas recomendadas y ejercicios de código. Los codelabs están disponibles para la mayoría de los productos para desarrolladores de Google y se publican en el catálogo de codelabs .
Encontrarás codelabs específicos de Apps Script a la izquierda, en Codelabs .
### Explora muestras de código de Apps Script en Git Hub
También puedes encontrar muestras de Apps Script en GitHub . Puedes bifurcar estos repositorios y usar el código como referencia para tus propios proyectos.
## Explora videos de Apps Script
Explora el contenido del canal de YouTube de Google Workspace Developers:
YouTube Get started with Vertex AI in Apps Script Use Apps Script's Vertex AI advanced service to call the Vertex AI API and prompt AI models to generate text, images, and more. #appsscript #vertexAI #Gemini Google Workspace Developers 27 de enero de 2026 YouTube How to Use Gemini 2.5 Flash in Apps Script with Vertex AI Learn how to get started with the Vertex AI advanced service in Apps Script. This video shows you how to set up and use the service to prompt the Gemini 2.5 Flash model to generate text. For more details, visit our documentation: Google Workspace Developers 21 de enero de 2026 YouTube Automate Your Tasks in 5 Minutes: Apps Script + Gemini for Beginners In this video, you will see how you can automate a task within Google Workspace with Gemini without having to write a single line of code. Subscribe to our YouTube channel: https://www.youtube.com/@googleworkspacedevs/ Subscribe to our Google Google Workspace Developers 15 de enero de 2026 YouTube Granular OAuth consent for web apps and Workspace add-ons Soon, published web apps and Google Workspace add-ons powered by Apps Script will also present users with this more granular consent screen when requesting an OAuth grant. #AppsScript #googleworkspaceplatform #googleworkspacedevelopernews Google Workspace Developers 9 de diciembre de 2025 YouTube Generate Apps Script code using Google AI Studio Check out how you can use Google AI Studio to write Apps Script code for you. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform Google Workspace Developers 3 de octubre de 2025 YouTube Use the Apps Script project dashboard Check out how you can use the Apps Script dashboard to manage your projects. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform Google Workspace Developers 29 de septiembre de 2025 YouTube Simplify your code using Apps Script libraries and services Check out how you can use Apps Script Libraries and Services to code more efficiently. 🤩 Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform Google Workspace Developers 26 de agosto de 2025 YouTube Format and fix code with the Apps Script command palette Check out how you can use Apps Script’s command palette to quickly edit your code. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform Google Workspace Developers 19 de agosto de 2025 YouTube Jump start your Apps Script project with a starter template See how you can use starter templates to speed up your Apps Script project. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform Google Workspace Developers 14 de agosto de 2025 YouTube Google Workspace Developer Summit 2025 📣 We are happy to announce the dates and locations for the Google Workspace Developer Summit 2025. → Sunnyvale, USA: October 8-9, 2025 → Paris, France: October 21-22, 2025 Want to join us? Please fill out this form: https://goo.gle/ws-dev-summit-25 Google Workspace Developers 29 de mayo de 2025 YouTube AI mocktail Bar demo explained 🍸 At Google Cloud Summit Benelux in Amsterdam, you could have AI generate a mocktail for you based on the image you uploaded. Hear Luc de Jager explain how this fun demo works. #GoogleCloudSummit #AppSheet #AppsScript Google Workspace Developers 26 de mayo de 2025 YouTube Use Apps Script’s Form Service to publish forms You can now use Apps Script’s Forms Service to publish forms, and to have granular control over who can respond to forms. #googleworkspaceplatform #googleworkspacedevelopernews #appsscript Google Workspace Developers 22 de mayo de 2025 expand_less Menos Más expand_more
YouTube
### Get started with Vertex AI in Apps Script
Use Apps Script's Vertex AI advanced service to call the Vertex AI API and prompt AI models to generate text, images, and more. #appsscript #vertexAI #Gemini
Google Workspace Developers
27 de enero de 2026
YouTube
### How to Use Gemini 2.5 Flash in Apps Script with Vertex AI
Learn how to get started with the Vertex AI advanced service in Apps Script. This video shows you how to set up and use the service to prompt the Gemini 2.5 Flash model to generate text. For more details, visit our documentation:
Google Workspace Developers
21 de enero de 2026
YouTube
### Automate Your Tasks in 5 Minutes: Apps Script + Gemini for Beginners
In this video, you will see how you can automate a task within Google Workspace with Gemini without having to write a single line of code. Subscribe to our YouTube channel: https://www.youtube.com/@googleworkspacedevs/ Subscribe to our Google
Google Workspace Developers
15 de enero de 2026
YouTube
### Granular OAuth consent for web apps and Workspace add-ons
Soon, published web apps and Google Workspace add-ons powered by Apps Script will also present users with this more granular consent screen when requesting an OAuth grant. #AppsScript #googleworkspaceplatform #googleworkspacedevelopernews
Google Workspace Developers
9 de diciembre de 2025
YouTube
### Generate Apps Script code using Google AI Studio
Check out how you can use Google AI Studio to write Apps Script code for you. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform
Google Workspace Developers
3 de octubre de 2025
YouTube
### Use the Apps Script project dashboard
Check out how you can use the Apps Script dashboard to manage your projects. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform
Google Workspace Developers
29 de septiembre de 2025
YouTube
### Simplify your code using Apps Script libraries and services
Check out how you can use Apps Script Libraries and Services to code more efficiently. 🤩 Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform
Google Workspace Developers
26 de agosto de 2025
YouTube
### Format and fix code with the Apps Script command palette
Check out how you can use Apps Script’s command palette to quickly edit your code. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform
Google Workspace Developers
19 de agosto de 2025
YouTube
### Jump start your Apps Script project with a starter template
See how you can use starter templates to speed up your Apps Script project. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform
Google Workspace Developers
14 de agosto de 2025
YouTube
### Google Workspace Developer Summit 2025 📣
We are happy to announce the dates and locations for the Google Workspace Developer Summit 2025. → Sunnyvale, USA: October 8-9, 2025 → Paris, France: October 21-22, 2025 Want to join us? Please fill out this form: https://goo.gle/ws-dev-summit-25
Google Workspace Developers
29 de mayo de 2025
YouTube
### AI mocktail Bar demo explained 🍸
At Google Cloud Summit Benelux in Amsterdam, you could have AI generate a mocktail for you based on the image you uploaded. Hear Luc de Jager explain how this fun demo works. #GoogleCloudSummit #AppSheet #AppsScript
Google Workspace Developers
26 de mayo de 2025
YouTube
### Use Apps Script’s Form Service to publish forms
You can now use Apps Script’s Forms Service to publish forms, and to have granular control over who can respond to forms. #googleworkspaceplatform #googleworkspacedevelopernews #appsscript
Google Workspace Developers
22 de mayo de 2025
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Guía de inicio rápido de Vertex AI

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Guía de inicio rápido: Genera texto con Vertex AI Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
En esta página, se explica cómo usar el servicio avanzado de Vertex AI de Google Apps Script para darle instrucciones al modelo Gemini 2.5 Flash para que genere texto.
Para obtener más información sobre el servicio avanzado de Vertex AI, consulta la documentación de referencia .
## Objetivos
- Configura el entorno.
- Crea un proyecto de Apps Script que use el servicio avanzado de Vertex AI.
- Ejecuta la secuencia de comandos para generar texto.
## Requisitos previos
- Un proyecto de Google Cloud con facturación habilitada. Para verificar que un proyecto existente tenga habilitada la facturación, consulta Verifica el estado de facturación de tus proyectos . Para crear un proyecto y configurar la facturación, consulta Crea un proyecto de Google Cloud .
## Configura tu entorno
En esta sección, se explica cómo configurar tu entorno en la consola de Google Cloud y Apps Script.
### Habilita la API de Vertex AI en tu proyecto de Cloud
- En la consola de Google Cloud, abre tu proyecto de Google Cloud y habilita la API de Vertex AI: Habilitar la API
En la consola de Google Cloud, abre tu proyecto de Google Cloud y habilita la API de Vertex AI:
Habilitar la API
- Confirma que habilitas la API en el proyecto de Cloud correcto y, luego, haz clic en Siguiente .
Confirma que habilitas la API en el proyecto de Cloud correcto y, luego, haz clic en Siguiente .
- Confirma que habilitas la API correcta y, luego, haz clic en Habilitar .
Confirma que habilitas la API correcta y, luego, haz clic en Habilitar .
### Crea y configura tu proyecto de Apps Script
Para crear y configurar tu proyecto de Apps Script, completa los siguientes pasos:
- Ve a script.google.com .
- Haz clic en Nuevo proyecto para crear un proyecto de Apps Script.
- En la parte superior izquierda, haz clic en Proyecto sin título .
- Nombra tu secuencia de comandos como Vertex AI quickstart y haz clic en Cambiar nombre .
#### Configura el servicio avanzado de Vertex AI
Para habilitar el servicio avanzado de Vertex AI y configurar el código, haz lo siguiente:
- En el editor de secuencias de comandos, ve a Servicios y haz clic en Agregar un servicio .
- En el menú desplegable, selecciona API de Vertex AI y haz clic en Agregar .
- Abre el archivo Code.gs y reemplaza el contenido por el siguiente código: /** * Main entry point to test the Vertex AI integration. */ function main () { const prompt = 'What is Apps Script in one sentence?' ; try { const response = callVertexAI ( prompt ); console . log ( `Response: ${ response } ` ); } catch ( error ) { console . error ( `Failed to call Vertex AI: ${ error . message } ` ); } } /** * Calls the Vertex AI Gemini model. * * @param {string} prompt - The user's input prompt. * @return {string} The text generated by the model. */ function callVertexAI ( prompt ) { // Configuration const projectId = ' GOOGLE_CLOUD_PROJECT_ID ' ; const region = 'us-central1' ; const modelName = 'gemini-2.5-flash' ; const model = `projects/ ${ projectId } /locations/ ${ region } /publishers/google/models/ ${ modelName } ` ; const payload = { contents : [{ role : 'user' , parts : [{ text : prompt }] }], generationConfig : { temperature : 0.1 , maxOutputTokens : 2048 } }; // Execute the request using the Vertex AI Advanced Service const response = VertexAI . Endpoints . generateContent ( payload , model ); // Use optional chaining for safe property access return response ? . candidates ? .[ 0 ] ? . content ? . parts ? .[ 0 ] ? . text || 'No response generated.' ; } Reemplaza GOOGLE_CLOUD_PROJECT_ID por el ID del proyecto de Cloud.
Abre el archivo Code.gs y reemplaza el contenido por el siguiente código:
`Code.gs`
```
/**


 * Main entry point to test the Vertex AI integration.


 */


function
 
main
()
 
{


  
const
 
prompt
 
=
 
'What is Apps Script in one sentence?'
;



  
try
 
{


    
const
 
response
 
=
 
callVertexAI
(
prompt
);


    
console
.
log
(
`Response: 
${
response
}
`
);


  
}
 
catch
 
(
error
)
 
{


    
console
.
error
(
`Failed to call Vertex AI: 
${
error
.
message
}
`
);


  
}


}



/**


 * Calls the Vertex AI Gemini model.


 *


 * @param {string} prompt - The user's input prompt.


 * @return {string} The text generated by the model.


 */


function
 
callVertexAI
(
prompt
)
 
{


  
// Configuration


  
const
 
projectId
 
=
 
'
GOOGLE_CLOUD_PROJECT_ID
'
;


  
const
 
region
 
=
 
'us-central1'
;


  
const
 
modelName
 
=
 
'gemini-2.5-flash'
;



  
const
 
model
 
=
 
`projects/
${
projectId
}
/locations/
${
region
}
/publishers/google/models/
${
modelName
}
`
;



  
const
 
payload
 
=
 
{


    
contents
:
 
[{


      
role
:
 
'user'
,


      
parts
:
 
[{


        
text
:
 
prompt


      
}]


    
}],


    
generationConfig
:
 
{


      
temperature
:
 
0.1
,


      
maxOutputTokens
:
 
2048


    
}


  
};



  
// Execute the request using the Vertex AI Advanced Service


  
const
 
response
 
=
 
VertexAI
.
Endpoints
.
generateContent
(
payload
,
 
model
);



  
// Use optional chaining for safe property access


  
return
 
response
?
.
candidates
?
.[
0
]
?
.
content
?
.
parts
?
.[
0
]
?
.
text
 
||
 
'No response generated.'
;


}
```
Reemplaza GOOGLE_CLOUD_PROJECT_ID por el ID del proyecto de Cloud.
`GOOGLE_CLOUD_PROJECT_ID`
- Haz clic en Guardar .
Haz clic en Guardar .
## Prueba la secuencia de comandos
- En el editor de secuencias de comandos, haz clic en Ejecutar para ejecutar la función main .
`main`
- Cuando se te solicite, autoriza la secuencia de comandos.
- Haz clic en Registro de ejecución para ver la respuesta de Vertex AI.
El servicio de Vertex AI muestra una respuesta a la instrucción What is Apps Script in one sentence? .
`What is Apps Script in one sentence?`
Por ejemplo, el registro de ejecución muestra una respuesta como la siguiente:
```
Response: Google Apps Script is a cloud-based, JavaScript platform that lets you
automate, integrate, and extend Google Workspace applications like Sheets, Docs,
and Gmail.
```
## Limpia
Para evitar que se apliquen cargos a tu cuenta de Google Cloud por los recursos que usaste en este instructivo, te recomendamos que borres el proyecto de Cloud.
- En la consola de Google Cloud, ve a la página Administrar recursos . Haz clic en el Menú menu > IAM y administración > Administrar recursos . Ir a Resource Manager
Ir a Resource Manager
- En la lista de proyectos, selecciona el proyecto que deseas borrar y haz clic en Borrar delete .
- En el diálogo, escribe el ID del proyecto y, luego, haz clic en Cerrar para borrar el proyecto.
Para evitar que se apliquen cargos a tu cuenta de Google Cloud por los recursos que usaste en esta guía de inicio rápido, te recomendamos que borres el proyecto de Cloud.
## Temas relacionados
- Documentación del servicio avanzado de Vertex AI
- Documentación de la plataforma de Vertex AI
- Consulta la galería de muestras de IA de Google Workspace
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Función personalizada de verificador de datos

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Verifica la exactitud de las declaraciones con un agente de IA del ADK y un modelo de Gemini Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Avanzado Duración : 30 minutos Tipo de proyecto : Función personalizada
## Descripción general
Una función personalizada de verificación de datos para Hojas de cálculo de Google que se usará como un proyecto de Google Apps Script vinculado potenciado por un agente de Vertex AI y un modelo de Gemini.
En este ejemplo, se muestra cómo puedes usar dos potentes tipos de recursos de IA directamente en tus archivos de Hojas de cálculo:
- Agentes de IA para capacidades de razonamiento sofisticadas, de varios pasos y con múltiples herramientas usando agentes del ADK implementados en Vertex AI Agent Engine.
- Modelos de IA para acceder a capacidades avanzadas de comprensión, generación y resumen usando modelos de Gemini de Vertex AI
## Objetivos
- Comprender qué hace la solución
- Comprender cómo se implementa la solución
- Implementar el agente de Vertex AI
- Configurar la secuencia de comandos
- Ejecutar la secuencia de comandos
## Acerca de esta solución
La función personalizada de Hojas de cálculo se llama FACT_CHECK y funciona como una solución de extremo a extremo. Analiza una declaración, fundamenta su respuesta con la información web más reciente y muestra el resultado en el formato que necesitas:
`FACT_CHECK`
- Uso: =FACT_CHECK("Your statement here") para obtener un resultado conciso y resumido =FACT_CHECK("Your statement here", "Your output formatting instructions here") para obtener un formato de resultado específico
- =FACT_CHECK("Your statement here") para obtener un resultado conciso y resumido
`=FACT_CHECK("Your statement here")`
- =FACT_CHECK("Your statement here", "Your output formatting instructions here") para obtener un formato de resultado específico
`=FACT_CHECK("Your statement here", "Your output formatting
instructions here")`
- Razonamiento: Agente de IA del ADK de LLM Auditor (muestra de Python) .
- Formato de resultado: Modelo de Gemini .
Esta solución solicita APIs de REST de Vertex AI con UrlFetchApp .
## Arquitectura
En el siguiente diagrama, se muestra la arquitectura de los recursos de Google Workspace y Google Cloud que usa la función personalizada.
## Requisitos previos
Para usar esta muestra, necesitas los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
Un navegador web con acceso a Internet
- Requisitos previos del agente del ADK de LLM Auditor Python 3.11 o versiones posteriores: Para la instalación, sigue las instrucciones del sitio web oficial de Python . Python Poetry: Para la instalación, sigue las instrucciones del sitio web oficial de Poetry . Google Cloud CLI: Para la instalación, sigue las instrucciones del sitio web oficial de Google Cloud .
Requisitos previos del agente del ADK de LLM Auditor
- Python 3.11 o versiones posteriores: Para la instalación, sigue las instrucciones del sitio web oficial de Python .
- Python Poetry: Para la instalación, sigue las instrucciones del sitio web oficial de Poetry .
- Google Cloud CLI: Para la instalación, sigue las instrucciones del sitio web oficial de Google Cloud .
## Prepara el entorno
En esta sección, se muestra cómo crear y configurar un proyecto de Google Cloud.
### Crea un proyecto de Google Cloud
- En la consola de Google Cloud, ve a Menú menu > IAM y administración > Crear un proyecto . Ir a Crear un proyecto
Ir a Crear un proyecto
- En el campo Nombre del proyecto , ingresa un nombre descriptivo para tu proyecto. Opcional: Para editar el ID del proyecto , haz clic en Editar . El ID del proyecto no se puede cambiar después de que se crea el proyecto. Por lo tanto, elige un ID que abarque tus necesidades durante todo el ciclo de vida del proyecto.
Opcional: Para editar el ID del proyecto , haz clic en Editar . El ID del proyecto no se puede cambiar después de que se crea el proyecto. Por lo tanto, elige un ID que abarque tus necesidades durante todo el ciclo de vida del proyecto.
- En el campo Ubicación , haz clic en Explorar para mostrar las posibles ubicaciones de tu proyecto. Luego, haga clic en Seleccionar .
- Haz clic en Crear . La consola de Google Cloud navega a la página Panel y tu proyecto se crea en unos minutos.
En uno de los siguientes entornos de desarrollo, accede a Google Cloud CLI ( gcloud ):
`gcloud`
- Cloud Shell : Para usar una terminal en línea con la CLI de gcloud ya configurada, activa Cloud Shell. Activar Cloud Shell
- Shell local : Para usar un entorno de desarrollo local, instala y inicializa la gcloud CLI. Para crear un proyecto de Cloud, usa el comando gcloud projects create : gcloud projects create PROJECT_ID Reemplaza PROJECT_ID configurando el ID del proyecto que deseas crear.
`gcloud projects create`
```
gcloud projects create 
PROJECT_ID
```
### Habilita la facturación para el proyecto de Cloud
- En la consola de Google Cloud, ve a Facturación . Haz clic en el Menú menu > Facturación > Mis proyectos . Ir a Facturación de Mis proyectos
Ir a Facturación de Mis proyectos
- En Selecciona una organización , elige la organización asociada con tu proyecto de Google Cloud.
- En la fila del proyecto, abre el menú Acciones ( more_vert ), haz clic en Cambiar facturación y elige la cuenta de Facturación de Cloud.
- Haz clic en Establecer cuenta .
- Para ver una lista de las cuentas de facturación disponibles, ejecuta el siguiente comando: gcloud billing accounts list
```
gcloud billing accounts list
```
- Vincula una cuenta de facturación con un proyecto de Google Cloud: gcloud billing projects link PROJECT_ID --billing-account= BILLING_ACCOUNT_ID Reemplaza lo siguiente: PROJECT_ID es el ID del proyecto de Cloud para el que deseas habilitar la facturación. BILLING_ACCOUNT_ID es el ID de la cuenta de facturación que se vinculará con el proyecto de Google Cloud.
```
gcloud billing projects link 
PROJECT_ID
 --billing-account=
BILLING_ACCOUNT_ID
```
Reemplaza lo siguiente:
- PROJECT_ID es el ID del proyecto de Cloud para el que deseas habilitar la facturación.
`PROJECT_ID`
- BILLING_ACCOUNT_ID es el ID de la cuenta de facturación que se vinculará con el proyecto de Google Cloud.
`BILLING_ACCOUNT_ID`
### Habilita la API de Vertex AI
- En la consola de Google Cloud, habilita las APIs de Vertex AI y Cloud Resource Manager. Habilitar las API
En la consola de Google Cloud, habilita las APIs de Vertex AI y Cloud Resource Manager.
Habilitar las API
- Confirma que habilitas la API de Vertex AI en el proyecto de Cloud correcto y, luego, haz clic en Siguiente .
Confirma que habilitas la API de Vertex AI en el proyecto de Cloud correcto y, luego, haz clic en Siguiente .
- Confirma que habilitas la API correcta y, luego, haz clic en Habilitar .
Confirma que habilitas la API correcta y, luego, haz clic en Habilitar .
- Si es necesario, configura el proyecto de Cloud actual como el que creaste con el comando gcloud config set project : gcloud config set project PROJECT_ID Reemplaza PROJECT_ID por el ID del proyecto de Cloud que creaste.
Si es necesario, configura el proyecto de Cloud actual como el que creaste con el comando gcloud config set project :
`gcloud config set project`
```
gcloud
 
config
 
set
 
project
 
PROJECT_ID
```
Reemplaza PROJECT_ID por el ID del proyecto de Cloud que creaste.
- Habilita la API de Vertex AI con el comando gcloud services enable : gcloud services enable aiplatform.googleapis.com
Habilita la API de Vertex AI con el comando gcloud services enable :
`gcloud services enable`
```
gcloud
 
services
 
enable
 
aiplatform.googleapis.com
```
### Crea una cuenta de servicio en la consola de Google Cloud
Para crear una cuenta de servicio nueva con la función Vertex AI User , sigue estos pasos:
`Vertex AI User`
- En la consola de Google Cloud, ve a Menú menu > IAM y administración > Cuentas de servicio . Ir a Cuentas de servicio
Ir a Cuentas de servicio
- Haga clic en Crear cuenta de servicio .
- Completa los detalles de la cuenta de servicio y, luego, haz clic en Crear y continuar .
- Opcional: Asigna funciones a tu cuenta de servicio para otorgar acceso a los recursos de tu proyecto de Google Cloud. Para obtener más detalles, consulta Otorga, cambia y revoca el acceso a los recursos .
- Haz clic en Continuar .
- Opcional: Ingresa usuarios o grupos que puedan administrar esta cuenta de servicio y realizar acciones con ella. Para obtener más detalles, consulta Administra la identidad temporal como cuenta de servicio .
- Haz clic en Listo . Toma nota de la dirección de correo electrónico de la cuenta de servicio.
- Crea la cuenta de servicio: gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \ --display-name=" SERVICE_ACCOUNT_NAME "
```
gcloud iam service-accounts create 
SERVICE_ACCOUNT_NAME
 \


  --display-name="
SERVICE_ACCOUNT_NAME
"
```
- Opcional: Asigna funciones a tu cuenta de servicio para otorgar acceso a los recursos de tu proyecto de Google Cloud. Para obtener más detalles, consulta Otorga, cambia y revoca el acceso a los recursos .
La cuenta de servicio aparece en la página de cuentas de servicio. A continuación, crea una clave privada para la cuenta de servicio.
### Crea una clave privada
Para crear y descargar una clave privada para la cuenta de servicio, sigue estos pasos:
- En la consola de Google Cloud, ve a Menú menu > IAM y administración > Cuentas de servicio . Ir a Cuentas de servicio
Ir a Cuentas de servicio
- Selecciona tu cuenta de servicio.
- Haz clic en Claves > AGREGAR CLAVE > Crear clave nueva .
- Selecciona JSON y, luego, haz clic en Crear . Ya se generó y descargó el nuevo par de claves pública/privada en tu equipo como un archivo nuevo. Guarda el archivo JSON descargado como credentials.json en tu directorio de trabajo. Este archivo es la única copia de esta clave. Para obtener información sobre cómo almacenar tu clave de forma segura, consulta Cómo administrar claves para cuentas de servicio .
Ya se generó y descargó el nuevo par de claves pública/privada en tu equipo como un archivo nuevo. Guarda el archivo JSON descargado como credentials.json en tu directorio de trabajo. Este archivo es la única copia de esta clave. Para obtener información sobre cómo almacenar tu clave de forma segura, consulta Cómo administrar claves para cuentas de servicio .
`credentials.json`
- Haz clic en Cerrar .
Para obtener más información sobre las cuentas de servicio, consulta Cuentas de servicio en la documentación de Cloud IAM de Google Cloud.
## Implementa el agente de IA del ADK de LLM Auditor
- Si aún no lo hiciste, autentícate con tu cuenta de Google Cloud y configura Google Cloud CLI para usar tu proyecto de Google Cloud. gcloud auth application-default login gcloud config set project PROJECT_ID gcloud auth application-default set-quota-project PROJECT_ID Reemplaza PROJECT_ID con el ID del proyecto en la nube que creaste.
Si aún no lo hiciste, autentícate con tu cuenta de Google Cloud y configura Google Cloud CLI para usar tu proyecto de Google Cloud.
```
gcloud
 
auth
 
application-default
 
login


gcloud
 
config
 
set
 
project
 
PROJECT_ID


gcloud
 
auth
 
application-default
 
set-quota-project
 
PROJECT_ID
```
Reemplaza PROJECT_ID con el ID del proyecto en la nube que creaste.
- Descarga este repositorio de GitHub: Descargar
Descarga este repositorio de GitHub:
Descargar
- En tu entorno de desarrollo local preferido, extrae el archivo comprimido descargado y abre el directorio adk-samples/python/agents/llm-auditor . unzip adk-samples-main.zip cd adk-samples-main/python/agents/llm-auditor
En tu entorno de desarrollo local preferido, extrae el archivo comprimido descargado y abre el directorio adk-samples/python/agents/llm-auditor .
`adk-samples/python/agents/llm-auditor`
```
unzip
 
adk-samples-main.zip


cd
 
adk-samples-main/python/agents/llm-auditor
```
- Crea un nuevo bucket de Cloud Storage dedicado al agente del ADK. gcloud storage buckets create gs:// CLOUD_STORAGE_BUCKET_NAME --project = PROJECT_ID --location = PROJECT_LOCATION Reemplaza lo siguiente: CLOUD_STORAGE_BUCKET_NAME con un nombre de bucket único que deseas usar. PROJECT_ID con el ID del proyecto en la nube que creaste. PROJECT_LOCATION con la ubicación del proyecto en la nube que creaste
Crea un nuevo bucket de Cloud Storage dedicado al agente del ADK.
```
gcloud
 
storage
 
buckets
 
create
 
gs://
CLOUD_STORAGE_BUCKET_NAME
 
--project
=
PROJECT_ID
 
--location
=
PROJECT_LOCATION
```
Reemplaza lo siguiente:
- CLOUD_STORAGE_BUCKET_NAME con un nombre de bucket único que deseas usar.
- PROJECT_ID con el ID del proyecto en la nube que creaste.
- PROJECT_LOCATION con la ubicación del proyecto en la nube que creaste
- Configura las siguientes variables de entorno: export GOOGLE_GENAI_USE_VERTEXAI = true export GOOGLE_CLOUD_PROJECT = PROJECT_ID export GOOGLE_CLOUD_LOCATION = PROJECT_LOCATION export GOOGLE_CLOUD_STORAGE_BUCKET = CLOUD_STORAGE_BUCKET_NAME Reemplaza lo siguiente: CLOUD_STORAGE_BUCKET_NAME con el nombre del bucket que creaste. PROJECT_ID con el ID del proyecto en la nube que creaste. PROJECT_LOCATION con la ubicación del proyecto en la nube que creaste
Configura las siguientes variables de entorno:
```
export
 
GOOGLE_GENAI_USE_VERTEXAI
=
true


export
 
GOOGLE_CLOUD_PROJECT
=
PROJECT_ID


export
 
GOOGLE_CLOUD_LOCATION
=
PROJECT_LOCATION


export
 
GOOGLE_CLOUD_STORAGE_BUCKET
=
CLOUD_STORAGE_BUCKET_NAME
```
Reemplaza lo siguiente:
- CLOUD_STORAGE_BUCKET_NAME con el nombre del bucket que creaste.
- PROJECT_ID con el ID del proyecto en la nube que creaste.
- PROJECT_LOCATION con la ubicación del proyecto en la nube que creaste
- Instala y, luego, implementa el agente del ADK desde el entorno virtual. python3 -m venv myenv source myenv/bin/activate poetry install --with deployment python3 deployment/deploy.py --create
Instala y, luego, implementa el agente del ADK desde el entorno virtual.
```
python3
 
-m
 
venv
 
myenv


source
 
myenv/bin/activate


poetry
 
install
 
--with
 
deployment


python3
 
deployment/deploy.py
 
--create
```
- Recupera el ID del agente. Lo necesitarás más adelante para configurar la función personalizada. python3 deployment/deploy.py --list
Recupera el ID del agente. Lo necesitarás más adelante para configurar la función personalizada.
```
python3
 
deployment/deploy.py
 
--list
```
## Analiza el código de muestra
De manera opcional, antes de crear la nueva hoja de cálculo, tómate un momento para revisar y familiarizarte con el código de muestra alojado en GitHub.
Ver en GitHub
## Crea y configura en una hoja de cálculo nueva
- Para hacer una copia completa de la hoja de cálculo de muestra de Hojas de cálculo, incluido su proyecto de Apps Script vinculado al contenedor, haz clic en el siguiente botón: Copiar hoja de cálculo de Google
Para hacer una copia completa de la hoja de cálculo de muestra de Hojas de cálculo, incluido su proyecto de Apps Script vinculado al contenedor, haz clic en el siguiente botón:
Copiar hoja de cálculo de Google
- En la hoja de cálculo recién creada, ve a Extensiones > Apps Script .
En la hoja de cálculo recién creada, ve a Extensiones > Apps Script .
- En el proyecto de Apps Script, ve a Configuración del proyecto , haz clic Editar propiedades de la secuencia de comandos y, luego, en Agregar propiedad de la secuencia de comandos para agregar las siguientes propiedades de la secuencia de comandos: LOCATION con la ubicación del proyecto de Google Cloud creado en los pasos anteriores, como us-central1 GEMINI_MODEL_ID con el modelo de Gemini que deseas usar, como gemini-2.5-flash-lite REASONING_ENGINE_ID con el ID del agente del ADK de LLM Auditor implementado en los pasos anteriores, como 1234567890 SERVICE_ACCOUNT_KEY con la clave JSON de la cuenta de servicio descargada en los pasos anteriores, como { ... }
En el proyecto de Apps Script, ve a Configuración del proyecto , haz clic Editar propiedades de la secuencia de comandos y, luego, en Agregar propiedad de la secuencia de comandos para agregar las siguientes propiedades de la secuencia de comandos:
- LOCATION con la ubicación del proyecto de Google Cloud creado en los pasos anteriores, como us-central1
`LOCATION`
`us-central1`
- GEMINI_MODEL_ID con el modelo de Gemini que deseas usar, como gemini-2.5-flash-lite
`GEMINI_MODEL_ID`
`gemini-2.5-flash-lite`
- REASONING_ENGINE_ID con el ID del agente del ADK de LLM Auditor implementado en los pasos anteriores, como 1234567890
`REASONING_ENGINE_ID`
`1234567890`
- SERVICE_ACCOUNT_KEY con la clave JSON de la cuenta de servicio descargada en los pasos anteriores, como { ... }
`SERVICE_ACCOUNT_KEY`
`{ ... }`
- Haz clic en Guardar las propiedades de las secuencias de comandos
Haz clic en Guardar las propiedades de las secuencias de comandos
## Prueba la función personalizada
- Ve a la hoja de cálculo recién creada.
- Cambia las declaraciones en la columna A .
- Las fórmulas de la columna B se ejecutan y, luego, muestran los resultados de la verificación de datos.
## Limpia
Para evitar que se apliquen cargos a tu cuenta de Google Cloud por los recursos que usaste en este instructivo, te recomendamos que borres el proyecto de Cloud.
- En la consola de Google Cloud, ve a la página Administrar recursos . Haz clic en el Menú menu > IAM y administración > Administrar recursos . Ir a Resource Manager
Ir a Resource Manager
- En la lista de proyectos, selecciona el proyecto que deseas borrar y haz clic en Borrar delete .
- En el diálogo, escribe el ID del proyecto y, luego, haz clic en Cerrar para borrar el proyecto.
## Próximos pasos
- Planifica viajes con un agente de IA accesible en Google Workspace
- Compila agentes de Gemini Enterprise que estén bien integrados con los almacenes de datos, las APIs y los complementos de Workspace
- Compila agentes de Vertex AI que estén bien integrados con los almacenes de datos, las APIs y los complementos de Workspace
- Funciones personalizadas en Hojas de cálculo
- Extiende Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Servicio de Vertex AI

- Página principal
- Google Workspace
- Apps Script
- Referencia
# Servicio de Vertex AI Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
El servicio de Vertex AI te permite usar la API de Vertex AI en Google Apps Script. Esta API te brinda acceso a Gemini y otros modelos de IA generativa para la generación de texto, de imágenes y mucho más.
Para comenzar a usar este servicio avanzado, prueba la guía de inicio rápido .
## Requisitos previos
- Un proyecto de Google Cloud con facturación habilitada. Para verificar que un proyecto existente tenga habilitada la facturación, consulta Verifica el estado de facturación de tus proyectos . Para crear un proyecto y configurar la facturación, consulta Crea un proyecto de Google Cloud .
Un proyecto de Google Cloud con facturación habilitada. Para verificar que un proyecto existente tenga habilitada la facturación, consulta Verifica el estado de facturación de tus proyectos . Para crear un proyecto y configurar la facturación, consulta Crea un proyecto de Google Cloud .
- En la consola de Google Cloud, ve a tu proyecto de Cloud y habilita la API de Vertex AI: Habilitar la API
En la consola de Google Cloud, ve a tu proyecto de Cloud y habilita la API de Vertex AI:
Habilitar la API
- En tu proyecto de Apps Script, activa el servicio de Vertex AI. Para conocer los pasos, consulta Servicios avanzados de Google .
En tu proyecto de Apps Script, activa el servicio de Vertex AI. Para conocer los pasos, consulta Servicios avanzados de Google .
## Referencia
Para obtener más información sobre este servicio, consulta la documentación de referencia de la API de Vertex AI . Al igual que todos los servicios avanzados en Apps Script, el servicio de Vertex AI usa los mismos objetos, métodos y parámetros que la API pública.
## Código de muestra
El siguiente código de muestra usa la versión 1 de la API de Vertex AI.
### Generar texto
En este código de muestra, se muestra cómo solicitarle al modelo Gemini 2.5 Flash que genere texto. La función devuelve el resultado al registro de ejecución de Apps Script.
```
/**


 * Main entry point to test the Vertex AI integration.


 */


function
 
main
()
 
{


  
const
 
prompt
 
=
 
'What is Apps Script in one sentence?'
;



  
try
 
{


    
const
 
response
 
=
 
callVertexAI
(
prompt
);


    
console
.
log
(
`Response: 
${
response
}
`
);


  
}
 
catch
 
(
error
)
 
{


    
console
.
error
(
`Failed to call Vertex AI: 
${
error
.
message
}
`
);


  
}


}



/**


 * Calls the Vertex AI Gemini model.


 *


 * @param {string} prompt - The user's input prompt.


 * @return {string} The text generated by the model.


 */


function
 
callVertexAI
(
prompt
)
 
{


  
// Configuration


  
const
 
projectId
 
=
 
'
GOOGLE_CLOUD_PROJECT_ID
'
;


  
const
 
region
 
=
 
'us-central1'
;


  
const
 
modelName
 
=
 
'gemini-2.5-flash'
;



  
const
 
model
 
=
 
`projects/
${
projectId
}
/locations/
${
region
}
/publishers/google/models/
${
modelName
}
`
;



  
const
 
payload
 
=
 
{


    
contents
:
 
[{


      
role
:
 
'user'
,


      
parts
:
 
[{


        
text
:
 
prompt


      
}]


    
}],


    
generationConfig
:
 
{


      
temperature
:
 
0.1
,


      
maxOutputTokens
:
 
2048


    
}


  
};



  
// Execute the request using the Vertex AI Advanced Service


  
const
 
response
 
=
 
VertexAI
.
Endpoints
.
generateContent
(
payload
,
 
model
);



  
// Use optional chaining for safe property access


  
return
 
response
?
.
candidates
?
.[
0
]
?
.
content
?
.
parts
?
.[
0
]
?
.
text
 
||
 
'No response generated.'
;


}
```
Reemplaza GOOGLE_CLOUD_PROJECT_ID por el ID del proyecto de tu proyecto de Cloud.
`GOOGLE_CLOUD_PROJECT_ID`
#### Genera texto con una cuenta de servicio
En el siguiente ejemplo, se muestra cómo generar texto autenticándose como un proyecto de Apps Script con una cuenta de servicio .
```
/**


 * Main entry point to test the Vertex AI integration.


 */


function
 
main
()
 
{


  
const
 
prompt
 
=
 
'What is Apps Script in one sentence?'
;



  
try
 
{


    
const
 
response
 
=
 
callVertexAI
(
prompt
);


    
console
.
log
(
`Response: 
${
response
}
`
);


  
}
 
catch
 
(
error
)
 
{


    
console
.
error
(
`Failed to call Vertex AI: 
${
error
.
message
}
`
);


  
}


}



/**


 * Calls the Vertex AI Gemini model.


 *


 * @param {string} prompt - The user's input prompt.


 * @return {string} The text generated by the model.


 */


function
 
callVertexAI
(
prompt
)
 
{


  
const
 
service
 
=
 
getServiceAccountService
();



  
// Configuration


  
const
 
projectId
 
=
 
'
GOOGLE_CLOUD_PROJECT_ID
'
;


  
const
 
region
 
=
 
'us-central1'
;


  
const
 
modelName
 
=
 
'gemini-2.5-flash'
;



  
const
 
model
 
=
 
`projects/
${
projectId
}
/locations/
${
region
}
/publishers/google/models/
${
modelName
}
`
;



  
const
 
payload
 
=
 
{


    
contents
:
 
[{


      
role
:
 
'user'
,


      
parts
:
 
[{


        
text
:
 
prompt


      
}]


    
}],


    
generationConfig
:
 
{


      
temperature
:
 
0.1
,


      
maxOutputTokens
:
 
2048


    
}


  
};



  
// Execute the request using the Vertex AI Advanced Service


  
const
 
response
 
=
 
VertexAI
.
Endpoints
.
generateContent
(


    
payload
,


    
model
,


    
{},


    
// Authenticate with the service account token.


    
{
 
Authorization
:
 
`Bearer 
${
service
.
getAccessToken
()
}
`
 
},


  
);



  
// Use optional chaining for safe property access


  
return
 
response
?
.
candidates
?
.[
0
]
?
.
content
?
.
parts
?
.[
0
]
?
.
text
 
||
 
'No response generated.'
;


}



/**


 * Get a new OAuth2 service for a given service account.


 */


function
 
getServiceAccountService
()
 
{


  
const
 
serviceAccountKeyString
 
=
 
PropertiesService
.
getScriptProperties
().
getProperty
(
'SERVICE_ACCOUNT_KEY'
);



  
if
 
(
!
serviceAccountKeyString
)
 
{


    
throw
 
new
 
Error
(
'SERVICE_ACCOUNT_KEY property is not set. Please follow the setup instructions.'
);


  
}



  
const
 
serviceAccountKey
 
=
 
JSON
.
parse
(
serviceAccountKeyString
);



  
const
 
CLIENT_EMAIL
 
=
 
serviceAccountKey
.
client_email
;


  
const
 
PRIVATE_KEY
 
=
 
serviceAccountKey
.
private_key
;


  
const
 
SCOPES
 
=
 
[
'https://www.googleapis.com/auth/cloud-platform'
];



  
return
 
OAuth2
.
createService
(
'ServiceAccount'
)


      
.
setTokenUrl
(
'https://oauth2.googleapis.com/token'
)


      
.
setPrivateKey
(
PRIVATE_KEY
)


      
.
setIssuer
(
CLIENT_EMAIL
)


      
.
setPropertyStore
(
PropertiesService
.
getScriptProperties
())


      
.
setScope
(
SCOPES
);


}
```
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-05-05 (UTC)

---

### Notas de la versión

- Home
- Google Workspace
- Apps Script
- Support
# Google Apps Script release notes Stay organized with collections Save and categorize content based on your preferences.
To get the latest product updates delivered to you, add the URL of this page to your feed reader , or add the feed URL directly: https://developers.google.com/feeds/apps-script-release-notes.xml .
`https://developers.google.com/feeds/apps-script-release-notes.xml`
This page contains release notes for features and updates to Apps Script. We recommend that Apps Script developers periodically check this list for any new announcements.
## March 12, 2026
Generally Available: The AddOnsResponseService and its associated classes in Apps Script are now generally available. This service allows developers to create and manage interactive responses for Google Workspace Add-ons that extend Google Chat.
`AddOnsResponseService`
## March 05, 2026
Deprecated: The method setAuthentication(clientId, signingKey) has been deprecated and is scheduled for sunset in June 2026. This change is because Maps platform client IDs were deprecated on May 26, 2025, and can't be used after May 31, 2026. Instead, use setAuthenticationByKey(apiKey) or setAuthenticationByKey(apiKey, signingKey) . To get an API key, refer to the Client ID Migration Guide .
`setAuthentication(clientId, signingKey)`
`setAuthenticationByKey(apiKey)`
`setAuthenticationByKey(apiKey, signingKey)`
Generally Available: To authenticate to the Maps service, you can now use an API key with the new methods setAuthenticationByKey(apiKey) and setAuthenticationByKey(apiKey, signingKey) . To reset authentication to the default mode, use resetAuthenticationApiKey() .
`setAuthenticationByKey(apiKey)`
`setAuthenticationByKey(apiKey, signingKey)`
`resetAuthenticationApiKey()`
## January 12, 2026
Generally Available: Use Apps Script's Vertex AI advanced service to call the Vertex AI API and prompt AI models to generate text, images, and more.
For details, see the Vertex AI advanced service reference documentation.
## January 07, 2026
The Apps Script samples gallery now lets you find samples by use case, products, and sample type. The gallery also features the following new samples:
- Build a Google Chat app with an ADK AI agent
- Build a Chat app with an Agent2Agent agent
- Analyze and label Gmail messages with Gemini and Vertex AI
## June 04, 2025
Google Analytics 4 has replaced Universal Analytics , which means the Apps Script Advanced Service for Google Analytics Management API and Reporting API is deprecated. Use the Google Analytics Data API Advanced Service instead.
## April 23, 2025
Between approximately September 2024 and March 2025, for Google Sheets modifications made by time-based Apps Script triggers, a bug caused incorrect OAuth App IDs and App Names to be logged in the Google Admin console.
This logging issue did not impact the functionality of Apps Script or Google Sheets. A fix was deployed on March 27, 2025, preventing future incorrect logging. Historical logs will not be corrected.
To learn more about Apps Script and audit logs, see Monitor and control Apps Script use in your Google Workspace organization .
## April 08, 2025
You can now use the Forms Service to publish forms, and to have granular control over who can respond to forms.
Learn about the setPublished method to publish forms .
`setPublished`
## February 20, 2025
As of February 20, 2025, the Rhino runtime is deprecated. Scripts running on Rhino will continue to function until January 31, 2026, after which they will no longer execute. Please migrate your scripts to the V8 runtime before this date. Refer to Migrate scripts to the V8 runtime .
## January 08, 2025
Generally Available : Granular OAuth permissions are now supported for users executing scripts in the Apps Script IDE. The granular OAuth consent screen lets users specify which individual OAuth scopes they would like to authorize. The granular consent screen will gradually launch to the remaining Apps Script surfaces, such as add-ons and trigger executions, in the future.
For more information, refer to the Workspace Updates blog post: Granular OAuth consent in Google Apps Script IDE executions .
Generally Available : To complement the release of the granular consent flow in Apps Script IDE executions, the following methods have been added to the ScriptApp and AuthorizationInfo classes to let Apps Script developers programmatically interact with the scopes granted for a script.
`ScriptApp`
`AuthorizationInfo`
ScriptApp class :
`ScriptApp`
- requireScopes(authMode, oAuthScopes)
`requireScopes(authMode, oAuthScopes)`
- requireAllScopes(authMode)
`requireAllScopes(authMode)`
- getAuthorizationInfo(authMode, oAuthScopes)
`getAuthorizationInfo(authMode, oAuthScopes)`
AuthorizationInfo class :
`AuthorizationInfo`
- getAuthorizedScopes()
`getAuthorizedScopes()`
For more information, refer to Handle granular OAuth permissions .
## December 09, 2024
The getUrl() method for the CellImage , CellImageBuilder , and OverGridImage classes of the Spreadsheet service has been deprecated. An image's source URL isn't available regardless of how the image is inserted into a spreadsheet.
`getUrl()`
`CellImage`
`CellImageBuilder`
`OverGridImage`
Generally available : The getSheetById() method has been added to the Spreadsheet class of the Spreadsheet service. This lets you get a sheet in a spreadsheet using its unique ID.
`getSheetById()`
`Spreadsheet`
Generally available : You can now get and set the transparency of a calendar event, meaning whether the event shows as "Busy" or "Available" in Google Calendar. For more information, refer to the following documentation:
- Enum EventTransparency
`EventTransparency`
- Class CalendarEvent
`CalendarEvent`
- Class CalendarEventSeries
`CalendarEventSeries`
## November 27, 2024
The Calendar service now has a getEventType() method that lets developers differentiate regular events from other types of events like out-of-office and working location events. For more information, see the following documentation:
`getEventType()`
- getEventType() for events
`getEventType()`
- getEventType() for event series
`getEventType()`
- EventType enum
`EventType`
## October 02, 2024
Apps Script has rescheduled the shutdown date of the Contacts service to January 31, 2025. Refer to the Apps Script sunset schedule .
The Apps Script Contacts service was deprecated in December 2022. Instead, use the People API advanced service. Refer to Migrate from Contacts service to People API advanced service .
## September 03, 2024
Generally available : You can now use Looker in Connected Sheets from Apps Script. This update lets you create a new or access existing Looker data source connections, connect a sheet to them, create pivot tables, and more.
The following updates have been made to the Spreadsheet service to support Looker in Connected Sheets from Apps Script.
`Spreadsheet`
- The following new data source type has been added: LOOKER
- LOOKER
`LOOKER`
- The following new classes have been added: LookerDataSourceSpec LookerDataSourceSpecBuilder
- LookerDataSourceSpec
`LookerDataSourceSpec`
- LookerDataSourceSpecBuilder
`LookerDataSourceSpecBuilder`
- The following new methods have been added to existing classes: DataSourceSpec.asLooker() DataSourceSpecBuilder.asLooker()
- DataSourceSpec.asLooker()
`DataSourceSpec.asLooker()`
- DataSourceSpecBuilder.asLooker()
`DataSourceSpecBuilder.asLooker()`
## August 15, 2024
Generally Available : You can now create and organize tabs in Google Docs documents using Apps Script's Document service. For more information, refer to Work with tabs .
## August 07, 2024
Google Workspace administrators can now turn on an allowlist in the admin console to control which external domains users can access through Apps Script's URL Fetch service .
- If you're using a script or add-on that accesses external domains, work with your administrator to add those URLs to the admin allowlist.
- If you've published an add-on on the Google Workspace Marketplace, it might be helpful to list the URLs that admins should add to their allowlist on your Marketplace listing.
For more information, refer to the Google Workspace Admin Help article: Allow only certain external connections for Apps Script and Sheets .
## July 25, 2024
( Generally Available ): Multiselect menus are now generally available for Add-ons.
For more information refer to the following:
- SelectionInput for Apps Script
`SelectionInput`
- SelectionInput for HTTP runtimes
`SelectionInput`
( Generally Available ): Columns are now generally available for Add-ons.
For more information refer to the following:
- Columns for Apps Script
`Columns`
- Columns for HTTP runtimes
`Columns`
## May 02, 2024
To subscribe to events using Apps Script, you can now use the Advanced Google Workspace Events service. For details, see the Apps Script reference documentation .
## April 30, 2024
The cancelDataRefresh() method has been added to the following classes of the Spreadsheet service:
`cancelDataRefresh()`
- DataSourceChart
`DataSourceChart`
- DataSourceFormula
`DataSourceFormula`
- DataSourcePivotTable
`DataSourcePivotTable`
- DataSourceSheet
`DataSourceSheet`
- DataSourceTable
`DataSourceTable`
The cancelDataRefresh() method cancels the data refresh associated with the object it's called on if the refresh is currently running.
`cancelDataRefresh()`
The cancelAllLinkedDataSourceObjectRefreshes() method has been added to the DataSource class. This method cancels all currently running refreshes of data source objects linked to the data source this method is called on.
`cancelAllLinkedDataSourceObjectRefreshes()`
`DataSource`
## April 22, 2024
(Generally Available) : Google Chat apps now support Google Apps Script's Card Service. If you've built your Chat app using Apps Script, you can use Card Service to build user interfaces such as card messages and dialogs. For more information, see the Card Service reference documentation .
## March 15, 2024
The default property for the TextButtonStyle enum in the Apps Script Card Service has been renamed from TEXT to OUTLINED to align with the Google Material 3 design system . Existing scripts that use the original default, TEXT , render the same as the new default, OUTLINED .
`TextButtonStyle`
`TEXT`
`OUTLINED`
`TEXT`
`OUTLINED`
## March 07, 2024
(Generally Available) : You can now delete multiple unused versions at the same time from the Project History page. Refer to Delete multiple versions .
## March 05, 2024
(Generally Available) : The LinkPreview class has been added to the Apps Script Card service. This class lets you control various aspects of link previews, including the smart chip title, the link preview title, and the link preview card.
`LinkPreview`
## February 29, 2024
The 200 version limit, first announced for new scripts on December 6, 2023 , has been extended to all script projects. If your existing script project already has more than 200 versions, after June 1, 2024 you won't be able to add a new version. To delete unused versions, refer to Delete a version .
## February 21, 2024
( Developer Preview ): Multiselect menus are now in Developer Preview for Add-ons.
For more information refer to the following:
- SelectionInput for Apps Script
`SelectionInput`
- SelectionInput for other runtimes
`SelectionInput`
( Developer Preview ): Columns are now in Developer Preview for Add-ons.
For more information refer to the following:
- Columns for Apps Script
`Columns`
- Columns for other runtimes
`Columns`
## February 20, 2024
(Developer Preview) : Google Chat apps now support Google Apps Script's Card Service. If you've built your Chat app using Apps Script, you can use Card Service to build user interfaces such as card messages and dialogs. For more information, see the Card Service reference documentation .
## January 24, 2024
( Generally Available ): Google Workspace Add-ons now support third-party resource creation from the @ menu in Google Docs. This feature is gradually rolling out over the next few weeks. To use this feature, see Create third-party resources from the @ menu .
## January 18, 2024
( Generally available ): Google Workspace Add-ons now support link previews in Google Sheets and Slides. To learn more, see Preview links with smart chips .
## December 13, 2023
( Generally available ): The setPersistValues(persistValues) method has been added to the Action class of the Card service . This means that you can now indicate whether form values are determined by the client's values or the server's values after an action response updates a form's card.
`setPersistValues(persistValues)`
`Action`
## December 11, 2023
( Generally Available ): You can now call version 3 of the Google Drive API from Apps Script with the advanced Drive service. To learn more, see Advanced Drive service .
## December 07, 2023
To fix a bug that prevented events of eventType != 'default' from importing, we updated the code sample in Populate a team vacation calendar , the popular Apps Script + Calendar API solution. Review the code change in GitHub .
`eventType != 'default'`
## December 06, 2023
( Generally available ): You can now delete versions in your Apps Script project from the project history page in the Apps Script IDE.
Script projects created after December 10, 2023 can have up to 200 versions. If your script reaches the versions limit, or you want to clean up your script project, delete undeployed versions that you no longer need.
To learn more, see Delete a version .
## November 15, 2023
( Developer Preview ) : Google Workspace Add-ons now support third-party resource creation from the @ menu in Google Docs. To use this feature, see Create third-party resources from the @ menu .
## November 13, 2023
(Developer Preview) : Available as part of the Google Workspace Developer Preview Program , which grants early access to certain features.
Google Workspace Add-ons now support link previews in Google Sheets and Slides. To learn more, see Preview links with smart chips .
## November 06, 2023
(Generally available) : You can now call the Chat API from Apps Script with the Advanced Chat Service. To learn how, see Advanced Chat Service in the Apps Script reference documentation.
We've also updated the Apps Script code samples to use the Advanced Chat Service in the following Chat API developer guides:
- Authenticate as an app
- Authenticate as a user
- Try it - Respond to Incidents
## September 26, 2023
The email address that sends notifications about errors in triggers has been updated from apps-scripts-notifications@google.com to noreply-apps-scripts-notifications@google.com .
`apps-scripts-notifications@google.com`
`noreply-apps-scripts-notifications@google.com`
## September 19, 2023
The classic Google Sites service has been deprecated due to the transition from classic Sites to new Sites . There isn't a way to connect to new Sites with Apps Script.
## August 23, 2023
You can now view previously deployed script versions and compare them to the current script version in the Apps Script IDE. Anyone who has edit permission on an Apps Script project can access the project history page. To learn more, refer to the following:
- Google Workspace Updates blog : View & compare script versions with Apps Script project history
Google Workspace Updates blog : View & compare script versions with Apps Script project history
- Developer documentation : Versions
Developer documentation : Versions
## June 12, 2023
Third-party smart chips and link previews are now generally available. To build a Google Workspace Add-on that uses this feature, see Preview links with smart chips .
## December 16, 2022
Apps Script has deprecated the Contacts service . Instead, use the People API advanced service . Refer to Migrate from Contacts service to People API advanced service .
The Contacts service shutdown has been rescheduled from April 2023 to January 2025. Refer to the Apps Script sunset schedule .
## November 03, 2022
Apps Script added a new method to the Utilities class . parseDate(date, timeZone, format ) parses a provided string date according to the specification described in the Java Standard Edition SimpleDateFormat class .
`parseDate(date, timeZone, format`
## November 01, 2022
Apps Script has sunset the following methods:
- getChatThreads()
`getChatThreads()`
- getChatThreads(start, max)
`getChatThreads(start, max)`
There isn't a replacement method to get this data with Apps Script.
Learn about the switch from Classic Hangouts to Chat .
## September 27, 2022
Apps Script has turned down the legacy integrated development environment (IDE) in favor of the redesigned IDE that launched in December 2020.
Learn more about the IDE updates from the following blog posts:
- Updated Apps Script integrated development environment will replace the legacy experience by Q4 2022 .
- Additional functionality for the Apps Script Integrated Development Environment (IDE) Script Editor .
- Use the new Apps Script Integrated Development Environment (IDE) Script Editor .
## July 19, 2022
Apps Script now automatically deletes default Google Cloud projects (Google Cloud projects that Apps Script creates in the background) when their associated scripts haven't run in 180 days or more. If the script runs after Apps Script deletes the default Google Cloud project, Apps Script creates one for the script.
This update doesn't affect standard Google Cloud projects (Google Cloud projects created by people).
## July 08, 2022
Apps Script has deprecated the following methods:
- getChatThreads()
`getChatThreads()`
- getChatThreads(start, max)
`getChatThreads(start, max)`
These methods will become unavailable later this year once Google switches all users from Classic Hangouts to Google Chat. There isn't a replacement method to get this data with Apps Script.
Learn about the switch from Classic Hangouts to Chat .
## June 06, 2022
You can now call functions in separate files before they're parsed. Previously, the V8 runtime required a script file to be parsed before any other file could call the functions it defines.
Now, the order of files in the Apps Script editor doesn't matter. This means that you can call a function in a different file to assign a value to a global variable—the function is always defined before it's called. This behavior reflects that of the legacy Rhino runtime.
## April 13, 2022
You can now perform the following actions in the new Apps Script integrated development environment (IDE):
- Create test deployments for Editor Add-ons .
- Add, edit, and delete script properties from the project settings page .
- Sort files alphabetically in the editor.
- Debug Rhino functions without migrating to the V8 runtime . If your code isn't V8 compatible, you might receive errors.
- Set the time zone for a script project .
## March 24, 2022
For Google Workspace Add-ons, an Attachment class has been added to the Card Service that lets you add custom attachments to Calendar events. You can also set an event trigger that fires when the user clicks on the add-on attachment provider in the Calendar dropdown menu. For more information, refer to EventAttachmentTrigger .
`Attachment`
`EventAttachmentTrigger`
## March 18, 2022
The get methods for several color objects in the Spreadsheet Service have been deprecated in favor of a new naming convention. The functionality remains the same. For example, the getFontColor() method from the Range class has been replaced with getFontColorObject() .
`get`
`getFontColor()`
`getFontColorObject()`
The following classes have updated get methods for color objects:
`get`
- Banding : getFirstColumnColor() is now getFirstColumnColorObject() . getFirstRowColor() is now getFirstRowColorObject() . getFooterColumnColor() is now getFooterColumnColor() . getFooterRowColor() is now getFooterRowColorObject() . getHeaderColumnColor() is now getHeaderColumnColorObject() . getHeaderRowColor() is now getHeaderRowColorObject() . getSecondColumnColor() is now getSecondColumnColorObject() . getSecondRowColor() is now getSecondRowColorObject() .
`Banding`
- getFirstColumnColor() is now getFirstColumnColorObject() .
`getFirstColumnColor()`
`getFirstColumnColorObject()`
- getFirstRowColor() is now getFirstRowColorObject() .
`getFirstRowColor()`
`getFirstRowColorObject()`
- getFooterColumnColor() is now getFooterColumnColor() .
`getFooterColumnColor()`
`getFooterColumnColor()`
- getFooterRowColor() is now getFooterRowColorObject() .
`getFooterRowColor()`
`getFooterRowColorObject()`
- getHeaderColumnColor() is now getHeaderColumnColorObject() .
`getHeaderColumnColor()`
`getHeaderColumnColorObject()`
- getHeaderRowColor() is now getHeaderRowColorObject() .
`getHeaderRowColor()`
`getHeaderRowColorObject()`
- getSecondColumnColor() is now getSecondColumnColorObject() .
`getSecondColumnColor()`
`getSecondColumnColorObject()`
- getSecondRowColor() is now getSecondRowColorObject() .
`getSecondRowColor()`
`getSecondRowColorObject()`
- BooleanCondition : getBackground() is now getBackgroundObject() . getFontColor() is now getFontColorObject() .
`BooleanCondition`
- getBackground() is now getBackgroundObject() .
`getBackground()`
`getBackgroundObject()`
- getFontColor() is now getFontColorObject() .
`getFontColor()`
`getFontColorObject()`
- GradientCondition : getMaxColor() is now getMaxColorObject . getMidColor() is now getMidColorObject . getMinColor() is now getMinColorObject .
`GradientCondition`
- getMaxColor() is now getMaxColorObject .
`getMaxColor()`
`getMaxColorObject`
- getMidColor() is now getMidColorObject .
`getMidColor()`
`getMidColorObject`
- getMinColor() is now getMinColorObject .
`getMinColor()`
`getMinColorObject`
- Range : getFontColor() is now getFontColorObject() . getFontColors() is now getFontColorObjects() .
`Range`
- getFontColor() is now getFontColorObject() .
`getFontColor()`
`getFontColorObject()`
- getFontColors() is now getFontColorObjects() .
`getFontColors()`
`getFontColorObjects()`
- Sheet : getTabColor() is now getTabColorObject .
`Sheet`
- getTabColor() is now getTabColorObject .
`getTabColor()`
`getTabColorObject`
- Slicer : getBackgroundColor() is now getBackgroundColorObject() .
`Slicer`
- getBackgroundColor() is now getBackgroundColorObject() .
`getBackgroundColor()`
`getBackgroundColorObject()`
## February 14, 2022
Owners receive email alerts when someone outside the owner's organization edits a script project in the new integrated development environment (IDE).
- For container-bound scripts : If someone outside the container owner's organization creates or edits a container-bound script project, the container owner receives an email notification.
For container-bound scripts : If someone outside the container owner's organization creates or edits a container-bound script project, the container owner receives an email notification.
- For standalone scripts : If someone outside the script project owner's organization edits a standalone script project, the script project owner receives an email notification.
For standalone scripts : If someone outside the script project owner's organization edits a standalone script project, the script project owner receives an email notification.
## January 19, 2022
The following classes have been added to the Spreadsheet Service to let you add images to cells:
- CellImageBuilder : This builder creates the image value needed to add an image to a cell.
`CellImageBuilder`
- CellImage : Represents an image to add to a cell.
`CellImage`
To add an image to a cell, you must create a new image value for the image using SpreadsheetApp.newCellImage() and CellImageBuilder . Then, use Range.setValue(value) or Range.setValues(values) to add the image value to the cell.
`SpreadsheetApp.newCellImage()`
`CellImageBuilder`
`Range.setValue(value)`
`Range.setValues(values)`
## December 15, 2021
Versions 1.0 and 1.1 of the TLS security protocol are disabled. To establish JDBC connections, use TLS 1.2 or higher.
## September 01, 2021
In the HTML Service iframe sandbox, allow-top-navigation , which allows the content to navigate its top-level browsing context, is restricted and not set as an attribute in the sandbox. Instead, the allow-top-navigation-by-user-activation attribute has been added to the sandbox.
`allow-top-navigation`
`allow-top-navigation-by-user-activation`
If you need to redirect your script, add a link or a button for the user to take action on.
Learn more about HMTL Service restrictions .
## August 31, 2021
The Drive Service has added three new methods to the file and folder classes to manage the use of resource keys when sharing files and folders.
- getSecurityUpdateEligible() : Gets whether a file for folder is eligible to apply the security update that requires a resource key for access when it's shared using a link.
`getSecurityUpdateEligible()`
- getSecurityUpdateEnabled() : Gets whether a file or folder requires a resource key for access when it's shared using a link.
`getSecurityUpdateEnabled()`
- setSecurityUpdateEnabled(enabled) : Sets whether the file or folder requires a resource key for access when it's shared using a link.
`setSecurityUpdateEnabled(enabled)`
Learn more about the resource key security update for Drive .
## August 23, 2021
The Document Service has added support for smart chips by adding three new classes:
- Date - An element representing a formatted date.
- Person - An element representing a link to a person.
- RichLink - An element representing a link to a Google resource, such as a Drive file or a YouTube video.
Learn more about smart chips in Google Docs .
## August 09, 2021
The Microsoft SQL Server JDBC driver was updated to version 7.2.1. If you encounter issues, report them on the issue tracker . If you're an administrator and need live support, contact Google Workspace support .
## June 01, 2021
A new divider widget has been added for Google Workspace Add-ons. To add a divider to an add-on card, use the newDivider() method within the Card service .
`newDivider()`
## May 27, 2021
A new method has been added to the Sheet class of the Spreadsheet service . setRowHeightsForced(startRow, numRows, height) lets you manually set the height for a row or a set of rows.
`Sheet`
`Spreadsheet`
`setRowHeightsForced(startRow, numRows, height)`
## March 15, 2021
The following updates have been made to deployments in the new editor:
- You can now have more than one active deployment.
- You can now change the version associated with an active deployment.
To learn more, see Create and manage deployments .
## December 07, 2020
The Apps Script integrated development environment, or IDE, has been fully redesigned. Along with a completely new interface, the following features have been updated:
- The editor now has a collapsible left sidebar to navigate to the Apps Script project overview, settings, executions, and triggers.
- The editor's resources panel now includes files, advanced services, and libraries.
- Autoformatting has been added to the editor.
- Autocomplete in the editor has been enhanced to be faster, more consistent, and extends its support to user-defined functions and JavaScript language features. You can add JSDoc to your functions for better autocomplete suggestions.
- The editor now supports codeblock and function collapsing.
- Keyboard shortcuts and a Command Palette has been added to the editor. Press F1 to view the Command Palette and available keyboard shortcuts.
- The editor now includes a contextual right-click menu with options such as Go To Symbol, Rename Symbols, and Command Palette.
- Enhancements have been made to the debugger's performance and speed.
- Logs now stream in real-time as you run a script.
- The deployments dialog auto-detects the deployment types from the script project's manifest. You can change or add more types as needed.
- Deployments have been merged with versions. Each time you create a new deployment, a new version is automatically created. clasp users are unaffected by this change.
- A single deployment can be an add-on deployment , web app, library, or API executable. Any deployment can be used as a library.
- Now only one deployment can be active at a time. This change doesn't affect existing active deployments. clasp users are unaffected by this change.
- You can no longer explicitly deactivate published web apps. Instead, delete the deployment that has the web app. To reactivate the web app, deploy it again.
- The debugger is no longer supported in the Rhino runtime. To use the debugger, migrate your script to the V8 runtime .
- Testing Editor Add-ons is not yet supported in this release and will be added in 2021. To test Editor Add-ons, switch back to the legacy IDE.
To switch back to the legacy IDE from within the editor, at the top, click Use legacy editor .
## October 23, 2020
An advanced service for Google Tables has been added to Apps Script. The Tables service allows scripts to programmatically read and edit rows within Tables .
`Tables`
`Tables`
## September 03, 2020
New classes and methods have been added to support Connected Sheets .
The following new classes have been added to the Spreadsheet service :
`Spreadsheet`
- DataSourceChart
`DataSourceChart`
- DataSourceColumn
`DataSourceColumn`
- DataSourceFormula
`DataSourceFormula`
- DataSourcePivotTable
`DataSourcePivotTable`
- DataSourceRefreshSchedule
`DataSourceRefreshSchedule`
- DataSourceRefreshScheduleFrequency
`DataSourceRefreshScheduleFrequency`
- DataSourceSheet
`DataSourceSheet`
- DataSourceSheetFilter
`DataSourceSheetFilter`
- DataSourceTableColumn
`DataSourceTableColumn`
- DataSourceTableFilter
`DataSourceTableFilter`
- DateTimeGroupingRule
`DateTimeGroupingRule`
- PivotGroupLimit
`PivotGroupLimit`
- SortSpec
`SortSpec`
New methods to support Connected Sheets have been added to the following classes in the Spreadsheet service :
`Spreadsheet`
- BigQueryDataSourceSpecBuilder
`BigQueryDataSourceSpecBuilder`
- BigQueryDataSourceSpec
`BigQueryDataSourceSpec`
- DataExecutionStatus
`DataExecutionStatus`
- DataSourceTable
`DataSourceTable`
- DataSource
`DataSource`
- EmbeddedChart
`EmbeddedChart`
- FilterCriteriaBuilder
`FilterCriteriaBuilder`
- `PivotFilter
- PivotGroup
`PivotGroup`
- PivotTable
`PivotTable`
- PivotValue
`PivotValue`
- Range
`Range`
- Sheet
`Sheet`
- SpreadsheetApp
`SpreadsheetApp`
- Spreadsheet
`Spreadsheet`
## August 27, 2020
A new class called DecoratedText has been added to the Card Service . DecoratedText adds text with optional decorations and was added to replace the KeyValue class .
`DecoratedText`
`DecoratedText`
`KeyValue`
## July 27, 2020
The following Folder class methods have been deprecated :
`Folder`
- addFile(File)
`addFile(File)`
- addFolder(Folder)
`addFolder(Folder)`
- removeFile(File)
`removeFile(File)`
- removeFolder(Folder)
`removeFolder(Folder)`
To help simplify Google Drive's folder structure and sharing models , new methods have been added to the Drive service and some existing methods have been deprecated.
`Drive`
The DriveApp now has an enforceSingleParent(value) method that enables or disables enforceSingleParent behavior.
`DriveApp`
`enforceSingleParent(value)`
`enforceSingleParent`
- The File class now has the following methods: file.getTargetId() : Gets a shortcut's file ID. file.getTargetMimeType() : Returns the mime type of the item a shortcut points to. file.moveTo(destination) : Moves a file to a specified destination folder.
The File class now has the following methods:
`File`
- file.getTargetId() : Gets a shortcut's file ID.
`file.getTargetId()`
- file.getTargetMimeType() : Returns the mime type of the item a shortcut points to.
`file.getTargetMimeType()`
- file.moveTo(destination) : Moves a file to a specified destination folder.
`file.moveTo(destination)`
The Folder class now has the following methods:
`Folder`
- folder.createShortcut(targetId) : Creates a shortcut to the provided Drive item ID, and returns it.
`folder.createShortcut(targetId)`
- folder.moveTo(destination) : Moves an item to the provided destination folder.
`folder.moveTo(destination)`
## June 12, 2020
New methods have been added to the Spreadsheet service :
`Spreadsheet`
- The RichTextValue class now has a RichTextValue.getLinkUrl() method that gets the URL of the specified value.
`RichTextValue`
`RichTextValue.getLinkUrl()`
- The RichTextValueBuilder class now has a RichTextValueBuilder.setLinkUrl() method that sets the link URL for the specified value.
`RichTextValueBuilder`
`RichTextValueBuilder.setLinkUrl()`
- The PivotTable class now has a PivotTable.getSourceDataRange() method that returns the source data range on which the pivot table is constructed.
`PivotTable`
`PivotTable.getSourceDataRange()`
- The PivotValue class now has a PivotValue.remove() method that removes the value from the pivot table.
`PivotValue`
`PivotValue.remove()`
## April 22, 2020
A new simple trigger, onSelectionChange(e) , has been added for Google Sheets. The onSelectionChange(e) trigger runs automatically when a user changes the selection in a spreadsheet.
`onSelectionChange(e)`
`onSelectionChange(e)`
## April 02, 2020
The following has been added to the Spreadsheet service :
- A new Drawing class has been added to support drawings.
`Drawing`
- You can now get your drawings with the Sheet.getDrawings() method .
`Sheet.getDrawings()`
The following has been added to the Drive service :
- There's a new FILE_ORGANIZER value in the Permission enum . If you have FILE_ORGANIZER permission on a shared drive, you can edit, trash, and move content within that drive.
`FILE_ORGANIZER`
`Permission`
`FILE_ORGANIZER`
## February 28, 2020
The following methods have been added to the Spreadsheet service to support the use of theme colors. Many of these methods duplicate the effect of existing color methods, but let you use Color objects instead of strings as parameters and return types:
`Color`
- The Banding class now has 16 new methods that manipulate color in the banding columns and rows using Color objects.
`Banding`
`Color`
- The BooleanCondition class now has two new methods that retrieve the color of the condition's background and font as Color objects.
`BooleanCondition`
`Color`
- The ConditionalFormatRuleBuilder class now has seven new methods that set color-based format rules using Color objects.
`ConditionalFormatRuleBuilder`
`Color`
- The GradientCondition class now has three new methods that retrieve condition colors as Color objects.
`GradientCondition`
`Color`
- The Range class now has eight new methods that get and set font and background colors using Color objects.
`Range`
`Color`
- The Sheet class now has two new methods that get and set tab colors using Color objects.
`Sheet`
`Color`
- The Slicer class now has two new methods that get and set the background color of the slicer using Color objects.
`Slicer`
`Color`
- The TextStyleBuilder class now has a TextStyleBuilder.setForegroundColorObject(color) method that updates the foreground color of the style builder using a Color object.
`TextStyleBuilder`
`TextStyleBuilder.setForegroundColorObject(color)`
`Color`
- The TextStyle class now has a TextStyle.getForegroundColorObject() method that gets the foreground color of the style as a Color object.
`TextStyle`
`TextStyle.getForegroundColorObject()`
`Color`
## February 05, 2020
Apps Script now supports the V8 runtime . This enables modern JavaScript features and syntax in Apps Script. You can migrate existing scripts to use V8 and its features.
## January 21, 2020
To support the launch of G Suite Add-ons , the following manifest changes, service, classes, and methods have been added to Add-ons:
- The add-ons manifest structure has been updated to provide configuration controls for G Suite Add-ons. All add-on manifest settings are specified in the AddOns object in the manifest. Manifest fields that previously supported Gmail add-ons still exist, but are now deprecated. See Upgrading your published add-ons for instructions on how to upgrade a Gmail add-on into a G Suite add-on.
The add-ons manifest structure has been updated to provide configuration controls for G Suite Add-ons. All add-on manifest settings are specified in the AddOns object in the manifest. Manifest fields that previously supported Gmail add-ons still exist, but are now deprecated. See Upgrading your published add-ons for instructions on how to upgrade a Gmail add-on into a G Suite add-on.
`AddOns`
- The Card service has been extended with the following classes and methods that provide new widgets and event responses: CalendarEventActionResponse CalendarEventActionResponseBuilder DatePicker DateTimePicker DisplayStyle DriveItemsSelectedActionResponse DriveItemsSelectedActionResponseBuilder FixedFooter SwitchControlType TimePicker CardBuilder.setDisplayStyle(displayStyle) CardBuilder.setFixedFooter(fixedFooter) CardBuilder.setPeekCardHeader(peekCardHeader) CardService.newCalendarEventActionResponseBuilder() CardService.newDatePicker() CardService.newDateTimePicker() CardService.newDriveItemsSelectedActionResponseBuilder() CardService.newFixedFooter() CardService.newTimePicker() Switch.setControlType(controlType)
The Card service has been extended with the following classes and methods that provide new widgets and event responses:
- CalendarEventActionResponse
`CalendarEventActionResponse`
- CalendarEventActionResponseBuilder
`CalendarEventActionResponseBuilder`
- DatePicker
`DatePicker`
- DateTimePicker
`DateTimePicker`
- DisplayStyle
`DisplayStyle`
- DriveItemsSelectedActionResponse
`DriveItemsSelectedActionResponse`
- DriveItemsSelectedActionResponseBuilder
`DriveItemsSelectedActionResponseBuilder`
- FixedFooter
`FixedFooter`
- SwitchControlType
`SwitchControlType`
- TimePicker
`TimePicker`
- CardBuilder.setDisplayStyle(displayStyle)
`CardBuilder.setDisplayStyle(displayStyle)`
- CardBuilder.setFixedFooter(fixedFooter)
`CardBuilder.setFixedFooter(fixedFooter)`
- CardBuilder.setPeekCardHeader(peekCardHeader)
`CardBuilder.setPeekCardHeader(peekCardHeader)`
- CardService.newCalendarEventActionResponseBuilder()
`CardService.newCalendarEventActionResponseBuilder()`
- CardService.newDatePicker()
`CardService.newDatePicker()`
- CardService.newDateTimePicker()
`CardService.newDateTimePicker()`
- CardService.newDriveItemsSelectedActionResponseBuilder()
`CardService.newDriveItemsSelectedActionResponseBuilder()`
- CardService.newFixedFooter()
`CardService.newFixedFooter()`
- CardService.newTimePicker()
`CardService.newTimePicker()`
- Switch.setControlType(controlType)
`Switch.setControlType(controlType)`
The Conference Data service has been added to Apps Script. The service helps G Suite Add-ons that extend Google Calendar to stay in sync with third-party conferencing applications. This service is only useful to developers who manage a conferencing application and want to make it available in Google Calendar.
## December 18, 2019
The Spreadsheet service has been extended with the following class and new methods to support using color building and theme colors:
- Color
`Color`
- ColorBuilder
`ColorBuilder`
- SpreadsheetTheme
`SpreadsheetTheme`
- ThemeColor
`ThemeColor`
- ThemeColorType
`ThemeColorType`
- SpreadsheetApp.newColor()
`SpreadsheetApp.newColor()`
- Spreadsheet.getPredefinedSpreadsheetThemes()
`Spreadsheet.getPredefinedSpreadsheetThemes()`
- Spreadsheet.getSpreadsheetTheme()
`Spreadsheet.getSpreadsheetTheme()`
- Spreadsheet.resetSpreadsheetTheme()
`Spreadsheet.resetSpreadsheetTheme()`
- Spreadsheet.setSpreadsheetTheme(theme)
`Spreadsheet.setSpreadsheetTheme(theme)`
## December 11, 2019
The Data Studio service has been extended with the following class and new methods to support different response types and dynamic statuses:
- GetDataResponse
`GetDataResponse`
- GetSchemaResponse
`GetSchemaResponse`
- SetCredentialsResponse
`SetCredentialsResponse`
- Checkbox.setIsDynamic(isDynamic)
`Checkbox.setIsDynamic(isDynamic)`
- CommunityConnector.newGetDataResponse()
`CommunityConnector.newGetDataResponse()`
- CommunityConnector.newGetSchemaResponse()
`CommunityConnector.newGetSchemaResponse()`
- CommunityConnector.newSetCredentialsResponse()
`CommunityConnector.newSetCredentialsResponse()`
- Config.setIsSteppedConfig(isSteppedConfig)
`Config.setIsSteppedConfig(isSteppedConfig)`
- SelectMultiple.setIsDynamic(isDynamic)
`SelectMultiple.setIsDynamic(isDynamic)`
- SelectSingle.setIsDynamic(isDynamic)
`SelectSingle.setIsDynamic(isDynamic)`
- TextArea.setIsDynamic(isDynamic)
`TextArea.setIsDynamic(isDynamic)`
- TextInput.setIsDynamic(isDynamic)
`TextInput.setIsDynamic(isDynamic)`
## November 06, 2019
The Spreadsheet service has been extended with the following class and new methods to support using slicers to filter ranges, charts, and pivot tables:
- Slicer
`Slicer`
- Sheet.getSlicers()
`Sheet.getSlicers()`
- Sheet.insertSlicer(range, anchorRowPos, anchorColPos)
`Sheet.insertSlicer(range, anchorRowPos, anchorColPos)`
- Sheet.insertSlicer(range, anchorRowPos, anchorColPos, offsetX, offsetY)
`Sheet.insertSlicer(range, anchorRowPos, anchorColPos, offsetX, offsetY)`
The Script service has been extended with the ScriptApp.getIdentityToken() method , which returns an identity token for the effective user.
`ScriptApp.getIdentityToken()`
## October 28, 2019
You can no longer publish web apps to the Chrome Web Store. The Chrome Web Store deprecated Chrome apps in 2016 and they are now only available for ChromeOS devices. This change includes published Apps Script web apps. Previously published web apps are no longer discoverable in the Chrome Web Store. Editor Add-ons aren't affected; you can still publish Editor Add-ons to the Chrome Web Store.
## October 23, 2019
Several classes and methods relating to the now shutdown UiApp service have been removed. Most of these methods involved interactions between the Charts service and UiApp that were very seldom used. The following is a full list of the removed classes and methods:
`UiApp`
- Charts service CategoryFilterBuilder Control DashboardPanel DashboardPanelBuilder Chart.getId() Chart.getType() Charts.newCategoryFilter() Charts.newDashboardPanel() Charts.newNumberRangeFilter() Charts.newStringFilter() NumberRangeFilterBuilder.build() NumberRangeFilterBuilder.setDataTable(tableBuilder) NumberRangeFilterBuilder.setDataTable(table) NumberRangeFilterBuilder.setFilterColumnIndex(columnIndex) NumberRangeFilterBuilder.setFilterColumnLabel(columnLabel) NumberRangeFilterBuilder.setLabel(label) NumberRangeFilterBuilder.setLabelSeparator(labelSeparator) NumberRangeFilterBuilder.setLabelStacking(orientation) StringFilterBuilder.build() StringFilterBuilder.setDataTable(tableBuilder) StringFilterBuilder.setDataTable(table) StringFilterBuilder.setFilterColumnIndex(columnIndex) StringFilterBuilder.setFilterColumnLabel(columnLabel) StringFilterBuilder.setLabel(label) StringFilterBuilder.setLabelSeparator(labelSeparator) StringFilterBuilder.setLabelStacking(orientation)
- CategoryFilterBuilder
`CategoryFilterBuilder`
- Control
`Control`
- DashboardPanel
`DashboardPanel`
- DashboardPanelBuilder
`DashboardPanelBuilder`
- Chart.getId()
`Chart.getId()`
- Chart.getType()
`Chart.getType()`
- Charts.newCategoryFilter()
`Charts.newCategoryFilter()`
- Charts.newDashboardPanel()
`Charts.newDashboardPanel()`
- Charts.newNumberRangeFilter()
`Charts.newNumberRangeFilter()`
- Charts.newStringFilter()
`Charts.newStringFilter()`
- NumberRangeFilterBuilder.build()
`NumberRangeFilterBuilder.build()`
- NumberRangeFilterBuilder.setDataTable(tableBuilder)
`NumberRangeFilterBuilder.setDataTable(tableBuilder)`
- NumberRangeFilterBuilder.setDataTable(table)
`NumberRangeFilterBuilder.setDataTable(table)`
- NumberRangeFilterBuilder.setFilterColumnIndex(columnIndex)
`NumberRangeFilterBuilder.setFilterColumnIndex(columnIndex)`
- NumberRangeFilterBuilder.setFilterColumnLabel(columnLabel)
`NumberRangeFilterBuilder.setFilterColumnLabel(columnLabel)`
- NumberRangeFilterBuilder.setLabel(label)
`NumberRangeFilterBuilder.setLabel(label)`
- NumberRangeFilterBuilder.setLabelSeparator(labelSeparator)
`NumberRangeFilterBuilder.setLabelSeparator(labelSeparator)`
- NumberRangeFilterBuilder.setLabelStacking(orientation)
`NumberRangeFilterBuilder.setLabelStacking(orientation)`
- StringFilterBuilder.build()
`StringFilterBuilder.build()`
- StringFilterBuilder.setDataTable(tableBuilder)
`StringFilterBuilder.setDataTable(tableBuilder)`
- StringFilterBuilder.setDataTable(table)
`StringFilterBuilder.setDataTable(table)`
- StringFilterBuilder.setFilterColumnIndex(columnIndex)
`StringFilterBuilder.setFilterColumnIndex(columnIndex)`
- StringFilterBuilder.setFilterColumnLabel(columnLabel)
`StringFilterBuilder.setFilterColumnLabel(columnLabel)`
- StringFilterBuilder.setLabel(label)
`StringFilterBuilder.setLabel(label)`
- StringFilterBuilder.setLabelSeparator(labelSeparator)
`StringFilterBuilder.setLabelSeparator(labelSeparator)`
- StringFilterBuilder.setLabelStacking(orientation)
`StringFilterBuilder.setLabelStacking(orientation)`
- Spreadsheet service EmbeddedChart.getId() EmbeddedChart.getType() EmbeddedChart.setId(id)
- EmbeddedChart.getId()
`EmbeddedChart.getId()`
- EmbeddedChart.getType()
`EmbeddedChart.getType()`
- EmbeddedChart.setId(id)
`EmbeddedChart.setId(id)`
The Slides service class RgbColor and the enumeration ColorType have been moved from the Slides service to the [Base script service](https://developers.google.com/apps-script/reference/base). The functionality of these classes has not changed. Moving these classes to the Base script service enables other services to make use of them in the future. You can now find the documentation for these classes at [ RgbColor ](https://developers.google.com/apps-script/reference/base/rgb-color) and [ ColorType`](https://developers.google.com/apps-script/reference/base/color-type).
`RgbColor`
`ColorType have been moved from the Slides service to the [Base script service](https://developers.google.com/apps-script/reference/base). The functionality of these classes has not changed. Moving these classes to the Base script service enables other services to make use of them in the future. You can now find the documentation for these classes at [`
`](https://developers.google.com/apps-script/reference/base/rgb-color) and [`
## September 09, 2019
The Card service methods CardHeader.setUrl(url) and Image.setUrl(url) have been updated to accept an encoded image data string as an input parameter. As before, you can alternatively use a publicly-available image URL as the input parameter.
`CardHeader.setUrl(url)`
`Image.setUrl(url)`
## August 07, 2019
Documentation for the UI service has been removed. This service was deprecated in December 2014 and officially shut down on July 15, 2019 . To build interfaces for web apps and Editor Add-ons, use the HTML service .
## July 26, 2019
- The Group service has been updated with the Groups.getRoles(user) method that can determine the list of roles a specific user in a group has.
`Groups.getRoles(user)`
- The Slides service has been extended with the following new methods to support concrete color schemes: ColorScheme.setConcreteColor(type, color) ColorScheme.setConcreteColor(type, red, green, blue) ColorScheme.setConcreteColor(type, hexColor)
- ColorScheme.setConcreteColor(type, color)
`ColorScheme.setConcreteColor(type, color)`
- ColorScheme.setConcreteColor(type, red, green, blue)
`ColorScheme.setConcreteColor(type, red, green, blue)`
- ColorScheme.setConcreteColor(type, hexColor)
`ColorScheme.setConcreteColor(type, hexColor)`
- The Spreadsheet service has been extended with the following new methods to support trimming whitespace and removing duplicate values: RangeList.trimWhitespace() Range.removeDuplicates() Range.removeDuplicates(columnsToCompare) Range.trimWhitespace()
- RangeList.trimWhitespace()
`RangeList.trimWhitespace()`
- Range.removeDuplicates()
`Range.removeDuplicates()`
- Range.removeDuplicates(columnsToCompare)
`Range.removeDuplicates(columnsToCompare)`
- Range.trimWhitespace()
`Range.trimWhitespace()`
## May 20, 2019
- The Gmail service has been updated with the GmailMessage.getHeader(name) method that can retrieve a RFC 2822 header from a message.
`GmailMessage.getHeader(name)`
- The Optimization service has been updated with the following batch methods: LinearOptimizationEngine.addContraints(lowerBounds, upperBounds, variableNames, coefficients) LinearOptimizationEngine.addVariables(names, lowerBounds, upperBounds, types, objectiveCoeffients)
- LinearOptimizationEngine.addContraints(lowerBounds, upperBounds, variableNames, coefficients)
`LinearOptimizationEngine.addContraints(lowerBounds, upperBounds, variableNames, coefficients)`
- LinearOptimizationEngine.addVariables(names, lowerBounds, upperBounds, types, objectiveCoeffients)
`LinearOptimizationEngine.addVariables(names, lowerBounds, upperBounds, types, objectiveCoeffients)`
## May 03, 2019
The Document service has been updated to add methods to get and set the language of a document:
- Document.getLanguage()
`Document.getLanguage()`
- Document.getSupportedLanguageCodes()
`Document.getSupportedLanguageCodes()`
- Document.setLanguage(languageCode)
`Document.setLanguage(languageCode)`
## April 19, 2019
The Data Studio service has been updated to add a few values to FieldType enum :
`FieldType`
- HYPERLINK
`HYPERLINK`
- IMAGE
`IMAGE`
- IMAGE_LINK
`IMAGE_LINK`
## April 08, 2019
The behavior of the Google Cloud (GCP) projects used by scripts has been altered. Now, the default GCP projects that Apps Script creates for new scripts are hidden and script owners can't access them directly. Admins and domain users with the resourcemanager.projects.list permission on the parenting GCP folder can still access default GCP projects.
`resourcemanager.projects.list`
If you need access to a script's GCP project (because you wish to publish it or take a similar action), it's best to switch your script to use a standard GCP project .
## April 05, 2019
- The Spreadsheet service has been extended with the following new classes and methods to support text finding, checkboxes, and other features: TextFinder RecalculationInterval SheetType DataValidationBuilder.requireCheckbox() DataValidationBuilder.requireCheckbox(checkedValue) DataValidationBuilder.requireCheckbox(checkedValue, uncheckedValue) A clearRanges() method has been added to the all the embedded chart type builder classes, such as EmbeddedAreaChartBuilder.clearRanges() EmbeddedChart.getChartId() RangeList.check() RangeList.insertCheckboxes() RangeList.insertCheckboxes(checkedValue) RangeList.insertCheckboxes(checkedValue, uncheckedValue) RangeList.removeCheckboxes() RangeList.uncheck() Range.check() Range.createTextFinder(findText) Range.getDataRegion() Range.getDataRegion(dimension) Range.insertCheckboxes() Range.insertCheckboxes(checkedValue) Range.insertCheckboxes(checkedValue, uncheckedValue) Range.removeCheckboxes() Range.uncheck() Sheet.createTextFinder(findText) Sheet.getType() Spreadsheet.createTextFinder(findText) Spreadsheet.getIterativeCalculationConvergenceThreshold() Spreadsheet.getMaxIterativeCalculationCycles() Spreadsheet.getRecalculationInterval() Spreadsheet.isIterativeCalculationEnabled() Spreadsheet.moveChartToObjectSheet(chart) Spreadsheet.setIterativeCalculationConvergenceThreshold(minThreshold) Spreadsheet.setIterativeCalculationEnabled(isEnabled) Spreadsheet.setMaxIterativeCalculationCycles(maxIterations) Spreadsheet.setRecalculationInterval(recalculationInterval)
- TextFinder
`TextFinder`
- RecalculationInterval
`RecalculationInterval`
- SheetType
`SheetType`
- DataValidationBuilder.requireCheckbox()
`DataValidationBuilder.requireCheckbox()`
- DataValidationBuilder.requireCheckbox(checkedValue)
`DataValidationBuilder.requireCheckbox(checkedValue)`
- DataValidationBuilder.requireCheckbox(checkedValue, uncheckedValue)
`DataValidationBuilder.requireCheckbox(checkedValue, uncheckedValue)`
- A clearRanges() method has been added to the all the embedded chart type builder classes, such as EmbeddedAreaChartBuilder.clearRanges()
`clearRanges()`
`EmbeddedAreaChartBuilder.clearRanges()`
- EmbeddedChart.getChartId()
`EmbeddedChart.getChartId()`
- RangeList.check()
`RangeList.check()`
- RangeList.insertCheckboxes()
`RangeList.insertCheckboxes()`
- RangeList.insertCheckboxes(checkedValue)
`RangeList.insertCheckboxes(checkedValue)`
- RangeList.insertCheckboxes(checkedValue, uncheckedValue)
`RangeList.insertCheckboxes(checkedValue, uncheckedValue)`
- RangeList.removeCheckboxes()
`RangeList.removeCheckboxes()`
- RangeList.uncheck()
`RangeList.uncheck()`
- Range.check()
`Range.check()`
- Range.createTextFinder(findText)
`Range.createTextFinder(findText)`
- Range.getDataRegion()
`Range.getDataRegion()`
- Range.getDataRegion(dimension)
`Range.getDataRegion(dimension)`
- Range.insertCheckboxes()
`Range.insertCheckboxes()`
- Range.insertCheckboxes(checkedValue)
`Range.insertCheckboxes(checkedValue)`
- Range.insertCheckboxes(checkedValue, uncheckedValue)
`Range.insertCheckboxes(checkedValue, uncheckedValue)`
- Range.removeCheckboxes()
`Range.removeCheckboxes()`
- Range.uncheck()
`Range.uncheck()`
- Sheet.createTextFinder(findText)
`Sheet.createTextFinder(findText)`
- Sheet.getType()
`Sheet.getType()`
- Spreadsheet.createTextFinder(findText)
`Spreadsheet.createTextFinder(findText)`
- Spreadsheet.getIterativeCalculationConvergenceThreshold()
`Spreadsheet.getIterativeCalculationConvergenceThreshold()`
- Spreadsheet.getMaxIterativeCalculationCycles()
`Spreadsheet.getMaxIterativeCalculationCycles()`
- Spreadsheet.getRecalculationInterval()
`Spreadsheet.getRecalculationInterval()`
- Spreadsheet.isIterativeCalculationEnabled()
`Spreadsheet.isIterativeCalculationEnabled()`
- Spreadsheet.moveChartToObjectSheet(chart)
`Spreadsheet.moveChartToObjectSheet(chart)`
- Spreadsheet.setIterativeCalculationConvergenceThreshold(minThreshold)
`Spreadsheet.setIterativeCalculationConvergenceThreshold(minThreshold)`
- Spreadsheet.setIterativeCalculationEnabled(isEnabled)
`Spreadsheet.setIterativeCalculationEnabled(isEnabled)`
- Spreadsheet.setMaxIterativeCalculationCycles(maxIterations)
`Spreadsheet.setMaxIterativeCalculationCycles(maxIterations)`
- Spreadsheet.setRecalculationInterval(recalculationInterval)
`Spreadsheet.setRecalculationInterval(recalculationInterval)`
- The Data Studio service has been extended with the following new classes and methods that support configuring BigQuery connectors: BigQueryConfig BigQueryParameterType CommunityConnector.newBigQueryConfig()
- BigQueryConfig
`BigQueryConfig`
- BigQueryParameterType
`BigQueryParameterType`
- CommunityConnector.newBigQueryConfig()
`CommunityConnector.newBigQueryConfig()`
- The Notification objects in the Card service no longer have a type that you must set. Calls to the now removed Notification.setType(type) method result in a no-op.
`Notification`
`Notification.setType(type)`
## February 26, 2019
- The Spreadsheet service has been extended with the following new classes and methods to support BigQuery data connectors in Sheets : BigQueryDataSourceSpec BigQueryDataSourceSpecBuilder DataExecutionErrorCode DataExecutionState DataExecutionStatus DataSourceParameterType DataSourceParameter DataSourceSpecBuilder DataSourceSpec DataSourceTable DataSourceType DataSource Range.getDataSourceTables() Sheet.getDataSourceTables() `SpreadsheetApp.enableAllDataSourcesExecution() SpreadsheetApp.enableBigQueryExecution() SpreadsheetApp.newDataSourceSpec() Spreadsheet.getDataSourceTables() Spreadsheet.insertSheetWithDataSourceTable(spec)
The Spreadsheet service has been extended with the following new classes and methods to support BigQuery data connectors in Sheets :
- BigQueryDataSourceSpec
`BigQueryDataSourceSpec`
- BigQueryDataSourceSpecBuilder
`BigQueryDataSourceSpecBuilder`
- DataExecutionErrorCode
`DataExecutionErrorCode`
- DataExecutionState
`DataExecutionState`
- DataExecutionStatus
`DataExecutionStatus`
- DataSourceParameterType
`DataSourceParameterType`
- DataSourceParameter
`DataSourceParameter`
- DataSourceSpecBuilder
`DataSourceSpecBuilder`
- DataSourceSpec
`DataSourceSpec`
- DataSourceTable
`DataSourceTable`
- DataSourceType
`DataSourceType`
- DataSource
`DataSource`
- Range.getDataSourceTables()
`Range.getDataSourceTables()`
- Sheet.getDataSourceTables()
`Sheet.getDataSourceTables()`
- `SpreadsheetApp.enableAllDataSourcesExecution()
- SpreadsheetApp.enableBigQueryExecution()
`SpreadsheetApp.enableBigQueryExecution()`
- SpreadsheetApp.newDataSourceSpec()
`SpreadsheetApp.newDataSourceSpec()`
- Spreadsheet.getDataSourceTables()
`Spreadsheet.getDataSourceTables()`
- Spreadsheet.insertSheetWithDataSourceTable(spec)
`Spreadsheet.insertSheetWithDataSourceTable(spec)`
- The Data Studio service has been extended with the following new methods involving reaggregation settings: Field.getIsReaggregatable() Field.setIsReaggregatable(isReaggregatable)
The Data Studio service has been extended with the following new methods involving reaggregation settings:
- Field.getIsReaggregatable()
`Field.getIsReaggregatable()`
- Field.setIsReaggregatable(isReaggregatable)
`Field.setIsReaggregatable(isReaggregatable)`
## January 22, 2019
The deprecated UiApp service will be officially shutdown on July 15th, 2019. After this date, the service will no longer function for any script project.
- The Spreadsheet service has been extended with the following new classes and methods to support text styles and Rich Text cell formatting: RichTextValue RichTextValueBuilder TextStyle TextStyleBuilder Range.getRichTextValue() Range.getRichTextValues() Range.getTextStyle() Range.getTextStyles() Range.setRichTextValue(value) Range.setRichTextValues(values) Range.setTextStyle(style) Range.setTextStyles(styles) SpreadsheetApp.newRichTextValue() SpreadsheetApp.newTextStyle()
- RichTextValue
`RichTextValue`
- RichTextValueBuilder
`RichTextValueBuilder`
- TextStyle
`TextStyle`
- TextStyleBuilder
`TextStyleBuilder`
- Range.getRichTextValue()
`Range.getRichTextValue()`
- Range.getRichTextValues()
`Range.getRichTextValues()`
- Range.getTextStyle()
`Range.getTextStyle()`
- Range.getTextStyles()
`Range.getTextStyles()`
- Range.setRichTextValue(value)
`Range.setRichTextValue(value)`
- Range.setRichTextValues(values)
`Range.setRichTextValues(values)`
- Range.setTextStyle(style)
`Range.setTextStyle(style)`
- Range.setTextStyles(styles)
`Range.setTextStyles(styles)`
- SpreadsheetApp.newRichTextValue()
`SpreadsheetApp.newRichTextValue()`
- SpreadsheetApp.newTextStyle()
`SpreadsheetApp.newTextStyle()`
- The Data Studio service has been extended with the following new classes and methods that define and support authentication types for community connectors: GetAuthTypeResponse AuthType CommunityConnector,newAuthTypeResponse()
- GetAuthTypeResponse
`GetAuthTypeResponse`
- AuthType
`AuthType`
- CommunityConnector,newAuthTypeResponse()
`CommunityConnector,newAuthTypeResponse()`
## January 04, 2019
- The Slides service has been extended with the following new classes and methods that support slide linking and text box insertion: SlideLinkingMode [ Layout.insertTextBox(text) }(https://developers.google.com/apps-script/reference/slides/layout#inserttextboxtext) Layout.insertTextBox(text, left, top, width, height) Master.insertTextBox(text) Master.insertTextBox(text, left, top, width, height) Page.insertTextBox(text) Page.insertTextBox(text, left, top, width, height) Presentation.appendSlide(slide, linkingMode) Presentation.insertSlide(insertionIndex, slide, linkingMode) Slide.getSlideLinkingMode() Slide.getSourcePresentationId() Slide.getSourceSlideObjectId() Slide.insertTextBox(text) Slide.insertTextBox(text, left, top, width, height) Slide.refreshSlide() Slide.unlink()
- SlideLinkingMode
`SlideLinkingMode`
- [ Layout.insertTextBox(text) }(https://developers.google.com/apps-script/reference/slides/layout#inserttextboxtext)
`Layout.insertTextBox(text)`
- Layout.insertTextBox(text, left, top, width, height)
`Layout.insertTextBox(text, left, top, width, height)`
- Master.insertTextBox(text)
`Master.insertTextBox(text)`
- Master.insertTextBox(text, left, top, width, height)
`Master.insertTextBox(text, left, top, width, height)`
- Page.insertTextBox(text)
`Page.insertTextBox(text)`
- Page.insertTextBox(text, left, top, width, height)
`Page.insertTextBox(text, left, top, width, height)`
- Presentation.appendSlide(slide, linkingMode)
`Presentation.appendSlide(slide, linkingMode)`
- Presentation.insertSlide(insertionIndex, slide, linkingMode)
`Presentation.insertSlide(insertionIndex, slide, linkingMode)`
- Slide.getSlideLinkingMode()
`Slide.getSlideLinkingMode()`
- Slide.getSourcePresentationId()
`Slide.getSourcePresentationId()`
- Slide.getSourceSlideObjectId()
`Slide.getSourceSlideObjectId()`
- Slide.insertTextBox(text)
`Slide.insertTextBox(text)`
- Slide.insertTextBox(text, left, top, width, height)
`Slide.insertTextBox(text, left, top, width, height)`
- Slide.refreshSlide()
`Slide.refreshSlide()`
- Slide.unlink()
`Slide.unlink()`
- The Data Studio service has been extended with the following new classes and methods that error displays: DebugError UserError CommunityConnector.newDebugError() CommunityConnector.newUserError()
- DebugError
`DebugError`
- UserError
`UserError`
- CommunityConnector.newDebugError()
`CommunityConnector.newDebugError()`
- CommunityConnector.newUserError()
`CommunityConnector.newUserError()`
## December 13, 2018
The Fusion Tables advanced service has been deprecated and will shutdown fully on December 3rd, 2019.
The Slides service has been extended with the following new classes and methods that support connector lines:
- ConnnectionSite
`ConnnectionSite`
- Group.getConnectionSites()
`Group.getConnectionSites()`
- Image.getConnectionSites()
`Image.getConnectionSites()`
- Line.getConnectionSites()
`Line.getConnectionSites()`
- Line.getEndConnection()
`Line.getEndConnection()`
- Line.getLineCategory()
`Line.getLineCategory()`
- Line.getStartConnection()
`Line.getStartConnection()`
- Line.isConnector()
`Line.isConnector()`
- Line.setEndConnection(connectionSite)
`Line.setEndConnection(connectionSite)`
- Line.setLineCategory(lineCategory)
`Line.setLineCategory(lineCategory)`
- Line.setStartConnection(connectionSite)
`Line.setStartConnection(connectionSite)`
- LineCategory.UNSUPPORTED
`LineCategory.UNSUPPORTED`
- PageElement.getConnectionSites()
`PageElement.getConnectionSites()`
- Shape.getConnectionSites()
`Shape.getConnectionSites()`
- SheetsChart.getConnectionSites()
`SheetsChart.getConnectionSites()`
- Table.getConnectionSites()
`Table.getConnectionSites()`
- Video.getConnectionSites()
`Video.getConnectionSites()`
- WordArt.getConnectionSites()
`WordArt.getConnectionSites()`
## November 14, 2018
- The Card service has been extended with the following new classes and methods that let you to customize the background of text button widgets: TextButtonStyle TextButton.setBackgroundColor(backgroundColor) TextButton.setDisabled(disabled) TextButton.setTextButtonStyle(textButtonStyle)
- TextButtonStyle
`TextButtonStyle`
- TextButton.setBackgroundColor(backgroundColor)
`TextButton.setBackgroundColor(backgroundColor)`
- TextButton.setDisabled(disabled)
`TextButton.setDisabled(disabled)`
- TextButton.setTextButtonStyle(textButtonStyle)
`TextButton.setTextButtonStyle(textButtonStyle)`
- The Slides service has been extended with the following new methods that let you control the Z-positioning of page elements in Slides. Other new methods let you add alt titles and alt descriptions to page elements. The following methods have been added to the Group , Image , Line , PageElement , Shape , SheetsChart , Table , Video , and WordArt classes: bringForward() bringToFront() sendBackward() sendToBack() setDescription(description) setTitle(title)
`Group`
`Image`
`Line`
`PageElement`
`Shape`
`SheetsChart`
`Table`
`Video`
`WordArt`
- bringForward()
`bringForward()`
- bringToFront()
`bringToFront()`
- sendBackward()
`sendBackward()`
- sendToBack()
`sendToBack()`
- setDescription(description)
`setDescription(description)`
- setTitle(title)
`setTitle(title)`
- The Spreadsheet service has been extended with the following new classes and methods that let you add and search for metadata strings attached to rows, columns, sheets, or spreadsheets: DeveloperMetadata DeveloperMetadataFinder DeveloperMetadataLocation DeveloperMetadataLocationType DeveloperMetadataVisibility Range.addDeveloperMetadata(key) Range.addDeveloperMetadata(key, visibility) Range.addDeveloperMetadata(key, value) Range.addDeveloperMetadata(key, value, visibility) Range.createDeveloperMetadataFinder() Range.getDeveloperMetadata() Sheet.addDeveloperMetadata(key) Sheet.addDeveloperMetadata(key, visibility) Sheet.addDeveloperMetadata(key, value) Sheet.addDeveloperMetadata(key, value, visibility) Sheet.createDeveloperMetadataFinder() Sheet.getDeveloperMetadata() Spreadsheet.addDeveloperMetadata(key) Spreadsheet.addDeveloperMetadata(key, visibility) Spreadsheet.addDeveloperMetadata(key, value) Spreadsheet.addDeveloperMetadata(key, value, visibility) Spreadsheet.createDeveloperMetadataFinder() Spreadsheet.getDeveloperMetadata()
- DeveloperMetadata
`DeveloperMetadata`
- DeveloperMetadataFinder
`DeveloperMetadataFinder`
- DeveloperMetadataLocation
`DeveloperMetadataLocation`
- DeveloperMetadataLocationType
`DeveloperMetadataLocationType`
- DeveloperMetadataVisibility
`DeveloperMetadataVisibility`
- Range.addDeveloperMetadata(key)
`Range.addDeveloperMetadata(key)`
- Range.addDeveloperMetadata(key, visibility)
`Range.addDeveloperMetadata(key, visibility)`
- Range.addDeveloperMetadata(key, value)
`Range.addDeveloperMetadata(key, value)`
- Range.addDeveloperMetadata(key, value, visibility)
`Range.addDeveloperMetadata(key, value, visibility)`
- Range.createDeveloperMetadataFinder()
`Range.createDeveloperMetadataFinder()`
- Range.getDeveloperMetadata()
`Range.getDeveloperMetadata()`
- Sheet.addDeveloperMetadata(key)
`Sheet.addDeveloperMetadata(key)`
- Sheet.addDeveloperMetadata(key, visibility)
`Sheet.addDeveloperMetadata(key, visibility)`
- Sheet.addDeveloperMetadata(key, value)
`Sheet.addDeveloperMetadata(key, value)`
- Sheet.addDeveloperMetadata(key, value, visibility)
`Sheet.addDeveloperMetadata(key, value, visibility)`
- Sheet.createDeveloperMetadataFinder()
`Sheet.createDeveloperMetadataFinder()`
- Sheet.getDeveloperMetadata()
`Sheet.getDeveloperMetadata()`
- Spreadsheet.addDeveloperMetadata(key)
`Spreadsheet.addDeveloperMetadata(key)`
- Spreadsheet.addDeveloperMetadata(key, visibility)
`Spreadsheet.addDeveloperMetadata(key, visibility)`
- Spreadsheet.addDeveloperMetadata(key, value)
`Spreadsheet.addDeveloperMetadata(key, value)`
- Spreadsheet.addDeveloperMetadata(key, value, visibility)
`Spreadsheet.addDeveloperMetadata(key, value, visibility)`
- Spreadsheet.createDeveloperMetadataFinder()
`Spreadsheet.createDeveloperMetadataFinder()`
- Spreadsheet.getDeveloperMetadata()
`Spreadsheet.getDeveloperMetadata()`
## October 30, 2018
- The Spreadsheet service has been extended with the following new classes and methods: OverGridImage Sheet.getImages() Sheet.isColumnHiddenByUser(columnPosition) Sheet.isRowHiddenByFilter(rowPosition) Sheet.isRowHiddenByUser(rowPosition) Spreadsheet.getImages() Spreadsheet.isColumnHiddenByUser(columnPosition) Spreadsheet.isRowHiddenByFilter(rowPosition) Spreadsheet.isRowHiddenByUser(rowPosition)
The Spreadsheet service has been extended with the following new classes and methods:
- OverGridImage
`OverGridImage`
- Sheet.getImages()
`Sheet.getImages()`
- Sheet.isColumnHiddenByUser(columnPosition)
`Sheet.isColumnHiddenByUser(columnPosition)`
- Sheet.isRowHiddenByFilter(rowPosition)
`Sheet.isRowHiddenByFilter(rowPosition)`
- Sheet.isRowHiddenByUser(rowPosition)
`Sheet.isRowHiddenByUser(rowPosition)`
- Spreadsheet.getImages()
`Spreadsheet.getImages()`
- Spreadsheet.isColumnHiddenByUser(columnPosition)
`Spreadsheet.isColumnHiddenByUser(columnPosition)`
- Spreadsheet.isRowHiddenByFilter(rowPosition)
`Spreadsheet.isRowHiddenByFilter(rowPosition)`
- Spreadsheet.isRowHiddenByUser(rowPosition)
`Spreadsheet.isRowHiddenByUser(rowPosition)`
- The following methods have been added to existing services: console service console.error() console.info() console.warn() DataStudio service Field.isHidden() Field.setIsHidden() Gmail service GmailAttachment.getHash() GmailMessage.getAttachments(options)
The following methods have been added to existing services:
- console service console.error() console.info() console.warn()
- console.error()
`console.error()`
- console.info()
`console.info()`
- console.warn()
`console.warn()`
- DataStudio service Field.isHidden() Field.setIsHidden()
- Field.isHidden()
`Field.isHidden()`
- Field.setIsHidden()
`Field.setIsHidden()`
- Gmail service GmailAttachment.getHash() GmailMessage.getAttachments(options)
- GmailAttachment.getHash()
`GmailAttachment.getHash()`
- GmailMessage.getAttachments(options)
`GmailMessage.getAttachments(options)`
The following methods in the Spreadsheet service now return an OverGridImage object instead of void:
`OverGridImage`
- Sheet.insertImage(blobSource, column, row)
`Sheet.insertImage(blobSource, column, row)`
- Sheet.insertImage(blobSource, column, row, offsetX, offsetY)
`Sheet.insertImage(blobSource, column, row, offsetX, offsetY)`
- Sheet.insertImage(url, column, row)
`Sheet.insertImage(url, column, row)`
- Sheet.insertImage(url, column, row, offsetX, offsetY)
`Sheet.insertImage(url, column, row, offsetX, offsetY)`
## October 18, 2018
The Card service has been extended with the following classes and methods to support Gmail add-on compose actions :
- CardService.UpdateDraftActionResponse
`CardService.UpdateDraftActionResponse`
- CardService.UpdateDraftActionResponseBuilder
`CardService.UpdateDraftActionResponseBuilder`
- CardService.UpdateDraftBodyAction
`CardService.UpdateDraftBodyAction`
- CardService.ContentType
`CardService.ContentType`
- CardService.UpdateDraftBodyType
`CardService.UpdateDraftBodyType`
- CardService.newUpdateDraftActionResponseBuilder()
`CardService.newUpdateDraftActionResponseBuilder()`
- CardService.newUpdateDraftBodyAction()
`CardService.newUpdateDraftBodyAction()`
## September 27, 2018
The Data Studio service is now available. You can use this service when building a Data Studio Community Connector .
## August 20, 2018
The Utilities service has been extended with the following methods and classes:
- Utilities.computeRsaSha1Signature(value, key)
`Utilities.computeRsaSha1Signature(value, key)`
- Utilities.computeRsaSha1Signature(value, key, charset)
`Utilities.computeRsaSha1Signature(value, key, charset)`
- Utilities.computeRsaSignature(algorithm, value, key)
`Utilities.computeRsaSignature(algorithm, value, key)`
- Utilities.computeRsaSignature(algorithm, value, key, charset)
`Utilities.computeRsaSignature(algorithm, value, key, charset)`
- RsaAlgorithm
`RsaAlgorithm`
## June 19, 2018
The quota on total data received by UrlFetch per day per user has been removed.
`UrlFetch`
- The Forms service now has the following method: Form.deleteResponse(responseId)`
- Form.deleteResponse(responseId)`
- The Utilities service now has the following methods: Utilities.computeDigest(algorithm, value) , where value is a Byte array Utilities.computeHmacSha256Signature(value, key) , where value and key are Byte arrays Utilities.computeHmacSignature(algorithm, value, key) , where value and key are Byte arrays
- Utilities.computeDigest(algorithm, value) , where value is a Byte array
`Utilities.computeDigest(algorithm, value)`
`Byte`
- Utilities.computeHmacSha256Signature(value, key) , where value and key are Byte arrays
`Utilities.computeHmacSha256Signature(value, key)`
`Byte`
- Utilities.computeHmacSignature(algorithm, value, key) , where value and key are Byte arrays
`Utilities.computeHmacSignature(algorithm, value, key)`
`Byte`
The quota limits for UrlFetch GET response size and POST size have been increased to 50MB / call.
`UrlFetch`
`GET`
`POST`
## April 23, 2018
- The Spreadsheet service has been extended with the new Group class and the GroupControlTogglePosition enum. Groups are an association between an interval of contiguous rows or columns that can be expanded or collapsed as a unit.
`Group`
`GroupControlTogglePosition`
- The Spreadsheet service has been extended with the following new methods to support Groups: Range.collapseGroups() Range.expandGroups() Range.shiftColumnGroupDepth(delta) Range.shiftRowGroupDepth(delta) Sheet.collapseAllColumnGroups() Sheet.collapseAllRowGroups() Sheet.expandAllColumnGroups() Sheet.expandAllRowGroups() Sheet.expandColumnGroupsUpToDepth(groupDepth) Sheet.expandRowGroupsUpToDepth(groupDepth) Sheet.getColumnGroup(columnIndex, groupDepth) Sheet.getColumnGroupControlPosition() Sheet.getColumnGroupDepth(columnIndex) Sheet.getRowGroup(rowIndex, groupDepth) Sheet.getRowGroupControlPosition() Sheet.getRowGroupDepth(rowIndex) Sheet.setColumnGroupControlPosition(position) Sheet.setRowGroupControlPosition(position)
- Range.collapseGroups()
`Range.collapseGroups()`
- Range.expandGroups()
`Range.expandGroups()`
- Range.shiftColumnGroupDepth(delta)
`Range.shiftColumnGroupDepth(delta)`
- Range.shiftRowGroupDepth(delta)
`Range.shiftRowGroupDepth(delta)`
- Sheet.collapseAllColumnGroups()
`Sheet.collapseAllColumnGroups()`
- Sheet.collapseAllRowGroups()
`Sheet.collapseAllRowGroups()`
- Sheet.expandAllColumnGroups()
`Sheet.expandAllColumnGroups()`
- Sheet.expandAllRowGroups()
`Sheet.expandAllRowGroups()`
- Sheet.expandColumnGroupsUpToDepth(groupDepth)
`Sheet.expandColumnGroupsUpToDepth(groupDepth)`
- Sheet.expandRowGroupsUpToDepth(groupDepth)
`Sheet.expandRowGroupsUpToDepth(groupDepth)`
- Sheet.getColumnGroup(columnIndex, groupDepth)
`Sheet.getColumnGroup(columnIndex, groupDepth)`
- Sheet.getColumnGroupControlPosition()
`Sheet.getColumnGroupControlPosition()`
- Sheet.getColumnGroupDepth(columnIndex)
`Sheet.getColumnGroupDepth(columnIndex)`
- Sheet.getRowGroup(rowIndex, groupDepth)
`Sheet.getRowGroup(rowIndex, groupDepth)`
- Sheet.getRowGroupControlPosition()
`Sheet.getRowGroupControlPosition()`
- Sheet.getRowGroupDepth(rowIndex)
`Sheet.getRowGroupDepth(rowIndex)`
- Sheet.setColumnGroupControlPosition(position)
`Sheet.setColumnGroupControlPosition(position)`
- Sheet.setRowGroupControlPosition(position)
`Sheet.setRowGroupControlPosition(position)`
## April 11, 2018
Macros for Google Sheets are now becoming available for users, and will finish rolling out over then next few weeks. This feature lets you record macros in the Google Sheets UI and use Apps Script to create or edit them.
The Sheets service has been extended with a large number of new classes and methods. The addition of these methods make it possible to reproduce in code nearly any action a Sheets user can take at a keyboard. The new classes and methods include:
- BandingTheme
`BandingTheme`
- Banding
`Banding`
- BooleanCondition
`BooleanCondition`
- BooleanCriteria
`BooleanCriteria`
- ConditionalFormatRuleBuilder
`ConditionalFormatRuleBuilder`
- ConditionalFormatRule
`ConditionalFormatRule`
- Dimension
`Dimension`
- Direction
`Direction`
- FilterCriteriaBuilder
`FilterCriteriaBuilder`
- FilterCriteria
`FilterCriteria`
- Filter
`Filter`
- GradientCondition
`GradientCondition`
- InterpolationType
`InterpolationType`
- PivotFilter
`PivotFilter`
- PivotGroup
`PivotGroup`
- PivotTableSummarizeFunction
`PivotTableSummarizeFunction`
- PivotTable
`PivotTable`
- PivotTableDisplayType
`PivotTableDisplayType`
- PivotValue
`PivotValue`
- RangeList
`RangeList`
- RelativeDate
`RelativeDate`
- Selection
`Selection`
- TextDirection
`TextDirection`
- TextRotation
`TextRotation`
- TextToColumnsDelimiter
`TextToColumnsDelimiter`
- WrapStrategy
`WrapStrategy`
- EmbeddedChartBuilder.setHiddenDimensionStrategy(strategy) (also in each of the type-specific chart builder classes)
`EmbeddedChartBuilder.setHiddenDimensionStrategy(strategy)`
- EmbeddedChartBuilder.setNumHeaders(headers) (also in each of the type-specific chart builder classes)
`EmbeddedChartBuilder.setNumHeaders(headers)`
- EmbeddedChartBuilder.setMergeStrategy(mergeStrategy) (also in each of the type-specific chart builder classes)
`EmbeddedChartBuilder.setMergeStrategy(mergeStrategy)`
- EmbeddedChartBuilder.setTransposeRowsAndColumns(transpose) (also in each of the type-specific chart builder classes)
`EmbeddedChartBuilder.setTransposeRowsAndColumns(transpose)`
- Range.activateAsCurrentCell()
`Range.activateAsCurrentCell()`
- Range.applyColumnBanding()
`Range.applyColumnBanding()`
- Range.applyColumnBanding(bandingTheme)
`Range.applyColumnBanding(bandingTheme)`
- Range.applyColumnBanding(bandingTheme, showHeader, showFooter)
`Range.applyColumnBanding(bandingTheme, showHeader, showFooter)`
- Range.applyRowBanding()
`Range.applyRowBanding()`
- Range.applyRowBanding(bandingTheme)
`Range.applyRowBanding(bandingTheme)`
- Range.applyRowBanding(bandingTheme, showHeader, showFooter)
`Range.applyRowBanding(bandingTheme, showHeader, showFooter)`
- Range.createFilter()
`Range.createFilter()`
- Range.createPivotTable(sourceData)
`Range.createPivotTable(sourceData)`
- Range.deleteCells(shiftDimension)
`Range.deleteCells(shiftDimension)`
- Range.getBandings()
`Range.getBandings()`
- Range.getNextDataCell(direction)
`Range.getNextDataCell(direction)`
- Range.getTextDirection()
`Range.getTextDirection()`
- Range.getTextDirections()
`Range.getTextDirections()`
- Range.getTextRotation()
`Range.getTextRotation()`
- Range.getTextRotations()
`Range.getTextRotations()`
- Range.getWrapStrategies()
`Range.getWrapStrategies()`
- Range.getWrapStrategy()
`Range.getWrapStrategy()`
- Range.insertCells(shiftDimension)
`Range.insertCells(shiftDimension)`
- Range.setShowHyperlink(showHyperlink)
`Range.setShowHyperlink(showHyperlink)`
- Range.setTextDirection(direction)
`Range.setTextDirection(direction)`
- Range.setTextDirections(directions)
`Range.setTextDirections(directions)`
- Range.setTextRotation(degrees)
`Range.setTextRotation(degrees)`
- Range.setTextRotation(rotation)
`Range.setTextRotation(rotation)`
- Range.setTextRotations(rotations)
`Range.setTextRotations(rotations)`
- Range.setVerticalText(isVertical)
`Range.setVerticalText(isVertical)`
- Range.setWrapStrategies(strategies)
`Range.setWrapStrategies(strategies)`
- Range.setWrapStrategy(strategy)
`Range.setWrapStrategy(strategy)`
- Range.setTextToColumns()
`Range.setTextToColumns()`
- Range.setTextToColumns(delimiter)
`Range.setTextToColumns(delimiter)`
- Range.setTextToColumns(delimiter)
`Range.setTextToColumns(delimiter)`
- Sheet.autoResizeColumns(startColumns, numColumns)
`Sheet.autoResizeColumns(startColumns, numColumns)`
- Sheet.autoResizeRows(startRows, numRows)
`Sheet.autoResizeRows(startRows, numRows)`
- Sheet.clearConditionalFormatRules()
`Sheet.clearConditionalFormatRules()`
- Sheet.getActiveRangeList()
`Sheet.getActiveRangeList()`
- Sheet.getBandings()
`Sheet.getBandings()`
- Sheet.getConditionalFormatRules()
`Sheet.getConditionalFormatRules()`
- Sheet.getCurrentCell()
`Sheet.getCurrentCell()`
- Sheet.getFilter()
`Sheet.getFilter()`
- Sheet.getPivotTables()
`Sheet.getPivotTables()`
- Sheet.getRangeList(a1Notations)
`Sheet.getRangeList(a1Notations)`
- Sheet.getSelection()
`Sheet.getSelection()`
- Sheet.hasHiddenGridlines()
`Sheet.hasHiddenGridlines()`
- Sheet.isRightToLeft()
`Sheet.isRightToLeft()`
- Sheet.setActiveRangeList(rangeList)
`Sheet.setActiveRangeList(rangeList)`
- Sheet.setColumnWidths(startColumn numColumns, width)
`Sheet.setColumnWidths(startColumn numColumns, width)`
- Sheet.setConditionalFormatRules(rules)
`Sheet.setConditionalFormatRules(rules)`
- Sheet.setCurrentCell(cell)
`Sheet.setCurrentCell(cell)`
- Sheet.setHiddenGridlines(hideGridlines)
`Sheet.setHiddenGridlines(hideGridlines)`
- Sheet.setRightToLeft(rightToLeft)
`Sheet.setRightToLeft(rightToLeft)`
- Sheet.setRowHeights(startRow, numRows, height)
`Sheet.setRowHeights(startRow, numRows, height)`
- Spreadsheet.getActiveRangeList()
`Spreadsheet.getActiveRangeList()`
- Spreadsheet.getBandings()
`Spreadsheet.getBandings()`
- Spreadsheet.getCurrentCell()
`Spreadsheet.getCurrentCell()`
- Spreadsheet.getRangeList(a1Notations)
`Spreadsheet.getRangeList(a1Notations)`
- Spreadsheet.getSelection()
`Spreadsheet.getSelection()`
- Spreadsheet.setActiveRangeList(rangeList)
`Spreadsheet.setActiveRangeList(rangeList)`
- Spreadsheet.setCurrentCell(cell)
`Spreadsheet.setCurrentCell(cell)`
The Charts service has been extended to support EmbeddedCharts in Google Sheets with the enums ChartHiddenDimensionStrategy and ChartMergeStrategy . In addition, the following ChartTypes have been added:
`EmbeddedCharts`
`ChartHiddenDimensionStrategy`
`ChartMergeStrategy`
`ChartTypes`
- TIMELINE
`TIMELINE`
- BUBBLE
`BUBBLE`
- CANDLESTICK
`CANDLESTICK`
- GAUGE
`GAUGE`
- GEO
`GEO`
- RADAR
`RADAR`
- ORG
`ORG`
- SPARKLINE
`SPARKLINE`
- STEPPED_AREA
`STEPPED_AREA`
- TREEMAP
`TREEMAP`
- WATERFALL
`WATERFALL`
## March 26, 2018
The Spreadsheet service has been extended with the following new methods:
- SpreadsheetApp.setActiveSheet(sheet, restoreSelection)
`SpreadsheetApp.setActiveSheet(sheet, restoreSelection)`
- Spreadsheet.setActiveSheet(sheet, restoreSelection)
`Spreadsheet.setActiveSheet(sheet, restoreSelection)`
- The deprecated enable(restriction) method of the ScriptApp.Service class has been sunset.
`enable(restriction)`
`ScriptApp.Service`
- The deprecated Service.Restriction enum used with the ScriptApp.Service class has been sunset.
`Service.Restriction`
`ScriptApp.Service`
## February 26, 2018
Calendar event triggers are now available. You can use these triggers in conjunction with the Calendar advanced service to discover recently changed calendar events via regular sync operations.
## February 13, 2018
- The Slides service has been extended with the following new methods: Layout.insertGroup(group) Layout.insertImage(image) Layout.insertLine(line) Layout.insertPageElement(pageElement) Layout.insertShape(shape) Layout.insertSheetsChart(sheetsChart) Layout.insertTable(table) Layout.insertVideo(video) Layout.insertWordArt(wordArt) Master.insertGroup(group) Master.insertImage(image) Master.insertLine(line) Master.insertPageElement(pageElement) Master.insertShape(shape) Master.insertSheetsChart(sheetsChart) Master.insertTable(table) Master.insertVideo(video) Master.insertWordArt(wordArt) Page.insertGroup(group) Page.insertImage(image) Page.insertLine(line) Page.insertPageElement(pageElement) Page.insertShape(shape) Page.insertSheetsChart(sheetsChart) Page.insertTable(table) Page.insertVideo(video) Page.insertWordArt(wordArt) Presentation.appendSlide(slide) Presentation.insertSlide(insertionIndex, slide) Slide.insertGroup(group) Slide.insertImage(image) Slide.insertLine(line) Slide.insertPageElement(pageElement) Slide.insertShape(shape) Slide.insertSheetsChart(sheetsChart) Slide.insertTable(table) Slide.insertVideo(video) Slide.insertWordArt(wordArt) TextRange.appendRange(textRange) TextRange.appendRange(textRange, matchSourceFormatting) TextRange.insertRange(startOffset, textRange) TextRange.insertRange(startOffset, textRange, matchSourceFormatting)
- Layout.insertGroup(group)
`Layout.insertGroup(group)`
- Layout.insertImage(image)
`Layout.insertImage(image)`
- Layout.insertLine(line)
`Layout.insertLine(line)`
- Layout.insertPageElement(pageElement)
`Layout.insertPageElement(pageElement)`
- Layout.insertShape(shape)
`Layout.insertShape(shape)`
- Layout.insertSheetsChart(sheetsChart)
`Layout.insertSheetsChart(sheetsChart)`
- Layout.insertTable(table)
`Layout.insertTable(table)`
- Layout.insertVideo(video)
`Layout.insertVideo(video)`
- Layout.insertWordArt(wordArt)
`Layout.insertWordArt(wordArt)`
- Master.insertGroup(group)
`Master.insertGroup(group)`
- Master.insertImage(image)
`Master.insertImage(image)`
- Master.insertLine(line)
`Master.insertLine(line)`
- Master.insertPageElement(pageElement)
`Master.insertPageElement(pageElement)`
- Master.insertShape(shape)
`Master.insertShape(shape)`
- Master.insertSheetsChart(sheetsChart)
`Master.insertSheetsChart(sheetsChart)`
- Master.insertTable(table)
`Master.insertTable(table)`
- Master.insertVideo(video)
`Master.insertVideo(video)`
- Master.insertWordArt(wordArt)
`Master.insertWordArt(wordArt)`
- Page.insertGroup(group)
`Page.insertGroup(group)`
- Page.insertImage(image)
`Page.insertImage(image)`
- Page.insertLine(line)
`Page.insertLine(line)`
- Page.insertPageElement(pageElement)
`Page.insertPageElement(pageElement)`
- Page.insertShape(shape)
`Page.insertShape(shape)`
- Page.insertSheetsChart(sheetsChart)
`Page.insertSheetsChart(sheetsChart)`
- Page.insertTable(table)
`Page.insertTable(table)`
- Page.insertVideo(video)
`Page.insertVideo(video)`
- Page.insertWordArt(wordArt)
`Page.insertWordArt(wordArt)`
- Presentation.appendSlide(slide)
`Presentation.appendSlide(slide)`
- Presentation.insertSlide(insertionIndex, slide)
`Presentation.insertSlide(insertionIndex, slide)`
- Slide.insertGroup(group)
`Slide.insertGroup(group)`
- Slide.insertImage(image)
`Slide.insertImage(image)`
- Slide.insertLine(line)
`Slide.insertLine(line)`
- Slide.insertPageElement(pageElement)
`Slide.insertPageElement(pageElement)`
- Slide.insertShape(shape)
`Slide.insertShape(shape)`
- Slide.insertSheetsChart(sheetsChart)
`Slide.insertSheetsChart(sheetsChart)`
- Slide.insertTable(table)
`Slide.insertTable(table)`
- Slide.insertVideo(video)
`Slide.insertVideo(video)`
- Slide.insertWordArt(wordArt)
`Slide.insertWordArt(wordArt)`
- TextRange.appendRange(textRange)
`TextRange.appendRange(textRange)`
- TextRange.appendRange(textRange, matchSourceFormatting)
`TextRange.appendRange(textRange, matchSourceFormatting)`
- TextRange.insertRange(startOffset, textRange)
`TextRange.insertRange(startOffset, textRange)`
- TextRange.insertRange(startOffset, textRange, matchSourceFormatting)
`TextRange.insertRange(startOffset, textRange, matchSourceFormatting)`
- The Spreadsheet service has been extended with the following new enum class and method: CopyPasteType , an enum class describing paste types. Range.copyTo(destination, copyPasteType, transposed)
- CopyPasteType , an enum class describing paste types.
`CopyPasteType`
- Range.copyTo(destination, copyPasteType, transposed)
`Range.copyTo(destination, copyPasteType, transposed)`
## January 19, 2018
- The UrlFetch service now has a fetchAll method that makes multiple fetch requests.
`UrlFetch`
`fetchAll`
- The Utilities service now has methods to compress and decompress Blob objects using gzip .
`gzip`
## January 11, 2018
- The Apps Script dashboard is now available. You can use it to see, search, and monitor all your script projects. The Apps Script API is now available. This API includes and extends the original Apps Script API. You can use the Apps Script API in an application to do any of the following: Create, read, and update Apps Script projects . Create and manage project versions . Create and manage project deployments . Monitor script use and metrics . Run script functions remotely .
- Create, read, and update Apps Script projects .
- Create and manage project versions .
- Create and manage project deployments .
- Monitor script use and metrics .
- Run script functions remotely .
- The open-source clasp tool is now available. It lets you manage and develop Apps Script projects locally from the command line instead of the Apps Script editor.
`clasp`
## October 24, 2017
- The Gmail add-ons framework is now available to all developers.
- A new Card service supports Gmail add-ons by defining several UI widget elements that you can use to create a Gmail add-on interface without HTML or CSS. These widgets function on both desktop and mobile. You can only use the Card service in a Gmail add-on project.
- You can now view and explicitly edit Apps Script project manifests . These files give you more direct control of project properties.
- You can now directly control the OAuth scopes that your project requests during authorization. Use this control to prevent your script project from asking for more access than it needs.
- You can now deploy a script project directly from the project manifest.
- We've updated the Publish script editor menu item to more accurately represent the various kinds of deployments a project can have, such as add-on, web app, or API executable deployments.
## October 10, 2017
- The Calendar service has been extended with the following new methods: CalendarApp.createAllDayEvent(title, startDate, endDate) CalendarApp.createAllDayEvent(title, startDate, endDate, options) CalendarApp.getEventById(iCalId) Calendar.createAllDayEvent(title, startDate, endDate) Calendar.createAllDayEvent(title, startDate, endDate, options) Calendar.getEventById(iCalId) CalendarEvent.setAllDayDates(startDate, endDate)
- CalendarApp.createAllDayEvent(title, startDate, endDate)
`CalendarApp.createAllDayEvent(title, startDate, endDate)`
- CalendarApp.createAllDayEvent(title, startDate, endDate, options)
`CalendarApp.createAllDayEvent(title, startDate, endDate, options)`
- CalendarApp.getEventById(iCalId)
`CalendarApp.getEventById(iCalId)`
- Calendar.createAllDayEvent(title, startDate, endDate)
`Calendar.createAllDayEvent(title, startDate, endDate)`
- Calendar.createAllDayEvent(title, startDate, endDate, options)
`Calendar.createAllDayEvent(title, startDate, endDate, options)`
- Calendar.getEventById(iCalId)
`Calendar.getEventById(iCalId)`
- CalendarEvent.setAllDayDates(startDate, endDate)
`CalendarEvent.setAllDayDates(startDate, endDate)`
- The Groups service has been extended with the following new methods: Group.getGroups() Group.hasGroup(group) Group.hasGroup(email)
- Group.getGroups()
`Group.getGroups()`
- Group.hasGroup(group)
`Group.hasGroup(group)`
- Group.hasGroup(email)
`Group.hasGroup(email)`
- The Spreadsheet service has been extended with the following new methods and classes: AutoFillSeries enumeration Range.autoFill(destination, series) Range.autoFillToNeighbor(series) Sheet.moveColumns(columnSpec, destinationIndex) Sheet.moveRows(rowSpec, destinationIndex)
- AutoFillSeries enumeration
`AutoFillSeries enumeration`
- Range.autoFill(destination, series)
`Range.autoFill(destination, series)`
- Range.autoFillToNeighbor(series)
`Range.autoFillToNeighbor(series)`
- Sheet.moveColumns(columnSpec, destinationIndex)
`Sheet.moveColumns(columnSpec, destinationIndex)`
- Sheet.moveRows(rowSpec, destinationIndex)
`Sheet.moveRows(rowSpec, destinationIndex)`
## October 06, 2017
Add-ons now require OAuth Client Verification prior to beginning the publication process. Verification no longer is conducted during the add-on review.
## September 26, 2017
Added Apps Script support for the Google Slides service . You can now use Apps Script to create and edit presentations and their contents; you can also build add-ons for Google Slides .
## September 15, 2017
- Added GmailDraft to the Gmail service. You can now create, edit, delete, and send new draft messages or draft replies to existing messages and threads. Drafts can reply to the original sender or "reply all".
`GmailDraft`
- You can now determine if a message or thread is in your priority inbox using GmailMessage.isInPriorityInbox() or GmailThread.isInPriorityInbox() .
`GmailMessage.isInPriorityInbox()`
`GmailThread.isInPriorityInbox()`
## July 28, 2017
- Added a Spreadsheet.getFormUrl() method that returns the URLs of Forms send responses to this Sheet or Spreadsheet.
`Spreadsheet.getFormUrl()`
- Adds a Checkbox Grid item to the Forms service.
- Enabled the collection of exception and error reports using Stackdriver Error Reporting .
## July 18, 2017
To protect users from abuse, Google OAuth clients that request certain sensitive OAuth scopes are subject to review by Google . Such apps may present users with a warning screen saying the app is unverified by Google. You can remove this screen from your app's authorization flow by submitting a review request .
## June 23, 2017
Stackdriver Logging has been moved out of Early Access . All scripts now have access to Stackdriver logging.
## June 20, 2017
Added the method Range.randomize() that randomizes the order of rows in a spreadsheet Range.
`Range.randomize()`
## April 26, 2017
- Quizzes in Google Forms is now accessible from the Apps Script Forms service .
- Added support for Combo and Histogram charts . Like other charts, these can be embedded in a Google Sheet.
- Added ability to getColor() and setColor() for Calendar Events. Events have their own color set: EventColor .
`getColor()`
`setColor()`
`EventColor`
## March 09, 2017
- Introduced project collaboration using Shared drives . Files and scripts in a shared drive are owned by the group instead of individuals, allowing collaborators to develop and maintain scripts more readily.
- Script editors (in addition to script owners) can now publish add-ons and deploy scripts as web apps or executables for the Execution API .
- For all container-bound scripts , the container owner takes ownership of a new script project regardless of who created it.
## March 07, 2017
- Enabled the Slides Advanced Service .
- Enabled the Sheets Advanced Service .
## December 01, 2016
Introduced the Early Access program for new G Suite Business features. These features include App Maker and Stackdriver Logging .
## November 23, 2016
Added forms validation classes for check boxes , generic data , grid items , paragraph text items , and text items .
## October 19, 2016
Added X-Frame-Option header support to HtmlService , allowing iframes to render Apps Script HTML and web apps.
`HtmlService`
## July 28, 2016
Added support for Android add-ons . Now you can make Google Docs and Sheets add-ons that work on Android.
## July 12, 2016
The use of project keys to identify scripts is now deprecated. The preferred unique identifier for a script is the Script ID . There are no plans to turn off or disable the use of project keys; code that uses project keys will continue to work for the foreseeable future.
## July 06, 2016
NATIVE sandbox mode is now shut down. All scripts default to IFRAME mode, regardless of which mode, if any, is specified. Scripts that relied on NATIVE mode features may need to be migrated .
`NATIVE`
`IFRAME`
`NATIVE`
## April 11, 2016
Support for PATCH requests has been added to UrlFetchApp .
`PATCH`
`UrlFetchApp`
## March 25, 2016
Deprecated the add(widget) method in the DashboardPanel class because it takes a UiApp.Widget argument, and UiApp was deprecated in 2014.
`add(widget)`
`DashboardPanel`
`UiApp.Widget`
## February 29, 2016
- The Spreadsheet API adds new methods for getTabColor() and setTabColor(color) .
The Spreadsheet API adds new methods for getTabColor() and setTabColor(color) .
`getTabColor()`
`setTabColor(color)`
- The Spreadsheet API adds a new NamedRange type and the following related methods: NamedRange.getName() gets the name of the named range NamedRange.setName(name) sets the name of the named range NamedRange.getRange() gets the underlying range associated with the named range NamedRange.setRange(range) sets the underlying range associated with the named range NamedRange.remove() deletes the named range Spreadsheet.getNamedRanges() gets an array of all the named ranges in the spreadsheet Sheet.getNamedRanges() gets an array of all the named ranges in the sheet Protection.setNamedRange(range) associates an existing protected range with an existing named range
The Spreadsheet API adds a new NamedRange type and the following related methods:
`NamedRange`
- NamedRange.getName() gets the name of the named range
`NamedRange.getName()`
- NamedRange.setName(name) sets the name of the named range
`NamedRange.setName(name)`
- NamedRange.getRange() gets the underlying range associated with the named range
`NamedRange.getRange()`
- NamedRange.setRange(range) sets the underlying range associated with the named range
`NamedRange.setRange(range)`
- NamedRange.remove() deletes the named range
`NamedRange.remove()`
- Spreadsheet.getNamedRanges() gets an array of all the named ranges in the spreadsheet
`Spreadsheet.getNamedRanges()`
- Sheet.getNamedRanges() gets an array of all the named ranges in the sheet
`Sheet.getNamedRanges()`
- Protection.setNamedRange(range) associates an existing protected range with an existing named range
`Protection.setNamedRange(range)`
- The Utilities API includes a new getUuid() method that generates a unique identifier.
The Utilities API includes a new getUuid() method that generates a unique identifier.
`getUuid()`
## December 10, 2015
In the HTML service , EMULATED sandbox mode was sunset . Any scripts that explicitly request EMULATED mode now default to IFRAME mode.
`EMULATED`
`EMULATED`
`IFRAME`
## November 12, 2015
In the HTML service , all new scripts default to IFRAME sandbox mode unless NATIVE mode is explicitly specified.
`IFRAME`
`NATIVE`
## August 10, 2015
Deprecated the method Service.enable() in the ScriptApp global object. This method is no longer useful because Apps Script's authorization model has changed since the time the method was introduced.
`Service.enable()`
## August 04, 2015
Added the following methods to the Spreadsheet service to let scripts control "warning-based" protection for spreadsheet ranges (which means that every user can edit data in the area, except editing prompts the user to confirm the edit):
- Protection.isWarningOnly()
`Protection.isWarningOnly()`
- Protection.setWarningOnly(warningOnly)
`Protection.setWarningOnly(warningOnly)`
## June 30, 2015
Added two variations of the method computeRsaSha256Signature to the Utilities global object to let scripts sign a string using the RSA SHA-256 algorithm.
`computeRsaSha256Signature`
`Utilities`
## May 27, 2015
Added the method getUserAgent() to the HtmlService global object to let scripts get the user-agent string for the current browser.
`getUserAgent()`
`HtmlService`
## May 20, 2015
Deprecated the following OAuth class and methods in favor of OAuth libraries : + OAuthConfig + UrlFetchApp.addOAuthService(serviceName) + UrlFetchApp.removeOAuthService(serviceName)
`OAuthConfig`
`UrlFetchApp.addOAuthService(serviceName)`
`UrlFetchApp.removeOAuthService(serviceName)`
- Added the following enum and methods to the Script service to allow scripts to identify their installation source and project keys: InstallationSource ScriptApp.getInstallationSource() ScriptApp.getProjectKey()
- InstallationSource
`InstallationSource`
- ScriptApp.getInstallationSource()
`ScriptApp.getInstallationSource()`
- ScriptApp.getProjectKey()
`ScriptApp.getProjectKey()`
- Added several new web-safe base-64 encoding and decoding methods: Utilities.base64DecodeWebSafe(String) Utilities.base64DecodeWebSafe(String, Charset) Utilities.base64EncodeWebSafe(Byte) Utilities.base64EncodeWebSafe(String) Utilities.base64EncodeWebSafe(String, Charset)
- Utilities.base64DecodeWebSafe(String)
`Utilities.base64DecodeWebSafe(String)`
- Utilities.base64DecodeWebSafe(String, Charset)
`Utilities.base64DecodeWebSafe(String, Charset)`
- Utilities.base64EncodeWebSafe(Byte)
`Utilities.base64EncodeWebSafe(Byte)`
- Utilities.base64EncodeWebSafe(String)
`Utilities.base64EncodeWebSafe(String)`
- Utilities.base64EncodeWebSafe(String, Charset)
`Utilities.base64EncodeWebSafe(String, Charset)`
## April 23, 2015
- Add-ons are now out of developer preview. This means anyone can now publish an add-on. New add-ons will still be reviewed prior to publishing, but the publishing process has been streamlined.
- Add-ons can now be developed and published from standalone scripts (as opposed to scripts bound to a Sheet, Doc, or Form). The add-on must still operate on a Sheet, Doc, or Form, but the script does not need to be bound to a single master file. Developing from a standalone script is preferred in that it makes collaboration and testing easier.
- Add-on scripts in development can be tested to ensure they behave as intended.
The DocsList service , which was deprecated in 2014 , has been sunset and no longer functions. Users relying on DocsList should switch to DriveApp .
`DocsList`
`DocsList`
`DriveApp`
## March 19, 2015
- Added the ability to publish add-ons for domain-wide installation . This lets an admin of a Google Apps domain install and authorize a Docs, Sheets, or Forms add-on for all users in the domain if the add-on is published to the Google Apps Marketplace . If the developer has already published a Google Apps Marketplace app that is closely related to their add-on, they can also choose to bundle the add-on with the Marketplace app so that admins install both the app and the add-on together.
- Added the ability to change the Google Developers Console project that a script uses for authorization. This feature is most commonly used to bundle an add-on with a Google Apps Marketplace app, as above.
## March 04, 2015
Deprecated the URL Fetch service's class OAuthConfig , which provided the ability to connect to OAuth 1.0 APIs. This has been replaced by the open source library OAuth1 for Apps Script . See the migration guide for more information.
`OAuthConfig`
## February 10, 2015
- Deprecated the following class and methods, which have been replaced by the more powerful Protection class above. Although this class and these methods are deprecated, they will remain available for compatibility with the older version of Sheets. PageProtection Spreadsheet.getSheetProtection() Spreadsheet.setSheetProtection(permissions) Sheet.getSheetProtection() Sheet.setSheetProtection(permissions)
Deprecated the following class and methods, which have been replaced by the more powerful Protection class above. Although this class and these methods are deprecated, they will remain available for compatibility with the older version of Sheets.
- PageProtection
`PageProtection`
- Spreadsheet.getSheetProtection()
`Spreadsheet.getSheetProtection()`
- Spreadsheet.setSheetProtection(permissions)
`Spreadsheet.setSheetProtection(permissions)`
- Sheet.getSheetProtection()
`Sheet.getSheetProtection()`
- Sheet.setSheetProtection(permissions)
`Sheet.setSheetProtection(permissions)`
- Replaced the method SpreadsheetApp.open(file) , which takes a File object from the deprecated DocsList service as a parameter, with a version that takes a File object from the Drive service instead. The new method has the same name.
Replaced the method SpreadsheetApp.open(file) , which takes a File object from the deprecated DocsList service as a parameter, with a version that takes a File object from the Drive service instead. The new method has the same name.
`SpreadsheetApp.open(file)`
`File`
`DocsList`
`File`
`Drive`
- Changed the Document service methods Text.getFontFamily() and Text.setFontFamily(fontFamilyName) to use string names for font families instead of the FontFamily enum , and consequently deprecated FontFamily .
Changed the Document service methods Text.getFontFamily() and Text.setFontFamily(fontFamilyName) to use string names for font families instead of the FontFamily enum , and consequently deprecated FontFamily .
`Text.getFontFamily()`
`Text.setFontFamily(fontFamilyName)`
`FontFamily`
`FontFamily`
Added the following class, enum, and methods to the Spreadsheet service, to give precise control over protected sheets and ranges:
- Protection
`Protection`
- ProtectionType
`ProtectionType`
- Range.canEdit()
`Range.canEdit()`
- Range.isEndColumnBounded()
`Range.isEndColumnBounded()`
- Range.isEndRowBounded()
`Range.isEndRowBounded()`
- Range.isStartColumnBounded()
`Range.isStartColumnBounded()`
- Range.isStartRowBounded()
`Range.isStartRowBounded()`
- Range.protect()
`Range.protect()`
- Sheet.getProtections(type)
`Sheet.getProtections(type)`
- Sheet.protect()
`Sheet.protect()`
- Spreadsheet.getProtections(type)
`Spreadsheet.getProtections(type)`
Issue 4617 : HTML service pages that use the new IFRAME sandbox mode now render correctly in Firefox.
`IFRAME`
Changed several Spreadsheet methods that previously returned void so that they now return a Spreadsheet object that can be used to chain method calls.
`Spreadsheet`
`Spreadsheet`
## December 11, 2014
- Deprecated both the UI service and the DocsList service . As announced in the blog post , the DocsList service will be turned off on April 20, 2015, and the UI service will be turned off on June 30, 2015. To create user interfaces, use the HTML service instead. To replace the DocsList service, use the Drive service instead.
`DocsList`
`DocsList`
`DocsList`
`Drive`
- Removed the Domain service , as announced earlier in the year .
Added a new IFRAME sandbox mode for HTML service that imposes many fewer restrictions than the other sandbox modes and runs much faster. However, IFRAME mode does not work at all in certain older browsers, including Internet Explorer 9.
`IFRAME`
`IFRAME`
## December 01, 2014
- Added five new FormApp methods: Form.getShuffleQuestions() : Determines whether the order of the questions on each page of the form is randomized. Form.hasLimitOneResponsePerUser() : Determines whether the form allows only one response per respondent. If the value is true, the script cannot submit form responses at all. Form.setLimitOneResponsePerUser(enabled) : Sets whether the form allows only one response per respondent. The default for new forms is false. If the value is set to true, the script cannot submit form responses at all. Form.setShuffleQuestions(shuffle) : Sets whether the order of the questions on each page of the form is randomized. Form.shortenFormUrl(url) : Converts a long URL for a form to a short URL.
`FormApp`
- Form.getShuffleQuestions() : Determines whether the order of the questions on each page of the form is randomized.
`Form.getShuffleQuestions()`
- Form.hasLimitOneResponsePerUser() : Determines whether the form allows only one response per respondent. If the value is true, the script cannot submit form responses at all.
`Form.hasLimitOneResponsePerUser()`
- Form.setLimitOneResponsePerUser(enabled) : Sets whether the form allows only one response per respondent. The default for new forms is false. If the value is set to true, the script cannot submit form responses at all.
`Form.setLimitOneResponsePerUser(enabled)`
- Form.setShuffleQuestions(shuffle) : Sets whether the order of the questions on each page of the form is randomized.
`Form.setShuffleQuestions(shuffle)`
- Form.shortenFormUrl(url) : Converts a long URL for a form to a short URL.
`Form.shortenFormUrl(url)`
- Added two new SpreadsheetApp methods: Sheet.insertImage(blob, column, row) : Inserts a Blob as an image in the sheet at a given row and column. Sheet.insertImage(blob, column, row, offsetX, offsetY) : Inserts a Blob as an image in the sheet at a given row and column, with a pixel offset.
`SpreadsheetApp`
- Sheet.insertImage(blob, column, row) : Inserts a Blob as an image in the sheet at a given row and column.
`Sheet.insertImage(blob, column, row)`
`Blob`
- Sheet.insertImage(blob, column, row, offsetX, offsetY) : Inserts a Blob as an image in the sheet at a given row and column, with a pixel offset.
`Sheet.insertImage(blob, column, row, offsetX, offsetY)`
`Blob`
## October 23, 2014
Add-ons are now available in Google Forms . As with add-ons for Docs and Sheets, Forms add-ons are in developer preview, so you must apply to publish them .
Removed the Finance service , as announced earlier in the year .
Issue 3928 : The Document method setSelection , the Sheet method activate , and the Spreadsheet methods setActiveRange and setActiveSelection now work correctly if they are called from an onOpen or onEdit trigger.
`Document`
`setSelection`
`Sheet`
`activate`
`Spreadsheet`
`setActiveRange`
`setActiveSelection`
`onOpen`
`onEdit`
## October 14, 2014
Add-ons for Google Sheets and Docs can now use time-driven installable triggers .
## September 30, 2014
- Added the LinearOptimizationService , which allows scripts to model and solve linear and mixed-integer linear programs.
`LinearOptimizationService`
- Add-ons for Google Sheets and Docs can now use most installable triggers , although they still cannot use time-driven triggers (sometimes called clock triggers).
- Added an installable open trigger for Google Docs. Like the installable open triggers for Sheets and Forms, this trigger is similar to the simple onOpen() trigger, but allows the triggered function to call services that require authorization, if the user has authorized the script ahead of time.
`onOpen()`
- Added several new ScriptApp methods, classes, and enums to support installable triggers in add-ons: AuthorizationInfo : An object used to determine whether the user needs to authorize this script to use one or more services, and to provide the URL for an authorization dialog. Returned by ScriptApp.getAuthorizationInfo() . AuthorizationStatus : An enumeration denoting the authorization status of a script. Returned by AuthorizationInfo.getAuthorizationStatus() . DocumentTriggerBuilder : A builder for document triggers. Returned by TriggerBuilder.forDocument(...) . ScriptApp.getUserTriggers(...) : Gets all installable triggers owned by this user in the given document, spreadsheet, or form.
`ScriptApp`
- AuthorizationInfo : An object used to determine whether the user needs to authorize this script to use one or more services, and to provide the URL for an authorization dialog. Returned by ScriptApp.getAuthorizationInfo() .
`AuthorizationInfo`
`ScriptApp.getAuthorizationInfo()`
- AuthorizationStatus : An enumeration denoting the authorization status of a script. Returned by AuthorizationInfo.getAuthorizationStatus() .
`AuthorizationStatus`
`AuthorizationInfo.getAuthorizationStatus()`
- DocumentTriggerBuilder : A builder for document triggers. Returned by TriggerBuilder.forDocument(...) .
`DocumentTriggerBuilder`
`TriggerBuilder.forDocument(...)`
- ScriptApp.getUserTriggers(...) : Gets all installable triggers owned by this user in the given document, spreadsheet, or form.
`ScriptApp.getUserTriggers(...)`
The UiService widget DocsListDialog now requires that you call DocsListDialog.setOAuthToken(oAuthToken) before calling DocsListDialog.showDocsPicker() .
`UiService`
`DocsListDialog`
`DocsListDialog.setOAuthToken(oAuthToken)`
`DocsListDialog.showDocsPicker()`
## September 04, 2014
Replaced the CacheService methods getPrivateCache() and getPublicCache() and the LockService methods getPrivateLock() and getPublicLock() with getUserCache() , getScriptCache() , getUserLock() , and getScriptLock() , respectively. The old method names have been deprecated, but will continue to function. The new names follow the same conventions as PropertiesService .
`CacheService`
`getPrivateCache()`
`getPublicCache()`
`LockService`
`getPrivateLock()`
`getPublicLock()`
`getUserCache()`
`getScriptCache()`
`getUserLock()`
`getScriptLock()`
`PropertiesService`
- Added the UiService method DocsListDialog.setOAuthToken(oAuthToken) , which sets an OAuth 2.0 token to use when fetching data for the dialog, on behalf of the user whose content should be shown. This method will become mandatory before calling DocsListDialog.showDocsPicker() on September 30, 2014.
`UiService`
`DocsListDialog.setOAuthToken(oAuthToken)`
`DocsListDialog.showDocsPicker()`
- Added the CacheService method getDocumentCache() and the LockService method getDocumentLock() , which get a cache and a lock that all users can access within the current document, if the script is published as an add-on. These methods are conceptually similar to the PropertiesService method getDocumentProperties() , which was introduced for use in add-ons earlier this year.
`CacheService`
`getDocumentCache()`
`LockService`
`getDocumentLock()`
`PropertiesService`
`getDocumentProperties()`
## July 17, 2014
Added the value ON_CHANGE to the ScriptApp.EventType enum so that Google Sheets change events can be detected correctly.
`ON_CHANGE`
`ScriptApp.EventType`
## June 20, 2014
Deprecated the script gallery in the old version of Google Sheets. As explained in the blog post , the add-on store in the new version of Sheets gives developers wider distribution, automatic updates, and several other features not available in the script gallery.
## May 29, 2014
Added the Document service methods getTextAlignment and setTextAlignment as well as the enum TextAlignment , to support NORMAL , SUPERSCRIPT , and SUBSCRIPT text alignment in Google Docs.
`Document`
`getTextAlignment`
`setTextAlignment`
`TextAlignment`
`NORMAL`
`SUPERSCRIPT`
`SUBSCRIPT`
## May 15, 2014
Deprecated both ScriptDB and the Domain service . As announced in the blog post, the services will remain available for the next six months but will be turned off on November 20, 2014. To replace ScriptDB , see the migration guide and the improved guide to connecting to external databases through JDBC . To replace the Domain service , see the Admin SDK Directory and Admin SDK Reports advanced services.
`ScriptDB`
`Domain`
`ScriptDB`
`Domain service`
Added a source property to the event parameter for form triggers . This makes it possible to retrieve the form that triggered the event.
- Issue 3956 : In the new version of Google Sheets, it is now possible to call methods that refer to the "active" sheet or spreadsheet even if the sheet or spreadsheet has just been created.
- Issue 3579 : The Blob method getA s can now create PDFs from spreadsheets created with the new version of Sheets.
`Blob`
`getA`
- Issue 3378 : The documentation page for a library version now uses the same CSS styles as the Apps Script reference documentation.
## May 08, 2014
The "Report an issue" dialog for add-ons now asks users whether they would like to share their name and email address with the developer.
## May 01, 2014
- Issue 3963 : The Apps Script dashboard is available again.
- Issue 3533 : The Trigger methods getEventType() and getTriggerSource() no longer throw an exception if the trigger belongs to a spreadsheet created by the new version of Google Sheets .
`Trigger`
`getEventType()`
`getTriggerSource()`
## April 24, 2014
In the new version of Google Sheets , the Undo command can now revert changes made by a script. This was already true in Docs, Forms, and the older version of Sheets.
- Issue 3891 : In the new version of Sheets, custom functions now recalculate correctly if more than 100 cells are passed as an argument.
- Issue 3859 : In the new version of Sheets, setting data-validation criteria for a cell that already contains a value no longer corrupts the spreadsheet.
- Issue 3773 : In the new version of Sheets, the Browser methods inputBox and msgBox now treat newline characters ( \n ) the same way that the older version of Sheets did. Specifically, \n produces a space, but \\n (double-escaped) produces a line break.
`inputBox`
`msgBox`
`\n`
`\n`
`\\n`
- Issue 2335 : The fact that the ID of a GmailThread varies based on the messages it contains is now documented .
`GmailThread`
- Issue 2288 : The fact that a Google Site or page of a site cannot have more than 500 child pages is now documented .
- Issue 1427 : The fact that the method getAs replaces the part of a filename that follows the last period with the new file type's extension is now documented .
`getAs`
## April 17, 2014
The Document method setSelection , the Sheet method activate , and the Spreadsheet methods setActiveRange and setActiveSelection no longer have any effect if they are called from an onOpen or onEdit trigger .
`Document`
`setSelection`
`Sheet`
`activate`
`Spreadsheet`
`setActiveRange`
`setActiveSelection`
`onOpen`
`onEdit`
- Issue 3669 : In the new version of Sheets , the Range methods getValue() and getValues() no longer throw an exception if a cell uses the built-in Sheets methods =IMAGE(url) or =SPARKLINE(data) .
`Range`
`getValue()`
`getValues()`
`=IMAGE(url)`
`=SPARKLINE(data)`
- Issue 2684 : If a script relies on a deleted version of a library, it is now possible to switch to a different version.
## April 10, 2014
- Issue 3788 : In the new version of Sheets, custom functions now calculate if they are passed an error value as an argument. This matches the behavior in the older version of Sheets.
- Issue 3539 : In the new version of Sheets, the Range methods setValue and setValues now automatically detect when a value should be set as a formula. This matches the behavior in the older version of Sheets.
`Range`
`setValue`
`setValues`
The deprecated SOAP service and old XML service have now been removed from autocomplete and documentation, as announced on July 9, 2013 and documented in the Apps Script sunset schedule . Existing scripts that use these services should still function. The UI service widgets DeckPanel , DecoratedPopupPanel , DockLayoutPanel , DockPanel , StackLayoutPanel , and TabLayoutPanel have been completely disabled, as announced on April 15, 2013.
`DeckPanel`
`DecoratedPopupPanel`
`DockLayoutPanel`
`DockPanel`
`StackLayoutPanel`
`TabLayoutPanel`
## April 03, 2014
The Range method getDataSourceUrl() is now supported in the new version of Google Sheets . For information on other incomplete Apps Script features in the new version of Sheets, see the list of known issues .
`getDataSourceUrl()`
- Issue 3866 : The DocsList methods File.getEditors() and File.getViewers() no longer throw a server error on every call.
`DocsList`
`File.getEditors()`
`File.getViewers()`
- Issue 3865 : The DocsList method File.getOwner() no longer throws a server error on every call.
`DocsList`
`File.getOwner()`
- Issue 3845 : The advanced Google services for Drive and Calendar are now documented.
- Issue 3624 : In the new version of Sheets, the Sheet method hideSheet() can now hide sheets that have just been inserted.
`Sheet`
`hideSheet()`
- Issue 3554 : In the new version of Sheets, the Range method sort() now succeeds for ranges that do not include column A.
`Range`
`sort()`
- Issue 3522 : In the new version of Sheets, the SpreadsheetApp method getActiveSheet() now returns the correct sheet in a single custom function call. However, getActiveSheet() still returns an incorrect value if the custom function is used in more than one cell with the same function arguments, or if called from an installable edit trigger in the new version of Sheets.
`SpreadsheetApp`
`getActiveSheet()`
`getActiveSheet()`
- Issue 3496 : In the new version of Sheets, the SpreadsheetApp method getActiveRange() now returns the correct range in a single custom function call. However, getActiveRange() still returns an incorrect value if the custom function is used in more than one cell with the same function arguments, or if called from an installable edit trigger in the new version of Sheets.
`SpreadsheetApp`
`getActiveRange()`
`getActiveRange()`
## March 27, 2014
- Issue 3691 : In the new version of Google Sheets, scripts can now run for 6 minutes instead of 5 minutes.
- Issue 3236 : Google Picker, a "file-open" dialog for information stored in Google servers, including files in Google Drive, is now supported in HTML service .
When an add-on is installed from the store, the onInstall() simple trigger is now passed an event parameter , e , which includes an authMode property. This makes it easier for an add-on to call onOpen(e) from onInstall(e) .
`onInstall()`
`e`
`authMode`
`onOpen(e)`
`onInstall(e)`
## March 24, 2014
In the new version of Google Sheets , Range.setValues() now automatically extends the spreadsheet if the range is larger than the present size.
`Range.setValues()`
- Issue 3800 : In the new version of Sheets, custom functions now accept numbers larger than 10,000,000 or smaller than 0.0001 as arguments.
- Issue 3770 : In the new version of Sheets, Sheet.insertImage() now inserts the image at the correct size.
`Sheet.insertImage()`
- Issue 3724 : In the new version of Sheets, Range.setValue() now correctly sets numeric values in non-English spreadsheets.
`Range.setValue()`
## March 18, 2014
Issue 3757 : The link to the Google Developers Console in the Advanced Google Services dialog now opens the correct project.
## March 11, 2014
Announced a developer preview for add-ons in Google Docs and the new version of Google Sheets, with support for Google Forms coming soon. An add-on is an Apps Script project published to a store inside Docs or Sheets, which makes it easy for users to find and install new features. Our guides cover everything you need to know to develop , design , and apply to publish your first add-on.
- Released a CSS package to apply Google styling to fonts, buttons, and form elements in HTML service dialogs and sidebars, primarily for use in add-ons.
- Added the UI method createAddonMenu() , which allows scripts to insert a sub-menu into the Add-ons menu in Google Sheets or Docs. For more information, see the guide to menus .
`createAddonMenu()`
- Added the ScriptApp enum AuthMode , which identifies categories of authorized services that Apps Script can execute through a triggered function. For more information, see the guide to the add-on authorization lifecycle .
`ScriptApp`
`AuthMode`
- Added support for the custom JsDoc annotation @OnlyCurrentDoc , which forces the authorization dialog to ask only for access to files in which an add-on or script is used, rather than all of a user's spreadsheets, documents, or forms. An opposing annotation, @NotOnlyCurrentDoc , is also available.
`@OnlyCurrentDoc`
`@NotOnlyCurrentDoc`
Changed the quota for Gmail from 10,000 reads and 10,000 writes per day (excluding sent messages) to 20,000 reads and writes combined per day.
## February 25, 2014
- Replaced ScriptProperties and UserProperties with a unified PropertiesService . For more information, see the guide to the Properties service .
`ScriptProperties`
`UserProperties`
`PropertiesService`
- In Google Docs and Forms, sidebars now ignore the setWidth() method; they cannot be changed from the default width of 300px. This change was applied to the new version of Sheets in the previous week's release.
`setWidth()`
- In Google Docs and Forms, the Undo command can now revert changes made by a script. This is also true in the older version of Sheets, but not the new version.
- In the HTML service, the NATIVE sandbox mode is now the default if you have not specified which mode your script should use. In a few edge cases, this may affect how existing web apps operate; if so, append .setSandboxMode(HtmlService.SandboxMode.EMULATED) to your HtmlOutput object to restore the old behavior.
`NATIVE`
`.setSandboxMode(HtmlService.SandboxMode.EMULATED)`
`HtmlOutput`
Issue 3622 : The title bar of a sidebar shown by a script in Google Docs, Forms, or the new version of Sheets is now the same height as in a sidebar shown by a built-in feature.
Deprecated the Finance service . As announced in the blog post , the service will remain available for the next six months but will be turned off on September 26, 2014.
- Added the following DocumentApp classes and methods, which allow scripts to create bookmarks and named ranges, plus set the user's cursor position or selection. Bookmark `NamedRange `RangeBuilder `Document.addBookmark(position) `Document.addNamedRange(name, range) `Document.getBookmark(id) `Document.getBookmarks() `Document.getNamedRangeById(id) `Document.getNamedRanges() `Document.getNamedRanges(name) `Document.newPosition(element, offset) `Document.newRange() `Document.setCursor(position) `Document.setSelection(range) `Position.insertBookmark()
`DocumentApp`
- Bookmark
`Bookmark`
- `NamedRange
- `RangeBuilder
- `Document.addBookmark(position)
- `Document.addNamedRange(name, range)
- `Document.getBookmark(id)
- `Document.getBookmarks()
- `Document.getNamedRangeById(id)
- `Document.getNamedRanges()
- `Document.getNamedRanges(name)
- `Document.newPosition(element, offset)
- `Document.newRange()
- `Document.setCursor(position)
- `Document.setSelection(range)
- `Position.insertBookmark()
- Added the following ScriptApp class and methods, which allow scripts to create state tokens that can be used in callback APIs (like OAuth flows), as well as to retrieve the script's own OAuth 2.0 access token. `StateTokenBuilder `ScriptApp.getOAuthToken() `ScriptApp.newStateToken()
`ScriptApp`
- `StateTokenBuilder
- `ScriptApp.getOAuthToken()
- `ScriptApp.newStateToken()
- Added the method showModalDialog(userInterface, title) to the Ui class, and replaced the method showDialog(userInterface) with showModelessDialog(userInterface, title) . This allows scripts to specify whether a dialog in Google Docs, Forms, or the new version of Sheets should prevent the user from interacting with anything other than the dialog.
`showModalDialog(userInterface, title)`
`showDialog(userInterface)`
`showModelessDialog(userInterface, title)`
- Added the client-side HTML-service method google.script.host.editor.focus() , which allows scripts to switch browser focus from the dialog or sidebar to the Google Docs, Sheets, or Forms editor.
`google.script.host.editor.focus()`
## February 18, 2014
- Issue 3522 : In the new version of Sheets, the SpreadsheetApp method getActiveSheet() now returns the correct sheet if called from a simple onEdit() trigger. However, getActiveSheet() still returns an incorrect value if used in a custom function or an installable edit trigger in the new version of Sheets.
`SpreadsheetApp`
`getActiveSheet()`
`simple onEdit()`
`getActiveSheet()`
- Issue 3496 : In the new version of Sheets, the SpreadsheetApp method getActiveRange() now returns the correct sheet if called from a simple onEdit() trigger. However, getActiveRange() still returns an incorrect value if used in a custom function or an installable edit trigger in the new version of Sheets.
`SpreadsheetApp`
`getActiveRange()`
`onEdit()`
`getActiveRange()`
- Issue 3332 : The DocumentApp method setHeading() now applies heading styles in the same way that the Google Docs editor does.
`DocumentApp`
`setHeading()`
Removed the Session method getActiveUserTimeZone() , which did not return a value for most users.
`getActiveUserTimeZone()`
- In Google Docs, Forms, and the new version of Sheets , showing a dialog now automatically closes any other dialogs opened by a script. This matches the longstanding behavior in the older version of Sheets.
- In the new version of Sheets, sidebars now ignore the setWidth() method; they cannot be changed from the default width of 300px. This change will affect Docs and Forms soon.
`setWidth()`
## January 27, 2014
Renamed several classes and methods in DocumentApp . The old names are deprecated but will continue to work. You do not need to update your code.
`DocumentApp`
- SearchResult and SelectedElement are now RangeElement .
`SearchResult`
`SelectedElement`
`RangeElement`
- Selection is now Range .
`Selection`
`Range`
- Selection.getSelectedElements() is now Range.getRangeElements() .
`Selection.getSelectedElements()`
`Range.getRangeElements()`
The quota for the number of email recipients for scripts running from consumer (gmail.com) or free Google Apps accounts has been reduced from 500 to 100 per day. The quota for paid Google Apps accounts has not been changed.
Added the following Session methods, which allow scripts to determine the user's locale and time zone:
`Session`
- getActiveUserLocale()
`getActiveUserLocale()`
- getActiveUserTimeZone()
`getActiveUserTimeZone()`
## January 21, 2014
The new SpreadsheetApp method Spreadsheet.getUi() allows scripts to access the spreadsheet's user-interface environment in order to add features like menus, dialogs, and sidebars. This method is consistent with the getUi() methods in DocumentApp and FormApp , but only works in the new version of Google Sheets. The older version of Google Sheets continues to use the existing methods documented in the guides to dialogs and sidebars and menus.
`SpreadsheetApp`
`Spreadsheet.getUi()`
`getUi()`
`DocumentApp`
`FormApp`
## January 13, 2014
Deprecated the SpreadsheetApp.Spreadsheet methods isAnonymousView() , isAnonymousWrite() , isReadable() , isWritable() , and setAnonymousAccess() . Various methods of the File class in DriveApp can achieve the same functionality.
`SpreadsheetApp.Spreadsheet`
`isAnonymousView()`
`isAnonymousWrite()`
`isReadable()`
`isWritable()`
`setAnonymousAccess()`
`File`
`DriveApp`
Renamed the Cursor object in DocumentApp to Position . This does not require any changes to existing code.
`Cursor`
`DocumentApp`
`Position`
Added the SpreadsheetApp method DataValidationBuilder.requireFormulaSatisfied(String) , as well as an accompanying CUSTOM_FORMULA value in DataValidationCriteria . This feature can only be used in the new version of Google Sheets.
`SpreadsheetApp`
`DataValidationBuilder.requireFormulaSatisfied(String)`
`CUSTOM_FORMULA`
`DataValidationCriteria`
## January 06, 2014
- Custom menus in Google Docs now appear in the Help menu search box.
- Custom dialogs created with the HTML service can now be resized by calling google.script.host.setWidth(width) and google.script.host.setHeight(height) in client-side code. Sidebars cannot be resized in client side code.
`google.script.host.setWidth(width)`
`google.script.host.setHeight(height)`
Added the advanced parameter escaping to UrlFetchApp.fetch() . If false , reserved characters in the URL will not be automatically escaped.
`UrlFetchApp.fetch()`
`false`
The Maps.DirectionFinder.Mode enum now includes the TRANSIT value allowing for the retrieval of public transit routes in the Maps service .
`Maps.DirectionFinder.Mode`
`TRANSIT`
`Maps`
## December 16, 2013
Issue 3461 : A yellow warning bar should no longer appear on Apps Script gadgets that are embedded in Google Sites.
- Changed the default syntax for all existing advanced services to match the underlying APIs' reference documentation. The old Apps Script getter/setter notation for these services will continue to work but will no longer appear in autocomplete.
- Renamed the menu entry Resources > Manage libraries to Resources > Libraries .
- Renamed the menu entry Resources > Google APIs Services to Resources > Advanced Google services .
Added seven new advanced services : + Admin SDK Directory service + Admin SDK Reports service + Fusion Tables service + Google+ Domains service + Mirror service + YouTube service + YouTube Analytics service
## December 02, 2013
- Issue 3101 : Removed the SitesApp method Site.deleteSite() , which was never functional.
`SitesApp`
`Site.deleteSite()`
- Issue 3046 : UrlFetchApp now properly preserves RFC 3986 escaping.
`UrlFetchApp`
- Issue 2497 : An rare edge case issue when using UiApp server handler callbacks and libraries no longer occurs.
`UiApp`
- Issue 1346 : An issue in which a library's UiApp server handlers created new server handlers that were not able to reference non-library functions should no longer occur.
`UiApp`
Added TITLE and SUBTITLE values to the DocumentApp.ParagraphHeading enum .
`TITLE`
`SUBTITLE`
`DocumentApp.ParagraphHeading`
## November 18, 2013
The Apps Script methods Utilities.jsonParse() and Utilities.jsonStringify() have been deprecated in favor of the now-standard JavaScript methods JSON.parse() and JSON.stringify() , which now appear in autocomplete.
`Utilities.jsonParse()`
`Utilities.jsonStringify()`
`JSON.parse()`
`JSON.stringify()`
## November 11, 2013
Issue 3189 : A rare issue in which LockService failed to acquire a lock should no longer occur.
`LockService`
## November 04, 2013
If a version of a library has been deleted by the library owner, scripts can no longer use that version.
Issue 2817 : Sporadic errors about missing libraries should now occur less frequently.
## October 21, 2013
Issue 74 : Simple onEdit() triggers now fire correctly when the user is not signed in to a Google account.
`onEdit()`
## October 08, 2013
Added the following FormApp methods, which allow scripts to work with progress bars, custom closed-form messages, and YouTube videos. + Form.hasProgressBar() + Form.setProgressBar(enabled) + Form.getCustomClosedFormMessage() + Form.setCustomClosedFormMessage(message) + Form.addVideoItem()
`FormApp`
`Form.hasProgressBar()`
`Form.setProgressBar(enabled)`
`Form.getCustomClosedFormMessage()`
`Form.setCustomClosedFormMessage(message)`
`Form.addVideoItem()`
## September 23, 2013
Added the following DriveApp methods, which allow scripts to get the owner of a File or Folder.
`DriveApp`
- File.getOwner()
`File.getOwner()`
- Folder.getOwner()
`Folder.getOwner()`
## September 16, 2013
- HTML Service now supports most CSS3 features. A notable exception is the :nth-child() pseudo-selector, which remains unsupported, along with a small number of obscure or non-standardized CSS3 features. To check whether the Caja security sandbox in HTML Service supports a specific feature, see the CSS whitelist definitions in Caja's public repository .
`:nth-child()`
- Added the following DriveApp methods, which allow scripts to save the state of a file or folder iterator and resume at a later time. These method are useful if processing an iterator in one execution would exceed the maximum execution time. FileIterator.getContinuationToken() FolderIterator.getContinuationToken() DriveApp.continueFileIterator(continuationToken) DriveApp.continueFolderIterator(continuationToken)
`DriveApp`
- FileIterator.getContinuationToken()
`FileIterator.getContinuationToken()`
- FolderIterator.getContinuationToken()
`FolderIterator.getContinuationToken()`
- DriveApp.continueFileIterator(continuationToken)
`DriveApp.continueFileIterator(continuationToken)`
- DriveApp.continueFolderIterator(continuationToken)
`DriveApp.continueFolderIterator(continuationToken)`
The UiApp widgets Hyperlink , InlineHyperlink , LayoutPanel , and RichTextArea have now been disabled, as announced on March 13, 2013 and documented in the Apps Script sunset schedule .
`UiApp`
`Hyperlink`
`InlineHyperlink`
`LayoutPanel`
`RichTextArea`
## September 09, 2013
Deprecated the DocumentApp methods getFootnotes() , getLinkUrl() , setLinkUrl(url) , and isAtDocumentEnd() in the classes FooterSection , FootnoteSection , and HeaderSection , as well as the methods getNextSibling() and getPreviousSibling() in the classes FooterSection and HeaderSection . These methods were not useful.
`DocumentApp`
`getFootnotes()`
`getLinkUrl()`
`setLinkUrl(url)`
`isAtDocumentEnd()`
`FooterSection`
`FootnoteSection`
`HeaderSection`
`getNextSibling()`
`getPreviousSibling()`
`FooterSection`
`HeaderSection`
Issue 2621: A situation in which certain scripts did not terminate despite exceeding the execution-time limit no longer occurs.
Added the DocumentApp methods InlineImage.getLinkUrl() and InlineImage.setLinkUrl(url) .
`DocumentApp`
`InlineImage.getLinkUrl()`
`InlineImage.setLinkUrl(url)`
## September 03, 2013
- Added the DriveApp methods DriveApp.getFoldersByName(name) and DriveApp.searchFolders(params) , which return a FolderIterator with the requested results.
`DriveApp`
`DriveApp.getFoldersByName(name)`
`DriveApp.searchFolders(params)`
`FolderIterator`
- Added the DriveApp methods File.getViewers() , File.getEditors() , Folder.getViewers() , and Folder.getEditors() , which return an array of Users with view or edit access.
`DriveApp`
`File.getViewers()`
`File.getEditors()`
`Folder.getViewers()`
`Folder.getEditors()`
`Users`
Removed the ability to get the user's email address in simple onEdit() triggers . Because simple triggers don't request user authentication, this change was important to protect the identity of collaborators who hadn't explicitly granted permission for the script to collect their email address.
`onEdit()`
## August 19, 2013
Added the DriveApp methods File.makeCopy(destination) and File.makeCopy(name, destination) , which allow scripts to specify a folder to which a file should be copied.
`DriveApp`
`File.makeCopy(destination)`
`File.makeCopy(name, destination)`
Issue 3097 : A performance issue that affected certain scripts no longer occurs.
## August 13, 2013
Added the method Spreadsheet.deleteSheet(sheet) , which allows deletions of sheets that are not the active sheet.
`Spreadsheet.deleteSheet(sheet)`
## August 05, 2013
- Added the method GmailMessage.getPlainBody() , which returns the content of the message without HTML formatting.
`GmailMessage.getPlainBody()`
- Launched a new feature to allow programmatic control over data-validation rules in Google Sheets.
- Issue 2916 : HTML files inserted into a new Apps Script project using the Google Drive SDK are no longer created with the server_js filetype.
`server_js`
- Issue 2880 : Special characters (such as apostrophes) no longer need to be escaped twice when passed to DriveApp.getFilesByName() .
`DriveApp.getFilesByName()`
- Issue 2780 : DriveApp now throws a more appropriate error message if Google Drive apps are prohibited within the user's domain.
`DriveApp`
Deprecated the DocsList methods find(query, start, max) , getAllFiles(start, max) , getAllFolders(start, max) , getFiles(start, max) , getFilesByType(fileType, start, max) , and getFolders(start, max) . Instead of these methods, use DriveApp or one of the DocsList.get*ForPaging() methods.
`DocsList`
`find(query, start, max)`
`getAllFiles(start, max)`
`getAllFolders(start, max)`
`getFiles(start, max)`
`getFilesByType(fileType, start, max)`
`getFolders(start, max)`
`DriveApp`
`DocsList.get*ForPaging()`
## July 29, 2013
All new scripts now use the new authorization flow by default.
Issue 2947 : Newlines are now supported in Ui.alert() and Ui.prompt() dialogs.
`Ui.alert()`
`Ui.prompt()`
On ChromeOS devices, it is now possible to activate autocomplete (sometimes called "content assist") with the keyboard shortcut Ctrl + Space .
`Ctrl + Space`
## July 22, 2013
Added DriveApp and FormApp to the services tracked on the Apps Script Dashboard .
`DriveApp`
`FormApp`
Issue 2801 : Fixed an issue in which specific URL parameters did not work with HtmlService .
`HtmlService`
## July 09, 2013
Deprecated the old Xml service, SoapService , and support for the JavaScript feature E4X.
`Xml`
`SoapService`
Added XmlService to replace the old Xml service.
`XmlService`
`Xml`
- Issue 2906 : Chained method calls in advanced Google services no longer throw an exception.
- Issue 2872 : File.removeEditor() no longer throws an exception when the editor is a group instead of an individual user.
`File.removeEditor()`
## June 25, 2013
- Issue 2820 : getActiveSheet() now properly returns the active sheet when used with an onChange trigger.
`getActiveSheet()`
`onChange`
- Issue 2761 : When a Document element that contains an image is copied, the image is now also copied.
`Document`
- Any script that is container-bound to a Google Doc can now access the active user's Cursor and Selection by calling Document.getCursor() and Document.getSelection() , respectively.
`Cursor`
`Selection`
`Document.getCursor()`
`Document.getSelection()`
- The Publish > Deploy as web app dialog now includes an option to save a version of the script, if a version has not previously been saved. Subsequent versions of the script must still be saved through the File > Manage versions dialog.
- Scripts now always require authorization to use the methods Session.getEffectiveUser() or Session.getUser() . Existing scripts that use those methods and were upgraded to the new authorization experience require reauthorization but will not prompt for authorization automatically. To reauthorize the script, follow these instructions .
`Session.getEffectiveUser()`
`Session.getUser()`
- UrlFetch requests made by scripts that run on a time-based trigger now include an If-Modified-Since HTTP header so that Apps Script can use a cached copy of the page if one is available and the page has not changed.
`UrlFetch`
`If-Modified-Since`
## June 17, 2013
- Issue 2626 : The execution transcript now correctly reports the execution time for methods that are called repeatedly.
- Issue 2559 : A sporadic issue in which Spreadsheet.getSheetByName() returned null for a valid sheet name no longer occurs.
`Spreadsheet.getSheetByName()`
- Issue 1965 : Emails forwarded using GmailMessage.forward() now preserve inline images.
`GmailMessage.forward()`
- Issue 1414 : Range.copyTo() now adds additional rows as necessary, if the destination sheet does not have enough rows to accommodate the range.
`Range.copyTo()`
- Issue 1034 : The new Drive Service methods addCommenter() and removeCommenter() allow scripts to add and remove commenters on files.
`addCommenter()`
`removeCommenter()`
- Issue 674 : Mail sent with GmailApp now appears in the Sent Mail folder in Gmail.
`GmailApp`
`Sent Mail`
## June 11, 2013
- Issue 2823 : Timestamps for the start and end of script execution, including total runtime, now appear in the execution transcript ( View > Execution transcript) instead of the log.
- Issue 2807 : A rare issue where a script could not be upgraded to the new authorization flow no longer occurs.
- Issue 2791 : Calling Trigger.getTriggerSource() for a Form-based trigger no longer throws an exception.
`Trigger.getTriggerSource()`
- Issue 2734 : HtmlService scripts that call long-running server-side functions no longer repeat the function call multiple times.
`HtmlService`
## June 03, 2013
- Issue 2819 : Folder.createFile(name, content, mimeType) now creates the file in the folder on which the method was executed.
`Folder.createFile(name, content, mimeType)`
- Issue 2776 : Existing deployed web apps now properly authenticate after upgrading a script to use the new authorization experience.
- Issue 2679 : The getAs() method of the File class no longer throws an error when converting .docx, .pptx, or .xlsx files to PDF.
`getAs()`
- Issue 2643 : The timestamps for a script's log messages are now in the script's timezone.
- Issue 2597 : The script editor's Find functionality no longer skips the first result.
- To simplify the end user experience, function names are no longer shown in the notification message for scripts that run successfully from a spreadsheet, document, or form. Function names are still displayed when there is an error (to help with debugging) and when the script is run from the script editor.
- To simplify the Document service, the following methods were removed from the Body class: getNextSibling() , getPreviousSibling() , isAtDocumentEnd() , getLinkUrl() , setLinkUrl() , and removeFromParent() .
`getNextSibling()`
`getPreviousSibling()`
`isAtDocumentEnd()`
`getLinkUrl()`
`setLinkUrl()`
`removeFromParent()`
## May 13, 2013
- The script editor is now available within Google Docs and the Google Forms editor, and both Docs and Forms can now be containers for scripts.
- Added Forms Service , which allows scripts to create and modify Google Forms.
- Added Drive Service , which allows scripts to create and modify files and folders in Google Drive. This is a newer version of the existing DocsList Service.
- Added a getUi method to DocumentApp and FormApp , which returns a Ui object that allows the script to add features like menus, dialogs, and sidebars to the Docs or Forms editor.
`getUi`
`DocumentApp`
`FormApp`
- Added the FormTriggerBuilder class to allow scripts to respond to Forms events.
`FormTriggerBuilder`
- Added a setSandboxMode method to enable a faster version of the HtmlService sandbox.
`setSandboxMode`
`HtmlService`
- Added a MimeType enum , which provides access to MIME -type declarations without typing the strings explicitly.
`MimeType`
`MIME`
- Added an option to upgrade to a new authorization flow that requires fewer clicks and automatically creates a Google Developers Console project for every script.
## May 09, 2013
Issue 2158 : The request object passed in to doPost() methods now contains the POST body. It can be accessed using e.postData.getDataAsString().
`doPost()`
`POST`
Issue 2740 : UrlFetchApp.fetch() calls no longer fail if the advanced parameters specify a payload without specifying the request method.
`UrlFetchApp.fetch()`
## May 02, 2013
Issue 2585 : Xml.parse() once again correctly parses well-structured XML and HTML documents.
`Xml.parse()`
Issue 1363 : Added support for spreadsheet change events. The onChange() event now fires when certain modifications, such as row insertions, are done to a spreadsheet.
`onChange()`
## April 29, 2013
- Issue 2695 : Form submits in UI Service apps once again work properly.
- Issue 2625 : The withUserObject() method in Html Service apps now works properly with Firefox 20.
`withUserObject()`
`Html`
- Issue 1612 : Element.copy() can now copy InlineImage elements from one document to another.
`Element.copy()`
`InlineImage`
- Issue 170 : Spreadsheet.addCollaborators() now sends an email invitation to collaborators when the emailInvitations advanced parameter is set.
`Spreadsheet.addCollaborators()`
`emailInvitations`
## April 22, 2013
- Issue 2665 : UrlFetchApp.fetch() once again allows URLs that contain spaces.
`UrlFetchApp.fetch()`
- Issue 2593 : Range.setValue() now behaves correctly in a function called from an onEdit spreadsheet trigger.
`Range.setValue()`
`onEdit`
- Issue 941 : The event parameter for a ListBox handler function now includes the value of the selected item rather than its name.
`ListBox`
- Issue 307 : The event parameter for a Tree handler function now includes the ID of the selected item.
`Tree`
Large scripts in the Script Gallery now install more quickly.
- Issue 1771 : Added a clear() method to the Tree and TreeItem classes. These methods remove all children from the object.
`clear()`
`Tree`
`TreeItem`
- Issue 1743 : Added an autoResizeColumn() method to the Sheet class. This method resizes a column to fit its contents.
`autoResizeColumn()`
`Sheet`
- Issue 1314 : Added support for lazy loading in the Tree class, which reduces wait times in rendering the UI.
`Tree`
## April 15, 2013
The following changes were made to simplify the Document service :
`Document`
- Renamed the DocumentBodySection class to Body .
`DocumentBodySection`
`Body`
- Renamed Document.getActiveSection() to getBody() .
`Document.getActiveSection()`
`getBody()`
- Removed methods of the Body class from Document so they only appear in one location.
`Body`
`Document`
- Removed merge() methods for various classes that cannot be merged, such as PageBreak and HorizontalRule .
`merge()`
`PageBreak`
`HorizontalRule`
- Removed text-related methods such as isBold() and isUnderline() from container elements such as Table while retaining them on the Text class. This functionality can now be achieved by calling editAsText() on the container element, and calling the text-related methods on the returned Text class.
`isBold()`
`isUnderline()`
`Table`
`Text`
`editAsText()`
`Text`
- Removed methods which allowed appending or inserting HorizonalRule elements with specified attributes.
`HorizonalRule`
Issue 2565 : DocsList.createFile() no longer allows the creation of files with invalid MIME types or Google document MIME types.
`DocsList.createFile()`
Deprecated UiApp widgets DeckPanel , DecoratedPopupPanel , DockLayoutPanel , DockPanel , StackLayoutPanel , and TabLayoutPanel , which had limited usability.
`UiApp`
`DeckPanel`
`DecoratedPopupPanel`
`DockLayoutPanel`
`DockPanel`
`StackLayoutPanel`
`TabLayoutPanel`
## April 08, 2013
- Issue 2548 : Triggers created in web apps that allow for anonymous access no longer fail to fire.
- Issue 2488 : Charts dashboard components no longer throw serialization errors in certain scenarios.
- Simplified the classes in the Document service , removing unnecessary .asSomething() methods.
`Document`
`.asSomething()`
- Added timestamps to the log output.
## April 01, 2013
Issue 995 : The new methods Sheet.hideSheet() , Sheet.isSheetHidden() , and Sheet.showSheet() allow scripts to control the visibility of individual sheets within a spreadsheet.
`Sheet.hideSheet()`
`Sheet.isSheetHidden()`
`Sheet.showSheet()`
- Issue 2524 : Scripts that rely on deleted libraries now display a clear error message.
- Issue 2169 : Installing scripts from the Script Gallery no longer results in occasional errors.
- Issue 459 : The event parameter for spreadsheet onEdit() functions now reports the affected range correctly in a variety of situations in which the range property was previously incorrect.
`onEdit()`
`range`
## March 25, 2013
- Issue 2534 : Debugging into a recursive function using certain GroupsManager methods no longer throws an error.
`GroupsManager`
- Issue 1106 : Restored the correct behavior of Range.mergeAcross() . This function, along with Range.merge() and the newly added Range.mergeVertically() , behave like the items under a spreadsheet's Format > Merge cells menu.
`Range.mergeAcross()`
`Range.merge()`
`Range.mergeVertically()`
## March 18, 2013
Renamed the action "Publish to Gallery" to "Submit to Gallery", to avoid confusion with publishing a web app.
Deprecated the GUI Builder and the UIApp widgets Hyperlink , InlineHyperlink , LayoutPanel , RichTextArea , and SuggestBox , which had limited usability.
`UIApp`
`Hyperlink`
`InlineHyperlink`
`LayoutPanel`
`RichTextArea`
`SuggestBox`
## March 11, 2013
Issue 1917 : It is no longer possible to install a script multiple times from the Script Gallery.
- View > Execution transcript now shows how much time it took to execute each statement.
- If a script is shared with editors other than its owner and published as a web app, those other editors can now update the app's version and access its development URL (which ends in /dev ).
`/dev`
- Added the method Utilities.formatString() , which allows printf-like substitution of placeholders within a format string.
`Utilities.formatString()`
- Added the property DocsList.FileType.FORM to let DocsList access new Google Forms.
`DocsList.FileType.FORM`
`DocsList`
## March 04, 2013
- Issue 1182 : Calendar.getEvents(startTime, endTime, statusFilters) now works properly.
`Calendar.getEvents(startTime, endTime, statusFilters)`
- Issue 459 : OnEdit callbacks triggered by pasting to a cell now provide the correct range parameter.
`OnEdit`
## February 25, 2013
When setting font colors in a spreadsheet using Range.setFontColor() or Range.setFontColors() , color names will now automatically be converted to their corresponding hexadecimal values. For example, after calling setFontColor('red') the method getFontColor() will return "#ff0000".
`Range.setFontColor()`
`Range.setFontColors()`
`setFontColor('red')`
`getFontColor()`
- Issue 2435 : Spreadsheet-bound scripts that use Browser.inputBox() no longer fail.
`Browser.inputBox()`
- Issue 1128 : Font colors set using Range.setFontColor() or Range.setFontColors() now appear correctly when printing the spreadsheet or exporting it as a PDF.
`Range.setFontColor()`
`Range.setFontColors()`
- Issue 529 : SpreadsheetApp.getActiveSheet() no longer fails to run in onOpen() triggers for certain spreadsheets.
`SpreadsheetApp.getActiveSheet()`
`onOpen()`
## February 14, 2013
Added the method DocumentApp.openByUrl() , which allows documents to be opened by their URL directly.
`DocumentApp.openByUrl()`
- Issue 2382 : File.makeCopy() no longer produces an error when copying a new Google Form.
`File.makeCopy()`
- Issue 2367 : The error message for invalid queries of ScriptDbInstance.between() is now more descriptive.
`ScriptDbInstance.between()`
- Issue 747 : Error messages now specify in which code file the error occurred.
## February 11, 2013
- Issue 2388 : The quota dashboard once again displays the correct number of columns.
- Issue 2344 : Scripts that contain onInstall() functions no longer produce an error when installed from the Script Gallery.
`onInstall()`
- Issue 2250 : Dates are now logged in the script's time zone.
- Issue 2021 : UiInstance.setStyleAttribute() now properly sets the backgroundImage property in all supported browsers.
`UiInstance.setStyleAttribute()`
`backgroundImage`
- Issue 1811 : The debugger can now step into libraries used in development mode.
- Issue 1300 : If a script bound to one spreadsheet uses an installable onEdit() trigger to monitor a separate spreadsheet, the range event parameter passed to the callback function now correctly recognizes the monitored spreadsheet as its parent.
`onEdit()`
- Issue 1226 : Client handlers for ListBox now fire properly in UiApp .
`ListBox`
`UiApp`
- Issue 1030 : The setStyleAttribute() method of various UiApp objects now properly sets the 'float' attribute in Firefox.
`setStyleAttribute()`
`UiApp`
- Issue 1014 : setFocus() now works correctly.
`setFocus()`
- Issue 231 : Added show() and hide() methods to PopupPanel .
`show()`
`hide()`
`PopupPanel`
Added the ability to directly attach StaticMap objects in emails.
`StaticMap`
## January 31, 2013
- Issue 2317 : Email address validation in UiApp now works correctly with uppercase input.
`UiApp`
- Issue 2306 : The GUI Builder dialog shown for File > Open no longer has two "Cancel" buttons.
- Issue 2265 : Static maps can now contain many more markers.
- Issue 2203 : CalendarEvent.getGuestList() now returns the event creator in addition to the other guests.
`CalendarEvent.getGuestList()`
- Issue 2137 : A DateBox containing an empty or invalid date will now have a null value when processed in a server handler or doPost() callback. By default, setting an empty or invalid date will not trigger a value-changed event, but you can call the method setFireEventsForInvalid() to override that behavior.
`DateBox`
`doPost()`
`setFireEventsForInvalid()`
- Issue 1795 : TextArea widgets created using the GUI Builder now default to displaying scrollbars when the text is too long.
`TextArea`
- Issue 1764 : ClockTriggerBuilder.onWeekDay() now works correctly when used in conjunction with everyWeeks() .
`ClockTriggerBuilder.onWeekDay()`
`everyWeeks()`
- Issue 1695 : GmailLabel.getThreads() now works correctly when the label name contains special characters.
- Issue 1366 : The methods getEditors() and getViewers() of the File class now return the full email address for entries that are groups.
- Issue 918 : Subsequent calls to Sheet.hideColumns() on different sheets no longer results in an error.
- Issue 53 : Rows containing only data-validation rules no longer count towards Sheet.getLastRow().
Added the method SpreadsheetApp.openByUrl() , which allows spreadsheets to be opened by their URL directly.
`SpreadsheetApp.openByUrl()`
- Changed the behavior of ClockTriggerBuilder so that it now respects the time zone of the script, instead of defaulting to Pacific Time.
`ClockTriggerBuilder`
- The editor's Find dialog now supports searching over all files in the project.
- Improved the error message returned by Range.setValues() when the values fail to pass the validation on those cells.
`Range.setValues()`
## January 24, 2013
- Issue 1642 : When connecting to an external database with Jdbc.getConnection , you can now include the advanced argument use JDBCCompliantTimezoneShift .
`Jdbc.getConnection`
`JDBCCompliantTimezoneShift`
- Issue 619 : UiInstance 's createAnchor method now allows links using the mailto scheme.
`UiInstance`
`createAnchor`
`mailto`
- Issue 286 : UrlFetchApp 's fetch method now accepts followRedirects as an advanced argument.
`UrlFetchApp`
`fetch`
`followRedirects`
- Issue 1012 : New calendar entries that span a time change (for example, the start of daylight saving time in that time zone) are now created with the correct duration.
- Issue 912 : It is now possible to display non-public images in a UiApp or HtmlService user interface, so long as the images are shared with the app's users.
`UiApp`
`HtmlService`
- Issue 815 : UiInstance 's createToggleButton(upText, downText) method now functions correctly.
`UiInstance`
`createToggleButton(upText, downText)`
- Issue 155 : Calendar.createAllDayEvent now always sets the event to the correct date.
`Calendar.createAllDayEvent`
## January 17, 2013
- Issue 2155 : The Uninstall link emailed to a user after authorizing a script embedded within a Google Site now works correctly.
`Uninstall`
- Issue 1882 : Icons in the Script Editor now display correctly on Macs with Retina displays.
Added the method after(durationMilliseconds) to class ClockTriggerBuilder to simplify the creation of one-off triggers.
`after(durationMilliseconds)`
`ClockTriggerBuilder`
## January 15, 2013
Issue 2204 : Utilities.formatDate no longer rejects certain time-zone formats, such as EST, CST, etc.
`Utilities.formatDate`
## December 17, 2012
- Issue 2131 : The timezone offset for "Europe/Moscow" is now correct.
- Issue 2124 : ScriptDb no longer throws an error when storing a float value.
`ScriptDb`
- Issue 2021 : Setting the background image of a UiApp panel now works correctly.
`UiApp`
- Issue 1856 : The Jdbc service now resolves host names correctly.
- Issue 1312 : The error message shown when the rate limit for spreadsheet creation is exceeded is now more readable.
- Issue 949 : Typing the character } on a Spanish keyboard now works correctly.
`}`
## December 11, 2012
Added extra validation to the datasource URLs used in charts. Custom datasource URLs that rely on non-Google authentication will no longer work.
- Issue 2100 : ScriptProperties.setProperties() now respects the deleteAllOthers parameter.
`ScriptProperties.setProperties()`
`deleteAllOthers`
- Issue 2052 : UiApp' s setStyleAttribute() method no longer rejects certain style attributes.
`UiApp'`
`setStyleAttribute()`
- Issue 2041 : The native Date methods toLocaleDateString() and toLocaleTimeString() now return the correct values.
`Date`
`toLocaleDateString()`
`toLocaleTimeString()`
- Issue 1972 : Web apps published from a domain, but available to everyone, now use the normal Google login page instead of domain's login page.
- Issue 1876 : The authorize link for scripts embedded in a Google Sites gadget now opens in a new tab/window.
- Issue 1870 : CalendarEvent.getVisibility() now returns the correct value.
`CalendarEvent.getVisibility()`
- Issue 1528 : Using ContactsApp to modify multiple fields of a contact in quick succession no longer causes an etags mismatch error.
`ContactsApp`
- Issue 1502 : Logs are now saved correctly for scripts that run as a web app, from a spreadsheet menu, or due to a trigger.
- Issue 1275 : Deleting a script now deletes any associated triggers.
## November 28, 2012
- Fixed an issue where onFormSubmit trigger's callback range was incorrect if the submit triggered a formula recalculation.
`onFormSubmit`
- Fixed an issue where XmlDocument properties and functions did not autocomplete when generating an XmlDocument with the Soap service.
`XmlDocument`
- Added an enhancement to GmailApp to allow retrieval of bcc addresses via GmailMessage.getBcc() .
`GmailApp`
`GmailMessage.getBcc()`
- Tree widgets now allow specifying open handlers as well as close handlers.
## November 21, 2012
- Fixed an issue where public locks are not correctly released.
- Fixed an issue to allow multiple comma-delimited replyTo addresses in MailApp.sendEmail() .
`replyTo`
`MailApp.sendEmail()`
- Fixed an issue with auto-complete for library functions not working when that library contained HTML files.
## November 13, 2012
Added the ability to disable SSL certificate validation in the SoapService , in response to a feature request.
`SoapService`
- Fixed an issue where MailApp 's and GmailApp 's sendEmail function ignored the advanced parameter name .
`MailApp`
`GmailApp`
`sendEmail`
`name`
- Fixed an issue where new library versions took a long time to propagate to other scripts.
## November 06, 2012
Updated some icons to match icons of other Google Drive applications.
- Fixed an issue where a script failure notice would refer to the script as "Not Found" in cases where the failure is caused by an auth issue.
- Fixed an issue where it was not possible to save scripts with more than ~1 million characters.
- Fixed an issue where LockService did not work correctly when called from a UiApp .
`LockService`
`UiApp`
Added options to EmbeddedChartBuilder to make it easier to configure embedded charts. EmbeddedChartBuilder now contains the methods asAreaChart() , asBarChart() , asColumnChart() , asLineChart() , asPieChart() , asScatterChart() and asTableChart() as replacements for calls to setChartType() .
`EmbeddedChartBuilder`
`EmbeddedChartBuilder`
`asAreaChart()`
`asBarChart()`
`asColumnChart()`
`asLineChart()`
`asPieChart()`
`asScatterChart()`
`asTableChart()`
`setChartType()`
## October 26, 2012
- Fixed an issue where the DocsList service was unable to retrieve more than 2000 files. Several new methods were added to the DocsList class ( getFilesForPaging, etc.) that use continuation tokens as described in the documentation.
`DocsList`
`DocsList`
`getFilesForPaging,`
- Fixed an issue where placing a null value via data table's addRow method produced an error.
`addRow`
- Fixed an issue where the debugger would throw an exception when using ScriptDb .
`ScriptDb`
- Fixed an issue where ScriptDb 's saveBatch() method was returning the incorrect number of result objects.
`ScriptDb`
`saveBatch()`
- Fixed an issue where UiApp 's setStyleAttribute() method failed when using the attribute backgroundImage .
`UiApp`
`setStyleAttribute()`
`backgroundImage`
- Fixed an issue where the last modified date for standalone wasn't updating.
- Fixed an issue where GmailThread 's moveToArchive() method wasn't working on threads in the trash.
`GmailThread`
`moveToArchive()`
- Fixed an issue where ampersands in UiApp 's Hidden widgets were being escaped incorrectly.
`UiApp`
`Hidden`
- Fixed an issue where UiApp 's validateOptions() method always threw an error.
`UiApp`
`validateOptions()`
- Added the ability to list alternate sender addresses using GmailApp.getAliases() and use them in GmailApp.sendEmail() with the advanced option "from".
`GmailApp.getAliases()`
`GmailApp.sendEmail()`
- Created the class GmailAttachment , which is the same as a Blob but provides a getSize() method that isn't subject to quota restrictions.
`GmailAttachment`
`Blob`
`getSize()`
- Added the ability to set a custom app icon for web apps published to the Chrome Web Store. This is the icon that shows up on Chrome's New Tab Page. More information on the Publishing to the Chrome Web Store page .
- Added the ability to close containing dialogs from HtmlService pages. More information on the Html Service page .
`HtmlService`
- Improved JavaScript execution performance.
- Removed the "File -> New -> From Script Template" option in the script editor.
- Limited the ability to programmatically submit a form in JavaScript served by the HtmlService . Calling form.submit() is only allowed when done in the callback for a user-generated click or keypress event.
`HtmlService`
`form.submit()`
## September 28, 2012
Fixed an issue where certain files could not be copied via DocsList.copy() .
`DocsList.copy()`
## September 21, 2012
- Fixed an issue where arrays retrieved from ScriptDb didn't behave properly.
`ScriptDb`
- Fixed an issue where the execution transcript would stop recording after Browser.msgBox() was called.
`Browser.msgBox()`
- Fixed an issue where scriptlet tags in HtmlTemplates behaved strangely when in attribute values.
`HtmlTemplates`
- Fixed a problem that prevented scripts from sending POST requests to other scripts that used the ContentService .
`POST`
`ContentService`
Updated DocsList.getFilesByType() to accept values from the DocsList.FileType enumeration. Passing in string values for the document type is deprecated but still functional. (Issue 1755)
`DocsList.getFilesByType()`
`DocsList.FileType`
Enabled SSL certificate validation for UrlFetchApp requests. If you wish to disable this behavior you can set the advanced option validateHttpsCertificates to "false".
Added a setLabelSeparator() method to CategoryFilterBuilder , to allow for label separator strings to be used.
`setLabelSeparator()`
`CategoryFilterBuilder`
## September 07, 2012
- Fixed an issue where selecting a value from a DateBox would cause the value changed handler to fire twice.
`DateBox`
- Fixed an issue where Chart dashboard StringFilters ignored the MatchType that was set.
`StringFilters`
`MatchType`
Added an isDeleted() method to SitesApp 's Page class .
`isDeleted()`
`SitesApp`
`Page`
## August 30, 2012
- Added methods to delete ScriptProperties and UserProperties . Additional methods were also added to set multiple properties, get all properties, etc.
`ScriptProperties`
`UserProperties`
- Added a setOption method to the various chart builders to make it possible to set advanced options for Charts.
`setOption`
Fixed an issue with scrolling in the script editor so that line numbers will be displayed even when horizontally scrolling on long lines.
## August 22, 2012
- Fixed an issue where only one project was copied when making a copy of a Spreadsheet with multiple projects.
- Fixed an issue where scripts were not installing properly from the Script Gallery.
## August 20, 2012
- UiApp widgets now have a setStyleAttributes method which allow you to set multiple attributes at once.
`UiApp`
`setStyleAttributes`
- Added a new log method to the Logger service which accepts a format string and a variable number of values to insert.
`log`
- Increased the allowed file upload size in web apps to 50MB, to match the limit in the DocsList service.
`DocsList`
- Streamlined the process for publishing web apps to the Chrome Web Store so that developers no longer need to manually verify web app URLs via Webmaster Central.
- Fixed an issue where the DatePicker widget returned strange values for dates before 1970.
`DatePicker`
- Fixed an issue where all day event series weren't scheduled correctly in certain timezones.
- Fixed an issue that prevented an HTML form element from being set in a google.script.run callback.
`google.script.run`
- Fixed an issue where embedded charts were returned with the wrong data type.
- Fixed an issue where Charts ignored advanced parameters of data source URLs.
## August 03, 2012
- Fixed an issue where the "parameter" field in the doGet() event argument was missing if no parameters were passed in the URL.
`doGet()`
- Fixed two issues where the DatePicker and DateBox UI components didn't have a setName() method, preventing them from being used as callback elements in UI apps.
`DatePicker`
`DateBox`
`setName()`
- Fixed an issue where the DatePicker part of a DateBox didn't inherit the z-index style.
`DatePicker`
`DateBox`
- Fixed an issue where HtmlTemplates could not be loaded within other templates.
`HtmlTemplates`
- Fixed an issue where users would receive "Summary of failures for Apps Script" error for a failed trigger, even after the script was deleted.
- Fixed an issue where incorrect JsDoc comments in a library would prevent auto-complete from working on it.
Added a getThumbnail() method to the DocsList service's File class .
`getThumbnail()`
`DocsList`
`File`
## July 26, 2012
- Fixed an error in the Gmail script template from the welcome screen.
- Fixed an issue where saving an object in ScriptDb with an empty string key causes errors.
`ScriptDb`
- Fixed an issue where scripts were not being copied when a Site was copied.
- Fixed an issue with DatePicker.setValue .
`DatePicker.setValue`
- Added support for chatting with script collaborators in the Script Editor. When two or more people are collaborating on a script, a chat panel will be visible on the right-hand side of the Script Editor.
- Added the ability to support autocomplete for included libraries when they are included in development mode.
- Added UiInstance.remove methods to remove widgets from UiInstance .
`UiInstance.remove`
`UiInstance`
- Added support for Google Analytics via the Analytics Service.
`Analytics`
Made improvements to the speed of handling large batches of data in ScriptDb .
`ScriptDb`
## July 19, 2012
Fixed an issue where setting an empty key in Script Properties or User Properties resulted in a "Data storage error" message.
`Script`
`User`
## July 16, 2012
Updated the link to the support page on the Google Apps Script Dashboard .
Fixed an issue where the script editor could not be accessed for some container-bound scripts.
## June 27, 2012
- Launched script.google.com and the ability to create standalone scripts that are not bound to a container like Google Sheets or Google Sites.
- Launched the Html Service , which you can use to create web apps using HTML, CSS, and JavaScript. The reference documentation is here .
`Html`
- Launched the Content Service , which you can use to serve text in various forms, such as text, XML, RSS, or JSON.
`Content`
- Launched ScriptDb , a JavaScript object database for Apps Script. The reference documentation is here .
`ScriptDb`
- Added the ability to publish web apps with versioning and with the option to have them execute as the user accessing the app.
- Added support for registering Apps Script web apps in the Chrome Web Store , making it quick and simple to publish and distribute your web apps.
## June 19, 2012
Added a scrollbar to the file panel in the Script Editor,
## June 18, 2012
- The Script Editor's user interface has been updated.
- Publish > Publish as service is now Publish > Deploy as web app . Additionally, for new scripts, before you can deploy them as a web app, you must first save a version of the script. You can then choose which version should be served when the script is deployed as a web app. For existing scripts that were already published as a service, you will still be able to access the published URL from the Deploy as web app dialog, but to make additional changes, you will need to save a version of the script.
## June 14, 2012
- Added the ability to create, modify, and remove Embedded Charts in Google Sheets. Embedded Charts are charts that live solely within Spreadsheets and use multiple ranges of data for their datasource.
- Added support to the Domain Service for NicknameManager and GroupsManager .
`Domain`
`NicknameManager`
`GroupsManager`
Fixed an issue where PDF documents uploaded and saved to Google Drive were being saved as blank files.
## June 08, 2012
Simplified sharing settings for scripts. For new script projects, the script will inherit the permissions of its parent. For example, if a script is associated with a Spreadsheet, and user1@example.com has edit access to the Spreadsheet, then user1@example.com will have edit access to the script. The extra blue Share button will no longer be present on these newly created scripts, since the permissions are tied to those of the parent. For scripts created prior to June 8, 2012, the Share button will remain if the checkbox to "Allow document collaborators to edit project" or "Allow site collaborators and owners to edit project" was not selected for that script. For more information see Security . If you would like to have script source that cannot be modified by the editors of your Spreadsheet or Site, then you can use Script Libraries .
## May 21, 2012
- Launched Script Libraries and Versions in response to this feature request .
- Added getDescription() and setDescription() methods to File and Folder .
`getDescription()`
`setDescription()`
`File`
`Folder`
- Updated the Help > Support link in the Script Editor to point to this support page .
- Set a limit of 20 triggers per script. This limit takes effect as of May 21. For scripts created prior to that date, which already have more than 20 triggers, they will keep the existing triggers, but cannot add new ones without removing existing triggers.
Fixed an issue with ClockTriggerBuilder.nearMinute , where invalid minute values were sometimes created.
`ClockTriggerBuilder.nearMinute`
## May 11, 2012
- Fixed an issue with the debugger, so that it no longer fails when a breakpoint is set on certain classes from the JDBC service.
- Fixed an issue with UiApp , so that modifying a spreadsheet cell from a submit handler no longer causes an empty file to be downloaded.
`UiApp`
## May 04, 2012
- Fixed an issue with Site.getOwners() , Site.getReaders() , Site.getEditors() , where the methods were failing in some cases.
`Site.getOwners()`
`Site.getReaders()`
`Site.getEditors()`
- Fixed an issue with ScriptApp.getService().getUrl() so that the method can be called by users other than just the script owner.
`ScriptApp.getService().getUrl()`
- Fixed an issue with the Script Editor, where developers were prompted to recover a draft version of another file in the same project, rather than the one being edited.
- Fixed an issue with resuming continuations (such as in a script that waits for user input via message box), so that the scripts correctly honor the 6 minute script execution limit.
- Fixed an issue with UiApp.ClientHandler.setValue() so that it doesn't return errors and also works for checkboxes.
`UiApp.ClientHandler.setValue()`
Added a DocumentApp.HorizontalAlignment.JUSTIFY value to the DocumentApp.HorizontalAlignment enumeration.
`DocumentApp.HorizontalAlignment.JUSTIFY`
`DocumentApp.HorizontalAlignment`
Launched the Google Apps Script Dashboard so that developers can view service health and quota limits.
## April 19, 2012
- Added the method everyMinutes() to Script Service.
`everyMinutes()`
`Script`
- Items in the Help menu in the Script Editor now open in a new tab instead of a new window.
- Made some modifications to the calculation of CPU time for scripts running on triggers, so that time spent waiting on certain processes is not counted toward that limi
## April 16, 2012
- Fixed an issue in the Script Editor where the debugger would not terminate after executing the last statement of a script.
- Fixed an issue where an embedded image would not copy properly in a Google Document.
- Fixed an issue where a shared folder would not show up in "Collections shared with me".
- Increased the size of the files that can be created via DocsListApp.createFile() from 2MB to 50MB.
`DocsListApp.createFile()`
- Increased the allowed argument value for Utilities.sleep() from 5000 (5 seconds) to 300000 (5 minutes).
`Utilities.sleep()`
- Updated the script failure notification emails to include the name and a link of the spreadsheet that contains the failed script in response to this issue
- Increased the allowed attachment size for emails sent via GmailApp and MailApp from 5MB to 25MB.
`GmailApp`
`MailApp`
- Added method to DocsList service to getRootFolder() .
`DocsList`
`getRootFolder()`
- Added method to File and Folder classes to check whether the item isTrashed() .
`File`
`Folder`
`isTrashed()`
## April 11, 2012
Fixed an issue where files and collections in Google Docs could not be shared with groups.
## April 04, 2012
Modified document collaboration and sharing rules to make them consistent with what is possible in the user interface.
Launched the Script service in response to this feature request , which allows developers to programmatically set triggers and manage the publishing of scripts as a service.
`Script`
## March 20, 2012
Fixed an issue where Spreadsheet.insertSheet() failed to properly copy a sheet when given a {template:sheet_obj} parameter.
`Spreadsheet.insertSheet()`
`{template:sheet_obj}`
## March 13, 2012
- Fixed an issue where functions in the Utilities Service were not handling UTF-8 strings correctly.
`Utilities`
- Fixed an issue where text in a ListBox widget was being unnecessarily HTML-encoded.
`ListBox`
- Fixed an issue where Anchor.setWordWrap() was throwing errors.
`Anchor.setWordWrap()`
- Fixed an issue with UiApp panels that launch from a Google Spreadsheet, where the X to close was not displaying if the title of the application was not set.
`UiApp`
- Fixed an issue in the GUI Builder where setting the visibility for a widget to false was not working.
Added the ability to set the subject line via the subject field in the advanced arguments for GmailMessage.forward() .
`subject`
`GmailMessage.forward()`
## March 07, 2012
- Added the ability to set the target for an Anchor in UI app, in response to this issue .
- Added the ability to include a limited set of HTML tags when working with UiApp widgets, in response to this issue . Here is the list of HTML tags that are permitted: B , BLOCKQUOTE , BODY , BR , CENTER , CAPTION , CITE , CODE , DIV , EM , H1 , H2 , H3 , H4 , H5 , H6 , HR , I , LABEL , LEGEND , LI , OL , P , SPAN , STRONG , SUB , SUP , TABLE , TBODY , TD , THEAD , TITLE , TR , TT , UL
`B`
`BLOCKQUOTE`
`BODY`
`BR`
`CENTER`
`CAPTION`
`CITE`
`CODE`
`DIV`
`EM`
`H1`
`H2`
`H3`
`H4`
`H5`
`H6`
`HR`
`I`
`LABEL`
`LEGEND`
`LI`
`OL`
`P`
`SPAN`
`STRONG`
`SUB`
`SUP`
`TABLE`
`TBODY`
`TD`
`THEAD`
`TITLE`
`TR`
`TT`
`UL`
- Added support for sheet protection, in reference to this issue . Introduced two new methods: Sheet.getSheetProtection and Sheet.setSheetProtection , as well as a new PageProtection class.
`Sheet.getSheetProtection`
`Sheet.setSheetProtection`
`PageProtection`
- Added documentation for DocsListDialog . "Unexpected error" is no longer thrown when trying to display it.
`DocsListDialog`
- The Script Editor's menus have been updated: A new Resources menu is added. The Share menu is renamed to Publish. Triggers' management is moved to Resources menu. Google API Services console is moved to Resources menu. Links under the Help menu now open in a new tab rather than a new window in Firefox 9.x and Chrome.
- A new Resources menu is added.
- The Share menu is renamed to Publish.
- Triggers' management is moved to Resources menu.
- Google API Services console is moved to Resources menu.
- Links under the Help menu now open in a new tab rather than a new window in Firefox 9.x and Chrome.
- Changed the window that appears after Authorization to the script has been granted. It is now displayed in a new tab rather than a pop-up. This tab will no longer close automatically after 5 seconds.
- Updated the appearance of the warning bar that is displayed when running a script that is published as a service by a user other than the owner, in response to this issue.
## February 12, 2012
- Added methods to the Document class to addHeader() and addFooter() .
`Document`
`addHeader()`
`addFooter()`
- Added a merge() method to the Range class.
`merge()`
`Range`
- Fixed an issue with using tab key to format code in the script editor.
- Fixed an issue where email quotas were too restrictive when executed by an anonymous user from a script running as a service.
## February 06, 2012
- Added a feature to cancel running scripts, when the script is run from the script editor.
- Added getEventSeriesById() to Calendar.
`getEventSeriesById()`
## January 31, 2012
Fixed an issue where Anchor.setWordWrap() was not working.
`Anchor.setWordWrap()`
## January 24, 2012
- Added the setNestingLevel() method to ListItem .
`setNestingLevel()`
`ListItem`
- Added the setGlyphType() method to ListItem to support glyph types other than numeric glyphs.
`setGlyphType()`
`ListItem`
- Added getWidth() and setWidth() methods to TableCell .
`getWidth()`
`setWidth()`
`TableCell`
- Fixed some issues where autocomplete stopped working after certain statements were typed in the script editor.
- Fixed an issue with the sizing of images when using Document.appendImage() .
`Document.appendImage()`
- Fixed an issue where an error occurred when opening a document after the Document.saveAndClose() method had previously been called.
`Document.saveAndClose()`
## January 11, 2012
Fixed an issue with Paragraph.setHeading() where text was not formatted as expected.
`Paragraph.setHeading()`
## December 14, 2011
Fixed an issue with the debugger, where it would close when stepping into a function that is located in a different file.
- Enabled Spreadsheet.show() in autocomplete.
`Spreadsheet.show()`
- Added the ability to copy and paste from the Revision History.
- Added support for the Groups Services .
`Groups`
- Added support for the Domain Services .
`Domain`
- Added support for the AdSense Services .
`AdSense`
## November 07, 2011
- Fixed an issue with Session.getTimezone() returning incorrect values.
`Session.getTimezone()`
- Fixed an issue with the Edit > Find feature in the script editor.
- Added the Lock and Cache services.
`Lock`
`Cache`
- Added support for client handlers and validators .
## September 26, 2011
- Added support for inlineImages when sending emails with MailApp.sendEmail() .
`inlineImages`
`MailApp.sendEmail()`
- Added the Charts Services , which allow users to dynamically create charts and embed them in emails, UiApp, or export them as images.
- Added the Prediction Services , which allow users to access a cloud hosted machine learning service that makes it easy to build smart apps. Added the Tasks Services , which allow users to manage tasks and task lists. Added the UrlShortener Services , which let you create, inspect, and manage goo.gl short URLs.
`UrlShortener`
Fixed an issue where an error occurred if an empty ListBox was used as a callback element.
`ListBox`
`callback`
## August 04, 2011
Added support for ScrollPanel to the GUI Builder.
`ScrollPanel`
## July 25, 2011
Added supports for projects in Apps Script.
Fixed an issue where Xml.element failed if the child elements were XmlElements .
`Xml.element`
`XmlElements`
## July 14, 2011
Fixed an issue where GmailApp.getUserLabelByName() failed for label names that contained spaces.
`GmailApp.getUserLabelByName()`
## May 04, 2011
- Added the Gmail service .
`Gmail`
- Added the Document service .
`Document`
- Introduced the GUI Builder .
## April 15, 2011
Added an appendRow() method to Spreadsheet.
`appendRow()`
Fixed an issue with UiApp.getActiveApplication().setStyleAttribute() for 'cursor.'
`UiApp.getActiveApplication().setStyleAttribute()`
## March 21, 2011
- Improved performance of the script editor. The editor can now handle large scripts without any issues in most major browsers.
- Improved the internal error handling of the Spreadsheet Service, so that fewer errors are received by users.
- Increased the timeout of UrlFetch to 30 seconds.
`UrlFetch`
- Binary files can be uploaded using FileUpload .
`FileUpload`
- Enhanced ListBox to function as a multi-select ListBox .
`ListBox`
`ListBox`
- Fixed a minor bug Script as a Service related to expired tokens.
- Breakpoint in debugger now clears as expected.
- SpreadsheetApp.getActiveSheet() when executed in Installable onEdit returns the correct sheet name.
`SpreadsheetApp.getActiveSheet()`
`Installable onEdit`
## March 08, 2011
- Fixed an issue which improves performance of various Services.
- Fixed an issue with Authorization of scripts.
Added a method in Utilities class that parses CSV text.
`Utilities`
## January 21, 2011
Introducing the Debugger! The debugger significantly enhances the ability of Apps Script users to debug their scripts. With the debugger, users can set breakpoints, inspect variables, step-in and step-out of functions.
## October 21, 2010
Added integration with Google Sites, so that Apps Script can now be run from within Google Sites. Read more here.
## October 16, 2010
- Added ability for users to create new recurring calendar events through CalendarApp.newRecurrence() and Calendar.createEventSeries() .
`CalendarApp.newRecurrence()`
`Calendar.createEventSeries()`
- Added ability to access existing event series through CalendarEvent.getEventSeries() .
`CalendarEvent.getEventSeries()`
- Added ability for users to modify or delete an entire event series through CalendarEventSeries .
`CalendarEventSeries`
## September 17, 2010
- Added new methods to CalendarEvent to get the creation date and the date the event was last updated: getDateCreated() and getLastUpdated() .
`CalendarEvent`
`getDateCreated()`
`getLastUpdated()`
- Added a new method to Contact to get the date a contact was last updated: getLastUpdated() .
`Contact`
`getLastUpdated()`
- Fixed two issues with Calendar.getEvents() . GetEvents previously returned only the first instance of a recurring event in a given time range. Now it returns all instances of the recurring event in the given time range. Additionally, editing the instance of the recurring event previously would edit the entire series. Now, editing an instance of a recurring event edits only the particular instance.
`Calendar.getEvents()`
`GetEvents`
- Fixed an issue where the unpublished version of onInstall was being run for scripts in the Script Gallery.
`onInstall`
- Fixed an issue where users could not type ( in the script editor when the autocomplete popup was visible.
`(`
- Fixed an issue where getActiveSheet was not working when called from onEdit events. Fixed an issue with UiApp where the UI panels were not displayed properly and an "Error encountered: An unexpected error occurred" error message was displayed.
`getActiveSheet`
`onEdit`
## August 16, 2010
- Added Spreadsheet.show() to the script editor autocomplete and the documentation.
`Spreadsheet.show()`
- Clarified the use of Session.getUser() and added two new methods: Session.getActiveUser() and Session.getEffectiveUser() .
`Session.getUser()`
`Session.getActiveUser()`
`Session.getEffectiveUser()`
- Added support for persistent storage in scripts via UserProperties and ScriptProperties . Script Properties and User Properties are also available from File > Properties in the script editor.
`UserProperties`
`ScriptProperties`
- Added several new methods to the Contact class: Contact.getGivenName() , Contact.setGivenName() , Contact.getMiddleName() , Contact.setMiddleName() , Contact.getFamilyName() , Contact.setFamilyName() , Contact.getMaidenName() , Contact.setMaidenName() , Contact.getNickname() , Contact.setNickname() .
`Contact`
`Contact.getGivenName()`
`Contact.setGivenName()`
`Contact.getMiddleName()`
`Contact.setMiddleName()`
`Contact.getFamilyName()`
`Contact.setFamilyName()`
`Contact.getMaidenName()`
`Contact.setMaidenName()`
`Contact.getNickname()`
`Contact.setNickname()`
- Major improvements to the Sites service, fixing many issues and adding new functionality.
- Added support for find and replace in the script editor.
- UiApp is now available to all users. Previously, it was only available to Google Apps Premier domains.
`UiApp`
- The timezone for a script can now be set from File > Properties in the script editor.
- The user interface for time-based triggers has been updated to make it more clear that the events are triggered between N and N+1 hours.
- The script timezone is now visible in the script triggers dialog.
- Revision history for scripts is now available from File > See revision history in the script editor.
- Added two new methods to the Utilities class provide JSON support: Utilities.jsonParse() and Utilities.jsonStringify() .
`Utilities.jsonParse()`
`Utilities.jsonStringify()`
- Added support for outbound OAuth requests. See UrlFetchApp.addOAuthService() .
`UrlFetchApp.addOAuthService()`
- Added a new method to class Spreadsheet to get the form URL: Spreadsheet.getFormUrl() .
`Spreadsheet`
`Spreadsheet.getFormUrl()`
- Added a new Blob class to simplify moving data between different Google Apps Script services.
`Blob`
## August 01, 2010
Fixed an issue with the Sheet.getFrozenRows , where an error was returned in some cases.
`Sheet.getFrozenRows`
- Added two new methods to the Sheet class for getting frozen rows and columns: Sheet.getFrozenRows() and Sheet.getFrozenColumns() .
`Sheet`
`Sheet.getFrozenRows()`
`Sheet.getFrozenColumns()`
- Added sorting methods: Sheet.sort() and Range.sort() .
`Sheet.sort()`
`Range.sort()`
- Added methods to get row height and column width in a Sheet: Sheet.getRowHeight() and Sheet.getColumnWidth() .
`Sheet.getRowHeight()`
`Sheet.getColumnWidth()`
## July 12, 2010
- Added two new methods to the Soap service for setting and getting the SOAP endpoint: WsdlService.getEndpointOverride() and WsdlService.setEndpointOverride() .
`WsdlService.getEndpointOverride()`
`WsdlService.setEndpointOverride()`
- Added a method to check if there is remaining quota for sending emails for the current day: MailApp.getRemainingDailyQuota() .
`MailApp.getRemainingDailyQuota()`
- Fixed an issue with the Contacts service, where a 'Mismatch: etags' error was thrown when a contact was modified more than once.
`Contacts`
- Fixed an issue where a popup dialog with the text "Error encountered: An unexpected error occurred" was displayed when the change handler for a ListBox was called , but no app was returned by the change handler.
`ListBox was called`
- Fixed an issue where ListBox.addItem wasn't working after calling getElementById .
`ListBox.addItem`
`getElementById`
- Fixed an issue with Utilities.formatDate , where it was previously always formatting the date into GMT.
`Utilities.formatDate`
Line numbers in error messages are now denoted with (line nnn), rather than (# nnn), where nnn is the line number.
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-04-20 UTC.

---

### Asistencia

- Página principal
- Google Workspace
- Apps Script
- Asistencia
# Cómo obtener ayuda Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Usamos una combinación de plataformas diferentes para brindar asistencia a los desarrolladores. Revisa las siguientes opciones para determinar la mejor forma de obtener ayuda.
## Preguntas y consejos
### Foros de la comunidad (oficiales)
Únete a la conversación sobre el desarrollo de Google Workspace en el foro de la comunidad de desarrolladores de Google Workspace .
### Reddit (no oficial)
También puedes encontrar ayuda en los subreddits administrados por la comunidad:
- r/GoogleAppsScript
- r/googleworkspacedevs
### Stack Overflow
También usamos el conocido sitio web de preguntas y respuestas sobre programación Stack Overflow para responder preguntas técnicas. Google no es propietario ni administra este sitio, pero puedes acceder con tu Cuenta de Google.
Stack Overflow contiene preguntas sobre varios temas, y los desarrolladores usan la etiqueta [google-apps-script] para marcar las preguntas relevantes para este servicio. Conviene agregar otras etiquetas a tu pregunta para captar la atención de expertos en tecnologías relacionadas.
`[google-apps-script]`
Buscar preguntas existentes Hacer una pregunta nueva
## Comentarios sobre productos para desarrolladores
Si tienes comentarios sobre las funciones o la funcionalidad de los productos para desarrolladores, busca en nuestro Issue Tracker para ver si otras personas ya enviaron los mismos comentarios. Si encuentras un informe de comentarios existente, haz clic en la estrella que se encuentra junto al número de problema para expresar tu acuerdo y ayudarnos a priorizar los informes más importantes. Si tienes contexto o información adicional para aportar, puedes agregar un comentario.
Si nadie más envió comentarios similares, puedes enviar un informe de comentarios nuevo. Describe tus comentarios de la manera más específica posible, incluido el motivo por el que crees que es importante.
Buscar comentarios existentes Enviar un error Enviar una solicitud de función
## Ponte en contacto con el equipo de asistencia de Google Workspace
Los administradores de Google Workspace pueden enviar un correo electrónico a un especialista del equipo de asistencia para desarrolladores de Google Workspace .
Asegúrate de incluir la siguiente información cuando te comuniques con nosotros:
- Una descripción del problema y el comportamiento que esperabas
- Una lista de pasos y un fragmento pequeño del código de muestra que se puede usar para reproducir el problema
- Una descripción del resultado que esperabas y lo que realmente ocurrió (incluí los mensajes de error que recibiste)
- Información sobre tu entorno de desarrollo, incluido el lenguaje de programación y las versiones de bibliotecas, entre otros datos.
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### API de REST

- Página principal
- Google Workspace
- Apps Script
- Guías
# Introducción Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
La API de Google Apps Script te permite automatizar la creación, la administración y la ejecución de secuencias de comandos en Google Apps Script. Puedes crear, modificar e implementar proyectos de Google Apps Script de forma programática, y ejecutar funciones de Apps Script de forma remota, acciones que, de lo contrario, requieren el uso del editor de Apps Script o su IU.
Esta API se suele usar para lo siguiente:
- Crear y administrar proyectos y las implementaciones de Apps Script
- Agregar o actualizar funciones en proyectos de secuencias de comandos
- Ejecutar funciones de Apps Script desde otras aplicaciones
- Supervisar los registros de ejecución y los estados de las secuencias de comandos
La API de Apps Script también reemplaza y extiende la API de ejecución de Apps Script. Puedes usar la API de Apps Script para ejecutar funciones de Apps Script de forma remota, tal como lo hacías con la API de Execution.
Para usar esta API en tus apps, debes habilitarla .
Para permitir que otras apps administren tus secuencias de comandos, debes otorgarles acceso .
## Descripción general de la API
La API de Apps Script se divide en varios recursos, cada uno con un propósito específico y un conjunto de solicitudes que puedes realizar. Estos recursos son los siguientes:
- projects : Es una representación de un proyecto de secuencia de comandos. La API proporciona métodos para crear, leer, supervisar y modificar proyectos. Usa este recurso para administrar los archivos de secuencia de comandos y los metadatos de tu proyecto.
`projects`
- projects.deployments : Es una representación de una implementación de secuencia de comandos. La API proporciona métodos para crear, enumerar, actualizar y borrar implementaciones de proyectos de secuencias de comandos. Usa las implementaciones para que tu secuencia de comandos esté disponible como una app web, un complemento o un archivo ejecutable.
`projects.deployments`
- projects.versions : Es una representación de una versión de proyecto de secuencia de comandos. La API proporciona métodos para crear y leer versiones de proyectos. Usa las versiones para hacer un seguimiento de las diferentes iteraciones de tu proyecto de secuencia de comandos.
`projects.versions`
- processes : Es una representación de la ejecución de una función de secuencia de comandos. La API proporciona métodos para enumerar los procesos existentes y recopilar información sobre ellos, como el tipo y el estado actual. Usa este recurso para supervisar las ejecuciones de secuencias de comandos que se inician con el método scripts.run .
`processes`
`scripts.run`
- scripts : Es el extremo que proporciona métodos para ejecutar de forma remota funciones de Apps Script. Usa este recurso para ejecutar funciones en tu proyecto de secuencia de comandos desde tu aplicación.
`scripts`
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

## Descripción general de Google Apps Script

### Apps Script

- Página principal
- Google Workspace
- Apps Script
### Automatiza y extiende Google Workspace con código sencillo.
Apps Script es una plataforma de JavaScript basada en la nube y potenciada por Google Drive que te permite integrar y automatizar tareas en los productos de Google.
## Desarrolla soluciones de alta calidad con facilidad
### Automatizaciones
Escriba un código que realice tareas de manera programática en todos los productos de Google. Las automatizaciones se activan mediante menús personalizados, botones, acciones del usuario o una programación basada en el tiempo.
### Funciones personalizadas
Escribe funciones de Hojas de cálculo de Google en Apps Script y llámalas desde tu hoja de cálculo como funciones integradas.
### Complementos
Compila una app que automatice tareas o se conecte a servicios de terceros desde Google Workspace. Comparta su solución con otras personas en Google Workspace Marketplace.
### Apps de chat
Proporciona una interfaz de conversación que permita a los usuarios de Google Chat interactuar con los servicios como si el servicio fuera una persona.
### Potencia tus secuencias de comandos con IA
### Guía de inicio rápido de Vertex AI
### Guía de inicio rápido del agente de ADK
### Guía de inicio rápido del agente A2A
### Analizador de mensajes de Gmail
### Agente de Viajes Concierge
### Función personalizada de verificador de datos
### Guía de inicio rápido del agente de ADK
### Guía de inicio rápido del agente A2A
### Guía de inicio rápido del agente de A2UI
### Servicio de Vertex AI
### Inicio rápido del agente de Gemini Enterprise
### Agentes de Gemini Enterprise
### Agentes de Vertex AI
### Crea un complemento de Gmail con vibe coding
### Notas de la versión
### Asistencia
### API de REST
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-03-03 (UTC)

---

### Guías

- Página principal
- Google Workspace
- Apps Script
- Guías
# Descripción general de Google Apps Script Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Apps Script es una plataforma de desarrollo de aplicaciones rápida que permite crear aplicaciones empresariales que se integran con Google Workspace con rapidez. Escribes código en JavaScript moderno y tienes acceso a bibliotecas integradas para aplicaciones de Google Workspace, como Gmail, Calendario de Google, Google Drive y muchas más. No debes instalar nada, ya que te proporcionamos un editor de código incorporado directamente en el navegador para que tu secuencia de comandos se guarde en Drive y se ejecute en los servidores de Google.
Si es la primera vez que usas JavaScript, Codecademy ofrece varios cursos de JavaScript . (Estos cursos no fueron desarrollados por Google ni están asociados con la empresa).
## ¿Qué puede hacer Apps Script?
Apps Script es versátil. Úsala para realizar las siguientes acciones:
- Agregar menús personalizados , y diálogos y barras laterales a Documentos de Google, Hojas de cálculo de Google y Formularios de Google
- Escribir funciones personalizadas y macros para Hojas de cálculo
- Publicar apps web independientes o incorporadas en Google Sites.
- Interactuar con otros servicios de Google , como Google AdSense, Google Analytics, Calendario, Drive, Gmail y Google Maps.
- Compilar complementos livianos add-ons y publicarlos en Google Workspace Marketplace. Si planeas compilar complementos a gran escala, consulta Cómo compilar un complemento de Google Workspace con extremos HTTP .
## Prueba una guía de inicio rápido
Prueba una de las siguientes guías de inicio rápido para ejecutar un proyecto de Apps Script en menos de 5 minutos.
- Guía de inicio rápido de automatización : Compila y ejecuta una automatización que cree un documento de Documentos y te envíe un vínculo a él por correo electrónico.
- Guía de inicio rápido de función personalizada : Crea una función personalizada que calcule el precio de venta de los artículos con descuento.
- Guía de inicio rápido de bot de Google Chat : Crea un bot de Chat al que se le puedan enviar mensajes directamente y que responda repitiendo tus mensajes.
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### menús personalizados

- Página principal
- Google Workspace
- Apps Script
- Guías
# Menús personalizados en Google Workspace Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Las secuencias de comandos pueden extender ciertos productos de Google agregando elementos de la interfaz de usuario que, cuando se hace clic en ellos, ejecutan una función de Google Apps Script. El ejemplo más común es ejecutar una secuencia de comandos desde un elemento de menú personalizado en Documentos, Hojas de cálculo, Presentaciones o Formularios de Google, pero las funciones de secuencias de comandos también se pueden activar haciendo clic en imágenes y dibujos en Hojas de cálculo.
## Menús personalizados en Documentos, Hojas de cálculo, Presentaciones o Formularios
Apps Script puede agregar menús nuevos en Documentos, Hojas de cálculo, Presentaciones o Formularios, con cada elemento de menú vinculado a una función en una secuencia de comandos. (En Formularios, los menús personalizados solo son visibles para un editor que abre el formulario para modificarlo, no para un usuario que lo abre para responder).
Solo las secuencias de comandos vinculadas pueden crear menús. Para mostrar el menú cuando el usuario abre un archivo, escribe el código del menú dentro de una onOpen función.
`onOpen`
En el siguiente ejemplo, se muestra cómo agregar un menú con un elemento, seguido de un separador visual y, luego, un submenú que contiene otro elemento. Cuando el usuario selecciona cualquiera de los elementos de menú, una función correspondiente abre un diálogo de alerta . Para obtener más información sobre los tipos de diálogos que puedes abrir, consulta la guía de diálogos y barras laterales .
```
function
 
onOpen
()
 
{


  
const
 
ui
 
=
 
SpreadsheetApp
.
getUi
();


  
// Or DocumentApp, SlidesApp or FormApp.


  
ui
.
createMenu
(
'Custom Menu'
)


      
.
addItem
(
'First item'
,
 
'menuItem1'
)


      
.
addSeparator
()


      
.
addSubMenu
(
ui
.
createMenu
(
'Sub-menu'
)


          
.
addItem
(
'Second item'
,
 
'menuItem2'
))


      
.
addToUi
();


}



function
 
menuItem1
()
 
{


  
SpreadsheetApp
.
getUi
()
 
// Or DocumentApp, SlidesApp or FormApp.


      
.
alert
(
'You clicked the first menu item!'
);


}



function
 
menuItem2
()
 
{


  
SpreadsheetApp
.
getUi
()
 
// Or DocumentApp, SlidesApp or FormApp.


      
.
alert
(
'You clicked the second menu item!'
);


}
```
Un documento, una hoja de cálculo, una presentación o un formulario solo pueden contener un menú con un nombre determinado. Si la misma secuencia de comandos o cualquier otra agrega un menú con el mismo nombre, el menú nuevo reemplaza al anterior. Los menús no se pueden quitar mientras el archivo está abierto, aunque puedes escribir tu onOpen función para omitir el menú en el futuro si se establece una propiedad determinada.
`onOpen`
Los complementos del editor también pueden tener elementos de menú, pero usan reglas especiales para definir cómo se definen.
## Imágenes y dibujos en los que se puede hacer clic en Hojas de cálculo
También puedes asignar una función de Apps Script a una imagen o un dibujo en Hojas de cálculo, siempre que la secuencia de comandos esté vinculada a la hoja de cálculo. En el siguiente ejemplo, se muestra cómo configurarlo.
- En Hojas de cálculo, selecciona el elemento de menú Extensiones > Apps Script para crear una secuencia de comandos vinculada a la hoja de cálculo.
- Borra cualquier código que haya en el editor de secuencias de comandos y pega el código que se encuentra a continuación.
```
function
 
showMessageBox
()
 
{


  
SpreadsheetApp
.
getUi
().
alert
(
'You clicked it!'
);


}
```
- Vuelve a Hojas de cálculo y selecciona Insertar > Imagen o Insertar > Dibujo para insertar una imagen o un dibujo.
- Después de insertar la imagen o el dibujo, haz clic en él. Aparecerá un pequeño selector de menú desplegable en la esquina superior derecha. Haz clic en él y elige Asignar secuencia de comandos .
- En el diálogo que aparece, escribe el nombre de la función de Apps Script que quieres ejecutar, sin paréntesis. En este caso, showMessageBox . Haz clic en Aceptar .
`showMessageBox`
- Vuelve a hacer clic en la imagen o el dibujo. Ahora se ejecuta la función.
La ejecución de la secuencia de comandos solo se activa cuando se hace clic en la imagen o el dibujo en un navegador web. La secuencia de comandos no se ejecuta si se hace clic en la imagen o el dibujo en un dispositivo móvil.
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### diálogos y barras laterales

- Página principal
- Google Workspace
- Apps Script
- Guías
# Diálogos y barras laterales en documentos de Google Workspace Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Los proyectos de Google Apps Script vinculados a Documentos, Hojas de cálculo o Formularios de Google pueden mostrar elementos de la interfaz de usuario, como alertas, mensajes, avisos, diálogos y barras laterales precompilados. Por lo general, estos elementos contienen contenido personalizado del servicio HTML y, a menudo, se abren desde elementos de menú . En Formularios, los elementos de la interfaz de usuario solo son visibles para un editor que abre el formulario para modificarlo, no para un encuestado.
## Diálogos de alerta
Una alerta es un diálogo precompilado que se abre dentro de un editor de Documentos, Hojas de cálculo, Presentaciones o Formularios. Muestra un mensaje y un botón Aceptar ; un título y botones alternativos son opcionales. Es similar a llamar a window.alert en JavaScript del cliente dentro de un navegador web.
`window.alert`
Las alertas suspenden la secuencia de comandos del servidor mientras el diálogo está abierto. La secuencia de comandos se reanuda después de que el usuario cierra el diálogo, pero JDBC no persisten durante la suspensión.
Como se muestra en el siguiente ejemplo, Documentos, Formularios, Presentaciones y Hojas de cálculo usan el método Ui.alert , que está disponible en tres variantes. Para anular el botón Aceptar predeterminado, pasa un valor del Ui.ButtonSet enum como el buttons argumento. Para evaluar en qué botón hizo clic el usuario, compara el valor que muestra para alert con el Ui.Button enum.
`Ui.alert`
`Ui.ButtonSet`
`buttons`
`alert`
`Ui.Button`
```
function
 
onOpen
()
 
{


  
SpreadsheetApp
.
getUi
()
 
// Or DocumentApp or SlidesApp or FormApp.


    
.
createMenu
(
"Custom Menu"
)


    
.
addItem
(
"Show alert"
,
 
"showAlert"
)


    
.
addToUi
();


}



function
 
showAlert
()
 
{


  
const
 
ui
 
=
 
SpreadsheetApp
.
getUi
();
 
// Same variations.



  
const
 
result
 
=
 
ui
.
alert
(


    
"Please confirm"
,


    
"Are you sure you want to continue?"
,


    
ui
.
ButtonSet
.
YES_NO
,


  
);



  
// Process the user's response.


  
if
 
(
result
 
===
 
ui
.
Button
.
YES
)
 
{


    
// User clicked "Yes".


    
ui
.
alert
(
"Confirmation received."
);


  
}
 
else
 
{


    
// User clicked "No" or X in the title bar.


    
ui
.
alert
(
"Permission denied."
);


  
}


}
```
## Diálogos de mensajes
Un mensaje es un diálogo precompilado que se abre dentro de un editor de Documentos, Hojas de cálculo, Presentaciones o Formularios. Muestra un mensaje, un campo de entrada de texto y un botón Aceptar ; un título y botones alternativos son opcionales. Es similar a llamar a window.prompt en JavaScript del cliente dentro de un navegador web.
`window.prompt`
Los mensajes suspenden la secuencia de comandos del servidor mientras el diálogo está abierto. La secuencia de comandos se reanuda después de que el usuario cierra el diálogo, pero JDBC no persisten durante la suspensión.
Como se muestra en el siguiente ejemplo, Documentos, Formularios, Presentaciones y Hojas de cálculo usan el método Ui.prompt , que está disponible en tres variantes. Para anular el botón Aceptar predeterminado, pasa un valor del enum Ui.ButtonSet como el buttons argumento. Para evaluar la respuesta del usuario, captura el valor que muestra prompt , luego llama a PromptResponse.getResponseText para recuperar la entrada del usuario y compara el valor que muestra PromptResponse.getSelectedButton con el enum Ui.Button .
`Ui.prompt`
`Ui.ButtonSet`
`buttons`
`prompt`
`PromptResponse.getResponseText`
`PromptResponse.getSelectedButton`
`Ui.Button`
```
function
 
onOpen
()
 
{


  
SpreadsheetApp
.
getUi
()
 
// Or DocumentApp or SlidesApp or FormApp.


    
.
createMenu
(
"Custom Menu"
)


    
.
addItem
(
"Show prompt"
,
 
"showPrompt"
)


    
.
addToUi
();


}



function
 
showPrompt
()
 
{


  
const
 
ui
 
=
 
SpreadsheetApp
.
getUi
();
 
// Same variations.



  
const
 
result
 
=
 
ui
.
prompt
(


    
"Let's get to know each other!"
,


    
"Please enter your name:"
,


    
ui
.
ButtonSet
.
OK_CANCEL
,


  
);



  
// Process the user's response.


  
const
 
button
 
=
 
result
.
getSelectedButton
();


  
const
 
text
 
=
 
result
.
getResponseText
();


  
if
 
(
button
 
===
 
ui
.
Button
.
OK
)
 
{


    
// User clicked "OK".


    
ui
.
alert
(
"Your name is "
 
+
 
text
 
+
 
"."
);


  
}
 
else
 
if
 
(
button
 
===
 
ui
.
Button
.
CANCEL
)
 
{


    
// User clicked "Cancel".


    
ui
.
alert
(
"I didn't get your name."
);


  
}
 
else
 
if
 
(
button
 
===
 
ui
.
Button
.
CLOSE
)
 
{


    
// User clicked X in the title bar.


    
ui
.
alert
(
"You closed the dialog."
);


  
}


}
```
## Avisos de hojas de cálculo
Un "aviso" es una pequeña ventana de diálogo en la esquina inferior derecha de un editor de Hojas de cálculo que muestra un mensaje, pero no suspende la secuencia de comandos. Es una buena manera de mostrar mensajes de estado o actualizaciones que no requieren la interacción del usuario.
Como se muestra en el siguiente ejemplo, Hojas de cálculo usa el método Spreadsheet.toast . Los avisos solo están disponibles en Hojas de cálculo.
`Spreadsheet.toast`
```
function
 
showToast
()
 
{


  
SpreadsheetApp
.
getActiveSpreadsheet
().
toast
(
"Task completed successfully."
);


}
```
## Diálogos personalizados
Un diálogo personalizado puede mostrar una interfaz de usuario del servicio HTML dentro de un editor de Documentos, Hojas de cálculo, Presentaciones o Formularios.
Los diálogos personalizados no suspenden la secuencia de comandos del servidor mientras el diálogo está abierto. Debido a que son asíncronos, la función del servidor que abre el diálogo finaliza de inmediato. Para pasar datos del diálogo personalizado al servidor, usa la google.script API en tu código del cliente.
`google.script`
El diálogo puede cerrarse llamando a google.script.host.close en el lado del cliente de una interfaz de servicio HTML. Otras interfaces no pueden cerrar el diálogo, solo el usuario o el diálogo mismo.
`google.script.host.close`
Como se muestra en el siguiente ejemplo, Documentos, Formularios, Presentaciones y Hojas de cálculo usan el método Ui.showModalDialog para abrir el diálogo.
`Ui.showModalDialog`
```
function
 
onOpen
()
 
{


  
SpreadsheetApp
.
getUi
()
 
//
 
Or
 
DocumentApp
 
or
 
SlidesApp
 
or
 
FormApp
.


      
.
createMenu
(
'Custom Menu'
)


      
.
addItem
(
'Show dialog'
,
 
'showDialog'
)


      
.
addToUi
();


}



function
 
showDialog
()
 
{


  
const
 
html
 
=
 
HtmlService
.
createHtmlOutputFromFile
(
'Page'
)


      
.
setWidth
(
400
)


      
.
setHeight
(
300
);


  
SpreadsheetApp
.
getUi
()
 
//
 
Or
 
DocumentApp
 
or
 
SlidesApp
 
or
 
FormApp
.


      
.
showModalDialog
(
html
,
 
'My custom dialog'
);


}
```
```
Hello, world! <input type="button" value="Close" onclick="google.script.host.close()" />
```
## Barras laterales personalizadas
Una barra lateral puede mostrar una interfaz de usuario del servicio HTML dentro de un editor de Documentos, Formularios, Presentaciones y Hojas de cálculo.
Las barras laterales no suspenden la secuencia de comandos del servidor mientras el diálogo está abierto. El componente del cliente puede realizar llamadas asíncronas a la secuencia de comandos del servidor con la google.script API para interfaces de servicio HTML.
`google.script`
La barra lateral puede cerrarse llamando a google.script.host.close en el lado del cliente de una interfaz de servicio HTML. Otras interfaces no pueden cerrar la barra lateral, solo el usuario o la barra lateral misma.
`google.script.host.close`
Como se muestra en el siguiente ejemplo, Documentos, Formularios, Presentaciones y Hojas de cálculo usan el método Ui.showSidebar para abrir la barra lateral.
`Ui.showSidebar`
```
function
 
onOpen
()
 
{


  
SpreadsheetApp
.
getUi
()
 
//
 
Or
 
DocumentApp
 
or
 
SlidesApp
 
or
 
FormApp
.


      
.
createMenu
(
'Custom Menu'
)


      
.
addItem
(
'Show sidebar'
,
 
'showSidebar'
)


      
.
addToUi
();


}



function
 
showSidebar
()
 
{


  
const
 
html
 
=
 
HtmlService
.
createHtmlOutputFromFile
(
'Page'
)


      
.
setTitle
(
'My custom sidebar'
);


  
SpreadsheetApp
.
getUi
()
 
//
 
Or
 
DocumentApp
 
or
 
SlidesApp
 
or
 
FormApp
.


      
.
showSidebar
(
html
);


}
```
```
Hello, world! <input type="button" value="Close" onclick="google.script.host.close()" />
```
## Diálogos de apertura de archivos
Google Picker es una API de JavaScript que permite a los usuarios seleccionar o subir archivos de Google Drive. Usa la biblioteca de Google Picker en el servicio HTML para crear un diálogo personalizado que permita a los usuarios seleccionar archivos existentes o subir archivos nuevos y, luego, pasar la selección a tu secuencia de comandos.
### Requisitos
El uso de Google Picker con Google Apps Script tiene varios requisitos:
- Configura tu entorno para Google Picker.
Configura tu entorno para Google Picker.
- Tu proyecto de secuencia de comandos debe usar un estándar proyecto de Google Cloud . Pasa el mismo número de proyecto de Cloud a PickerBuilder.setAppId si usas el alcance drive.file .
Tu proyecto de secuencia de comandos debe usar un estándar proyecto de Google Cloud .
Pasa el mismo número de proyecto de Cloud a PickerBuilder.setAppId si usas el alcance drive.file .
`PickerBuilder.setAppId`
`drive.file`
- El manifiesto del proyecto de Apps Script debe especificar los alcances de autorización que requiere la API de Google Picker para que ScriptApp.getOAuthToken muestre el token correcto para PickerBuilder.setOauthtoken .
El manifiesto del proyecto de Apps Script debe especificar los alcances de autorización que requiere la API de Google Picker para que ScriptApp.getOAuthToken muestre el token correcto para PickerBuilder.setOauthtoken .
`ScriptApp.getOAuthToken`
`PickerBuilder.setOauthtoken`
- Restringe la clave de API establecida en PickerBuilder.setDeveloperKey a Apps Script. En Restricciones de aplicaciones , sigue estos pasos: Selecciona URLs de referencia HTTP (sitios web) . En Restricciones de sitios web , haz clic en Agregar un elemento . Haz clic en Referente y, luego, ingresa *.google.com . Agrega otro elemento y, luego, ingresa *.googleusercontent.com como el referente. Haz clic en Listo .
Restringe la clave de API establecida en PickerBuilder.setDeveloperKey a Apps Script. En Restricciones de aplicaciones , sigue estos pasos:
`PickerBuilder.setDeveloperKey`
- Selecciona URLs de referencia HTTP (sitios web) .
- En Restricciones de sitios web , haz clic en Agregar un elemento .
- Haz clic en Referente y, luego, ingresa *.google.com .
`*.google.com`
- Agrega otro elemento y, luego, ingresa *.googleusercontent.com como el referente.
`*.googleusercontent.com`
- Haz clic en Listo .
- Llama a PickerBuilder.setOrigin .
Llama a PickerBuilder.setOrigin .
`PickerBuilder.setOrigin`
### Ejemplo
En el siguiente ejemplo, se muestra Google Picker en Apps Script.
```
/**


 * Creates a custom menu in Google Sheets when the spreadsheet opens.


 */


function
 
onOpen
()
 
{


  
SpreadsheetApp
.
getUi
()


    
.
createMenu
(
"Picker"
)


    
.
addItem
(
"Start"
,
 
"showPicker"
)


    
.
addToUi
();


}



/**


 * Displays an HTML-service dialog in Google Sheets that contains client-side


 * JavaScript code for the Google Picker API.


 */


function
 
showPicker
()
 
{


  
const
 
html
 
=
 
HtmlService
.
createHtmlOutputFromFile
(
"dialog.html"
)


    
.
setWidth
(
800
)


    
.
setHeight
(
600
)


    
.
setSandboxMode
(
HtmlService
.
SandboxMode
.
IFRAME
);


  
SpreadsheetApp
.
getUi
().
showModalDialog
(
html
,
 
"Select a file"
);


}


// Ensure the Drive API is enabled.


if
 
(
!
Drive
)
 
{


  
throw
 
new
 
Error
(
"Please enable the Drive advanced service."
);


}



/**


 * Checks that the file can be accessed.


 * @param {string} fileId The ID of the file.


 * @return {Object} The file resource.


 */


function
 
getFile
(
fileId
)
 
{


  
return
 
Drive
.
Files
.
get
(
fileId
,
 
{
 
fields
:
 
"*"
 
});


}



/**


 * Gets the user's OAuth 2.0 access token so that it can be passed to Picker.


 * This technique keeps Picker from needing to show its own authorization


 * dialog, but is only possible if the OAuth scope that Picker needs is


 * available in Apps Script. In this case, the function includes an unused call


 * to a DriveApp method to ensure that Apps Script requests access to all files


 * in the user's Drive.


 *


 * @return {string} The user's OAuth 2.0 access token.


 */


function
 
getOAuthToken
()
 
{


  
return
 
ScriptApp
.
getOAuthToken
();


}
```
```
<!DOCTYPE html>
<html>
  <head>
    <link
      rel="stylesheet"
      href="https://ssl.gstatic.com/docs/script/css/add-ons.css"
    />
    <style>
      #result {
        display: flex;
        flex-direction: column;
        gap: 0.25em;
      }

      pre {
        font-size: x-small;
        max-height: 25vh;
        overflow-y: scroll;
        background: #eeeeee;
        padding: 1em;
        border: 1px solid #cccccc;
      }
    </style>
    <script>
      // TODO: Replace the value for DEVELOPER_KEY with the API key obtained
      // from the Google Developers Console.
      const DEVELOPER_KEY = "AIza...";
      // TODO: Replace the value for CLOUD_PROJECT_NUMBER with the project
      // number obtained from the Google Developers Console.
      const CLOUD_PROJECT_NUMBER = "1234567890";

      let pickerApiLoaded = false;
      let oauthToken;

      /**
       * Loads the Google Picker API.
       */
      function onApiLoad() {
        gapi.load("picker", {
          callback: function () {
            pickerApiLoaded = true;
          },
        });
      }

      /**
       * Gets the user's OAuth 2.0 access token from the server-side script so that
       * it can be passed to Picker. This technique keeps Picker from needing to
       * show its own authorization dialog, but is only possible if the OAuth scope
       * that Picker needs is available in Apps Script. Otherwise, your Picker code
       * will need to declare its own OAuth scopes.
       */
      function getOAuthToken() {
        google.script.run
          .withSuccessHandler((token) => {
            oauthToken = token;
            createPicker(token);
          })
          .withFailureHandler(showError)
          .getOAuthToken();
      }

      /**
       * Creates a Picker that can access the user's spreadsheets. This function
       * uses advanced options to hide the Picker's left navigation panel and
       * default title bar.
       *
       * @param {string} token An OAuth 2.0 access token that lets Picker access the
       *     file type specified in the addView call.
       */
      function createPicker(token) {
        document.getElementById("result").innerHTML = "";

        if (pickerApiLoaded && token) {
          const picker = new google.picker.PickerBuilder()
            // Instruct Picker to display only spreadsheets in Drive. For other
            // views, see https://developers.google.com/picker/reference/picker.viewid
            .addView(
              new google.picker.DocsView(
                google.picker.ViewId.SPREADSHEETS
              ).setOwnedByMe(true)
            )
            // Hide the navigation panel so that Picker fills more of the dialog.
            .enableFeature(google.picker.Feature.NAV_HIDDEN)
            // Hide the title bar since an Apps Script dialog already has a title.
            .hideTitleBar()
            .setOAuthToken(token)
            .setDeveloperKey(DEVELOPER_KEY)
            .setAppId(CLOUD_PROJECT_NUMBER)
            .setCallback(pickerCallback)
            .setOrigin(google.script.host.origin)
            .build();
          picker.setVisible(true);
        } else {
          showError("Unable to load the file picker.");
        }
      }

      /**
       * @typedef {Object} PickerResponse
       * @property {string} action
       * @property {PickerDocument[]} docs
       */

      /**
       * @typedef {Object} PickerDocument
       * @property {string} id
       * @property {string} name
       * @property {string} mimeType
       * @property {string} url
       * @property {string} lastEditedUtc
       */

      /**
       * A callback function that extracts the chosen document's metadata from the
       * response object. For details on the response object, see
       * https://developers.google.com/picker/reference/picker.responseobject
       *
       * @param {PickerResponse} data The response object.
       */
      function pickerCallback(data) {
        const action = data[google.picker.Response.ACTION];
        if (action == google.picker.Action.PICKED) {
          handlePicked(data);
        } else if (action == google.picker.Action.CANCEL) {
          document.getElementById("result").innerHTML = "Picker canceled.";
        }
      }

      /**
       * Handles `"PICKED"` responsed from the Google Picker.
       *
       * @param {PickerResponse} data The response object.
       */
      function handlePicked(data) {
        const doc = data[google.picker.Response.DOCUMENTS][0];
        const id = doc[google.picker.Document.ID];

        google.script.run
          .withSuccessHandler((driveFilesGetResponse) => {
            // Render the response from Picker and the Drive.Files.Get API.
            const resultElement = document.getElementById("result");
            resultElement.innerHTML = "";

            for (const response of [
              {
                title: "Picker response",
                content: JSON.stringify(data, null, 2),
              },
              {
                title: "Drive.Files.Get response",
                content: JSON.stringify(driveFilesGetResponse, null, 2),
              },
            ]) {
              const titleElement = document.createElement("h3");
              titleElement.appendChild(document.createTextNode(response.title));
              resultElement.appendChild(titleElement);

              const contentElement = document.createElement("pre");
              contentElement.appendChild(
                document.createTextNode(response.content)
              );
              resultElement.appendChild(contentElement);
            }
          })
          .withFailureHandler(showError)
          .getFile(data[google.picker.Response.DOCUMENTS][0].id);
      }

      /**
       * Displays an error message within the #result element.
       *
       * @param {string} message The error message to display.
       */
      function showError(message) {
        document.getElementById("result").innerHTML = "Error: " + message;
      }
    </script>
  </head>

  <body>
    <div>
      <button onclick="getOAuthToken()">Select a file</button>
      <div id="result"></div>
    </div>
    <script src="https://apis.google.com/js/api.js?onload=onApiLoad"></script>
  </body>
</html>
```
```
{


  
"timeZone"
:
 
"America/Los_Angeles"
,


  
"exceptionLogging"
:
 
"STACKDRIVER"
,


  
"runtimeVersion"
:
 
"V8"
,


  
"oauthScopes"
:
 
[


    
"https://www.googleapis.com/auth/script.container.ui"
,


    
"https://www.googleapis.com/auth/drive.file"


  
],


  
"dependencies"
:
 
{


    
"enabledAdvancedServices"
:
 
[


      
{


        
"userSymbol"
:
 
"Drive"
,


        
"version"
:
 
"v3"
,


        
"serviceId"
:
 
"drive"


      
}


    
]


  
}


}
```
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### funciones personalizadas

- Página principal
- Google Workspace
- Apps Script
- Guías
# Funciones personalizadas en Hojas de cálculo de Google Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Hojas de cálculo de Google ofrece cientos de funciones integradas , como AVERAGE , SUM y VLOOKUP . Cuando estas no son suficientes para tus necesidades, puedes usar Apps Script para escribir funciones personalizadas y, luego, usarlas en Hojas de cálculo como si fueran funciones integradas.
`AVERAGE`
`SUM`
`VLOOKUP`
Para ver ejemplos de funciones personalizadas, consulta los siguientes instructivos:
- Cómo calcular el precio de venta de los artículos con descuento (guía de inicio rápido)
- Cómo calcular un descuento de precios por niveles
- Cómo calcular la distancia en automóvil y convertir metros a millas
- Resume datos de varias hojas
- Verifica la veracidad de las afirmaciones con un agente de IA del ADK y un modelo de Gemini
## Cómo comenzar
Las funciones personalizadas se crean con JavaScript estándar. Si es la primera vez que usas JavaScript, Codecademy ofrece un curso para principiantes . Este curso no fue desarrollado por Google ni está asociado a la empresa.
Esta es una función personalizada, llamada DOUBLE , que multiplica un valor de entrada por 2:
`DOUBLE`
```
/**


 * Multiplies an input value by 2.


 * @param {number} input The number to double.


 * @return The input multiplied by 2.


 * @customfunction


*/


function
 
DOUBLE
(
input
)
 
{


  
return
 
input
 
*
 
2
;


}
```
Si no sabes cómo escribir código JavaScript y no tienes tiempo para aprender, consulta la tienda de complementos de Google Workspace para ver si alguien más ya creó la función personalizada que necesitas.
### Cómo crear una función personalizada
Para escribir una función personalizada, sigue estos pasos:
- Crea o abre una hoja de cálculo en Hojas de cálculo.
- Selecciona el elemento de menú Extensiones > Apps Script .
- Borra cualquier código que aparezca en el editor de secuencias de comandos. Para la función DOUBLE que se mostró anteriormente, copia y pega el código en el editor de secuencias de comandos.
`DOUBLE`
- En la parte superior, haz clic en Guardar save .
Ahora puedes usar la función personalizada .
### Obtén una función personalizada de Google Workspace Marketplace
Google Workspace Marketplace ofrece varias funciones personalizadas como complementos de Google Workspace para Hojas de cálculo . Para usar o explorar estos complementos, haz lo siguiente:
- Crea o abre una hoja de cálculo en Hojas de cálculo.
- En la parte superior, haz clic en Complementos > Obtener complementos .
- Una vez que se abra Google Workspace Marketplace , haz clic en el cuadro de búsqueda de la esquina superior derecha.
- Escribe "función personalizada" y presiona Intro.
- Si encuentras un complemento de funciones personalizadas que te interese, haz clic en Instalar para instalarlo.
- Es posible que aparezca un diálogo que te indique que el complemento requiere autorización. Si es así, lee atentamente el aviso y, luego, haz clic en Permitir .
- El complemento estará disponible en la hoja de cálculo. Para usar el complemento en otra hoja de cálculo, ábrela y, en la parte superior, haz clic en Complementos > Administrar complementos . Busca el complemento que quieras usar y haz clic en Opciones more_vert > Usar en este documento .
### Usa una función personalizada
Una vez que escribas una función personalizada o instales una desde Google Workspace Marketplace, se usará como una función integrada:
- Haz clic en la celda en la que quieres usar la función.
- Escribe un signo igual ( = ) seguido del nombre de la función y cualquier valor de entrada (por ejemplo, =DOUBLE(A1) ) y presiona Intro.
`=`
`=DOUBLE(A1)`
- La celda muestra Loading... por un momento y, luego, devuelve el resultado.
`Loading...`
## Lineamientos para funciones personalizadas
Antes de escribir tu propia función personalizada, debes conocer algunos lineamientos.
### Nombres de funciones
Además de las convenciones estándar para nombrar funciones de JavaScript, ten en cuenta lo siguiente:
- El nombre de una función personalizada debe ser diferente de los nombres de las funciones integradas , como SUM() .
`SUM()`
- El nombre de una función personalizada no puede terminar con un guion bajo ( _ ), que denota una función privada en Apps Script.
`_`
- El nombre de una función personalizada se debe declarar con la sintaxis function myFunction() , no var myFunction = new Function() .
`function myFunction()`
`var myFunction = new Function()`
- El uso de mayúsculas no importa, aunque los nombres de las funciones de la hoja de cálculo suelen estar en mayúsculas.
### Argumentos
Al igual que una función integrada, una función personalizada puede tomar argumentos como valores de entrada:
- Si llamas a tu función con una referencia a una sola celda como argumento (como =DOUBLE(A1) ), el argumento es el valor de la celda.
`=DOUBLE(A1)`
- Si llamas a tu función con una referencia a un rango de celdas como argumento (como =DOUBLE(A1:B10) ), el argumento es un array bidimensional de los valores de las celdas. Por ejemplo, en la siguiente captura de pantalla, Apps Script interpreta los argumentos en =DOUBLE(A1:B2) como double([[1,3],[2,4]]) . Ten en cuenta que el código de muestra para DOUBLE descrito anteriormente debería modificarse para aceptar un array como entrada .
Si llamas a tu función con una referencia a un rango de celdas como argumento (como =DOUBLE(A1:B10) ), el argumento es un array bidimensional de los valores de las celdas. Por ejemplo, en la siguiente captura de pantalla, Apps Script interpreta los argumentos en =DOUBLE(A1:B2) como double([[1,3],[2,4]]) . Ten en cuenta que el código de muestra para DOUBLE descrito anteriormente debería modificarse para aceptar un array como entrada .
`=DOUBLE(A1:B10)`
`=DOUBLE(A1:B2)`
`double([[1,3],[2,4]])`
`DOUBLE`
- Los argumentos de las funciones personalizadas deben ser determinísticos . Es decir, las funciones integradas de la hoja de cálculo que devuelven un resultado diferente cada vez que se calculan, como NOW() o RAND() , no se permiten como argumentos para una función personalizada. Si una función personalizada intenta devolver un valor basado en una de estas funciones integradas volátiles, se mostrará Loading... de forma indefinida.
Los argumentos de las funciones personalizadas deben ser determinísticos . Es decir, las funciones integradas de la hoja de cálculo que devuelven un resultado diferente cada vez que se calculan, como NOW() o RAND() , no se permiten como argumentos para una función personalizada. Si una función personalizada intenta devolver un valor basado en una de estas funciones integradas volátiles, se mostrará Loading... de forma indefinida.
`NOW()`
`RAND()`
`Loading...`
- Para activar el recálculo, debes pasar una celda o un rango de celdas referenciados directamente como argumento a la función personalizada. De lo contrario, la función personalizada no se vuelve a calcular hasta que edites la función o cambies el valor de una celda a la que se hace referencia. Si usas el método getValue en funciones personalizadas, ten en cuenta que el rango al que se hace referencia no se pasa directamente como argumento a la función personalizada.
Para activar el recálculo, debes pasar una celda o un rango de celdas referenciados directamente como argumento a la función personalizada. De lo contrario, la función personalizada no se vuelve a calcular hasta que edites la función o cambies el valor de una celda a la que se hace referencia. Si usas el método getValue en funciones personalizadas, ten en cuenta que el rango al que se hace referencia no se pasa directamente como argumento a la función personalizada.
`getValue`
### Valores de retorno
Cada función personalizada debe devolver un valor para mostrar, de modo que se cumpla lo siguiente:
- Si una función personalizada devuelve un valor, este se muestra en la celda desde la que se llamó a la función.
- Si una función personalizada devuelve un array bidimensional de valores, estos se desbordan en las celdas adyacentes, siempre y cuando estén vacías. Si esto provocara que el array sobrescriba el contenido existente de las celdas, la función personalizada arrojará un error. Para ver un ejemplo, consulta la sección sobre cómo optimizar funciones personalizadas .
- Una función personalizada no puede afectar a las celdas que no sean aquellas en las que devuelve un valor. En otras palabras, una función personalizada no puede editar celdas arbitrarias, solo las celdas desde las que se llama y sus celdas adyacentes. Para editar celdas arbitrarias, usa un menú personalizado para ejecutar una función.
- Una llamada a función personalizada debe devolver un resultado en un plazo de 30 segundos. De lo contrario, la celda mostrará #ERROR! y la nota de la celda será Exceeded maximum execution time (line 0). .
`#ERROR!`
`Exceeded maximum execution time
(line 0).`
### Tipos de datos
Hojas de cálculo almacena los datos en diferentes formatos según la naturaleza de los datos. Cuando estos valores se usan en funciones personalizadas, Apps Script los trata como el tipo de datos adecuado en JavaScript . Estas son las áreas de confusión más comunes:
- Las horas y las fechas en Hojas de cálculo se convierten en objetos Date en Apps Script. Si la hoja de cálculo y la secuencia de comandos usan zonas horarias diferentes (un problema poco común), la función personalizada debe compensar la diferencia.
- Los valores de duración en Hojas de cálculo también se convierten en objetos Date , pero trabajar con ellos puede ser complicado .
`Date`
- Los valores de porcentaje en Hojas de cálculo se convierten en números decimales en Apps Script. Por ejemplo, una celda con el valor 10% se convierte en 0.1 en Apps Script.
`10%`
`0.1`
### Autocompletar
Hojas de cálculo admite el autocompletado para las funciones personalizadas, al igual que para las funciones integradas . A medida que escribes el nombre de una función en una celda, verás una lista de funciones integradas y personalizadas que coinciden con lo que ingresas.
Las funciones personalizadas aparecen en esta lista si su secuencia de comandos incluye una etiqueta JSDoc @customfunction , como en el ejemplo de DOUBLE() .
`@customfunction`
`DOUBLE()`
```
/**


 * Multiplies the input value by 2.


 *


 * @param {number} input The value to multiply.


 * @return {number} The input multiplied by 2.


 * @customfunction


 */


function
 
DOUBLE
(
input
)
 
{


  
return
 
input
 
*
 
2
;


}
```
## Avanzado
En esta sección, se abordan temas avanzados sobre las funciones personalizadas.
### Usa los servicios de Google Apps Script
Las funciones personalizadas pueden llamar a ciertos servicios de Apps Script para realizar tareas más complejas. Por ejemplo, una función personalizada puede llamar al servicio Language para traducir una frase en inglés al español.
A diferencia de la mayoría de los otros tipos de Apps Scripts, las funciones personalizadas nunca les solicitan a los usuarios que autoricen el acceso a datos personales. Por lo tanto, solo pueden llamar a servicios que no tienen acceso a datos personales, específicamente a los siguientes:
`getUserProperties()`
`get*()`
`set*()`
`SpreadsheetApp.openById()`
`SpreadsheetApp.openByUrl()`
Si tu función personalizada arroja el mensaje de error You do not have permission to call X service. , el servicio requiere autorización del usuario y, por lo tanto, no se puede usar en una función personalizada.
`You do not have permission to
call X service.`
Para usar un servicio que no se encuentre en la lista anterior, crea un menú personalizado que ejecute una función de Apps Script en lugar de escribir una función personalizada. Una función que se activa desde un menú le pide autorización al usuario si es necesario y, en consecuencia, puede usar todos los servicios de Apps Script.
### Comparte funciones personalizadas
Las funciones personalizadas comienzan vinculadas a la hoja de cálculo en la que se crearon. Esto significa que una función personalizada escrita en una hoja de cálculo no se puede usar en otras hojas de cálculo, a menos que uses uno de los siguientes métodos:
- Haz clic en Extensiones > Apps Script para abrir el editor de secuencias de comandos. Luego, copia el texto de la secuencia de comandos de la hoja de cálculo original y pégalo en el editor de secuencias de comandos de otra hoja de cálculo.
- Haz clic en Archivo > Crear una copia para crear una copia de la hoja de cálculo que contiene la función personalizada. Cuando se copia una hoja de cálculo, también se copian las secuencias de comandos adjuntas. Cualquier persona que tenga acceso a la hoja de cálculo puede copiar la secuencia de comandos. (Los colaboradores que solo tienen acceso de lectura no pueden abrir el editor de secuencias de comandos en la hoja de cálculo original. Sin embargo, cuando hacen una copia, se convierten en propietarios de ella y pueden ver la secuencia de comandos.
- Publica la secuencia de comandos como un complemento de editor de Hojas de cálculo.
Todas las secuencias de comandos vinculadas a contenedores comparten las mismas listas de acceso que sus contenedores. Esto significa que cualquier persona con permiso para editar la hoja de cálculo también puede editar cualquier código de Apps Script adjunto a ella. Para obtener más información, consulta acceso a secuencias de comandos vinculadas .
### Optimización
Cada vez que se usa una función personalizada en una hoja de cálculo, Hojas de cálculo realiza una llamada independiente al servidor de Apps Script. Si tu hoja de cálculo contiene docenas (o cientos, o miles) de llamadas a funciones personalizadas, este proceso puede ser lento. Es posible que algunos proyectos con muchas funciones personalizadas o funciones personalizadas complejas experimenten una demora temporal en las ejecuciones.
Por lo tanto, si planeas usar una función personalizada varias veces en un rango grande de datos, considera modificar la función para que acepte un rango como entrada en forma de un array bidimensional y, luego, devuelva un array bidimensional que pueda desbordarse en las celdas correspondientes.
Por ejemplo, la función DOUBLE() que se mostró anteriormente se puede volver a escribir para que acepte una sola celda o un rango de celdas de la siguiente manera:
`DOUBLE()`
```
/**


 * Multiplies the input value by 2.


 *


 * @param {number|Array<Array<number>>} input The value or range of cells


 *     to multiply.


 * @return The input multiplied by 2.


 * @customfunction


 */


function
 
DOUBLE
(
input
)
 
{


  
return
 
Array
.
isArray
(
input
)
 
?


      
input
.
map
(
row
 
=
>
 
row
.
map
(
cell
 
=
>
 
cell
 
*
 
2
))
 
:


      
input
 
*
 
2
;


}
```
Este enfoque usa el método map del objeto Array de JavaScript en el array bidimensional de celdas para obtener cada fila y, luego, para cada fila, vuelve a usar map para devolver el doble del valor de cada celda. Devuelve un array bidimensional que contiene los resultados. De esta manera, puedes llamar a DOUBLE solo una vez, pero hacer que calcule una gran cantidad de celdas a la vez, como se muestra en la siguiente captura de pantalla. Podrías lograr lo mismo con instrucciones if anidadas en lugar de la llamada a map .
`Array`
`map`
`DOUBLE`
`if`
`map`
Del mismo modo, la siguiente función personalizada recupera de manera eficiente contenido en vivo de Internet y usa un array bidimensional para mostrar dos columnas de resultados con una sola llamada a función. Si cada celda requiriera su propia llamada a función, la operación tardaría mucho más, ya que el servidor de Apps Script tendría que descargar y analizar el feed XML cada vez.
```
/**


 * Show the title and date for the first page of posts on the


 * Developer blog.


 *


 * @return Two columns of data representing posts on the


 *     Developer blog.


 * @customfunction


 */


function
 
getBlogPosts
()
 
{


  
var
 
array
 
=
 
[];


  
var
 
url
 
=
 
'https://gsuite-developers.googleblog.com/atom.xml'
;


  
var
 
xml
 
=
 
UrlFetchApp
.
fetch
(
url
).
getContentText
();


  
var
 
document
 
=
 
XmlService
.
parse
(
xml
);


  
var
 
root
 
=
 
document
.
getRootElement
();


  
var
 
atom
 
=
 
XmlService
.
getNamespace
(
'http://www.w3.org/2005/Atom'
);


  
var
 
entries
 
=
 
document
.
getRootElement
().
getChildren
(
'entry'
,
 
atom
);


  
for
 
(
var
 
i
 
=
 
0
;
 
i
 < 
entries
.
length
;
 
i
++
)
 
{


    
var
 
title
 
=
 
entries
[
i
].
getChild
(
'title'
,
 
atom
).
getText
();


    
var
 
date
 
=
 
entries
[
i
].
getChild
(
'published'
,
 
atom
).
getValue
();


    
array
.
push
([
title
,
 
date
]);


  
}


  
return
 
array
;


}
```
Estas técnicas se pueden aplicar a casi cualquier función personalizada que se use repetidamente en una hoja de cálculo, aunque los detalles de implementación varían según el comportamiento de la función.
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-26 (UTC)

---

### macros

- Página principal
- Google Workspace
- Apps Script
- Guías
# Macros de Hojas de cálculo de Google Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Hojas de cálculo de Google te permite grabar macros que duplican una serie específica de interacciones de la IU que definas. Una vez que hayas grabado una macro, puedes vincularla a una combinación de teclas en el formulario Ctrl+Alt+Shift+Number . Usa ese atajo para ejecutar rápidamente los pasos exactos de la macro de nuevo, por lo general, en otro lugar o con datos diferentes. También puedes activar la macro desde el menú Extensiones > Macros de Hojas de cálculo.
`Ctrl+Alt+Shift+Number`
Cuando grabas una macro, Hojas de cálculo crea automáticamente una función de Apps Script (la función de macro ) que replica los pasos de la macro. La función de macro se agrega a un proyecto de Apps Script vinculado a la hoja, en un archivo titulado macros.gs . En el caso de que ya haya un archivo de proyecto vinculado a la hoja con ese nombre, se le agrega la función de macro. Hojas de cálculo también actualiza automáticamente el manifiesto del proyecto de secuencia de comandos, y registra el nombre y el atajo de teclado asignados a la macro.
`macros.gs`
Dado que cada macro grabada se define por completo en Apps Script, puedes editarlas directamente en el editor de Apps Script. Incluso puedes escribir macros desde cero en Apps Script o tomar funciones que ya escribiste y convertirlas en macros.
## Crea macros en Apps Script
Puedes tomar funciones escritas en Apps Script y usarlas como funciones de macro. Una forma directa de hacerlo es importar una función existente desde el editor de Hojas de cálculo.
Como alternativa, puedes crear macros en el editor de Apps Script siguiendo estos pasos:
- En la IU de Hojas de cálculo, selecciona Extensiones > Apps Script para abrir la secuencia de comandos vinculada a la hoja en el editor de Apps Script.
- Escribe la función de macro. Las funciones de macro no deben tomar argumentos ni mostrar valores.
- Edita el manifiesto de la secuencia de comandos para crear la macro y vincularla a la función de macro. Asigna un atajo de teclado y un nombre únicos.
- Guarda el proyecto de secuencia de comandos. Luego, la macro estará disponible para usarse en la hoja.
- Prueba la función de macro en la hoja para verificar que funcione según lo previsto.
## Cómo editar macros
Para editar las macros adjuntas a una hoja, haz lo siguiente:
- En la IU de Hojas de cálculo, selecciona Extensiones > Macros > Administrar macros .
- Busca la macro que quieras editar y selecciona more_vert > Editar macro . Se abrirá el editor de Apps Script en el archivo del proyecto que contiene la función de macro.
- Edita la función de la macro para cambiar su comportamiento.
- Guarda el proyecto de secuencia de comandos. Luego, la macro estará disponible para usarse en la hoja.
- Prueba la función de macro en la hoja para verificar que funcione según lo previsto.
## Cómo importar funciones como macros
Si ya hay una secuencia de comandos vinculada a una hoja, puedes importar una función en la secuencia de comandos como una macro nueva y, luego, asignarle un atajo de teclado. Para ello, edita el archivo de manifiesto y agrega otro elemento a la propiedad sheets.macros[] .
`sheets.macros[]`
Como alternativa, sigue estos pasos para importar una función como una macro desde la IU de Hojas de cálculo:
- En la IU de Hojas de cálculo, selecciona Extensiones > Macros > Importar .
- Selecciona una función de la lista que se presenta y, luego, haz clic en Agregar función .
- Selecciona clear para cerrar el diálogo.
- Selecciona Extensiones > Macros > Administrar macros .
- Ubica la función que acabas de importar en la lista. Asigna un atajo de teclado único a la macro. También puedes cambiar el nombre de la macro aquí. De forma predeterminada, el nombre es el de la función.
- Haz clic en Actualizar para guardar la configuración de la macro.
## Estructura del manifiesto para macros
En el siguiente fragmento de ejemplo de un archivo de manifiesto, se muestra la sección de un manifiesto que define las macros de Hojas de cálculo. La sección sheets del manifiesto define el nombre y la combinación de teclas asignados a la macro, y el nombre de la función de la macro.
`sheets`
Los manifiestos incluyen otros componentes relacionados con las propiedades de Apps Script. Los campos de la clave sheets se relacionan directamente con la funcionalidad de Hojas de cálculo. Este ejemplo es solo una parte de un archivo de manifiesto completo y no es un manifiesto completamente funcional.
`sheets`
```
{


  
...


  
"sheets"
:
 
{


    
"macros"
:
 
[{


      
"menuName"
:
 
"QuickRowSum"
,


      
"functionName"
:
 
"calculateRowSum"
,


      
"defaultShortcut"
:
 
"Ctrl+Alt+Shift+1"


    
},
 
{


      
"menuName"
:
 
"Headerfy"
,


      
"functionName"
:
 
"updateToHeaderStyle"
,


      
"defaultShortcut"
:
 
"Ctrl+Alt+Shift+2"


    
}]


  
}


}
```
Consulta el recurso de manifiesto de la macro de Hojas de cálculo para obtener más detalles sobre cómo se construyen los manifiestos de las macros de Hojas de cálculo.
## Prácticas recomendadas
Cuando crees o administres macros en Apps Script, sigue estos lineamientos:
- Las macros tienen mejor rendimiento cuando son ligeras. Cuando sea posible, limita la cantidad de acciones que realiza una macro.
- Las macros son más adecuadas para operaciones rutinarias que deben repetirse con frecuencia con poca o ninguna configuración. Para otras operaciones, considera usar un elemento de menú personalizado .
- Recuerda siempre que las combinaciones de teclas de las macros deben ser únicas y que una hoja determinada solo puede tener diez macros con combinaciones de teclas en un momento dado. Las macros adicionales solo se pueden ejecutar desde el menú Extensiones > Macros .
- Las macros que realizan cambios en una sola celda se pueden aplicar a un rango de celdas. Para ello, primero selecciona el rango completo y, luego, activa la macro. Esto significa que, a menudo, no es necesario crear macros que dupliquen la misma operación en un rango de celdas predefinido.
## Qué no puedes hacer
Existen algunas restricciones sobre lo que puedes hacer con las macros:
#### Usa macros fuera de las secuencias de comandos vinculadas
Las macros se definen en secuencias de comandos vinculadas a Hojas de cálculo específicas. Las definiciones de macros se ignoran si se definen en una secuencia de comandos independiente o una app web .
#### Cómo definir macros en complementos de Hojas de cálculo de Google Workspace
No puedes distribuir definiciones de macros con un complemento de Hojas de cálculo de Google Workspace . Los usuarios del complemento ignoran las definiciones de macros en un proyecto de complemento de Hojas de cálculo.
#### Cómo distribuir macros en bibliotecas de secuencias de comandos
No puedes distribuir definiciones de macros con bibliotecas de Apps Script.
#### Cómo usar macros fuera de Hojas de cálculo
Las macros son solo una función de Hojas de cálculo y no existen en Documentos, Formularios ni Presentaciones de Google.
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### apps web

- Página principal
- Google Workspace
- Apps Script
- Guías
# Apps web Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Publica la secuencia de comandos como una app web si compilas una interfaz de usuario para ella. Por ejemplo, un script que permite a los usuarios programar citas con miembros de un equipo de asistencia es mejor presentarlo como una app web para que los usuarios accedan a él directamente desde sus navegadores.
Tanto los scripts independientes como los scripts vinculados a aplicaciones de Google Workspace se pueden convertir en apps web, siempre y cuando cumplan con los siguientes requisitos.
## Requisitos para las apps web
Un lenguaje de secuencias de comandos se puede publicar como una app web si cumple con los siguientes requisitos:
- Contiene una función doGet o doPost .
`doGet`
`doPost`
- La función devuelve un objeto HtmlOutput de servicio HTML o un objeto TextOutput de servicio de contenido .
`HtmlOutput`
`TextOutput`
## Parámetros de solicitud
Cuando un usuario visita una app o un programa le envía a la app una solicitud HTTP GET , Google Apps Script ejecuta la función doGet . Cuando un programa envía a la app una solicitud HTTP POST , Apps Script ejecuta doPost en su lugar. En ambos casos, el argumento e representa un parámetro de evento que puede contener información sobre cualquier parámetro de solicitud. La estructura del objeto de evento se muestra en la siguiente tabla:
`GET`
`doGet`
`POST`
`doPost`
`e`
`e.queryString`
El valor de la parte de la cadena de consulta de la URL o null si no se especifica ninguna cadena de consulta
`null`
```
name=alice&n=1&n=2
```
`e.parameter`
Objeto de pares clave-valor que corresponden a los parámetros de la solicitud. Solo se devuelve el primer valor para los parámetros que tienen varios valores.
```
{"name": "alice", "n": "1"}
```
`e.parameters`
Es un objeto similar a e.parameter , pero con un array de valores para cada clave.
`e.parameter`
```
{"name": ["alice"], "n": ["1", "2"]}
```
`e.pathInfo`
Es la ruta de URL después de /exec o /dev . Por ejemplo, si la ruta de URL termina en /exec/hello , la información de la ruta es hello .
`/exec`
`/dev`
`/exec/hello`
`hello`
`e.contextPath`
`e.contentLength`
Longitud del cuerpo de la solicitud para las solicitudes POST o -1 para las solicitudes GET
`-1`
```
332
```
`e.postData.length`
Es igual a e.contentLength
`e.contentLength`
```
332
```
`e.postData.type`
Tipo de MIME del cuerpo de la solicitud POST
```
text/csv
```
`e.postData.contents`
El texto del contenido del cuerpo de la solicitud POST
```
Alice,21
```
`e.postData.name`
Siempre es el valor "postData".
```
postData
```
Pasa parámetros como username y age a una URL como la siguiente:
`username`
`age`
```
https://script.google.com/.../exec?username=jsmith&age=21
```
Muestra los parámetros de la siguiente manera:
```
function
 
doGet
(
e
)
 
{


  
var
 
params
 
=
 
JSON
.
stringify
(
e
);


  
return
 
ContentService
.
createTextOutput
(
params
).
setMimeType
(
ContentService
.
MimeType
.
JSON
);


}
```
En el ejemplo anterior, doGet devuelve el siguiente resultado:
`doGet`
```
{


  
"queryString"
:
 
"username=jsmith&age=21"
,


  
"parameter"
:
 
{


    
"username"
:
 
"jsmith"
,


    
"age"
:
 
"21"


  
},


  
"contextPath"
:
 
""
,


  
"parameters"
:
 
{


    
"username"
:
 
[


      
"jsmith"


    
],


    
"age"
:
 
[


      
"21"


    
]


  
},


  
"contentLength"
:
 
-1


}
```
El sistema reserva los siguientes nombres de parámetros, por lo que no se deben usar en los parámetros de URL ni en los cuerpos de POST:
- c
`c`
- sid
`sid`
El uso de estos parámetros puede generar una respuesta HTTP 405 con el mensaje de error "Lo sentimos, el archivo que solicitaste no existe". Si es posible, actualiza tu secuencia de comandos para usar nombres de parámetros diferentes.
## Implementa una secuencia de comandos como una app web
Para implementar una secuencia de comandos como una app web, sigue estos pasos:
- En la parte superior derecha del proyecto de secuencia de comandos, haz clic en Implementar > Nueva implementación .
- Junto a "Seleccionar tipo", haz clic en Habilitar los tipos de implementación settings > app web .
- Ingresa la información sobre tu app web en los campos de "Configuración de implementación".
- Haz clic en Implementar .
Comparte la URL de la app web con quienes quieras que la usen, siempre y cuando les hayas otorgado acceso.
Las apps web implementadas en un dominio dejan de funcionar si su propiedad cambia a una unidad compartida o a una cuenta en un dominio diferente. Para corregir esto, el nuevo propietario o colaborador debe volver a implementar la app web en el nuevo dominio. Como alternativa, si la app web se vuelve a mover a su dominio original, comenzará a funcionar nuevamente para ese dominio sin necesidad de volver a implementarla.
## Prueba la implementación de una app web
Para probar tu secuencia de comandos como una app web, sigue estos pasos:
- En la parte superior derecha del proyecto de secuencia de comandos, haz clic en Implementar > Implementaciones de prueba .
- Junto a "Seleccionar tipo", haz clic en Habilitar los tipos de implementación settings > Aplicación web .
- Debajo de la URL de la app web, haz clic en Copiar .
- Pega la URL en tu navegador y prueba tu app web. Esta URL termina en /dev y solo pueden acceder a ella los usuarios que tienen acceso de edición a la secuencia de comandos. Esta instancia de la app siempre ejecuta el código guardado más recientemente y solo está diseñada para realizar pruebas durante el desarrollo.
Pega la URL en tu navegador y prueba tu app web.
Esta URL termina en /dev y solo pueden acceder a ella los usuarios que tienen acceso de edición a la secuencia de comandos. Esta instancia de la app siempre ejecuta el código guardado más recientemente y solo está diseñada para realizar pruebas durante el desarrollo.
`/dev`
Para probar la función de OAuth granular en la app web, asegúrate de que tu proyecto no tenga ya algunas autorizaciones. Para invalidar las autorizaciones existentes, usa ScriptApp.invalidateAuth . En el caso de las apps web que ya se implementaron y se ejecutan con la identidad del usuario activo , modifica el campo executeAs de JSON en el manifiesto a USER_DEPLOYING .
`executeAs`
`USER_DEPLOYING`
Cuando implementes apps web para que se ejecuten como el desarrollador, ten mucho cuidado al controlar los tokens de OAuth obtenidos a través de ScriptApp.getOAuthToken . Estos tokens pueden otorgar a otras aplicaciones acceso a tus datos. Nunca los transmitas al cliente.
## Permisos
Los permisos de una app web varían según la forma en que elijas ejecutarla:
- Ejecutar la app como yo : En este caso, la secuencia de comandos siempre se ejecuta como tú, el propietario de la secuencia de comandos, sin importar quién acceda a la app web.
- Ejecutar la app como el usuario que accede a la app web : En este caso, la secuencia de comandos se ejecuta con la identidad del usuario activo que usa la app web. Este enfoque de permisos hace que la app web muestre el correo electrónico del propietario de la secuencia de comandos cuando el usuario autoriza el acceso.
Para evitar abusos, Apps Script impone límites en la frecuencia con la que los usuarios nuevos pueden autorizar una app web que se ejecuta como el usuario. Estos límites dependen, entre otros factores, de si la cuenta de publicación forma parte de un dominio de Google Workspace .
Colabora en apps web con una unidad compartida . Cuando se implementa una app web en una unidad compartida, si se elige la opción "Ejecutar como tú", la app web se ejecuta bajo la autoridad del usuario que la implementó (ya que no hay propietario del script).
## Incorpora tu app web en Google Sites {:#embed-web-app}
Las apps web integradas siguen sujetas a permisos de acceso para evitar el uso malicioso. Si parece que tu app web integrada no funciona, verifica si los permisos establecidos por el propietario de la app web y el administrador del dominio permiten su uso.
Para incorporar una app web en Sites, primero se debe implementar . También necesitas la URL implementada del diálogo Implementar .
Para incorporar una app web en una página de Sites , sigue estos pasos:
- Abre la página de Sites en la que deseas agregar la app web.
- Selecciona Insertar > URL de incorporación .
- Pega la URL de la app web y, luego, haz clic en AGREGAR .
La app web aparece en un marco en la vista previa de la página. Cuando publiques la página, es posible que los usuarios de tu sitio deban autorizar la app web antes de que se ejecute con normalidad. Las apps web no autorizadas muestran mensajes de autorización al usuario.
## Historial del navegador y apps web
Para simular una aplicación de varias páginas o una con una IU dinámica controlada con parámetros de URL, define un objeto de estado para representar la IU o la página de la aplicación, y envía el estado al historial del navegador a medida que el usuario navega por tu aplicación. Escucha los eventos del historial para que tu app web muestre la IU correcta cuando el usuario navegue hacia atrás y hacia adelante con los botones del navegador. Cuando consultes los parámetros de URL en el tiempo de carga, haz que tu app compile dinámicamente su IU en función de esos parámetros, lo que permitirá que el usuario inicie la app en un estado particular.
Apps Script proporciona dos APIs de JavaScript asíncronas del cliente para ayudar a crear apps web vinculadas al historial del navegador:
- google.script.history proporciona métodos para permitir una respuesta dinámica a los cambios en el historial del navegador. Esto incluye insertar estados (objetos simples que defines) en el historial del navegador, reemplazar el estado superior en la pila del historial y establecer una función de devolución de llamada del objeto de escucha para responder a los cambios del historial.
google.script.history proporciona métodos para permitir una respuesta dinámica a los cambios en el historial del navegador. Esto incluye insertar estados (objetos simples que defines) en el historial del navegador, reemplazar el estado superior en la pila del historial y establecer una función de devolución de llamada del objeto de escucha para responder a los cambios del historial.
`google.script.history`
- google.script.url proporciona los medios para recuperar los parámetros de URL y el fragmento de URL de la página actual, si están presentes.
google.script.url proporciona los medios para recuperar los parámetros de URL y el fragmento de URL de la página actual, si están presentes.
`google.script.url`
Estas APIs de historial solo están disponibles para las apps web. No se admiten en barras laterales, diálogos ni complementos. Tampoco se recomienda usar esta función en apps web incorporadas en un sitio de Sites .
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### servicios de Google

- Página principal
- Google Workspace
- Apps Script
- Guías
# Servicios de Google integrados Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Google Apps Script proporciona más de 30 servicios integrados para interactuar con los datos del usuario, otros sistemas de Google y sistemas externos. Estos servicios se proporcionan como objetos globales similares al objeto Math estándar de JavaScript. Por ejemplo, al igual que Math ofrece métodos como random() y constantes como PI , el servicio de hojas de cálculo de Apps Script ofrece métodos como openById(id) , clases (objetos secundarios) como Range y enumeraciones como DataValidationCriteria .
`Math`
`Math`
`random()`
`PI`
`openById(id)`
`Range`
`DataValidationCriteria`
La documentación de referencia para los servicios que controlan los productos de Google Workspace se recopila en la sección "Servicios de Google Workspace" que se encuentra debajo del encabezado "Referencia" en la barra lateral de este sitio. Los servicios de utilidad (para tareas como crear interfaces de usuario, analizar XML o escribir datos de registro) se recopilan en la sección "Servicios de secuencias de comandos".
## Funciones modernas de Java Script
Apps Script admite dos entornos de ejecución de JavaScript: el entorno de ejecución moderno V8 y uno más antiguo con tecnología del intérprete de JavaScript Rhino de Mozilla.
El tiempo de ejecución de V8 admite la sintaxis y las funciones modernas de ECMAScript . El entorno de ejecución de Rhino se basa en el estándar anterior de JavaScript 1.6 , además de algunas funciones de 1.7 y 1.8 . Elige el tiempo de ejecución que deseas usar con tu secuencia de comandos, pero se recomienda el tiempo de ejecución de V8.
Cada entorno de ejecución admite clases y objetos de JavaScript que están disponibles para tu secuencia de comandos, además de los servicios avanzados de Google y los integrados. Tus secuencias de comandos pueden usar objetos comunes como Array , Date , RegExp , y así sucesivamente , así como los objetos globales Math y Object .
`Array`
`Date`
`RegExp`
`Math`
`Object`
Dado que el código de Apps Script se ejecuta en los servidores de Google (con la excepción de las páginas de servicio HTML ), las funciones de JavaScript basadas en el navegador, como la manipulación del DOM o la API de Window , no están disponibles en Apps Script.
`Window`
## Autocompletar
El editor de secuencias de comandos proporciona una función de "asistencia de contenido", más comúnmente llamada "autocompletar", que revela los objetos globales, así como los métodos y las enumeraciones que son válidos en el contexto actual de la secuencia de comandos. Las sugerencias de autocompletado aparecen automáticamente cada vez que escribes un punto después de un objeto global, una enumeración o una llamada a un método que devuelve una clase de Apps Script. Por ejemplo:
- Si escribes el nombre completo de un objeto global o seleccionas uno de la función de autocompletar y, luego, escribes . (un punto), verás todos los métodos y las enumeraciones de esa clase.
`.`
- Si escribes algunos caracteres, verás todas las sugerencias válidas que comiencen con esos caracteres.
## Objetos globales
Cada servicio proporciona al menos un objeto global (de nivel superior). Por ejemplo, se accede al servicio de Gmail únicamente desde el objeto GmailApp . Algunos servicios proporcionan varios objetos globales. Por ejemplo, el servicio básico incluye cuatro objetos globales: Browser , Logger , MimeType y Session .
`GmailApp`
`Browser`
`Logger`
`MimeType`
`Session`
## Métodos
Los objetos globales de casi todos los servicios avanzados o integrados incluyen métodos que devuelven datos o una clase de Apps Script. Las secuencias de comandos realizan llamadas a métodos con este formato:
```
GlobalObjectName.methodName(argument1, argument2, ..., argumentN);
```
Por ejemplo, una secuencia de comandos puede enviar un correo electrónico llamando al método sendEmail(recipient, subject, body) del servicio de Gmail de la siguiente manera:
`sendEmail(recipient, subject, body)`
```
GmailApp
.
sendEmail
(
'claire@example.com'
,
 
'Subject line'
,
 
'This is the body.'
);
```
Si un método devuelve otra clase de Apps Script, encadena las llamadas a métodos en una sola línea. (Los tipos de devolución se muestran tanto en el autocompletado como en la documentación de referencia de un método). Por ejemplo, el método DocumentApp.create() devuelve un Document , por lo que las siguientes dos secciones de código son equivalentes:
`DocumentApp.create()`
`Document`
```
var
 
doc
 
=
 
DocumentApp
.
create
(
'New document'
);


var
 
body
 
=
 
doc
.
getTab
(
't.0'
)
.
asDocumentTab
()
.
getBody
();


body
.
appendParagraph
(
'New paragraph.'
);



//
 
Same
 
result
 
as
 
above
.


DocumentApp
.
create
(
'New document'
)
.
getTab
(
't.0'
)
.
asDocumentTab
()
.
getBody
()


    
.
appendParagraph
(
'New paragraph.'
);
```
## Clases secundarias
Cada servicio incluye una o más clases secundarias a las que no puedes acceder desde el nivel superior como un objeto global. Tampoco puedes usar la palabra clave new para construir estas clases, como lo harías con las clases estándar de JavaScript, como Date . Para acceder a una clase secundaria, debes llamar a un método que la devuelva. Si no sabes cómo acceder a una clase determinada, visita la página principal de la documentación de referencia del servicio, en la que se enumeran las clases del servicio y los métodos que las devuelven.
`new`
`Date`
## Interfaces
Algunos servicios incluyen clases etiquetadas como "interfaces" en la documentación de referencia. Son clases genéricas que se usan como tipos de datos que se muestran para los métodos que no pueden determinar el tipo preciso por adelantado. Por ejemplo, el método Document service Body.getChild(childIndex) devuelve un objeto Element genérico. La interfaz Element representa alguna otra clase, posiblemente un Paragraph o un Table . Los objetos de interfaz rara vez son útiles por sí solos; en cambio, llama a un método como Element.asParagraph() para volver a convertir el objeto en una clase específica.
`Body.getChild(childIndex)`
`Element`
`Element`
`Paragraph`
`Table`
`Element.asParagraph()`
## Enums
La mayoría de los servicios incluyen enumeraciones (tipos enumerados) de valores con nombre. Por ejemplo, el servicio de Google Drive usa las enumeraciones Access y Permission para determinar qué usuarios tienen acceso a un archivo o una carpeta. En la mayoría de los casos, accedes a estos enumeradores desde el objeto global, como se muestra en el siguiente ejemplo:
`Access`
`Permission`
```
// Creates a folder that anyone on the Internet can read from and write to.


// (Domain administrators can prohibit this setting for Google Workspace users.)


var
 
folder
 
=
 
DriveApp
.
createFolder
(
'Shared Folder'
);


folder
.
setSharing
(
DriveApp
.
Access
.
ANYONE
,
 
DriveApp
.
Permission
.
EDIT
);
```
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### add-ons

- Página principal
- Google Workspace
- Complementos
- Add-ons
# Descripción general de los complementos Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Los complementos son aplicaciones personalizadas que extienden las aplicaciones de Google Workspace.
## Agrega nuevas capacidades a Google Workspace
Los complementos ayudan a automatizar tareas o a poner a disposición servicios o información de terceros en Google Workspace. Con los complementos, puedes hacer lo siguiente:
- Crear interfaces de usuario personalizadas que se integren directamente en las aplicaciones de Google Workspace. Estas interfaces pueden mostrar información al usuario y proporcionar controles de usuario.
- Aumentar la eficiencia del flujo de trabajo cuando se trabaja con Google Workspace mediante la automatización o la optimización de tareas.
- Controlar y mover datos entre las aplicaciones de Google.
- Eliminar la necesidad de cambiar de navegador, ya que se le proporciona al usuario todo lo que necesita en Google Workspace.
- Conectarse a servicios que no son de Google dentro de las aplicaciones de Google Workspace, lo que te permite recuperar o subir datos de esos servicios a Google Workspace.
## Tipos de complementos
Hay dos tipos de complementos que puedes compilar: complementos de Google Workspace y complementos del Editor . Para obtener más información, consulta Tipos de complementos .
## API Google Workspace Add-ons
Algunas funciones, como la extensión del menú desplegable de videoconferencias de Google Calendar y las capacidades de iOS, aún no son compatibles con la API de Google Workspace Add-ons.
Con la API de Google Workspace Add-ons, puedes hacer lo siguiente:
- Automatizar pruebas e implementaciones.
- Realizar tareas en segundo plano con el servicio de hosting de tu complemento.
- Crear y administrar implementaciones con herramientas de línea de comandos.
- Administrar permisos de implementación para cuentas de servicio o usuarios habituales con permisos detallados de Cloud IAM.
Para obtener más información sobre la API de Google Workspace Add-ons, consulta la documentación de referencia .
## Prueba una guía de inicio rápido
Para ver cómo funciona la compilación de un complemento, prueba una guía de inicio rápido:
- Guía de inicio rápido del complemento de Google Workspace de Node.js
- Guía de inicio rápido del complemento de Google Workspace de Apps Script
- Guía de inicio rápido del complemento del Editor de Apps Script
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-04 (UTC)

---

### Guía de inicio rápido de automatización

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Guía de inicio rápido de automatización Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Crea y ejecuta una automatización que cree un documento de Documentos de Google y te envíe por correo electrónico un vínculo a él.
## Objetivos
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
Para crear la automatización, haz lo siguiente:
- Para abrir el editor de secuencias de comandos de Google Apps, ve a script.google.com . Si es la primera vez que visitas script.google.com , haz clic en Ver panel .
`script.google.com`
`script.google.com`
- Haz clic en Proyecto nuevo .
- Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código. templates/standalone/helloWorld.gs Ver en GitHub /** * Creates a Google Doc and sends an email to the current user with a link to the doc. */ function createAndSendDocument () { try { // Create a new Google Doc named 'Hello, world!' const doc = DocumentApp . create ( "Hello, world!" ); // Access the body of the document, then add a paragraph. doc . getBody () . appendParagraph ( "This document was created by Google Apps Script." ); // Get the URL of the document. const url = doc . getUrl (); // Get the email address of the active user - that's you. const email = Session . getActiveUser (). getEmail (); // Get the name of the document to use as an email subject line. const subject = doc . getName (); // Append a new string to the "url" variable to use as an email body. const body = `Link to your doc: ${ url } ` ; // Send yourself an email with a link to the document. GmailApp . sendEmail ( email , subject , body ); } catch ( err ) { // TODO (developer) - Handle exception console . log ( "Failed with error %s" , err . message ); } }
Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código.
```
/**


 * Creates a Google Doc and sends an email to the current user with a link to the doc.


 */


function
 
createAndSendDocument
()
 
{


  
try
 
{


    
// Create a new Google Doc named 'Hello, world!'


    
const
 
doc
 
=
 
DocumentApp
.
create
(
"Hello, world!"
);



    
// Access the body of the document, then add a paragraph.


    
doc


      
.
getBody
()


      
.
appendParagraph
(
"This document was created by Google Apps Script."
);



    
// Get the URL of the document.


    
const
 
url
 
=
 
doc
.
getUrl
();



    
// Get the email address of the active user - that's you.


    
const
 
email
 
=
 
Session
.
getActiveUser
().
getEmail
();



    
// Get the name of the document to use as an email subject line.


    
const
 
subject
 
=
 
doc
.
getName
();



    
// Append a new string to the "url" variable to use as an email body.


    
const
 
body
 
=
 
`Link to your doc: 
${
url
}
`
;



    
// Send yourself an email with a link to the document.


    
GmailApp
.
sendEmail
(
email
,
 
subject
,
 
body
);


  
}
 
catch
 
(
err
)
 
{


    
// TODO (developer) - Handle exception


    
console
.
log
(
"Failed with error %s"
,
 
err
.
message
);


  
}


}
```
- Haz clic en Guardar .
Haz clic en Guardar .
- Haz clic en Proyecto sin título .
Haz clic en Proyecto sin título .
- Ingresa un nombre para tu secuencia de comandos y haz clic en Cambiar nombre .
Ingresa un nombre para tu secuencia de comandos y haz clic en Cambiar nombre .
## Ejecuta la secuencia de comandos:
Para ejecutar la secuencia de comandos, haz lo siguiente:
- Haz clic en Ejecutar .
- Cuando se te solicite, autoriza la secuencia de comandos. <<../samples/_snippets/oauth.md>>
- Cuando finalice la ejecución de la secuencia de comandos, revisa tu carpeta Recibidos de Gmail para ver el correo electrónico.
- Abre el correo electrónico y haz clic en el vínculo para abrir el documento que creaste.
## Próximos pasos
- Extender Docs
- Extiende Hojas de cálculo de Google
- Extiende Presentaciones de Google
- Funciones básicas de JavaScript
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Guía de inicio rápido de función personalizada

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Guía de inicio rápido de las funciones personalizadas Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Puedes usar Google Apps Script para escribir una función personalizada y, luego, usarla en Hojas de cálculo de Google como si fuera una función integrada.
En el siguiente ejemplo de inicio rápido, se crea una función personalizada que calcula el precio de venta de los artículos con descuento. El precio de oferta se muestra en dólares estadounidenses.
## Objetivos
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
- Crea una hoja de cálculo nueva .
- En la hoja de cálculo nueva, selecciona el elemento de menú Extensiones > Apps Script .
- Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código. Luego, haz clic en Guardar . /** * Calculates the sale price of a value at a given discount . * The sale price is formatted as US dollars . * * @ param { number } input The value to discount . * @ param { number } discount The discount to apply , such as . 5 or 50 % . * @ return The sale price formatted as USD . * @ customfunction */ function salePrice ( input, discount ) { let price = input - ( input * discount ); let dollarUS = Intl . NumberFormat ( "en-US" , { style : "currency" , currency : "USD" , }); return dollarUS . format ( price ); }
Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código. Luego, haz clic en Guardar .
```
/**


 
*
 
Calculates
 
the
 
sale
 
price
 
of
 
a
 
value
 
at
 
a
 
given
 
discount
.


 
*
 
The
 
sale
 
price
 
is
 
formatted
 
as
 
US
 
dollars
.


 
*


 
*
 
@
param
 
{
number
}
 
input
 
The
 
value
 
to
 
discount
.


 
*
 
@
param
 
{
number
}
 
discount
 
The
 
discount
 
to
 
apply
,
 
such
 
as
 
.
5
 
or
 
50
%
.


 
*
 
@
return
 
The
 
sale
 
price
 
formatted
 
as
 
USD
.


 
*
 
@
customfunction


 
*/


function
 
salePrice
(
input, discount
)
 
{


  
let
 
price
 
=
 
input
 
-
 
(
input
 
*
 
discount
);


  
let
 
dollarUS
 
=
 
Intl
.
NumberFormat
(
"en-US"
,
 
{


    
style
:
 
"currency"
,


    
currency
:
 
"USD"
,


});


  
return
 
dollarUS
.
format
(
price
);


}
```
## Ejecuta la secuencia de comandos:
- Vuelve a tu hoja de cálculo.
- En una celda, ingresa =salePrice(100,20) . El primer parámetro representa el precio original y el segundo parámetro representa el porcentaje de descuento. Si te encuentras en una ubicación que usa comas decimales, es posible que debas ingresar =salePrice(100;20) .
`=salePrice(100,20)`
`=salePrice(100;20)`
La fórmula que ingresas en la celda ejecuta la función en la secuencia de comandos que creaste en la sección anterior. La función genera un precio de oferta de $80.00 .
`$80.00`
## Próximos pasos
Para seguir aprendiendo a extender Hojas de cálculo con Apps Script, consulta los siguientes recursos:
- Funciones personalizadas de hojas de cálculo
- Menús personalizados en Google Workspace
- Extender Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Guía de inicio rápido de bot de Google Chat

- Página principal
- Google Workspace
- Google Chat
- Guías
# Compila una app de Google Chat con Google Apps Script Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Crea una app de Google Chat con la que puedas enviar mensajes y que responda directamente con la repetición de tus mensajes.
En el siguiente diagrama, se muestran la arquitectura y el patrón de mensajería:
En el diagrama anterior, un usuario que interactúa con una app de chat de Apps Script tiene el siguiente flujo de información:
- Un usuario envía un mensaje a una app de Chat, ya sea en un mensaje directo o en un espacio de Chat.
- La lógica de la app de Chat implementada en Apps Script, que reside en Google Cloud, recibe y procesa el mensaje.
- De manera opcional, la lógica de la app de Chat puede integrarse con los servicios de Google Workspace, como Calendario o Hojas de cálculo, o con otros servicios de Google, como Google Maps o YouTube.
- La lógica de la app de Chat envía una respuesta al servicio de la app de Chat en Chat.
- La respuesta se entrega al usuario.
## Objetivos
- Configura el entorno.
- Configura la secuencia de comandos.
- Configura la app de Chat.
- Prueba la app de Chat.
## Requisitos previos
- Una cuenta de Google Workspace para empresas o Enterprise con acceso a Google Chat
- Un proyecto de Google Cloud, Para crear uno, consulta Crea un proyecto de Google Cloud .
## Configura tu entorno
### Abre tu proyecto de Cloud en la consola de Google Cloud.
Si aún no está abierto, abre el proyecto de Cloud que deseas usar para esta muestra:
- En la consola de Google Cloud, ve a la página Seleccionar un proyecto . Selecciona un proyecto de Cloud
Selecciona un proyecto de Cloud
- Selecciona el proyecto de Google Cloud que deseas usar. O bien, haz clic en Crear proyecto y sigue las instrucciones en pantalla. Si creas un proyecto de Google Cloud, es posible que debas activar la facturación para el proyecto .
### Activa la API de Chat
- En la consola de Google Cloud, habilita la API de Google Chat. Habilitar la API
En la consola de Google Cloud, habilita la API de Google Chat.
Habilitar la API
### Cómo configurar la pantalla de consentimiento de OAuth
Todas las apps que usan OAuth 2.0 requieren una configuración de pantalla de consentimiento. Cuando configuras la pantalla de consentimiento de OAuth de tu app, defines lo que se muestra a los usuarios y revisores de apps, y registras tu app para que puedas publicarla más adelante.
- En la consola de APIs de Google, ve a Menú menu > Plataforma de Google Auth > Branding . Ir a Branding
Ir a Branding
- Si ya configuraste la plataforma de Google Auth, puedes configurar los siguientes parámetros de configuración de la pantalla de consentimiento de OAuth en Desarrollo de marca , Público y Acceso a los datos . Si ves un mensaje que dice Aún no se configuró Google Auth Platform , haz clic en Comenzar :
- En Información de la app , en Nombre de la app , ingresa un nombre para la app.
- En Correo electrónico de asistencia al usuario , elige una dirección de correo electrónico de asistencia a la que los usuarios puedan comunicarse contigo si tienen preguntas sobre su consentimiento.
- Haz clic en Siguiente .
- En Público , selecciona Interno .
- Haz clic en Siguiente .
- En Información de contacto , ingresa una Dirección de correo electrónico en la que puedas recibir notificaciones sobre cualquier cambio en tu proyecto.
- Haz clic en Siguiente .
- En Finalizar , revisa la Política de Datos del Usuario de los Servicios de las APIs de Google y, si la aceptas, selecciona Acepto la Política de Datos del Usuario de los Servicios de las APIs de Google .
- Haz clic en Continuar .
- Haz clic en Crear .
- Por el momento, puedes omitir la adición de permisos. En el futuro, cuando crees una app para usarla fuera de tu organización de Google Workspace, deberás cambiar el Tipo de usuario a Externo . Luego, agrega los permisos de autorización que requiere tu app. Para obtener más información, consulta la guía completa Configura el consentimiento de OAuth .
## Configura la secuencia de comandos
Para configurar la secuencia de comandos, usa una plantilla y, luego, configura tu proyecto de Cloud en Apps Script.
### Crea la secuencia de comandos a partir de la plantilla
- Ve a la página de introducción a Apps Script .
- Haz clic en la plantilla Chat App en la parte superior de la página.
- Haz clic en Proyecto sin título , escribe Quickstart app y haz clic en Cambiar nombre .
`Quickstart app`
En el futuro, si quieres usar ciertas APIs de Google o publicar tu app, debes asociar tu proyecto de Cloud con tu proyecto de Apps Script. Para esta guía, no es necesario que lo hagas. Para obtener más información, consulta la guía de proyectos de Google Cloud .
### Crea una implementación de prueba
Necesitas un ID de implementación para este proyecto de Apps Script, de modo que puedas usarlo en el siguiente paso.
Para obtener el ID de la implementación principal, haz lo siguiente:
- En el proyecto de Apps Script de la app de Chat, haz clic en Implementar > Implementaciones de prueba .
- Copia el ID de implementación principal para usarlo en un paso posterior y haz clic en Listo .
## Configura la app de Chat
Configura la app de Chat desde la Consola de APIs.
- En la Consola de APIs , busca Google Chat API y haz clic en API de Google Chat .
`Google Chat API`
- Haz clic en Administrar .
- Haz clic en Configuración y configura la app de Chat: Desmarca la opción Crea esta app de Chat como complemento de Google Workspace . Se abrirá un diálogo en el que se te pedirá que confirmes la acción. En el diálogo que aparece, haz clic en Inhabilitar . En el campo Nombre de la app , ingresa Quickstart app . En el campo URL del avatar , ingresa https://developers.google.com/chat/images/quickstart-app-avatar.png . En el campo Descripción , ingresa Quickstart app . En Funcionalidad , selecciona Unirse a espacios y conversaciones grupales . En Configuración de conexión, selecciona Apps Script . En el campo ID de implementación , pega el ID de implementación principal que copiaste anteriormente. En Visibilidad, selecciona Personas y grupos específicos de tu dominio y escribe tu correo electrónico.
Haz clic en Configuración y configura la app de Chat:
- Desmarca la opción Crea esta app de Chat como complemento de Google Workspace . Se abrirá un diálogo en el que se te pedirá que confirmes la acción. En el diálogo que aparece, haz clic en Inhabilitar .
- En el campo Nombre de la app , ingresa Quickstart app .
`Quickstart app`
- En el campo URL del avatar , ingresa https://developers.google.com/chat/images/quickstart-app-avatar.png .
`https://developers.google.com/chat/images/quickstart-app-avatar.png`
- En el campo Descripción , ingresa Quickstart app .
`Quickstart app`
- En Funcionalidad , selecciona Unirse a espacios y conversaciones grupales .
- En Configuración de conexión, selecciona Apps Script .
- En el campo ID de implementación , pega el ID de implementación principal que copiaste anteriormente.
- En Visibilidad, selecciona Personas y grupos específicos de tu dominio y escribe tu correo electrónico.
- Haz clic en Guardar .
Haz clic en Guardar .
La app de Chat está lista para responder mensajes.
## Prueba la app de Chat
Para probar tu app de Chat, abre un espacio de mensajes directos con la app de Chat y envía un mensaje:
- Abre Google Chat con la cuenta de Google Workspace que proporcionaste cuando te agregaste como verificador de confianza. Ir a Google Chat
Abre Google Chat con la cuenta de Google Workspace que proporcionaste cuando te agregaste como verificador de confianza.
Ir a Google Chat
- Haz clic en add Nuevo chat .
- En el campo Agrega 1 o más personas , escribe el nombre de tu app de Chat.
- Selecciona tu app de Chat en los resultados. Se abrirá un mensaje directo.
Selecciona tu app de Chat en los resultados. Se abrirá un mensaje directo.
- En el nuevo mensaje directo con la app, escribe Hello y presiona enter . La app de Chat te agradece que la hayas agregado y repite tu mensaje.
En el nuevo mensaje directo con la app, escribe Hello y presiona enter .
`Hello`
`enter`
La app de Chat te agradece que la hayas agregado y repite tu mensaje.
Para agregar verificadores de confianza y obtener más información sobre las pruebas de funciones interactivas, consulta Cómo probar funciones interactivas para apps de Google Chat .
## Solucionar problemas
Cuando una app o una tarjeta de Google Chat muestra un error, la interfaz de Chat muestra un mensaje que dice "Se produjo un error". o "No se pudo procesar tu solicitud". A veces, la IU de Chat no muestra ningún mensaje de error, pero la app o la tarjeta de Chat producen un resultado inesperado. Por ejemplo, es posible que no aparezca un mensaje de la tarjeta.
Si bien es posible que no se muestre un mensaje de error en la IU de Chat, hay mensajes de error descriptivos y datos de registro disponibles para ayudarte a corregir errores cuando se activa el registro de errores para las apps de Chat. Para obtener ayuda para ver, depurar y corregir errores, consulta Soluciona y corrige errores de Google Chat .
## Limpia
Para evitar que se apliquen cargos a tu cuenta de Google Cloud por los recursos que usaste en este instructivo, te recomendamos que borres el proyecto de Cloud.
- En la consola de APIs de Google, ve a la página Administrar recursos . Haz clic en Menú menu > IAM y administración > Administrar recursos . Ir a Resource Manager
Ir a Resource Manager
- En la lista de proyectos, selecciona el proyecto que deseas borrar y haz clic en Borrar delete .
- En el diálogo, escribe el ID del proyecto y, luego, haz clic en Cerrar para borrar el proyecto.
## Próximos pasos
- Crea tarjetas interactivas : Los mensajes de tarjetas admiten un diseño definido, elementos interactivos de la IU, como botones, y rich media, como imágenes. Usa mensajes de tarjetas para presentar información detallada, recopilar información de los usuarios y guiarlos para que realicen el siguiente paso.
- Responder a comandos : Los comandos ayudan a los usuarios a descubrir y usar las funciones clave de tu app de Chat.
- Diálogos de lanzamiento : Los diálogos son interfaces basadas en tarjetas y ventanas que tu app puede abrir para interactuar con un usuario. Se pueden encadenar varias tarjetas de forma secuencial, lo que ayuda a los usuarios a completar procesos de varios pasos, como completar datos de formularios.
- code Codelab: ¿Quieres compilar una app de chat más avanzada? Consulta la app de chat de comentarios del codelab Compila apps para Google Chat con Gemini .
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

## Descripción general de la referencia

### Apps Script

- Página principal
- Google Workspace
- Apps Script
### Automatiza y extiende Google Workspace con código sencillo.
Apps Script es una plataforma de JavaScript basada en la nube y potenciada por Google Drive que te permite integrar y automatizar tareas en los productos de Google.
## Desarrolla soluciones de alta calidad con facilidad
### Automatizaciones
Escriba un código que realice tareas de manera programática en todos los productos de Google. Las automatizaciones se activan mediante menús personalizados, botones, acciones del usuario o una programación basada en el tiempo.
### Funciones personalizadas
Escribe funciones de Hojas de cálculo de Google en Apps Script y llámalas desde tu hoja de cálculo como funciones integradas.
### Complementos
Compila una app que automatice tareas o se conecte a servicios de terceros desde Google Workspace. Comparta su solución con otras personas en Google Workspace Marketplace.
### Apps de chat
Proporciona una interfaz de conversación que permita a los usuarios de Google Chat interactuar con los servicios como si el servicio fuera una persona.
### Potencia tus secuencias de comandos con IA
### Guía de inicio rápido de Vertex AI
### Guía de inicio rápido del agente de ADK
### Guía de inicio rápido del agente A2A
### Analizador de mensajes de Gmail
### Agente de Viajes Concierge
### Función personalizada de verificador de datos
### Guía de inicio rápido del agente de ADK
### Guía de inicio rápido del agente A2A
### Guía de inicio rápido del agente de A2UI
### Servicio de Vertex AI
### Inicio rápido del agente de Gemini Enterprise
### Agentes de Gemini Enterprise
### Agentes de Vertex AI
### Crea un complemento de Gmail con vibe coding
### Notas de la versión
### Asistencia
### API de REST
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-03-03 (UTC)

---

### Referencia

- Página principal
- Google Workspace
- Apps Script
- Referencia
# Descripción general de la referencia Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
La documentación de referencia que se proporciona en esta sección describe los diversos servicios de Google Apps Script y los recursos del proyecto.
## Servicios de Apps Script
Los servicios de Apps Script proporcionan formas para que tu secuencia de comandos acceda a los datos de Google y de sistemas externos. Estos servicios están integrados en el entorno de Apps Script, por lo que no tienes que importarlos ni implementar controles de autorización por tu cuenta. Los servicios se expresan como objetos globales con métodos asociados, de forma similar a los objetos de JavaScript, como Math .
`Math`
Apps Script incluye los siguientes servicios:
- Los servicios de Google son servicios que te permiten acceder a los datos de las apps de Google Workspace, como Drive, Gmail y Hojas de cálculo, y otras apps de Google, como Maps y Traductor.
Los servicios de Google son servicios que te permiten acceder a los datos de las apps de Google Workspace, como Drive, Gmail y Hojas de cálculo, y otras apps de Google, como Maps y Traductor.
- Los servicios de utilidad son servicios que no están conectados a un producto específico de Google. Te permiten realizar acciones como registrar información, crear HTML, comprimir datos y mucho más.
Los servicios de utilidad son servicios que no están conectados a un producto específico de Google. Te permiten realizar acciones como registrar información, crear HTML, comprimir datos y mucho más.
### Servicios avanzados
Google ofrece algunos servicios como servicios avanzados . Un servicio avanzado es un servicio de Apps Script que te permite acceder a las APIs de productos de Google, incluidas, entre otras, las APIs de productos de Google Workspace. Un servicio avanzado de Google es un wrapper delgado en torno a una API y no es una API en sí. Para obtener más detalles, consulta Servicios avanzados de Google .
## Recursos del proyecto de secuencia de comandos
Los recursos del proyecto de secuencia de comandos proporcionan información sobre tu proyecto de Apps Script para ayudarlo a ejecutarse correctamente. Los recursos del proyecto incluyen información sobre la configuración del manifiesto, los activadores de automatización y las cuotas.
## Recursos de complementos de Google Workspace
Consulta los recursos de complementos si compilas un complemento de Google Workspace .
## API de Apps Script
Usa estos recursos si deseas crear, modificar o implementar proyectos de Apps Script de forma programática con la API de Apps Script .
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Servicios avanzados de Google

- Página principal
- Google Workspace
- Apps Script
- Guías
# Servicios avanzados de Google Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Los servicios avanzados de Google Apps Script te permiten conectarte a ciertas APIs públicas de Google con menos configuración que si usaras sus interfaces HTTP. Los servicios avanzados son wrappers delgados en torno a esas APIs de Google. Funcionan de manera muy similar a los servicios integrados de Apps Script. Por ejemplo, ofrecen autocompletado y Apps Script controla el flujo de autorización automáticamente. Habilita un servicio avanzado antes de usarlo en una secuencia de comandos.
## Habilita los servicios avanzados
Para usar un servicio avanzado de Google, sigue estas instrucciones:
### Paso 1: Habilita el servicio avanzado
Habilita un servicio avanzado con el editor de Apps Script o editando el manifiesto.
#### Método A: Usa el editor
- Abre el proyecto de Apps Script.
- A la izquierda, haz clic en Editor code .
- A la izquierda, junto a Servicios , haz clic en Agregar un servicio add .
- Selecciona un servicio avanzado de Google y haz clic en Agregar .
#### Método B: Usa el manifiesto
Habilita los servicios avanzados editando el archivo de manifiesto . Por ejemplo, para habilitar el servicio avanzado de Google Drive, agrega el campo enabledAdvancedServices al objeto dependencies :
`enabledAdvancedServices`
`dependencies`
```
{


  
"timeZone"
:
 
"America/Denver"
,


  
"dependencies"
:
 
{


    
"enabledAdvancedServices"
:
 
[


      
{


        
"userSymbol"
:
 
"Drive"
,


        
"version"
:
 
"v3"
,


        
"serviceId"
:
 
"drive"


      
}


    
]


  
},


  
"exceptionLogging"
:
 
"STACKDRIVER"
,


  
"runtimeVersion"
:
 
"V8"


}
```
Después de habilitar un servicio avanzado, estará disponible en el autocompletado.
### Paso 2: Habilita la API de Google Cloud (solo para proyectos estándar de Google Cloud)
Si usas un proyecto de Google Cloud predeterminado (creado automáticamente por Apps Script), omite este paso. La API se habilita automáticamente cuando agregas el servicio en el paso 1.
Si usas un proyecto estándar de Google Cloud , habilita manualmente la API correspondiente al servicio avanzado. Para habilitar la API de forma manual, sigue estos pasos:
- Abre el proyecto de Cloud asociado con tu secuencia de comandos en la **consola de Google Cloud** .
Abre el proyecto de Cloud asociado con tu secuencia de comandos en la **consola de Google Cloud** .
- En la parte superior de la consola, haz clic en la barra de búsqueda y escribe parte del nombre de la API (por ejemplo, "Calendar"). Luego, haz clic en el nombre cuando lo veas.
En la parte superior de la consola, haz clic en la barra de búsqueda y escribe parte del nombre de la API (por ejemplo, "Calendar"). Luego, haz clic en el nombre cuando lo veas.
- Haz clic en Habilitar la API .
Haz clic en Habilitar la API .
- Cierra la consola de Google Cloud y regresa al editor de secuencias de comandos.
Cierra la consola de Google Cloud y regresa al editor de secuencias de comandos.
## Cómo se determinan las firmas de métodos
En general, los servicios avanzados usan los mismos objetos, nombres de métodos y parámetros que las APIs públicas correspondientes, aunque las firmas de métodos se traducen para su uso en Apps Script. La función de autocompletar del editor de secuencias de comandos suele proporcionar suficiente información para comenzar. En las siguientes reglas, se explica cómo Apps Script genera una firma de método a partir de una API pública de Google.
Las solicitudes a las APIs de Google pueden aceptar una variedad de tipos de datos diferentes, incluidos parámetros de ruta, parámetros de consulta, un cuerpo de solicitud o un archivo adjunto de carga de medios. Algunos servicios avanzados también pueden aceptar encabezados de solicitudes HTTP específicos (por ejemplo, el servicio avanzado de Calendar ).
La firma del método correspondiente en Apps Script tiene los siguientes argumentos:
- El cuerpo de la solicitud (por lo general, un recurso), como un objeto JavaScript.
- Parámetros de ruta o obligatorios, como argumentos individuales. Si el método requiere varios parámetros de ruta, estos aparecen en el orden en que se enumeran en la URL del endpoint de API.
- El archivo adjunto de carga de medios, como un argumento Blob
`Blob`
- Parámetros opcionales (por lo general, parámetros de consulta), como un objeto JavaScript que asigna nombres de parámetros a valores.
- Encabezados de solicitud HTTP, como un objeto JavaScript que asigna nombres de encabezado a valores de encabezado.
Si el método no tiene ningún elemento en una categoría determinada, se omite esa parte de la firma.
Ten en cuenta estas excepciones:
- En el caso de los métodos que aceptan cargas de medios, el parámetro uploadType se establece automáticamente.
`uploadType`
- Los métodos denominados delete en la API de Google se denominan remove en Apps Script, ya que delete es una palabra reservada en JavaScript.
`delete`
`remove`
`delete`
- Si un servicio avanzado está configurado para aceptar encabezados de solicitudes HTTP y estableces un objeto JavaScript de encabezados de solicitudes, también debes establecer el objeto JavaScript de parámetros opcionales (en un objeto vacío si no usas parámetros opcionales).
### Ejemplo: Calendar.Events.insert
Para crear un evento de calendario , sigue estos pasos:
La documentación de la API de Calendario de Google muestra la estructura de la solicitud HTTP correspondiente:
- Verbo HTTP : POST
`POST`
- URL de la solicitud : https://www.googleapis.com/calendar/v3/calendars/{calendarId}/events
`https://www.googleapis.com/calendar/v3/calendars/{calendarId}/events`
- Cuerpo de la solicitud : Es un recurso Event .
Cuerpo de la solicitud : Es un recurso Event .
- Parámetros de consulta : sendUpdates , supportsAttachments , etcétera
Parámetros de consulta : sendUpdates , supportsAttachments , etcétera
`sendUpdates`
`supportsAttachments`
En Apps Script, la firma del método se determina reordenando estas entradas:
- Cuerpo : Es el recurso del evento (objeto JavaScript).
- Ruta : Es calendarId (cadena).
`calendarId`
- Parámetros opcionales : Son los parámetros de consulta (objeto de JavaScript).
La llamada de método resultante se ve de la siguiente manera:
```
const
 
event
 
=
 
{


  
summary
:
 
'Lunch'
,


  
location
:
 
'Deli'
,


  
start
:
 
{


    
dateTime
:
 
'2026-01-01T12:00:00-05:00'


  
},


  
end
:
 
{


    
dateTime
:
 
'2026-01-01T13:00:00-05:00'


  
}


};


const
 
calendarId
 
=
 
'primary'
;


const
 
optionalArgs
 
=
 
{


  
sendUpdates
:
 
'all'


};



Calendar
.
Events
.
insert
(
event
,
 
calendarId
,
 
optionalArgs
);
```
## ¿Servicios avanzados o HTTP?
Cada servicio avanzado de Google está asociado a una API pública de Google. En Apps Script, accede a estas APIs con servicios avanzados o realiza las solicitudes a la API directamente con UrlFetch .
`UrlFetch`
Si usas el método de servicio avanzado , Apps Script controla el flujo de autorización y ofrece compatibilidad con la función de autocompletar. Habilita el servicio avanzado antes de usarlo.
Si usas el método UrlFetch para acceder directamente a la API , básicamente tratas la API de Google como una API externa . Con este método, puedes usar todos los aspectos de la API. Sin embargo, debes controlar la autorización de la API.
`UrlFetch`
En la siguiente tabla, se comparan los dos métodos:
### Comparación de código
En los ejemplos de código, se muestra la diferencia en la complejidad entre crear un evento de calendario con el servicio avanzado y con UrlFetchApp .
`UrlFetchApp`
Servicio avanzado:
```
const
 
event
 
=
 
{


  
summary
:
 
'Lunch'
,


  
location
:
 
'Deli'
,


  
start
:
 
{
 
dateTime
:
 
'2026-01-01T12:00:00-05:00'
 
},


  
end
:
 
{
 
dateTime
:
 
'2026-01-01T13:00:00-05:00'
 
}


};



const
 
optionalArgs
 
=
 
{


  
sendUpdates
:
 
'all'


};



Calendar
.
Events
.
insert
(
event
,
 
'primary'
,
 
optionalArgs
);
```
UrlFetch (HTTP):
```
const
 
event
 
=
 
{


  
summary
:
 
'Lunch'
,


  
location
:
 
'Deli'
,


  
start
:
 
{
 
dateTime
:
 
'2026-01-01T12:00:00-05:00'
 
},


  
end
:
 
{
 
dateTime
:
 
'2026-01-01T13:00:00-05:00'
 
}


};


const
 
url
 
=
 
'https://www.googleapis.com/calendar/v3/calendars/primary/events?sendUpdates=all'
;


const
 
options
 
=
 
{


  
method
:
 
'post'
,


  
contentType
:
 
'application/json'
,


  
headers
:
 
{


    
Authorization
:
 
`Bearer 
${
ScriptApp
.
getOAuthToken
()
}
`


  
},


  
payload
:
 
JSON
.
stringify
(
event
)


};



UrlFetchApp
.
fetch
(
url
,
 
options
);
```
En el caso del método UrlFetchApp , especifica manualmente los permisos de OAuth necesarios en el archivo de manifiesto de la secuencia de comandos.
`UrlFetchApp`
Usa un servicio avanzado siempre que sea posible y solo usa el método UrlFetch cuando el servicio avanzado no esté disponible o no proporcione la funcionalidad que necesitas.
`UrlFetch`
## Compatibilidad con servicios avanzados
Dado que los servicios avanzados son wrappers delgados en torno a las APIs de Google, cualquier problema que se encuentre al usarlos suele ser un problema con la API subyacente, no con Apps Script.
Si tienes un problema mientras usas un servicio avanzado, infórmalo siguiendo las instrucciones de asistencia de la API subyacente.
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### API de Apps Script

- Página principal
- Google Workspace
- Apps Script
- Guías
# Introducción Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
La API de Google Apps Script te permite automatizar la creación, la administración y la ejecución de secuencias de comandos en Google Apps Script. Puedes crear, modificar e implementar proyectos de Google Apps Script de forma programática, y ejecutar funciones de Apps Script de forma remota, acciones que, de lo contrario, requieren el uso del editor de Apps Script o su IU.
Esta API se suele usar para lo siguiente:
- Crear y administrar proyectos y las implementaciones de Apps Script
- Agregar o actualizar funciones en proyectos de secuencias de comandos
- Ejecutar funciones de Apps Script desde otras aplicaciones
- Supervisar los registros de ejecución y los estados de las secuencias de comandos
La API de Apps Script también reemplaza y extiende la API de ejecución de Apps Script. Puedes usar la API de Apps Script para ejecutar funciones de Apps Script de forma remota, tal como lo hacías con la API de Execution.
Para usar esta API en tus apps, debes habilitarla .
Para permitir que otras apps administren tus secuencias de comandos, debes otorgarles acceso .
## Descripción general de la API
La API de Apps Script se divide en varios recursos, cada uno con un propósito específico y un conjunto de solicitudes que puedes realizar. Estos recursos son los siguientes:
- projects : Es una representación de un proyecto de secuencia de comandos. La API proporciona métodos para crear, leer, supervisar y modificar proyectos. Usa este recurso para administrar los archivos de secuencia de comandos y los metadatos de tu proyecto.
`projects`
- projects.deployments : Es una representación de una implementación de secuencia de comandos. La API proporciona métodos para crear, enumerar, actualizar y borrar implementaciones de proyectos de secuencias de comandos. Usa las implementaciones para que tu secuencia de comandos esté disponible como una app web, un complemento o un archivo ejecutable.
`projects.deployments`
- projects.versions : Es una representación de una versión de proyecto de secuencia de comandos. La API proporciona métodos para crear y leer versiones de proyectos. Usa las versiones para hacer un seguimiento de las diferentes iteraciones de tu proyecto de secuencia de comandos.
`projects.versions`
- processes : Es una representación de la ejecución de una función de secuencia de comandos. La API proporciona métodos para enumerar los procesos existentes y recopilar información sobre ellos, como el tipo y el estado actual. Usa este recurso para supervisar las ejecuciones de secuencias de comandos que se inician con el método scripts.run .
`processes`
`scripts.run`
- scripts : Es el extremo que proporciona métodos para ejecutar de forma remota funciones de Apps Script. Usa este recurso para ejecutar funciones en tu proyecto de secuencia de comandos desde tu aplicación.
`scripts`
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

## Ejemplos de Google Apps Script

### Apps Script

- Página principal
- Google Workspace
- Apps Script
### Automatiza y extiende Google Workspace con código sencillo.
Apps Script es una plataforma de JavaScript basada en la nube y potenciada por Google Drive que te permite integrar y automatizar tareas en los productos de Google.
## Desarrolla soluciones de alta calidad con facilidad
### Automatizaciones
Escriba un código que realice tareas de manera programática en todos los productos de Google. Las automatizaciones se activan mediante menús personalizados, botones, acciones del usuario o una programación basada en el tiempo.
### Funciones personalizadas
Escribe funciones de Hojas de cálculo de Google en Apps Script y llámalas desde tu hoja de cálculo como funciones integradas.
### Complementos
Compila una app que automatice tareas o se conecte a servicios de terceros desde Google Workspace. Comparta su solución con otras personas en Google Workspace Marketplace.
### Apps de chat
Proporciona una interfaz de conversación que permita a los usuarios de Google Chat interactuar con los servicios como si el servicio fuera una persona.
### Potencia tus secuencias de comandos con IA
### Guía de inicio rápido de Vertex AI
### Guía de inicio rápido del agente de ADK
### Guía de inicio rápido del agente A2A
### Analizador de mensajes de Gmail
### Agente de Viajes Concierge
### Función personalizada de verificador de datos
### Guía de inicio rápido del agente de ADK
### Guía de inicio rápido del agente A2A
### Guía de inicio rápido del agente de A2UI
### Servicio de Vertex AI
### Inicio rápido del agente de Gemini Enterprise
### Agentes de Gemini Enterprise
### Agentes de Vertex AI
### Crea un complemento de Gmail con vibe coding
### Notas de la versión
### Asistencia
### API de REST
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-03-03 (UTC)

---

### Ejemplos

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Ejemplos de Google Apps Script Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Explora muestras y soluciones de Apps Script que te muestran cómo automatizar tareas, extender las interfaces de usuario de Google Workspace y realizar integraciones en Google y servicios externos.
Consulta las muestras por caso de uso, productos destacados de Google y tipo :
Filtrar por Casos de uso Seleccionar todo Borrar todo Automatización Administración de proyectos de Apps Script Análisis de datos Correo electrónico y comunicación Administración de empleados Planificación de eventos Administración de archivos Administración del tiempo Productos Seleccionar todo Borrar todo Gemini Gmail Consola del administrador de Google Calendario de Google Google Chat Documentos de Google Google Drive Formularios de Google Google Maps Hojas de cálculo de Google Presentaciones de Google VertexAi YouTube expand_less Menos expand_more Más Tipo de muestra Seleccionar todo Borrar todo Guía de inicio rápido Instructivo Codelab GitHub Restablecer Listo filter_list Filtros Planifica viajes con un agente de IA accesible en todo Google Workspace Nivel de programación: Avanzado Duración: 45 minutos Tipo de proyecto: Complemento de Google Workspace que extiende Chat, Gmail, Calendario, Drive y Documentos, Hojas de cálculo y Presentaciones. En este instructivo, se muestra cómo publicar agentes Hojas de cálculo de Google Google Drive Vertex AI Calendario de Google Documentos de Google Presentaciones de Google Gemini Gmail Apps Script Google Workspace Vertex AI Agent Engine Google Chat Complementos de Google Workspace Responde a incidentes con Google Chat, Vertex AI, Apps Script y autenticación de usuarios Respond to incidents in Chat and generate an AI-based summary of the resolution in Docs. Gemini Google Chat Vertex AI Google Workspace Apps Script Consola del administrador Documentos de Google Complementos de Google Workspace Cómo traducir texto en un documento de Documentos de Google En esta guía de inicio rápido, se crea un complemento del Editor de Documentos de Google que traduce el texto seleccionado en un documento. Para usar este ejemplo, debes cumplir con los siguientes requisitos previos: Reemplaza el contenido de cada Documentos de Google Google Workspace Apps Script Enviar correos electrónicos sobre los envíos nuevos de Formularios de Google En esta guía de inicio rápido, se crea un complemento del Editor de Formularios de Google que usa activadores para enviar mensajes de Gmail cuando un usuario responde al formulario. Para usar este ejemplo, debes cumplir con los siguientes Apps Script Formularios de Google Google Workspace Cómo agregar un servicio de conferencias web al Calendario de Google Importante: Este inicio rápido solo es para proveedores de conferencias web. La siguiente guía de inicio rápido del complemento de Google Workspace extiende Calendario de Google para sincronizarlo con un servicio ficticio de conferencias web llamado Google Workspace Apps Script Compila un complemento de Google Workspace con Apps Script En esta guía de inicio rápido, se crea un complemento de Google Workspace que muestra páginas principales, activadores contextuales y cómo conectarse a APIs de terceros. El complemento crea interfaces contextuales y no contextuales en Gmail, Google Drive Google Workspace Apps Script Calendario de Google Gmail Cómo traducir texto desde Presentaciones de Google En esta guía de inicio rápido, se crea un complemento del Editor de Presentaciones de Google que traduce el texto seleccionado en una presentación. Para usar esta muestra, debes cumplir con los siguientes requisitos previos: Reemplaza el contenido de Apps Script Google Workspace Presentaciones de Google Compila una app de Google Chat con Google Apps Script Crea una app de Google Chat con la que puedas enviar mensajes y que responda directamente con la repetición de tus mensajes. En el siguiente diagrama, se muestran la arquitectura y el patrón de mensajería: En el diagrama anterior, un usuario que Google Chat Google Workspace Apps Script Guía de inicio rápido de Google Apps Script Crea una secuencia de comandos de Google Apps Script que realice solicitudes a la API de Google Chat. En las guías de inicio rápido, se explica cómo configurar y ejecutar una app que llama a una API de Google Workspace. En esta guía de inicio rápido, Apps Script Google Workspace Google Chat Programa reuniones desde Google Chat Create Google Calendar events from a Chat space. Apps Script Google Workspace Calendario de Google Google Chat Recopila y administra contactos en Google Chat Help users manage their personal and business contacts by collecting information in card messages and dialogs. Google Workspace Apps Script Google Chat Recibe alertas sobre descuentos en acciones Enumera tus acciones en una hoja de cálculo de Hojas de Google y recibe alertas por correo electrónico si el precio de una acción baja más que su precio de compra. Apps Script Google Workspace Hojas de cálculo de Google Gmail Genera y envía archivos PDF desde Hojas de cálculo de Google Crea y envía PDFs por correo electrónico automáticamente desde Hojas de cálculo de Google con Apps Script. Google Workspace Google Drive Gmail Apps Script Hojas de cálculo de Google Realiza un seguimiento de las vistas y los comentarios de videos de YouTube Hacer un seguimiento del rendimiento de los videos de YouTube en una hoja de cálculo de Hojas de cálculo de Google y recibir notificaciones de Gmail sobre los comentarios nuevos YouTube Gmail Apps Script Hojas de cálculo de Google Google Workspace Propague el calendario de vacaciones del equipo Automatiza un calendario de vacaciones compartido del equipo sincronizando los eventos de ausencia de los calendarios de Google individuales con Google Apps Script. Google Workspace Grupos de Google Apps Script Calendario de Google Crea un corchete de torneo Aprende a usar Apps Script para crear un cuadro de torneo de eliminación simple para hasta 64 participantes. Apps Script Hojas de cálculo de Google Google Workspace Crea un registro para un sitio externo Automatiza los registros de actividades fuera de la oficina creando un formulario para las preferencias de los empleados y relacionándolos con un programa de actividades. Hojas de cálculo de Google Google Workspace Formularios de Google Apps Script Verifica la exactitud de las declaraciones con un agente de IA del ADK y un modelo de Gemini Aprende a crear una función personalizada de Hojas de cálculo de Google para verificar la exactitud de las declaraciones con un agente de Vertex AI y un modelo de Gemini. Vertex AI Google Workspace Hojas de cálculo de Google Apps Script Gemini Complementos de Google Workspace Enviar contenido seleccionado Aprende a usar Formularios de Google para permitir que los usuarios seleccionen contenido y recibirlo automáticamente por correo electrónico. Gmail Documentos de Google Formularios de Google Hojas de cálculo de Google Apps Script Google Workspace Guía de inicio rápido de las funciones personalizadas Crea funciones personalizadas en Google Apps Script y úsalas en Hojas de cálculo de Google como si fueran funciones integradas. Apps Script Hojas de cálculo de Google Google Workspace Complementos de Google Workspace Registra tiempos y actividades en el Calendario de Google y Hojas de cálculo de Google Aprende a hacer un seguimiento del tiempo dedicado a un proyecto en el Calendario de Google y a sincronizarlo con Hojas de cálculo de Google para crear hojas de horas. Apps Script Calendario de Google Hojas de cálculo de Google Google Workspace Compartir recursos con empleados nuevos Automatiza la incorporación de empleados nuevos a un Grupo de Google con Formularios de Google y Apps Script para compartir recursos. Hojas de cálculo de Google Documentos de Google Apps Script Grupos de Google Google Workspace Gmail Formularios de Google Analiza la opinión de los comentarios con la API de Google Cloud Natural Language Aprende a analizar datos de texto y opiniones a gran escala en Hojas de cálculo de Google con Apps Script y la API de Google Cloud Natural Language. Google Workspace Apps Script Hojas de cálculo de Google Guía de inicio rápido: Genera texto con Vertex AI En esta página, se explica cómo usar el servicio avanzado de Vertex AI de Google Apps Script para darle instrucciones al modelo Gemini 2.5 Flash para que genere texto. Para obtener más información sobre el servicio avanzado de Vertex AI, consulta la Apps Script Vertex AI Google Workspace Calcula un descuento de precios por niveles Esta función personalizada facilita el cálculo de los importes de descuento para un sistema de precios por niveles en Hojas de cálculo de Google. Complementos de Google Workspace Google Workspace Hojas de cálculo de Google Apps Script Sube archivos a Google Drive desde Formularios de Google Aprende a usar Apps Script para subir y organizar archivos en Google Drive desde Formularios de Google. Formularios de Google Google Workspace Google Drive Apps Script Calcula la distancia en automóvil y convierte los metros a millas Aprende a usar funciones personalizadas para calcular la distancia en automóvil, convertir metros a millas y agregar instrucciones paso a paso a una hoja. Apps Script Complementos de Google Workspace Hojas de cálculo de Google Google Workspace Google Maps Envía certificados de agradecimiento personalizados a los empleados Automatiza la creación y el envío de certificados personalizados de reconocimiento para empleados combinando datos de Hojas de cálculo de Google con una plantilla de Presentaciones de Google y enviándolos con Gmail. Hojas de cálculo de Google Gmail Presentaciones de Google Google Drive Google Workspace Apps Script Resumir datos de varias hojas Usa una función personalizada para resumir datos con estructuras similares de varias hojas en una hoja de cálculo de Google. Apps Script Google Workspace Hojas de cálculo de Google Complementos de Google Workspace Guía de inicio rápido de la biblioteca Crea una biblioteca de Apps Script que puedas usar para quitar filas duplicadas en los datos de hojas de cálculo. Google Workspace Hojas de cálculo de Google Apps Script expand_less Menos Más expand_more
Filtrar por
### Planifica viajes con un agente de IA accesible en todo Google Workspace
Nivel de programación: Avanzado Duración: 45 minutos Tipo de proyecto: Complemento de Google Workspace que extiende Chat, Gmail, Calendario, Drive y Documentos, Hojas de cálculo y Presentaciones. En este instructivo, se muestra cómo publicar agentes
- Hojas de cálculo de Google
- Google Drive
- Vertex AI
- Calendario de Google
- Documentos de Google
- Presentaciones de Google
- Gemini
- Gmail
- Apps Script
- Google Workspace
- Vertex AI Agent Engine
- Google Chat
- Complementos de Google Workspace
### Responde a incidentes con Google Chat, Vertex AI, Apps Script y autenticación de usuarios
Respond to incidents in Chat and generate an AI-based summary of the resolution in Docs.
- Gemini
- Google Chat
- Vertex AI
- Google Workspace
- Apps Script
- Consola del administrador
- Documentos de Google
- Complementos de Google Workspace
### Cómo traducir texto en un documento de Documentos de Google
En esta guía de inicio rápido, se crea un complemento del Editor de Documentos de Google que traduce el texto seleccionado en un documento. Para usar este ejemplo, debes cumplir con los siguientes requisitos previos: Reemplaza el contenido de cada
- Documentos de Google
- Google Workspace
- Apps Script
### Enviar correos electrónicos sobre los envíos nuevos de Formularios de Google
En esta guía de inicio rápido, se crea un complemento del Editor de Formularios de Google que usa activadores para enviar mensajes de Gmail cuando un usuario responde al formulario. Para usar este ejemplo, debes cumplir con los siguientes
- Apps Script
- Formularios de Google
- Google Workspace
### Cómo agregar un servicio de conferencias web al Calendario de Google
Importante: Este inicio rápido solo es para proveedores de conferencias web. La siguiente guía de inicio rápido del complemento de Google Workspace extiende Calendario de Google para sincronizarlo con un servicio ficticio de conferencias web llamado
- Google Workspace
- Apps Script
### Compila un complemento de Google Workspace con Apps Script
En esta guía de inicio rápido, se crea un complemento de Google Workspace que muestra páginas principales, activadores contextuales y cómo conectarse a APIs de terceros. El complemento crea interfaces contextuales y no contextuales en Gmail,
- Google Drive
- Google Workspace
- Apps Script
- Calendario de Google
- Gmail
### Cómo traducir texto desde Presentaciones de Google
En esta guía de inicio rápido, se crea un complemento del Editor de Presentaciones de Google que traduce el texto seleccionado en una presentación. Para usar esta muestra, debes cumplir con los siguientes requisitos previos: Reemplaza el contenido de
- Apps Script
- Google Workspace
- Presentaciones de Google
### Compila una app de Google Chat con Google Apps Script
Crea una app de Google Chat con la que puedas enviar mensajes y que responda directamente con la repetición de tus mensajes. En el siguiente diagrama, se muestran la arquitectura y el patrón de mensajería: En el diagrama anterior, un usuario que
- Google Chat
- Google Workspace
- Apps Script
### Guía de inicio rápido de Google Apps Script
Crea una secuencia de comandos de Google Apps Script que realice solicitudes a la API de Google Chat. En las guías de inicio rápido, se explica cómo configurar y ejecutar una app que llama a una API de Google Workspace. En esta guía de inicio rápido,
- Apps Script
- Google Workspace
- Google Chat
### Programa reuniones desde Google Chat
Create Google Calendar events from a Chat space.
- Apps Script
- Google Workspace
- Calendario de Google
- Google Chat
### Recopila y administra contactos en Google Chat
Help users manage their personal and business contacts by collecting information in card messages and dialogs.
- Google Workspace
- Apps Script
- Google Chat
### Recibe alertas sobre descuentos en acciones
Enumera tus acciones en una hoja de cálculo de Hojas de Google y recibe alertas por correo electrónico si el precio de una acción baja más que su precio de compra.
- Apps Script
- Google Workspace
- Hojas de cálculo de Google
- Gmail
### Genera y envía archivos PDF desde Hojas de cálculo de Google
Crea y envía PDFs por correo electrónico automáticamente desde Hojas de cálculo de Google con Apps Script.
- Google Workspace
- Google Drive
- Gmail
- Apps Script
- Hojas de cálculo de Google
### Realiza un seguimiento de las vistas y los comentarios de videos de YouTube
Hacer un seguimiento del rendimiento de los videos de YouTube en una hoja de cálculo de Hojas de cálculo de Google y recibir notificaciones de Gmail sobre los comentarios nuevos
- YouTube
- Gmail
- Apps Script
- Hojas de cálculo de Google
- Google Workspace
### Propague el calendario de vacaciones del equipo
Automatiza un calendario de vacaciones compartido del equipo sincronizando los eventos de ausencia de los calendarios de Google individuales con Google Apps Script.
- Google Workspace
- Grupos de Google
- Apps Script
- Calendario de Google
### Crea un corchete de torneo
Aprende a usar Apps Script para crear un cuadro de torneo de eliminación simple para hasta 64 participantes.
- Apps Script
- Hojas de cálculo de Google
- Google Workspace
### Crea un registro para un sitio externo
Automatiza los registros de actividades fuera de la oficina creando un formulario para las preferencias de los empleados y relacionándolos con un programa de actividades.
- Hojas de cálculo de Google
- Google Workspace
- Formularios de Google
- Apps Script
### Verifica la exactitud de las declaraciones con un agente de IA del ADK y un modelo de Gemini
Aprende a crear una función personalizada de Hojas de cálculo de Google para verificar la exactitud de las declaraciones con un agente de Vertex AI y un modelo de Gemini.
- Vertex AI
- Google Workspace
- Hojas de cálculo de Google
- Apps Script
- Gemini
- Complementos de Google Workspace
### Enviar contenido seleccionado
Aprende a usar Formularios de Google para permitir que los usuarios seleccionen contenido y recibirlo automáticamente por correo electrónico.
- Gmail
- Documentos de Google
- Formularios de Google
- Hojas de cálculo de Google
- Apps Script
- Google Workspace
### Guía de inicio rápido de las funciones personalizadas
Crea funciones personalizadas en Google Apps Script y úsalas en Hojas de cálculo de Google como si fueran funciones integradas.
- Apps Script
- Hojas de cálculo de Google
- Google Workspace
- Complementos de Google Workspace
### Registra tiempos y actividades en el Calendario de Google y Hojas de cálculo de Google
Aprende a hacer un seguimiento del tiempo dedicado a un proyecto en el Calendario de Google y a sincronizarlo con Hojas de cálculo de Google para crear hojas de horas.
- Apps Script
- Calendario de Google
- Hojas de cálculo de Google
- Google Workspace
### Compartir recursos con empleados nuevos
Automatiza la incorporación de empleados nuevos a un Grupo de Google con Formularios de Google y Apps Script para compartir recursos.
- Hojas de cálculo de Google
- Documentos de Google
- Apps Script
- Grupos de Google
- Google Workspace
- Gmail
- Formularios de Google
### Analiza la opinión de los comentarios con la API de Google Cloud Natural Language
Aprende a analizar datos de texto y opiniones a gran escala en Hojas de cálculo de Google con Apps Script y la API de Google Cloud Natural Language.
- Google Workspace
- Apps Script
- Hojas de cálculo de Google
### Guía de inicio rápido: Genera texto con Vertex AI
En esta página, se explica cómo usar el servicio avanzado de Vertex AI de Google Apps Script para darle instrucciones al modelo Gemini 2.5 Flash para que genere texto. Para obtener más información sobre el servicio avanzado de Vertex AI, consulta la
- Apps Script
- Vertex AI
- Google Workspace
### Calcula un descuento de precios por niveles
Esta función personalizada facilita el cálculo de los importes de descuento para un sistema de precios por niveles en Hojas de cálculo de Google.
- Complementos de Google Workspace
- Google Workspace
- Hojas de cálculo de Google
- Apps Script
### Sube archivos a Google Drive desde Formularios de Google
Aprende a usar Apps Script para subir y organizar archivos en Google Drive desde Formularios de Google.
- Formularios de Google
- Google Workspace
- Google Drive
- Apps Script
### Calcula la distancia en automóvil y convierte los metros a millas
Aprende a usar funciones personalizadas para calcular la distancia en automóvil, convertir metros a millas y agregar instrucciones paso a paso a una hoja.
- Apps Script
- Complementos de Google Workspace
- Hojas de cálculo de Google
- Google Workspace
- Google Maps
### Envía certificados de agradecimiento personalizados a los empleados
Automatiza la creación y el envío de certificados personalizados de reconocimiento para empleados combinando datos de Hojas de cálculo de Google con una plantilla de Presentaciones de Google y enviándolos con Gmail.
- Hojas de cálculo de Google
- Gmail
- Presentaciones de Google
- Google Drive
- Google Workspace
- Apps Script
### Resumir datos de varias hojas
Usa una función personalizada para resumir datos con estructuras similares de varias hojas en una hoja de cálculo de Google.
- Apps Script
- Google Workspace
- Hojas de cálculo de Google
- Complementos de Google Workspace
### Guía de inicio rápido de la biblioteca
Crea una biblioteca de Apps Script que puedas usar para quitar filas duplicadas en los datos de hojas de cálculo.
- Google Workspace
- Hojas de cálculo de Google
- Apps Script
### Acerca de los tipos de muestras
A continuación, se proporciona una explicación de cada tipo de muestra:
Las muestras de inicio rápido ofrecen muestras de código rápidas de prueba de concepto para que comiences a trabajar con Apps Script en menos de cinco minutos. Las guías de inicio rápido están disponibles para la mayoría de los tipos de proyectos de Apps Script.
Encuentra guías de inicio rápido organizadas por tipo de proyecto a la izquierda en Samples by project type o prueba esta automatización sencilla que crea un documento de Google y te envía un vínculo a él por correo electrónico.
Las muestras de soluciones son proyectos de Apps Script completamente funcionales. Las soluciones abordan problemas comerciales realistas y muestran cómo puedes automatizar flujos de trabajo en Google Workspace. A menudo, puedes implementar soluciones sin necesidad de editar o actualizar el código.
Encuentra soluciones organizadas por tipo de proyecto a la izquierda, en Samples by project type o prueba esta solución popular de combinación de correo electrónico .
Los codelabs son instructivos técnicos interactivos paso a paso. Combinan explicaciones, código de muestra de prácticas recomendadas y ejercicios de código. Los codelabs están disponibles para la mayoría de los productos para desarrolladores de Google y se publican en el catálogo de codelabs .
Encontrarás codelabs específicos de Apps Script a la izquierda, en Codelabs .
### Explora muestras de código de Apps Script en GitHub
También puedes encontrar muestras de Apps Script en GitHub . Puedes bifurcar estos repositorios y usar el código como referencia para tus propios proyectos.
## Explora videos de Apps Script
Explora el contenido del canal de YouTube de Google Workspace Developers:
YouTube Get started with Vertex AI in Apps Script Use Apps Script's Vertex AI advanced service to call the Vertex AI API and prompt AI models to generate text, images, and more. #appsscript #vertexAI #Gemini Google Workspace Developers 27 de enero de 2026 YouTube How to Use Gemini 2.5 Flash in Apps Script with Vertex AI Learn how to get started with the Vertex AI advanced service in Apps Script. This video shows you how to set up and use the service to prompt the Gemini 2.5 Flash model to generate text. For more details, visit our documentation: Google Workspace Developers 21 de enero de 2026 YouTube Automate Your Tasks in 5 Minutes: Apps Script + Gemini for Beginners In this video, you will see how you can automate a task within Google Workspace with Gemini without having to write a single line of code. Subscribe to our YouTube channel: https://www.youtube.com/@googleworkspacedevs/ Subscribe to our Google Google Workspace Developers 15 de enero de 2026 YouTube Granular OAuth consent for web apps and Workspace add-ons Soon, published web apps and Google Workspace add-ons powered by Apps Script will also present users with this more granular consent screen when requesting an OAuth grant. #AppsScript #googleworkspaceplatform #googleworkspacedevelopernews Google Workspace Developers 9 de diciembre de 2025 YouTube Generate Apps Script code using Google AI Studio Check out how you can use Google AI Studio to write Apps Script code for you. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform Google Workspace Developers 3 de octubre de 2025 YouTube Use the Apps Script project dashboard Check out how you can use the Apps Script dashboard to manage your projects. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform Google Workspace Developers 29 de septiembre de 2025 YouTube Simplify your code using Apps Script libraries and services Check out how you can use Apps Script Libraries and Services to code more efficiently. 🤩 Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform Google Workspace Developers 26 de agosto de 2025 YouTube Format and fix code with the Apps Script command palette Check out how you can use Apps Script’s command palette to quickly edit your code. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform Google Workspace Developers 19 de agosto de 2025 YouTube Jump start your Apps Script project with a starter template See how you can use starter templates to speed up your Apps Script project. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform Google Workspace Developers 14 de agosto de 2025 YouTube Google Workspace Developer Summit 2025 📣 We are happy to announce the dates and locations for the Google Workspace Developer Summit 2025. → Sunnyvale, USA: October 8-9, 2025 → Paris, France: October 21-22, 2025 Want to join us? Please fill out this form: https://goo.gle/ws-dev-summit-25 Google Workspace Developers 29 de mayo de 2025 YouTube AI mocktail Bar demo explained 🍸 At Google Cloud Summit Benelux in Amsterdam, you could have AI generate a mocktail for you based on the image you uploaded. Hear Luc de Jager explain how this fun demo works. #GoogleCloudSummit #AppSheet #AppsScript Google Workspace Developers 26 de mayo de 2025 YouTube Use Apps Script’s Form Service to publish forms You can now use Apps Script’s Forms Service to publish forms, and to have granular control over who can respond to forms. #googleworkspaceplatform #googleworkspacedevelopernews #appsscript Google Workspace Developers 22 de mayo de 2025 expand_less Menos Más expand_more
YouTube
### Get started with Vertex AI in Apps Script
Use Apps Script's Vertex AI advanced service to call the Vertex AI API and prompt AI models to generate text, images, and more. #appsscript #vertexAI #Gemini
Google Workspace Developers
27 de enero de 2026
YouTube
### How to Use Gemini 2.5 Flash in Apps Script with Vertex AI
Learn how to get started with the Vertex AI advanced service in Apps Script. This video shows you how to set up and use the service to prompt the Gemini 2.5 Flash model to generate text. For more details, visit our documentation:
Google Workspace Developers
21 de enero de 2026
YouTube
### Automate Your Tasks in 5 Minutes: Apps Script + Gemini for Beginners
In this video, you will see how you can automate a task within Google Workspace with Gemini without having to write a single line of code. Subscribe to our YouTube channel: https://www.youtube.com/@googleworkspacedevs/ Subscribe to our Google
Google Workspace Developers
15 de enero de 2026
YouTube
### Granular OAuth consent for web apps and Workspace add-ons
Soon, published web apps and Google Workspace add-ons powered by Apps Script will also present users with this more granular consent screen when requesting an OAuth grant. #AppsScript #googleworkspaceplatform #googleworkspacedevelopernews
Google Workspace Developers
9 de diciembre de 2025
YouTube
### Generate Apps Script code using Google AI Studio
Check out how you can use Google AI Studio to write Apps Script code for you. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform
Google Workspace Developers
3 de octubre de 2025
YouTube
### Use the Apps Script project dashboard
Check out how you can use the Apps Script dashboard to manage your projects. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform
Google Workspace Developers
29 de septiembre de 2025
YouTube
### Simplify your code using Apps Script libraries and services
Check out how you can use Apps Script Libraries and Services to code more efficiently. 🤩 Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform
Google Workspace Developers
26 de agosto de 2025
YouTube
### Format and fix code with the Apps Script command palette
Check out how you can use Apps Script’s command palette to quickly edit your code. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform
Google Workspace Developers
19 de agosto de 2025
YouTube
### Jump start your Apps Script project with a starter template
See how you can use starter templates to speed up your Apps Script project. Check out the documentation ➡️ https://goo.gle/41FutZS #googleappscript #appsscript #googleworkspaceplatform
Google Workspace Developers
14 de agosto de 2025
YouTube
### Google Workspace Developer Summit 2025 📣
We are happy to announce the dates and locations for the Google Workspace Developer Summit 2025. → Sunnyvale, USA: October 8-9, 2025 → Paris, France: October 21-22, 2025 Want to join us? Please fill out this form: https://goo.gle/ws-dev-summit-25
Google Workspace Developers
29 de mayo de 2025
YouTube
### AI mocktail Bar demo explained 🍸
At Google Cloud Summit Benelux in Amsterdam, you could have AI generate a mocktail for you based on the image you uploaded. Hear Luc de Jager explain how this fun demo works. #GoogleCloudSummit #AppSheet #AppsScript
Google Workspace Developers
26 de mayo de 2025
YouTube
### Use Apps Script’s Form Service to publish forms
You can now use Apps Script’s Forms Service to publish forms, and to have granular control over who can respond to forms. #googleworkspaceplatform #googleworkspacedevelopernews #appsscript
Google Workspace Developers
22 de mayo de 2025
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Recibe alertas sobre descuentos en acciones

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Recibe alertas sobre descuentos en acciones Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 5 minutos Tipo de proyecto : Automatización con un activador basado en el tiempo
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Si compras una acción y su valor disminuye, puedes venderla, comprar otra y reclamar una deducción fiscal. Esto se conoce como compensación de pérdidas fiscales. Enumera tus acciones en una hoja de cálculo de Google Sheets y recibe alertas por correo electrónico si el precio de una acción cae por debajo de su precio de compra.
### Cómo funciona
La hoja de cálculo usa la función integrada de Google Finance en Hojas de cálculo para obtener los precios actuales de las acciones. La secuencia de comandos compara el precio de compra de cada acción que aparece en la lista con su precio actual. Luego, te envía por correo electrónico una lista de las acciones que cayeron por debajo de su precio de compra. Puedes configurar la secuencia de comandos para que se ejecute con la frecuencia que desees.
### Servicios de Apps Script
En esta solución, se usan los siguientes servicios:
- Servicio de hojas de cálculo : Recorre en bucle cada acción que aparece en la lista y compara el precio de la acción con el precio de compra.
- Servicio de Gmail : Crea y envía un correo electrónico de las acciones que cayeron por debajo de su precio de compra.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
- Haz clic en el siguiente botón para crear una copia de la hoja de cálculo de muestra de Alertas de compensación de pérdidas fiscales . El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo. Crear una copia
Haz clic en el siguiente botón para crear una copia de la hoja de cálculo de muestra de Alertas de compensación de pérdidas fiscales . El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo.
Crear una copia
- En la hoja de cálculo copiada, actualiza la hoja con tu propia información de stock o usa los datos de prueba proporcionados.
En la hoja de cálculo copiada, actualiza la hoja con tu propia información de stock o usa los datos de prueba proporcionados.
## Ejecuta la secuencia de comandos:
- En la hoja de cálculo copiada, selecciona Extensiones > Apps Script .
- En el menú desplegable de funciones, selecciona checkLosses .
- Haz clic en Ejecutar .
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
- Revisa tu correo electrónico para ver una lista de las acciones que cayeron por debajo de su precio de compra. Si no recibiste un correo electrónico, verifica si alguno de los precios de las acciones de tu lista es inferior a su precio de compra.
### Crea un activador basado en el tiempo
- Regresa al proyecto de secuencias de comandos.
- A la izquierda, haz clic en Activadores alarm .
- En la esquina inferior derecha, haz clic en Agregar activador .
- En Elige qué función ejecutar , asegúrate de que esté seleccionada checkLosses .
- En Seleccionar la fuente del evento , selecciona Basado en el tiempo .
- Configura la frecuencia con la que deseas que se ejecute la secuencia de comandos y haz clic en Guardar .
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/automations/tax-loss-harvest-alerts



/*


Copyright 2022 Google LLC



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



/**


 * Checks for losses in the sheet.


 */


function
 
checkLosses
()
 
{


  
// Pulls data from the spreadsheet


  
const
 
sheet
 
=


    
SpreadsheetApp
.
getActiveSpreadsheet
().
getSheetByName
(
"Calculations"
);


  
const
 
source
 
=
 
sheet
.
getRange
(
"A:G"
);


  
const
 
data
 
=
 
source
.
getValues
();



  
//Prepares the email alert content


  
let
 
message
 
=
 
"Stocks: <br><br>"
;



  
let
 
send_message
 
=
 
false
;



  
console
.
log
(
"starting loop"
);



  
//Loops through the cells in the spreadsheet to find cells where the stock fell below purchase price


  
let
 
n
 
=
 
0
;


  
for
 
(
const
 
i
 
in
 
data
)
 
{


    
//Skips the first row


    
if
 
(
n
++
 
===
 
0
)
 
continue
;



    
//Loads the current row


    
const
 
row
 
=
 
data
[
i
];



    
console
.
log
(
row
[
1
]);


    
console
.
log
(
row
[
6
]);



    
//Once at the end of the list, exits the loop


    
if
 
(
row
[
1
]
 
===
 
""
)
 
break
;



    
//If value is below purchase price, adds stock ticker and difference to list of tax loss opportunities


    
if
 
(
row
[
6
]
 < 
0
)
 
{


      
message
 
+=
 
`
${
row
[
1
]
}
: 
${
(
Number
.
parseFloat
(
row
[
6
].
toString
())
 
*
 
100
).
toFixed
(
2
).
toString
()
}
%<br>`
;


      
send_message
 
=
 
true
;


    
}


  
}


  
if
 
(
!
send_message
)
 
return
;



  
MailApp
.
sendEmail
({


    
to
:
 
SpreadsheetApp
.
getActiveSpreadsheet
().
getOwner
().
getEmail
(),


    
subject
:
 
"Tax-loss harvest"
,


    
htmlBody
:
 
message
,


  
});


}
```
## Colaboradores
Jeremy Glassenberg, asesor de estrategia de productos y plataformas, creó esta muestra. Encuentra a Jeremy en Twitter: @jglassenberg .
Google mantiene esta muestra con la ayuda de los Google Developer Experts.
## Próximos pasos
- Activadores basados en el tiempo
- Extender Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Genera y envía archivos PDF desde Hojas de cálculo de Google

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Genera y envía archivos PDF desde Hojas de cálculo de Google Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 15 minutos Tipo de proyecto : Automatización con un menú personalizado
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Crea automáticamente archivos PDF con información de hojas en una hoja de cálculo de Hojas de cálculo. Una vez que se generan los archivos PDF, puedes enviarlos por correo electrónico directamente desde Hojas de cálculo. Esta solución se centra en la creación de facturas personalizadas, pero puedes actualizar la plantilla y la secuencia de comandos para que se adapten a tus necesidades.
### Cómo funciona
La secuencia de comandos usa la hoja Invoice template como plantilla para generar archivos PDF. La información se obtiene de las otras hojas para completar celdas específicas en la plantilla. Para enviar los archivos PDF por correo electrónico, la secuencia de comandos itera a través de la hoja Invoices para obtener el vínculo del PDF y la dirección de correo electrónico asociada. La secuencia de comandos crea un asunto y un cuerpo de correo electrónico genéricos, y adjunta el PDF antes de enviarlo.
### Servicios de Apps Script
Esta solución usa los siguientes servicios:
- Servicio de hojas de cálculo : Proporciona toda la información para generar archivos PDF de facturas y crear el correo electrónico. Borra los datos de la plantilla cuando un usuario hace clic en Reset template en el menú personalizado.
- Servicio de utilidades : Pausa la secuencia de comandos con el método sleep mientras itera a través de cada cliente para garantizar que se agregue la información correcta a cada factura.
`sleep`
- Servicio de recuperación de URL : Exporta la hoja Invoice template a un PDF.
- Servicio de secuencias de comandos : Autoriza al servicio de recuperación de URL para acceder a la hoja de cálculo.
- Servicio de Google Drive : Crea una carpeta para los archivos PDF exportados y adjunta los archivos PDF a los correos electrónicos.
- Servicio de Gmail : Compila y envía los correos electrónicos.
## Requisitos previos
Para usar esta muestra, debes cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
- Haz clic en el siguiente botón para copiar la hoja de cálculo Generate and send PDFs from Sheets . El proyecto de Apps Script para esta solución está adjunto a la hoja de cálculo. Crear una copia
Haz clic en el siguiente botón para copiar la hoja de cálculo Generate and send PDFs from Sheets . El proyecto de Apps Script para esta solución está adjunto a la hoja de cálculo.
Crear una copia
- Haz clic en Extensiones > Apps Script .
Haz clic en Extensiones > Apps Script .
- En el archivo Code.gs , actualiza las siguientes variables: Establece EMAIL_OVERRIDE en true . Establece EMAIL_ADDRESS_OVERRIDE en tu dirección de correo electrónico.
En el archivo Code.gs , actualiza las siguientes variables:
`Code.gs`
- Establece EMAIL_OVERRIDE en true .
`EMAIL_OVERRIDE`
`true`
- Establece EMAIL_ADDRESS_OVERRIDE en tu dirección de correo electrónico.
`EMAIL_ADDRESS_OVERRIDE`
- Haz clic en Guardar .
Haz clic en Guardar .
## Ejecuta la secuencia de comandos
- Vuelve a la hoja de cálculo y haz clic en Generate and send PDFs > Process invoices .
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
- Vuelve a hacer clic en Generate and send PDFs > Process invoices .
- Para ver los archivos PDF, cambia a la hoja Invoices y haz clic en los vínculos de la columna Invoice link .
- Haz clic en Generate and send PDFs > Send emails .
- Revisa tu correo electrónico para revisar los correos electrónicos y los archivos PDF adjuntos. Como estableciste EMAIL_OVERRIDE en true en la sección anterior, la secuencia de comandos envía todos los correos electrónicos a la dirección de correo electrónico que especificaste para EMAIL_ADDRESS_OVERRIDE . Si estableces EMAIL_OVERRIDE en false , la secuencia de comandos envía los correos electrónicos a las direcciones de correo electrónico que aparecen en la hoja Customers .
`EMAIL_OVERRIDE`
`true`
`EMAIL_ADDRESS_OVERRIDE`
`EMAIL_OVERRIDE`
`false`
- (Opcional) Para borrar los datos de la hoja Invoice template , haz clic en Generate and send PDFs > Reset template .
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver el código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/automations/generate-pdfs



/*


Copyright 2022 Google LLC



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



// TODO: To test this solution, set EMAIL_OVERRIDE to true and set EMAIL_ADDRESS_OVERRIDE to your email address.


const
 
EMAIL_OVERRIDE
 
=
 
false
;


const
 
EMAIL_ADDRESS_OVERRIDE
 
=
 
"test@example.com"
;



// Application constants


const
 
APP_TITLE
 
=
 
"Generate and send PDFs"
;


const
 
OUTPUT_FOLDER_NAME
 
=
 
"Customer PDFs"
;


const
 
DUE_DATE_NUM_DAYS
 
=
 
15
;



// Sheet name constants. Update if you change the names of the sheets.


const
 
CUSTOMERS_SHEET_NAME
 
=
 
"Customers"
;


const
 
PRODUCTS_SHEET_NAME
 
=
 
"Products"
;


const
 
TRANSACTIONS_SHEET_NAME
 
=
 
"Transactions"
;


const
 
INVOICES_SHEET_NAME
 
=
 
"Invoices"
;


const
 
INVOICE_TEMPLATE_SHEET_NAME
 
=
 
"Invoice Template"
;



// Email constants


const
 
EMAIL_SUBJECT
 
=
 
"Invoice Notification"
;


const
 
EMAIL_BODY
 
=
 
"Hello!\rPlease see the attached PDF document."
;



/**


 * Iterates through the worksheet data populating the template sheet with


 * customer data, then saves each instance as a PDF document.


 *


 * Called by user via custom menu item.


 */


function
 
processDocuments
()
 
{


  
const
 
ss
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
();


  
const
 
customersSheet
 
=
 
ss
.
getSheetByName
(
CUSTOMERS_SHEET_NAME
);


  
const
 
productsSheet
 
=
 
ss
.
getSheetByName
(
PRODUCTS_SHEET_NAME
);


  
const
 
transactionsSheet
 
=
 
ss
.
getSheetByName
(
TRANSACTIONS_SHEET_NAME
);


  
const
 
invoicesSheet
 
=
 
ss
.
getSheetByName
(
INVOICES_SHEET_NAME
);


  
const
 
invoiceTemplateSheet
 
=
 
ss
.
getSheetByName
(
INVOICE_TEMPLATE_SHEET_NAME
);



  
// Gets data from the storage sheets as objects.


  
const
 
customers
 
=
 
dataRangeToObject
(
customersSheet
);


  
const
 
products
 
=
 
dataRangeToObject
(
productsSheet
);


  
const
 
transactions
 
=
 
dataRangeToObject
(
transactionsSheet
);



  
ss
.
toast
(
"Creating Invoices"
,
 
APP_TITLE
,
 
1
);


  
const
 
invoices
 
=
 
[];



  
// Iterates for each customer calling createInvoiceForCustomer routine.


  
for
 
(
const
 
customer
 
of
 
customers
)
 
{


    
ss
.
toast
(
`Creating Invoice for 
${
customer
.
customer_name
}
`
,
 
APP_TITLE
,
 
1
);


    
const
 
invoice
 
=
 
createInvoiceForCustomer
(


      
customer
,


      
products
,


      
transactions
,


      
invoiceTemplateSheet
,


      
ss
.
getId
(),


    
);


    
invoices
.
push
(
invoice
);


  
}


  
// Writes invoices data to the sheet.


  
invoicesSheet


    
.
getRange
(
2
,
 
1
,
 
invoices
.
length
,
 
invoices
[
0
].
length
)


    
.
setValues
(
invoices
);


}



/**


 * Processes each customer instance with passed in data parameters.


 *


 * @param {object} customer - Object for the customer


 * @param {object} products - Object for all the products


 * @param {object} transactions - Object for all the transactions


 * @param {object} invoiceTemplateSheet - Object for the invoice template sheet


 * @param {string} ssId - Google Sheet ID


 * Return {array} of instance customer invoice data


 */


function
 
createInvoiceForCustomer
(


  
customer
,


  
products
,


  
transactions
,


  
templateSheet
,


  
ssId
,


)
 
{


  
const
 
customerTransactions
 
=
 
transactions
.
filter
(


    
(
transaction
)
 
=
>
 
transaction
.
customer_name
 
===
 
customer
.
customer_name
,


  
);



  
// Clears existing data from the template.


  
clearTemplateSheet
();



  
const
 
lineItems
 
=
 
[];


  
let
 
totalAmount
 
=
 
0
;


  
for
 
(
const
 
lineItem
 
of
 
customerTransactions
)
 
{


    
const
 
lineItemProduct
 
=
 
products
.
filter
(


      
(
product
)
 
=
>
 
product
.
sku_name
 
===
 
lineItem
.
sku
,


    
)[
0
];


    
const
 
qty
 
=
 
Number
.
parseInt
(
lineItem
.
licenses
);


    
const
 
price
 
=
 
Number
.
parseFloat
(
lineItemProduct
.
price
).
toFixed
(
2
);


    
const
 
amount
 
=
 
Number
.
parseFloat
(
qty
 
*
 
price
).
toFixed
(
2
);


    
lineItems
.
push
([


      
lineItemProduct
.
sku_name
,


      
lineItemProduct
.
sku_description
,


      
""
,


      
qty
,


      
price
,


      
amount
,


    
]);


    
totalAmount
 
+=
 
Number
.
parseFloat
(
amount
);


  
}



  
// Generates a random invoice number. You can replace with your own document ID method.


  
const
 
invoiceNumber
 
=
 
Math
.
floor
(
100000
 
+
 
Math
.
random
()
 
*
 
900000
);



  
// Calulates dates.


  
const
 
todaysDate
 
=
 
new
 
Date
().
toDateString
();


  
const
 
dueDate
 
=
 
new
 
Date
(


    
Date
.
now
()
 
+
 
1000
 
*
 
60
 
*
 
60
 
*
 
24
 
*
 
DUE_DATE_NUM_DAYS
,


  
).
toDateString
();



  
// Sets values in the template.


  
templateSheet
.
getRange
(
"B10"
).
setValue
(
customer
.
customer_name
);


  
templateSheet
.
getRange
(
"B11"
).
setValue
(
customer
.
address
);


  
templateSheet
.
getRange
(
"F10"
).
setValue
(
invoiceNumber
);


  
templateSheet
.
getRange
(
"F12"
).
setValue
(
todaysDate
);


  
templateSheet
.
getRange
(
"F14"
).
setValue
(
dueDate
);


  
templateSheet
.
getRange
(
18
,
 
2
,
 
lineItems
.
length
,
 
6
).
setValues
(
lineItems
);



  
// Cleans up and creates PDF.


  
SpreadsheetApp
.
flush
();


  
Utilities
.
sleep
(
500
);
 
// Using to offset any potential latency in creating .pdf


  
const
 
pdf
 
=
 
createPDF
(


    
ssId
,


    
templateSheet
,


    
`Invoice#
${
invoiceNumber
}
-
${
customer
.
customer_name
}
`
,


  
);


  
return
 
[


    
invoiceNumber
,


    
todaysDate
,


    
customer
.
customer_name
,


    
customer
.
email
,


    
""
,


    
totalAmount
,


    
dueDate
,


    
pdf
.
getUrl
(),


    
"No"
,


  
];


}



/**


 * Resets the template sheet by clearing out customer data.


 * You use this to prepare for the next iteration or to view blank


 * the template for design.


 *


 * Called by createInvoiceForCustomer() or by the user via custom menu item.


 */


function
 
clearTemplateSheet
()
 
{


  
const
 
ss
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
();


  
const
 
templateSheet
 
=
 
ss
.
getSheetByName
(
INVOICE_TEMPLATE_SHEET_NAME
);


  
// Clears existing data from the template.


  
const
 
rngClear
 
=
 
templateSheet


    
.
getRangeList
([
"B10:B11"
,
 
"F10"
,
 
"F12"
,
 
"F14"
])


    
.
getRanges
();


  
for
 
(
const
 
cell
 
of
 
rngClear
)
 
{


    
cell
.
clearContent
();


  
}


  
// This sample only accounts for six rows of data 'B18:G24'. You can extend or make dynamic as necessary.


  
templateSheet
.
getRange
(
18
,
 
2
,
 
7
,
 
6
).
clearContent
();


}



/**


 * Creates a PDF for the customer given sheet.


 * @param {string} ssId - Id of the Google Spreadsheet


 * @param {object} sheet - Sheet to be converted as PDF


 * @param {string} pdfName - File name of the PDF being created


 * @return {file object} PDF file as a blob


 */


function
 
createPDF
(
ssId
,
 
sheet
,
 
pdfName
)
 
{


  
const
 
fr
 
=
 
0
;


  
const
 
fc
 
=
 
0
;


  
const
 
lc
 
=
 
9
;


  
const
 
lr
 
=
 
27
;


  
const
 
url
 
=
 
`https://docs.google.com/spreadsheets/d/
${
ssId
}
/export?format=pdf&size=7&fzr=true&portrait=true&fitw=true&gridlines=false&printtitle=false&top_margin=0.5&bottom_margin=0.25&left_margin=0.5&right_margin=0.5&sheetnames=false&pagenum=UNDEFINED&attachment=true&gid=
${
sheet
.
getSheetId
()
}
&
r1=
${
fr
}
&
c1=
${
fc
}
&
r2=
${
lr
}
&
c2=
${
lc
}
`
;



  
const
 
params
 
=
 
{


    
method
:
 
"GET"
,


    
headers
:
 
{
 
authorization
:
 
`Bearer 
${
ScriptApp
.
getOAuthToken
()
}
`
 
},


  
};


  
const
 
blob
 
=
 
UrlFetchApp
.
fetch
(
url
,
 
params
)


    
.
getBlob
()


    
.
setName
(
`
${
pdfName
}
.pdf`
);



  
// Gets the folder in Drive where the PDFs are stored.


  
const
 
folder
 
=
 
getFolderByName_
(
OUTPUT_FOLDER_NAME
);



  
const
 
pdfFile
 
=
 
folder
.
createFile
(
blob
);


  
return
 
pdfFile
;


}



/**


 * Sends emails with PDF as an attachment.


 * Checks/Sets 'Email Sent' column to 'Yes' to avoid resending.


 *


 * Called by user via custom menu item.


 */


function
 
sendEmails
()
 
{


  
const
 
ss
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
();


  
const
 
invoicesSheet
 
=
 
ss
.
getSheetByName
(
INVOICES_SHEET_NAME
);


  
const
 
invoicesData
 
=
 
invoicesSheet


    
.
getRange
(
1
,
 
1
,
 
invoicesSheet
.
getLastRow
(),
 
invoicesSheet
.
getLastColumn
())


    
.
getValues
();


  
const
 
keysI
 
=
 
invoicesData
.
splice
(
0
,
 
1
)[
0
];


  
const
 
invoices
 
=
 
getObjects
(
invoicesData
,
 
createObjectKeys
(
keysI
));


  
ss
.
toast
(
"Emailing Invoices"
,
 
APP_TITLE
,
 
1
);


  
invoices
.
forEach
((
invoice
,
 
index
)
 
=
>
 
{


    
if
 
(
invoice
.
email_sent
 
!==
 
"Yes"
)
 
{


      
ss
.
toast
(
`Emailing Invoice for 
${
invoice
.
customer
}
`
,
 
APP_TITLE
,
 
1
);



      
const
 
fileId
 
=
 
invoice
.
invoice_link
.
match
(
/[-\w]{25,}(?!.*[-\w]{25,})/
);


      
const
 
attachment
 
=
 
DriveApp
.
getFileById
(
fileId
);



      
let
 
recipient
 
=
 
invoice
.
email
;


      
if
 
(
EMAIL_OVERRIDE
)
 
{


        
recipient
 
=
 
EMAIL_ADDRESS_OVERRIDE
;


      
}



      
GmailApp
.
sendEmail
(
recipient
,
 
EMAIL_SUBJECT
,
 
EMAIL_BODY
,
 
{


        
attachments
:
 
[
attachment
.
getAs
(
MimeType
.
PDF
)],


        
name
:
 
APP_TITLE
,


      
});


      
invoicesSheet
.
getRange
(
index
 
+
 
2
,
 
9
).
setValue
(
"Yes"
);


    
}


  
});


}



/**


 * Helper function that turns sheet data range into an object.


 *


 * @param {SpreadsheetApp.Sheet} sheet - Sheet to process


 * Return {object} of a sheet's datarange as an object


 */


function
 
dataRangeToObject
(
sheet
)
 
{


  
const
 
dataRange
 
=
 
sheet


    
.
getRange
(
1
,
 
1
,
 
sheet
.
getLastRow
(),
 
sheet
.
getLastColumn
())


    
.
getValues
();


  
const
 
keys
 
=
 
dataRange
.
splice
(
0
,
 
1
)[
0
];


  
return
 
getObjects
(
dataRange
,
 
createObjectKeys
(
keys
));


}



/**


 * Utility function for mapping sheet data to objects.


 */


function
 
getObjects
(
data
,
 
keys
)
 
{


  
const
 
objects
 
=
 
[];


  
for
 
(
let
 
i
 
=
 
0
;
 
i
 < 
data
.
length
;
 
++
i
)
 
{


    
const
 
object
 
=
 
{};


    
let
 
hasData
 
=
 
false
;


    
for
 
(
let
 
j
 
=
 
0
;
 
j
 < 
data
[
i
].
length
;
 
++
j
)
 
{


      
const
 
cellData
 
=
 
data
[
i
][
j
];


      
if
 
(
isCellEmpty
(
cellData
))
 
{


        
continue
;


      
}


      
object
[
keys
[
j
]]
 
=
 
cellData
;


      
hasData
 
=
 
true
;


    
}


    
if
 
(
hasData
)
 
{


      
objects
.
push
(
object
);


    
}


  
}


  
return
 
objects
;


}


// Creates object keys for column headers.


function
 
createObjectKeys
(
keys
)
 
{


  
return
 
keys
.
map
((
key
)
 
=
>
 
key
.
replace
(
/\W+/g
,
 
"_"
).
toLowerCase
());


}


// Returns true if the cell where cellData was read from is empty.


function
 
isCellEmpty
(
cellData
)
 
{


  
return
 
typeof
 
cellData
 
===
 
"string"
 && 
cellData
 
===
 
""
;


}
```
```
/**


 * Copyright 2022 Google LLC


 *


 * Licensed under the Apache License, Version 2.0 (the "License");


 * you may not use this file except in compliance with the License.


 * You may obtain a copy of the License at


 *


 *      http://www.apache.org/licenses/LICENSE-2.0


 *


 * Unless required by applicable law or agreed to in writing, software


 * distributed under the License is distributed on an "AS IS" BASIS,


 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


 * See the License for the specific language governing permissions and


 * limitations under the License.


 */



/**


 * @OnlyCurrentDoc


 *


 * The above comment specifies that this automation will only


 * attempt to read or modify the spreadsheet this script is bound to.


 * The authorization request message presented to users reflects the


 * limited scope.


 */



/**


 * Creates a custom menu in the Google Sheets UI when the document is opened.


 *


 * @param {object} e The event parameter for a simple onOpen trigger.


 */


function
 
onOpen
(
e
)
 
{


  
const
 
menu
 
=
 
SpreadsheetApp
.
getUi
().
createMenu
(
APP_TITLE
);


  
menu


    
.
addItem
(
"Process invoices"
,
 
"processDocuments"
)


    
.
addItem
(
"Send emails"
,
 
"sendEmails"
)


    
.
addSeparator
()


    
.
addItem
(
"Reset template"
,
 
"clearTemplateSheet"
)


    
.
addToUi
();


}
```
```
/**


 * Copyright 2022 Google LLC


 *


 * Licensed under the Apache License, Version 2.0 (the "License");


 * you may not use this file except in compliance with the License.


 * You may obtain a copy of the License at


 *


 *      http://www.apache.org/licenses/LICENSE-2.0


 *


 * Unless required by applicable law or agreed to in writing, software


 * distributed under the License is distributed on an "AS IS" BASIS,


 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


 * See the License for the specific language governing permissions and


 * limitations under the License.


 */



/**


 * Returns a Google Drive folder in the same location


 * in Drive where the spreadsheet is located. First, it checks if the folder


 * already exists and returns that folder. If the folder doesn't already


 * exist, the script creates a new one. The folder's name is set by the


 * "OUTPUT_FOLDER_NAME" variable from the Code.gs file.


 *


 * @param {string} folderName - Name of the Drive folder.


 * @return {object} Google Drive Folder


 */


function
 
getFolderByName_
(
folderName
)
 
{


  
// Gets the Drive Folder of where the current spreadsheet is located.


  
const
 
ssId
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
().
getId
();


  
const
 
parentFolder
 
=
 
DriveApp
.
getFileById
(
ssId
).
getParents
().
next
();



  
// Iterates the subfolders to check if the PDF folder already exists.


  
const
 
subFolders
 
=
 
parentFolder
.
getFolders
();


  
while
 
(
subFolders
.
hasNext
())
 
{


    
const
 
folder
 
=
 
subFolders
.
next
();



    
// Returns the existing folder if found.


    
if
 
(
folder
.
getName
()
 
===
 
folderName
)
 
{


      
return
 
folder
;


    
}


  
}


  
// Creates a new folder if one does not already exist.


  
return
 
parentFolder


    
.
createFolder
(
folderName
)


    
.
setDescription
(


      
`Created by 
${
APP_TITLE
}
 application to store PDF output files`
,


    
);


}



/**


 * Test function to run getFolderByName_.


 * @prints a Google Drive FolderId.


 */


function
 
test_getFolderByName
()
 
{


  
// Gets the PDF folder in Drive.


  
const
 
folder
 
=
 
getFolderByName_
(
OUTPUT_FOLDER_NAME
);



  
console
.
log
(


    
`Name: 
${
folder
.
getName
()
}
\rID: 
${
folder
.
getId
()
}
\rDescription: 
${
folder
.
getDescription
()
}
`
,


  
);


  
// To automatically delete test folder, uncomment the following code:


  
// folder.setTrashed(true);


}
```
## Colaboradores
Google mantiene esta muestra con la ayuda de Expertos de Google Developers.
## Próximos pasos
- Menús personalizados en Google Workspace
- Extiende Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Realiza un seguimiento de las vistas y los comentarios de videos de YouTube

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Realiza un seguimiento de las vistas y los comentarios de videos de You Tube Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 20 minutos Tipo de proyecto : Automatización con un activador basado en el tiempo
## Objetivos
- Comprender qué hace la solución
- Comprender qué hacen los servicios de Google Apps Script dentro de la solución
- Configurar la secuencia de comandos
- Ejecutar la secuencia de comandos
## Acerca de esta solución
Esta solución hace un seguimiento del rendimiento de los videos públicos de YouTube, incluidas las vistas, los Me gusta y los comentarios, en una hoja de cálculo de Google Sheets. El activador verifica si hay información actualizada cada día y envía un mensaje de Gmail si los videos tienen actividad de comentarios nueva para que puedas interactuar con las preguntas y los comentarios.
### Cómo funciona
La secuencia de comandos usa el servicio avanzado de YouTube para obtener los detalles y las estadísticas de los videos de YouTube para las URLs de los videos que se enumeran en la columna Vínculo del video de cada hoja. Si aumentó la cantidad de comentarios de un video que aparece en la lista, la secuencia de comandos envía una notificación por correo electrónico a la dirección de correo electrónico con la que se nombra la hoja.
### Servicios de Apps Script
Esta solución usa los siguientes servicios:
- Servicio de hojas de cálculo : Obtiene la información de la URL de YouTube de la hoja de cálculo.
- Servicio avanzado de la API de datos de YouTube : Obtiene los detalles y las estadísticas de los videos de YouTube para cada URL de video.
- Servicio de correo : Crea y envía un correo electrónico en Gmail con una lista de videos que tienen comentarios nuevos.
## Requisitos previos
Para usar esta muestra, debes cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
Para configurar esta secuencia de comandos, sigue estos pasos:
### Crea el proyecto de Apps Script
- Para crear una copia de la hoja de cálculo Track YouTube video views and comments , haz clic en el siguiente botón: Crear una copia El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo.
- En la hoja de cálculo copiada, cambia el nombre de la hoja Your_Email_Address por tu dirección de correo electrónico.
- Agrega las URLs de los videos de YouTube que quieres rastrear o usa las URLs proporcionadas para realizar pruebas. Las URLs deben comenzar con el formato www.youtube.com/watch?v= .
`www.youtube.com/watch?v=`
- Haz clic en Extensiones > Apps Script . Si YouTube ya aparece en Servicios , puedes omitir los siguientes 2 pasos.
- Junto a Servicios , haz clic en Agregar un servicio add .
- En la lista, selecciona API de YouTube Data y haz clic en Agregar .
### Crear un activador
- En el proyecto de Apps Script, haz clic en Activadores alarm > Agregar activador .
- En Elige qué función ejecutar , selecciona markVideos .
- En Seleccionar la fuente del evento , selecciona Basado en el tiempo .
- En Seleccionar el tipo de activador basado en el tiempo , selecciona Temporizador por día .
- En Seleccionar la hora del día , elige la hora que prefieras.
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
## Ejecuta la secuencia de comandos
El activador que configuraste ejecuta la secuencia de comandos una vez al día. Puedes ejecutar la secuencia de comandos de forma manual para probarla.
- En el proyecto de Apps Script, haz clic en Editor code .
- En el menú desplegable de funciones, selecciona markVideos .
- Haz clic en Ejecutar .
- Vuelve a la hoja de cálculo para revisar la información que la secuencia de comandos agregó a la hoja.
- Abre tu correo electrónico para revisar el correo electrónico con la lista de videos que tienen más de cero comentarios. Cuando la secuencia de comandos se ejecute en el futuro, solo enviará un correo electrónico con los videos cuya cantidad de comentarios haya aumentado desde la última vez que se ejecutó la secuencia de comandos.
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver el código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/automations/youtube-tracker



/*


Copyright 2022 Google LLC



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



// Sets preferences for email notification. Choose 'Y' to send emails, 'N' to skip emails.


const
 
EMAIL_ON
 
=
 
"Y"
;



// Matches column names in Video sheet to variables. If the column names change, update these variables.


const
 
COLUMN_NAME
 
=
 
{


  
VIDEO
:
 
"Video Link"
,


  
TITLE
:
 
"Video Title"
,


};



/**


 * Gets YouTube video details and statistics for all


 * video URLs listed in 'Video Link' column in each


 * sheet. Sends email summary, based on preferences above,


 * when videos have new comments or replies.


 */


function
 
markVideos
()
 
{


  
const
 
ss
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
();


  
const
 
sheets
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
().
getSheets
();



  
// Runs through process for each tab in Spreadsheet.


  
for
 
(
const
 
dataSheet
 
of
 
sheets
)
 
{


    
const
 
tabName
 
=
 
dataSheet
.
getName
();


    
const
 
range
 
=
 
dataSheet
.
getDataRange
();


    
const
 
numRows
 
=
 
range
.
getNumRows
();


    
const
 
rows
 
=
 
range
.
getValues
();


    
const
 
headerRow
 
=
 
rows
[
0
];



    
// Finds the column indices.


    
const
 
videoColumnIdx
 
=
 
headerRow
.
indexOf
(
COLUMN_NAME
.
VIDEO
);


    
const
 
titleColumnIdx
 
=
 
headerRow
.
indexOf
(
COLUMN_NAME
.
TITLE
);



    
// Creates empty array to collect data for email table.


    
const
 
emailContent
 
=
 
[];



    
// Processes each row in spreadsheet.


    
for
 
(
let
 
i
 
=
 
1
;
 
i
 < 
numRows
;
 
++
i
)
 
{


      
const
 
row
 
=
 
rows
[
i
];


      
// Extracts video ID.


      
const
 
videoId
 
=
 
extractVideoIdFromUrl
(
row
[
videoColumnIdx
]);


      
// Processes each row that contains a video ID.


      
if
 
(
!
videoId
)
 
{


        
continue
;


      
}


      
// Calls getVideoDetails function and extracts target data for the video.


      
const
 
detailsResponse
 
=
 
getVideoDetails
(
videoId
);


      
const
 
title
 
=
 
detailsResponse
.
items
[
0
].
snippet
.
title
;


      
const
 
publishDate
 
=
 
detailsResponse
.
items
[
0
].
snippet
.
publishedAt
;


      
const
 
publishDateFormatted
 
=
 
new
 
Date
(
publishDate
);


      
const
 
views
 
=
 
detailsResponse
.
items
[
0
].
statistics
.
viewCount
;


      
const
 
likes
 
=
 
detailsResponse
.
items
[
0
].
statistics
.
likeCount
;


      
const
 
comments
 
=
 
detailsResponse
.
items
[
0
].
statistics
.
commentCount
;


      
const
 
channel
 
=
 
detailsResponse
.
items
[
0
].
snippet
.
channelTitle
;



      
// Collects title, publish date, channel, views, comments, likes details and pastes into tab.


      
const
 
detailsRow
 
=
 
[


        
title
,


        
publishDateFormatted
,


        
channel
,


        
views
,


        
comments
,


        
likes
,


      
];


      
dataSheet


        
.
getRange
(
i
 
+
 
1
,
 
titleColumnIdx
 
+
 
1
,
 
1
,
 
6
)


        
.
setValues
([
detailsRow
]);



      
// Determines if new count of comments/replies is greater than old count of comments/replies.


      
const
 
addlCommentCount
 
=
 
comments
 
-
 
row
[
titleColumnIdx
 
+
 
4
];



      
// Adds video title, link, and additional comment count to table if new counts > old counts.


      
if
 
(
addlCommentCount
 > 
0
)
 
{


        
const
 
emailRow
 
=
 
[
title
,
 
row
[
videoColumnIdx
],
 
addlCommentCount
];


        
emailContent
.
push
(
emailRow
);


      
}


    
}


    
// Sends notification email if Content is not empty.


    
if
 
(
emailContent
.
length
 > 
0
 && 
EMAIL_ON
 
===
 
"Y"
)
 
{


      
sendEmailNotificationTemplate
(
emailContent
,
 
tabName
);


    
}


  
}


}



/**


 * Gets video details for YouTube videos


 * using YouTube advanced service.


 */


function
 
getVideoDetails
(
videoId
)
 
{


  
const
 
part
 
=
 
"snippet,statistics"
;


  
const
 
response
 
=
 
YouTube
.
Videos
.
list
(
part
,
 
{
 
id
:
 
videoId
 
});


  
return
 
response
;


}



/**


 * Extracts YouTube video ID from url.


 * (h/t https://stackoverflow.com/a/3452617)


 */


function
 
extractVideoIdFromUrl
(
url
)
 
{


  
let
 
videoId
 
=
 
url
.
split
(
"v="
)[
1
];


  
const
 
ampersandPosition
 
=
 
videoId
.
indexOf
(
"&"
);


  
if
 
(
ampersandPosition
 
!==
 
-
1
)
 
{


    
videoId
 
=
 
videoId
.
substring
(
0
,
 
ampersandPosition
);


  
}


  
return
 
videoId
;


}



/**


 * Assembles notification email with table of video details.


 * (h/t https://stackoverflow.com/questions/37863392/making-table-in-google-apps-script-from-array)


 */


function
 
sendEmailNotificationTemplate
(
content
,
 
emailAddress
)
 
{


  
const
 
template
 
=
 
HtmlService
.
createTemplateFromFile
(
"email"
);


  
template
.
content
 
=
 
content
;


  
const
 
msg
 
=
 
template
.
evaluate
();


  
MailApp
.
sendEmail
(


    
emailAddress
,


    
"New comments or replies on YouTube"
,


    
msg
.
getContent
(),


    
{
 
htmlBody
:
 
msg
.
getContent
()
 
},


  
);


}
```
```
<!--
 Copyright 2022 Google LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->

<body>
  Hello,<br><br>You have new comments and/or replies on videos: <br><br>
  <table border="1">
    <tr>
      <th>Video Title</th>
      <th>Link</th>
      <th>Number of new replies and comments</th>
    </tr>
    <? for (var i = 0; i < content.length; i++) { ?>
    <tr>
      <? for (var j = 0; j < content[i].length; j++) { ?>
      <td align="center"><?= content[i][j] ?></td>
      <? } ?>
    </tr>
    <? } ?>
  </table>
</body>
```
## Colaboradores
Google mantiene esta muestra con la ayuda de Expertos de Google Developers.
## Próximos pasos
- Activadores basados en el tiempo
- Extiende Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Propague el calendario de vacaciones del equipo

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Propague el calendario de vacaciones del equipo Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 15 min Tipo de proyecto : Automatización con un activador basado en el tiempo
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Google Apps Script dentro de la solución.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Un calendario de vacaciones compartido es una excelente herramienta para ayudar a tu equipo a colaborar, ya que cualquiera puede determinar quién está fuera de la oficina de un vistazo. Esta solución te permite ver cuándo tus colegas están fuera de la oficina, sin necesidad de ingresar datos manualmente.
### Cómo funciona
Esta solución completa un calendario de vacaciones compartido basado en los calendarios individuales de cada persona de un grupo de Google. Cuando alguien reserva tiempo libre, agrega un evento a su Calendario de Google personal con una palabra clave como "Vacaciones" o "Fuera de la oficina".
Cada hora, la secuencia de comandos analiza los calendarios de los miembros del grupo y sincroniza los eventos correspondientes con el calendario compartido. Puedes cambiar la frecuencia con la que la secuencia de comandos analiza los eventos nuevos .
Esta solución solo accede a los eventos de Calendario que tus colegas hicieron visibles para ti a través de su configuración de privacidad.
### Servicios de Apps Script
En esta solución, se usan los siguientes servicios:
- Servicio de Grupos de Google : Determina los miembros del grupo de Grupos de Google.
- Servicio avanzado de Calendario : Proporciona acceso a la API de Calendario de Google y busca eventos en los calendarios de los miembros del grupo.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
Para configurar la secuencia de comandos que completará el calendario de vacaciones del equipo, completa los siguientes pasos:
### Crea un calendario de vacaciones del equipo
- Abre Calendario .
- Crea un calendario nuevo llamado "Vacaciones del equipo".
- En la configuración del calendario, en Integrar calendario , copia el ID del calendario .
### Crea el proyecto de Apps Script
- Para abrir el proyecto de Apps Script Vacation Calendar , haz clic en el siguiente botón: Abrir el proyecto
- Haz clic en Descripción general info_outline .
- En la página de descripción general, haz clic en Crear una copia .
- En el proyecto de Apps Script que copiaste, configura la variable TEAM_CALENDAR_ID en el ID del calendario que creaste antes.
`TEAM_CALENDAR_ID`
- Establece la variable GROUP_EMAIL en la dirección de correo electrónico de un grupo de Grupos de Google que contenga a los miembros de tu equipo.
`GROUP_EMAIL`
- Junto a Servicios , haz clic en Agregar un servicio add .
- Selecciona API de Calendario de Google y haz clic en Agregar .
## Ejecuta la secuencia de comandos:
- En el proyecto de Apps Script que copiaste, en el menú desplegable de funciones, selecciona setup .
- Haz clic en Ejecutar .
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
- Cuando termines, vuelve al Calendario para confirmar que el calendario de vacaciones del equipo se haya completado con eventos.
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/automations/vacation-calendar



/*


Copyright 2022 Google LLC



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



// Set the ID of the team calendar to add events to. You can find the calendar's


// ID on the settings page.


const
 
TEAM_CALENDAR_ID
 
=
 
"ENTER_TEAM_CALENDAR_ID_HERE"
;


// Set the email address of the Google Group that contains everyone in the team.


// Ensure the group has less than 500 members to avoid timeouts.


// Change to an array in order to add indirect members frrm multiple groups, for example:


// let GROUP_EMAIL = ['ENTER_GOOGLE_GROUP_EMAIL_HERE', 'ENTER_ANOTHER_GOOGLE_GROUP_EMAIL_HERE'];


const
 
GROUP_EMAIL
 
=
 
"ENTER_GOOGLE_GROUP_EMAIL_HERE"
;



const
 
ONLY_DIRECT_MEMBERS
 
=
 
false
;



const
 
KEYWORDS
 
=
 
[
"vacation"
,
 
"ooo"
,
 
"out of office"
,
 
"offline"
];


const
 
MONTHS_IN_ADVANCE
 
=
 
3
;



/**


 * Sets up the script to run automatically every hour.


 */


function
 
setup
()
 
{


  
const
 
triggers
 
=
 
ScriptApp
.
getProjectTriggers
();


  
if
 
(
triggers
.
length
 > 
0
)
 
{


    
throw
 
new
 
Error
(
"Triggers are already setup."
);


  
}


  
ScriptApp
.
newTrigger
(
"sync"
).
timeBased
().
everyHours
(
1
).
create
();


  
// Runs the first sync immediately.


  
sync
();


}



/**


 * Looks through the group members' public calendars and adds any


 * 'vacation' or 'out of office' events to the team calendar.


 */


function
 
sync
()
 
{


  
// Defines the calendar event date range to search.


  
const
 
today
 
=
 
new
 
Date
();


  
const
 
maxDate
 
=
 
new
 
Date
();


  
maxDate
.
setMonth
(
maxDate
.
getMonth
()
 
+
 
MONTHS_IN_ADVANCE
);



  
// Determines the time the the script was last run.


  
let
 
lastRun
 
=
 
PropertiesService
.
getScriptProperties
().
getProperty
(
"lastRun"
);


  
lastRun
 
=
 
lastRun
 
?
 
new
 
Date
(
lastRun
)
 
:
 
null
;



  
// Gets the list of users in the Google Group.


  
let
 
users
 
=
 
getAllMembers
(
GROUP_EMAIL
);


  
if
 
(
ONLY_DIRECT_MEMBERS
)
 
{


    
users
 
=
 
GroupsApp
.
getGroupByEmail
(
GROUP_EMAIL
).
getUsers
();


  
}
 
else
 
if
 
(
Array
.
isArray
(
GROUP_EMAIL
))
 
{


    
users
 
=
 
getUsersFromGroups
(
GROUP_EMAIL
);


  
}



  
// For each user, finds events having one or more of the keywords in the event


  
// summary in the specified date range. Imports each of those to the team


  
// calendar.


  
let
 
count
 
=
 
0
;


  
for
 
(
const
 
user
 
of
 
users
)
 
{


    
const
 
username
 
=
 
user
.
getEmail
().
split
(
"@"
)[
0
];


    
const
 
events
 
=
 
findEvents
(
user
,
 
today
,
 
maxDate
,
 
lastRun
);


    
for
 
(
const
 
event
 
of
 
events
)
 
{


      
importEvent
(
username
,
 
event
);


      
count
++
;


    
}


  
}



  
PropertiesService
.
getScriptProperties
().
setProperty
(
"lastRun"
,
 
today
);


  
console
.
log
(
`Imported 
${
count
}
 events`
);


}



/**


 * Imports the given event from the user's calendar into the shared team


 * calendar.


 * @param {string} username The team member that is attending the event.


 * @param {Calendar.Event} event The event to import.


 */


function
 
importEvent
(
username
,
 
event
)
 
{


  
event
.
summary
 
=
 
`[
${
username
}
] 
${
event
.
summary
}
`
;


  
event
.
organizer
 
=
 
{


    
id
:
 
TEAM_CALENDAR_ID
,


  
};


  
event
.
attendees
 
=
 
[];



  
// If the event is not of type 'default', it can't be imported, so it needs


  
// to be changed.


  
if
 
(
event
.
eventType
 
!==
 
"default"
)
 
{


    
event
.
eventType
 
=
 
"default"
;


    
event
.
outOfOfficeProperties
 
=
 
undefined
;


    
event
.
focusTimeProperties
 
=
 
undefined
;


  
}



  
console
.
log
(
"Importing: %s"
,
 
event
.
summary
);


  
try
 
{


    
Calendar
.
Events
.
import
(
event
,
 
TEAM_CALENDAR_ID
);


  
}
 
catch
 
(
e
)
 
{


    
console
.
error
(


      
"Error attempting to import event: %s. Skipping."
,


      
e
.
toString
(),


    
);


  
}


}



/**


 * In a given user's calendar, looks for occurrences of the given keyword


 * in events within the specified date range and returns any such events


 * found.


 * @param {Session.User} user The user to retrieve events for.


 * @param {string} keyword The keyword to look for.


 * @param {Date} start The starting date of the range to examine.


 * @param {Date} end The ending date of the range to examine.


 * @param {Date} optSince A date indicating the last time this script was run.


 * @return {Calendar.Event[]} An array of calendar events.


 */


function
 
findEvents
(
user
,
 
start
,
 
end
,
 
optSince
)
 
{


  
const
 
params
 
=
 
{


    
eventTypes
:
 
"outOfOffice"
,


    
timeMin
:
 
formatDateAsRFC3339
(
start
),


    
timeMax
:
 
formatDateAsRFC3339
(
end
),


    
showDeleted
:
 
true
,


  
};


  
if
 
(
optSince
)
 
{


    
// This prevents the script from examining events that have not been


    
// modified since the specified date (that is, the last time the


    
// script was run).


    
params
.
updatedMin
 
=
 
formatDateAsRFC3339
(
optSince
);


  
}


  
let
 
pageToken
 
=
 
null
;


  
let
 
events
 
=
 
[];


  
do
 
{


    
params
.
pageToken
 
=
 
pageToken
;


    
let
 
response
;


    
try
 
{


      
response
 
=
 
Calendar
.
Events
.
list
(
user
.
getEmail
(),
 
params
);


    
}
 
catch
 
(
e
)
 
{


      
console
.
error
(


        
"Error retriving events for %s, %s: %s; skipping"
,


        
user
,


        
keyword
,


        
e
.
toString
(),


      
);


      
continue
;


    
}


    
events
 
=
 
events
.
concat
(
response
.
items
);


    
pageToken
 
=
 
response
.
nextPageToken
;


  
}
 
while
 
(
pageToken
);


  
return
 
events
;


}



/**


 * Returns an RFC3339 formated date String corresponding to the given


 * Date object.


 * @param {Date} date a Date.


 * @return {string} a formatted date string.


 */


function
 
formatDateAsRFC3339
(
date
)
 
{


  
return
 
Utilities
.
formatDate
(
date
,
 
"UTC"
,
 
"yyyy-MM-dd'T'HH:mm:ssZ"
);


}



/**


 * Get both direct and indirect members (and delete duplicates).


 * @param {string} the e-mail address of the group.


 * @return {object} direct and indirect members.


 */


function
 
getAllMembers
(
groupEmail
)
 
{


  
const
 
group
 
=
 
GroupsApp
.
getGroupByEmail
(
groupEmail
);


  
let
 
users
 
=
 
group
.
getUsers
();


  
const
 
childGroups
 
=
 
group
.
getGroups
();


  
for
 
(
let
 
i
 
=
 
0
;
 
i
 < 
childGroups
.
length
;
 
i
++
)
 
{


    
const
 
childGroup
 
=
 
childGroups
[
i
];


    
users
 
=
 
users
.
concat
(
getAllMembers
(
childGroup
.
getEmail
()));


  
}


  
// Remove duplicate members


  
const
 
uniqueUsers
 
=
 
[];


  
const
 
userEmails
 
=
 
{};


  
for
 
(
let
 
i
 
=
 
0
;
 
i
 < 
users
.
length
;
 
i
++
)
 
{


    
const
 
user
 
=
 
users
[
i
];


    
if
 
(
!
userEmails
[
user
.
getEmail
()])
 
{


      
uniqueUsers
.
push
(
user
);


      
userEmails
[
user
.
getEmail
()]
 
=
 
true
;


    
}


  
}


  
return
 
uniqueUsers
;


}



/**


 * Get indirect members from multiple groups (and delete duplicates).


 * @param {array} the e-mail addresses of multiple groups.


 * @return {object} indirect members of multiple groups.


 */


function
 
getUsersFromGroups
(
groupEmails
)
 
{


  
const
 
users
 
=
 
[];


  
for
 
(
const
 
groupEmail
 
of
 
groupEmails
)
 
{


    
const
 
groupUsers
 
=
 
GroupsApp
.
getGroupByEmail
(
groupEmail
).
getUsers
();


    
for
 
(
const
 
user
 
of
 
groupUsers
)
 
{


      
if
 
(
!
users
.
some
((
u
)
 
=
>
 
u
.
getEmail
()
 
===
 
user
.
getEmail
()))
 
{


        
users
.
push
(
user
);


      
}


    
}


  
}


  
return
 
users
;


}
```
## Modificaciones
Puedes editar la automatización del calendario de vacaciones del equipo tantas veces como quieras para que se ajuste a tus necesidades. El siguiente es un cambio opcional para modificar el activador.
#### Cambia la frecuencia con la que la secuencia de comandos analiza los eventos nuevos
Para cambiar la frecuencia con la que se ejecuta la secuencia de comandos, sigue estos pasos:
- En el proyecto de Apps Script, haz clic en Activadores alarm .
- Junto al activador, haz clic en Editar activador edit .
- Selecciona los cambios y haz clic en Guardar .
## Colaboradores
Google mantiene esta muestra con la ayuda de los Google Developer Experts.
## Próximos pasos
- Activadores basados en el tiempo
- Eventos de calendario
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Crea un corchete de torneo

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Crea un corchete de torneo Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 5 minutos Tipo de proyecto : Automatización con un menú personalizado
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Crea un cuadro de torneo para hasta 64 personas o equipos. Esta solución crea un diagrama de árbol que representa un torneo de eliminación única.
### Cómo funciona
El script itera la lista de jugadores y determina cuántas rondas se necesitan en el cuadro. La secuencia de comandos da formato a la hoja Bracket para crear el diagrama de árbol y agrega los nombres de los jugadores a la primera ronda.
### Servicios de Apps Script
En esta solución, se usa el siguiente servicio:
- Servicio de hojas de cálculo : Obtiene el rango de jugadores y crea el diagrama de árbol para el torneo.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
Haz clic en el siguiente botón para crear una copia de la hoja de cálculo de ejemplo Crea un cuadro de torneo :
Crear una copia
## Ejecuta la secuencia de comandos:
- En la hoja de cálculo que copiaste, haz clic en Bracket maker > Create bracket . Es posible que debas actualizar la página para que aparezca este menú personalizado.
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
- Haz clic en Bracket maker > Create bracket de nuevo.
Haz clic en Bracket maker > Create bracket de nuevo.
- Cambia a la pestaña Bracket para ver el cuadro del torneo.
Cambia a la pestaña Bracket para ver el cuadro del torneo.
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/automations/bracket-maker



/*


Copyright 2022 Google LLC



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



const
 
RANGE_PLAYER1
 
=
 
"FirstPlayer"
;


const
 
SHEET_PLAYERS
 
=
 
"Players"
;


const
 
SHEET_BRACKET
 
=
 
"Bracket"
;


const
 
CONNECTOR_WIDTH
 
=
 
15
;



/**


 * Adds a custom menu item to run the script.


 */


function
 
onOpen
()
 
{


  
const
 
ss
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
();


  
ss
.
addMenu
(
"Bracket maker"
,
 
[


    
{
 
name
:
 
"Create bracket"
,
 
functionName
:
 
"createBracket"
 
},


  
]);


}



/**


 * Creates the brackets based on the data provided on the players.


 */


function
 
createBracket
()
 
{


  
const
 
ss
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
();


  
let
 
rangePlayers
 
=
 
ss
.
getRangeByName
(
RANGE_PLAYER1
);


  
const
 
sheetControl
 
=
 
ss
.
getSheetByName
(
SHEET_PLAYERS
);


  
const
 
sheetResults
 
=
 
ss
.
getSheetByName
(
SHEET_BRACKET
);



  
// Gets the players from column A.  Assumes the entire column is filled.


  
rangePlayers
 
=
 
rangePlayers
.
offset
(


    
0
,


    
0
,


    
sheetControl
.
getMaxRows
()
 
-
 
rangePlayers
.
getRowIndex
()
 
+
 
1
,


    
1
,


  
);


  
let
 
players
 
=
 
rangePlayers
.
getValues
();



  
// Figures out how many players there are by skipping the empty cells.


  
let
 
numPlayers
 
=
 
0
;


  
for
 
(
let
 
i
 
=
 
0
;
 
i
 < 
players
.
length
;
 
i
++
)
 
{


    
if
 
(
!
players
[
i
][
0
]
 
||
 
players
[
i
][
0
].
length
 
===
 
0
)
 
{


      
break
;


    
}


    
numPlayers
++
;


  
}


  
players
 
=
 
players
.
slice
(
0
,
 
numPlayers
);



  
// Provides some error checking in case there are too many or too few players/teams.


  
if
 
(
numPlayers
 > 
64
)
 
{


    
Browser
.
msgBox
(


      
"Sorry, this script can only create brackets for 64 or fewer players."
,


    
);


    
return
;
 
// Early exit


  
}



  
if
 
(
numPlayers
 < 
3
)
 
{


    
Browser
.
msgBox
(
"Sorry, you must have at least 3 players."
);


    
return
;
 
// Early exit


  
}



  
// Clears the 'Bracket' sheet and all formatting.


  
sheetResults
.
clear
();



  
let
 
upperPower
 
=
 
Math
.
ceil
(
Math
.
log
(
numPlayers
)
 
/
 
Math
.
log
(
2
));



  
// Calculates the number that is a power of 2 and lower than numPlayers.


  
const
 
countNodesUpperBound
 
=
 
2
 
**
 
upperPower
;



  
// Calculates the number that is a power of 2 and higher than numPlayers.


  
const
 
countNodesLowerBound
 
=
 
countNodesUpperBound
 
/
 
2
;



  
// Determines the number of nodes that will not show in the 1st level.


  
const
 
countNodesHidden
 
=
 
numPlayers
 
-
 
countNodesLowerBound
;



  
// Enters the players for the 1st round.


  
const
 
currentPlayer
 
=
 
0
;


  
for
 
(
let
 
i
 
=
 
0
;
 
i
 < 
countNodesLowerBound
;
 
i
++
)
 
{


    
if
 
(
i
 < 
countNodesHidden
)
 
{


      
// Must be on the first level


      
const
 
rng
 
=
 
sheetResults
.
getRange
(
i
 
*
 
4
 
+
 
1
,
 
1
);


      
setBracketItem_
(
rng
,
 
players
);


      
setBracketItem_
(
rng
.
offset
(
2
,
 
0
,
 
1
,
 
1
),
 
players
);


      
setConnector_
(
sheetResults
,
 
rng
.
offset
(
0
,
 
1
,
 
3
,
 
1
));


      
setBracketItem_
(
rng
.
offset
(
1
,
 
2
,
 
1
,
 
1
));


    
}
 
else
 
{


      
// This player gets a bye.


      
setBracketItem_
(
sheetResults
.
getRange
(
i
 
*
 
4
 
+
 
2
,
 
3
),
 
players
);


    
}


  
}



  
// Fills in the rest of the bracket.


  
upperPower
--
;


  
for
 
(
let
 
i
 
=
 
0
;
 
i
 < 
upperPower
;
 
i
++
)
 
{


    
const
 
pow1
 
=
 
2
 
**
 
(
i
 
+
 
1
);


    
const
 
pow2
 
=
 
2
 
**
 
(
i
 
+
 
2
);


    
const
 
pow3
 
=
 
2
 
**
 
(
i
 
+
 
3
);


    
for
 
(
let
 
j
 
=
 
0
;
 
j
 < 
2
 
**
 
(
upperPower
 
-
 
i
 
-
 
1
);
 
j
++
)
 
{


      
setBracketItem_
(
sheetResults
.
getRange
(
j
 
*
 
pow3
 
+
 
pow2
,
 
i
 
*
 
2
 
+
 
5
));


      
setConnector_
(


        
sheetResults
,


        
sheetResults
.
getRange
(
j
 
*
 
pow3
 
+
 
pow1
,
 
i
 
*
 
2
 
+
 
4
,
 
pow2
 
+
 
1
,
 
1
),


      
);


    
}


  
}


}



/**


 * Sets the value of an item in the bracket and the color.


 * @param {Range} rng The Spreadsheet Range.


 * @param {string[]} players The list of players.


 */


function
 
setBracketItem_
(
rng
,
 
players
)
 
{


  
if
 
(
players
)
 
{


    
const
 
rand
 
=
 
Math
.
ceil
(
Math
.
random
()
 
*
 
players
.
length
);


    
rng
.
setValue
(
players
.
splice
(
rand
 
-
 
1
,
 
1
)[
0
][
0
]);


  
}


  
rng
.
setBackgroundColor
(
"yellow"
);


}



/**


 * Sets the color and width for connector cells.


 * @param {Sheet} sheet The spreadsheet to setup.


 * @param {Range} rng The spreadsheet range.


 */


function
 
setConnector_
(
sheet
,
 
rng
)
 
{


  
sheet
.
setColumnWidth
(
rng
.
getColumnIndex
(),
 
CONNECTOR_WIDTH
);


  
rng
.
setBackgroundColor
(
"green"
);


}
```
```
</section>
```
## Colaboradores
Google mantiene esta muestra con la ayuda de los Google Developer Experts.
## Próximos pasos
- Menús personalizados en Google Workspace
- Extensión de Hojas de cálculo de Google
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Crea un registro para un sitio externo

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Crea un registro para un sitio externo Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 5 minutos Tipo de proyecto : Automatización con un menú personalizado
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Crea un sistema integral de registro de actividades fuera del sitio. La solución crea un formulario para que los empleados expresen sus preferencias de actividad y las hace coincidir con el cronograma de actividades.
### Cómo funciona
Con un cronograma de actividades en Hojas de cálculo de Google, la secuencia de comandos crea un formulario de Formularios de Google para que los empleados seleccionen sus preferencias de actividad. Una vez que se reciben las respuestas, la secuencia de comandos hace coincidir las preferencias de los empleados con el cronograma y la capacidad de cada actividad. Las coincidencias se proporcionan en dos hojas nuevas, una organizada por empleado y la otra por actividad.
### Servicios de Apps Script
Esta solución usa los siguientes servicios:
- Servicio de hojas de cálculo : Contiene el cronograma de actividades y las respuestas del formulario, y asigna actividades a los empleados.
- Servicio de formularios : Crea un formulario para que los empleados ingresen sus preferencias de actividad.
- Servicio de utilidades : Da formato a cadenas y fechas.
## Requisitos previos
Para usar esta muestra, debes cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
Para copiar la hoja de cálculo y su secuencia de comandos adjunta, haz clic en el siguiente botón:
Crear una copia
## Ejecuta la secuencia de comandos
- En la hoja de cálculo copiada, haz clic en Actividades > Crear formulario . Es posible que debas actualizar la página para que aparezca este menú personalizado.
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
- Vuelve a hacer clic en Actividades > Crear formulario .
- Para generar respuestas de prueba, haz clic en Actividades > Generar datos de prueba .
- Para probar el formulario, haz clic en Herramientas > Administrar formulario > Ir al formulario publicado .
- Completa el formulario y envíalo.
- En la hoja de cálculo, haz clic en Actividades > Asignar actividades .
- Revisa las dos hojas nuevas: Actividades por persona y Listas de actividades .
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver el código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/automations/offsite-activity-signup



/*


Copyright 2022 Google LLC



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



const
 
NUM_ITEMS_TO_RANK
 
=
 
5
;


const
 
ACTIVITIES_PER_PERSON
 
=
 
2
;


const
 
NUM_TEST_USERS
 
=
 
150
;



/**


 * Adds custom menu items when opening the sheet.


 */


function
 
onOpen
()
 
{


  
const
 
menu
 
=
 
SpreadsheetApp
.
getUi
()


    
.
createMenu
(
"Activities"
)


    
.
addItem
(
"Create form"
,
 
"buildForm_"
)


    
.
addItem
(
"Generate test data"
,
 
"generateTestData_"
)


    
.
addItem
(
"Assign activities"
,
 
"assignActivities_"
)


    
.
addToUi
();


}



/**


 * Builds a form based on the "Activity Schedule" sheet. The form asks attendees to rank their top


 * N choices of activities, where N is defined by NUM_ITEMS_TO_RANK.


 */


function
 
buildForm_
()
 
{


  
const
 
ss
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
();


  
if
 
(
ss
.
getFormUrl
())
 
{


    
const
 
msg
 
=
 
"Form already exists. Unlink the form and try again."
;


    
SpreadsheetApp
.
getUi
().
alert
(
msg
);


    
return
;


  
}


  
const
 
form
 
=
 
FormApp
.
create
(
"Activity Signup"
)


    
.
setDestination
(
FormApp
.
DestinationType
.
SPREADSHEET
,
 
ss
.
getId
())


    
.
setAllowResponseEdits
(
true
)


    
.
setLimitOneResponsePerUser
(
true
)


    
.
setCollectEmail
(
true
);


  
const
 
sectionHelpText
 
=
 
Utilities
.
formatString
(


    
"Please choose your top %d activities"
,


    
NUM_ITEMS_TO_RANK
,


  
);


  
form


    
.
addSectionHeaderItem
()


    
.
setTitle
(
"Activity choices"
)


    
.
setHelpText
(
sectionHelpText
);



  
// Presents activity ranking as a form grid with each activity as a row and rank as a column.


  
const
 
rows
 
=
 
loadActivitySchedule_
(
ss
).
map
(


    
(
activity
)
 
=
>
 
activity
.
description
,


  
);


  
const
 
columns
 
=
 
range_
(
1
,
 
NUM_ITEMS_TO_RANK
).
map
((
value
)
 
=
>

    
Utilities
.
formatString
(
"%s"
,
 
toOrdinal_
(
value
)),


  
);


  
const
 
gridValidation
 
=
 
FormApp
.
createGridValidation
()


    
.
setHelpText
(
"Select one item per column."
)


    
.
requireLimitOneResponsePerColumn
()


    
.
build
();


  
form


    
.
addGridItem
()


    
.
setColumns
(
columns
)


    
.
setRows
(
rows
)


    
.
setValidation
(
gridValidation
);



  
form


    
.
addListItem
()


    
.
setTitle
(
"Assign other activities if choices are not available?"
)


    
.
setChoiceValues
([
"Yes"
,
 
"No"
]);


}



/**


 * Assigns activities using a random priority/random serial dictatorship approach. The results


 * are then populated into two new sheets, one listing activities per person, the other listing


 * the rosters for each activity.


 *


 * See https://en.wikipedia.org/wiki/Random_serial_dictatorship for additional information.


 */


function
 
assignActivities_
()
 
{


  
const
 
ss
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
();


  
const
 
activities
 
=
 
loadActivitySchedule_
(
ss
);


  
const
 
activityIds
 
=
 
activities
.
map
((
activity
)
 
=
>
 
activity
.
id
);


  
const
 
attendees
 
=
 
loadAttendeeResponses_
(
ss
,
 
activityIds
);


  
assignWithRandomPriority_
(
attendees
,
 
activities
,
 
2
);


  
writeAttendeeAssignments_
(
ss
,
 
attendees
);


  
writeActivityRosters_
(
ss
,
 
activities
);


}



/**


 * Selects activities via random priority.


 *


 * @param {object[]} attendees - Array of attendees to assign activities to


 * @param {object[]} activities - Array of all available activities


 * @param {number} numActivitiesPerPerson - Maximum number of activities to assign


 */


function
 
assignWithRandomPriority_
(


  
attendees
,


  
activities
,


  
numActivitiesPerPerson
,


)
 
{


  
const
 
activitiesById
 
=
 
activities
.
reduce
((
obj
,
 
activity
)
 
=
>
 
{


    
obj
[
activity
.
id
]
 
=
 
activity
;


    
return
 
obj
;


  
},
 
{});


  
for
 
(
let
 
i
 
=
 
0
;
 
i
 < 
numActivitiesPerPerson
;
 
++
i
)
 
{


    
const
 
randomizedAttendees
 
=
 
shuffleArray_
(
attendees
);


    
for
 
(
const
 
attendee
 
of
 
randomizedAttendees
)
 
{


      
makeChoice_
(
attendee
,
 
activitiesById
);


    
}


  
}


}



/**


 * Attempts to assign an activity for an attendee based on their preferences and current schedule.


 *


 * @param {object} attendee - Attendee looking to join an activity


 * @param {object} activitiesById - Map of all available activities


 */


function
 
makeChoice_
(
attendee
,
 
activitiesById
)
 
{


  
for
 
(
let
 
i
 
=
 
0
;
 
i
 < 
attendee
.
preferences
.
length
;
 
++
i
)
 
{


    
const
 
activity
 
=
 
activitiesById
[
attendee
.
preferences
[
i
]];


    
if
 
(
!
activity
)
 
{


      
continue
;


    
}


    
const
 
canJoin
 
=
 
checkAvailability_
(
attendee
,
 
activity
);


    
if
 
(
canJoin
)
 
{


      
attendee
.
assigned
.
push
(
activity
);


      
activity
.
roster
.
push
(
attendee
);


      
break
;


    
}


  
}


}



/**


 * Checks that an activity has capacity and doesn't conflict with previously assigned


 * activities.


 *


 * @param {object} attendee - Attendee looking to join the activity


 * @param {object} activity - Proposed activity


 * @return {boolean} - True if attendee can join the activity


 */


function
 
checkAvailability_
(
attendee
,
 
activity
)
 
{


  
if
 
(
activity
.
capacity
 
<
=
 
activity
.
roster
.
length
)
 
{


    
return
 
false
;


  
}


  
const
 
timesConflict
 
=
 
attendee
.
assigned
.
some
(


    
(
assignedActivity
)
 
=
>

      
!
(


        
assignedActivity
.
startAt
.
getTime
()
 > 
activity
.
endAt
.
getTime
()
 
||


        
activity
.
startAt
.
getTime
()
 > 
assignedActivity
.
endAt
.
getTime
()


      
),


  
);


  
return
 
!
timesConflict
;


}



/**


 * Populates a sheet with the assigned activities for each attendee.


 *


 * @param {Spreadsheet} ss - Spreadsheet to write to.


 * @param {object[]} attendees - Array of attendees with their activity assignments


 */


function
 
writeAttendeeAssignments_
(
ss
,
 
attendees
)
 
{


  
const
 
sheet
 
=
 
findOrCreateSheetByName_
(
ss
,
 
"Activities by person"
);


  
sheet
.
clear
();


  
sheet
.
appendRow
([
"Email address"
,
 
"Activities"
]);


  
sheet
.
getRange
(
"B1:1"
).
merge
();


  
const
 
rows
 
=
 
attendees
.
map
((
attendee
)
 
=
>
 
{


    
// Prefill row to ensure consistent length otherwise


    
// can't bulk update the sheet with range.setValues()


    
const
 
row
 
=
 
fillArray_
([],
 
ACTIVITIES_PER_PERSON
 
+
 
1
,
 
""
);


    
row
[
0
]
 
=
 
attendee
.
email
;


    
attendee
.
assigned
.
forEach
((
activity
,
 
index
)
 
=
>
 
{


      
row
[
index
 
+
 
1
]
 
=
 
activity
.
description
;


    
});


    
return
 
row
;


  
});


  
bulkAppendRows_
(
sheet
,
 
rows
);


  
sheet
.
setFrozenRows
(
1
);


  
sheet
.
getRange
(
"1:1"
).
setFontWeight
(
"bold"
);


  
sheet
.
autoResizeColumns
(
1
,
 
sheet
.
getLastColumn
());


}



/**


 * Populates a sheet with the rosters for each activity.


 *


 * @param {Spreadsheet} ss - Spreadsheet to write to.


 * @param {object[]} activities - Array of activities with their rosters


 */


function
 
writeActivityRosters_
(
ss
,
 
activities
)
 
{


  
const
 
sheet
 
=
 
findOrCreateSheetByName_
(
ss
,
 
"Activity rosters"
);


  
sheet
.
clear
();


  
let
 
rows
 
=
 
activities
.
map
((
activity
)
 
=
>
 
{


    
const
 
roster
 
=
 
activity
.
roster
.
map
((
attendee
)
 
=
>
 
attendee
.
email
);


    
return
 
[
activity
.
description
].
concat
(
roster
);


  
});


  
// Transpose the data so each activity is a column


  
rows
 
=
 
transpose_
(
rows
,
 
""
);


  
bulkAppendRows_
(
sheet
,
 
rows
);


  
sheet
.
setFrozenRows
(
1
);


  
sheet
.
getRange
(
"1:1"
).
setFontWeight
(
"bold"
);


  
sheet
.
autoResizeColumns
(
1
,
 
sheet
.
getLastColumn
());


}



/**


 * Loads the activity schedule.


 *


 * @param {Spreadsheet} ss - Spreadsheet to load from


 * @return {object[]} Array of available activities.


 */


function
 
loadActivitySchedule_
(
ss
)
 
{


  
const
 
timeZone
 
=
 
ss
.
getSpreadsheetTimeZone
();


  
const
 
sheet
 
=
 
ss
.
getSheetByName
(
"Activity Schedule"
);


  
const
 
rows
 
=
 
sheet
.
getSheetValues
(


    
sheet
.
getFrozenRows
()
 
+
 
1
,


    
1
,


    
sheet
.
getLastRow
()
 
-
 
1
,


    
sheet
.
getLastRow
(),


  
);


  
const
 
activities
 
=
 
rows
.
map
((
row
,
 
index
)
 
=
>
 
{


    
const
 
name
 
=
 
row
[
0
];


    
const
 
startAt
 
=
 
new
 
Date
(
row
[
1
]);


    
const
 
endAt
 
=
 
new
 
Date
(
row
[
2
]);


    
const
 
capacity
 
=
 
Number
.
parseInt
(
row
[
3
]);


    
const
 
formattedStartAt
 
=
 
Utilities
.
formatDate
(


      
startAt
,


      
timeZone
,


      
"EEE hh:mm a"
,


    
);


    
const
 
formattedEndAt
 
=
 
Utilities
.
formatDate
(
endAt
,
 
timeZone
,
 
"hh:mm a"
);


    
const
 
description
 
=
 
Utilities
.
formatString
(


      
"%s (%s-%s)"
,


      
name
,


      
formattedStartAt
,


      
formattedEndAt
,


    
);


    
return
 
{


      
id
:
 
index
,


      
name
:
 
name
,


      
description
:
 
description
,


      
capacity
:
 
capacity
,


      
startAt
:
 
startAt
,


      
endAt
:
 
endAt
,


      
roster
:
 
[],


    
};


  
});


  
return
 
activities
;


}



/**


 * Loads the attendeee response data.


 *


 * @param {Spreadsheet} ss - Spreadsheet to load from


 * @param {number[]} allActivityIds - Full set of available activity IDs


 * @return {object[]} Array of parsed attendee respones.


 */


function
 
loadAttendeeResponses_
(
ss
,
 
allActivityIds
)
 
{


  
const
 
sheet
 
=
 
findResponseSheetForForm_
(
ss
);



  
if
 
(
!
sheet
 
||
 
sheet
.
getLastRow
()
 
===
 
1
)
 
{


    
return
 
undefined
;


  
}



  
const
 
rows
 
=
 
sheet
.
getSheetValues
(


    
sheet
.
getFrozenRows
()
 
+
 
1
,


    
1
,


    
sheet
.
getLastRow
()
 
-
 
1
,


    
sheet
.
getLastRow
(),


  
);


  
const
 
attendees
 
=
 
rows
.
map
((
row
)
 
=
>
 
{


    
const
 
_
 
=
 
row
.
shift
();
 
// Ignore timestamp


    
const
 
email
 
=
 
row
.
shift
();


    
const
 
autoAssign
 
=
 
row
.
pop
();


    
// Find ranked items in the response data.


    
let
 
preferences
 
=
 
row
.
reduce
((
prefs
,
 
value
,
 
index
)
 
=
>
 
{


      
const
 
match
 
=
 
value
.
match
(
/(\d+).*/
);


      
if
 
(
!
match
)
 
{


        
return
 
prefs
;


      
}


      
const
 
rank
 
=
 
Number
.
parseInt
(
match
[
1
])
 
-
 
1
;
 
// Convert ordinal to array index


      
prefs
[
rank
]
 
=
 
index
;


      
return
 
prefs
;


    
},
 
[]);


    
if
 
(
autoAssign
 
===
 
"Yes"
)
 
{


      
// If auto assigning additional activites, append a randomized list of all the activities.


      
// These will then be considered as if the attendee ranked them.


      
const
 
additionalChoices
 
=
 
shuffleArray_
(
allActivityIds
);


      
preferences
 
=
 
preferences
.
concat
(
additionalChoices
);


    
}


    
return
 
{


      
email
:
 
email
,


      
preferences
:
 
preferences
,


      
assigned
:
 
[],


    
};


  
});


  
return
 
attendees
;


}



/**


 * Simulates a large number of users responding to the form. This enables users to quickly


 * experience the full solution without having to collect sufficient form responses


 * through other means.


 */


function
 
generateTestData_
()
 
{


  
const
 
ss
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
();


  
const
 
sheet
 
=
 
findResponseSheetForForm_
(
ss
);


  
if
 
(
!
sheet
)
 
{


    
const
 
msg
 
=
 
"No response sheet found. Create the form and try again."
;


    
SpreadsheetApp
.
getUi
().
alert
(
msg
);


  
}


  
if
 
(
sheet
.
getLastRow
()
 > 
1
)
 
{


    
const
 
msg
 
=


      
"Response sheet is not empty, can not generate test data. "
 
+


      
"Remove responses and try again."
;


    
SpreadsheetApp
.
getUi
().
alert
(
msg
);


    
return
;


  
}



  
const
 
activities
 
=
 
loadActivitySchedule_
(
ss
);


  
const
 
choices
 
=
 
fillArray_
([],
 
activities
.
length
,
 
""
);


  
for
 
(
const
 
value
 
of
 
range_
(
1
,
 
5
))
 
{


    
choices
[
value
]
 
=
 
toOrdinal_
(
value
);


  
}



  
const
 
rows
 
=
 
range_
(
1
,
 
NUM_TEST_USERS
).
map
((
value
)
 
=
>
 
{


    
const
 
randomizedChoices
 
=
 
shuffleArray_
(
choices
);


    
const
 
email
 
=
 
Utilities
.
formatString
(
"person%d@example.com"
,
 
value
);


    
return
 
[
new
 
Date
(),
 
email
].
concat
(
randomizedChoices
).
concat
([
"Yes"
]);


  
});


  
bulkAppendRows_
(
sheet
,
 
rows
);


}



/**


 * Retrieves a sheet by name, creating it if it doesn't yet exist.


 *


 * @param {Spreadsheet} ss - Containing spreadsheet


 * @Param {string} name - Name of sheet to return


 * @return {Sheet} Sheet instance


 */


function
 
findOrCreateSheetByName_
(
ss
,
 
name
)
 
{


  
const
 
sheet
 
=
 
ss
.
getSheetByName
(
name
);


  
if
 
(
sheet
)
 
{


    
return
 
sheet
;


  
}


  
return
 
ss
.
insertSheet
(
name
);


}



/**


 * Faster version of appending multiple rows via ranges. Requires all rows are equal length.


 *


 * @param {Sheet} sheet - Sheet to append to


 * @param {Array<Array<object>>} rows - Rows to append


 */


function
 
bulkAppendRows_
(
sheet
,
 
rows
)
 
{


  
const
 
startRow
 
=
 
sheet
.
getLastRow
()
 
+
 
1
;


  
const
 
startColumn
 
=
 
1
;


  
const
 
numRows
 
=
 
rows
.
length
;


  
const
 
numColumns
 
=
 
rows
[
0
].
length
;


  
sheet
.
getRange
(
startRow
,
 
startColumn
,
 
numRows
,
 
numColumns
).
setValues
(
rows
);


}



/**


 * Copies and randomizes an array.


 *


 * @param {object[]} array - Array to shuffle


 * @return {object[]} randomized copy of the array


 */


function
 
shuffleArray_
(
array
)
 
{


  
const
 
clone
 
=
 
array
.
slice
(
0
);


  
for
 
(
let
 
i
 
=
 
clone
.
length
 
-
 
1
;
 
i
 > 
0
;
 
i
--
)
 
{


    
const
 
j
 
=
 
Math
.
floor
(
Math
.
random
()
 
*
 
(
i
 
+
 
1
));


    
const
 
temp
 
=
 
clone
[
i
];


    
clone
[
i
]
 
=
 
clone
[
j
];


    
clone
[
j
]
 
=
 
temp
;


  
}


  
return
 
clone
;


}



/**


 * Formats an number as an ordinal.


 *


 * See: https://stackoverflow.com/questions/13627308/add-st-nd-rd-and-th-ordinal-suffix-to-a-number/13627586


 *


 * @param {number} i - Number to format


 * @return {string} Formatted string


 */


function
 
toOrdinal_
(
i
)
 
{


  
const
 
j
 
=
 
i
 
%
 
10
;


  
const
 
k
 
=
 
i
 
%
 
100
;


  
if
 
(
j
 
===
 
1
 && 
k
 
!==
 
11
)
 
{


    
return
 
`
${
i
}
st`
;


  
}


  
if
 
(
j
 
===
 
2
 && 
k
 
!==
 
12
)
 
{


    
return
 
`
${
i
}
nd`
;


  
}


  
if
 
(
j
 
===
 
3
 && 
k
 
!==
 
13
)
 
{


    
return
 
`
${
i
}
rd`
;


  
}


  
return
 
`
${
i
}
th`
;


}



/**


 * Locates the sheet containing the form responses.


 *


 * @param {Spreadsheet} ss - Spreadsheet instance to search


 * @return {Sheet} Sheet with form responses, undefined if not found.


 */


function
 
findResponseSheetForForm_
(
ss
)
 
{


  
const
 
formUrl
 
=
 
ss
.
getFormUrl
();


  
if
 
(
!
ss
 
||
 
!
formUrl
)
 
{


    
return
 
undefined
;


  
}


  
const
 
sheets
 
=
 
ss
.
getSheets
();


  
for
 
(
const
 
i
 
in
 
sheets
)
 
{


    
if
 
(
sheets
[
i
].
getFormUrl
()
 
===
 
formUrl
)
 
{


      
return
 
sheets
[
i
];


    
}


  
}


  
return
 
undefined
;


}



/**


 * Fills an array with a value ([].fill() not supported in Apps Script).


 *


 * @param {object[]} arr - Array to fill


 * @param {number} length - Number of items to fill.


 * @param {object} value - Value to place at each index.


 * @return {object[]} the array, for chaining purposes


 */


function
 
fillArray_
(
arr
,
 
length
,
 
value
)
 
{


  
for
 
(
let
 
i
 
=
 
0
;
 
i
 < 
length
;
 
++
i
)
 
{


    
arr
[
i
]
 
=
 
value
;


  
}


  
return
 
arr
;


}



/**


 * Creates and fills an array with numbers in the range [start, end].


 *


 * @param {number} start - First value in the range, inclusive


 * @param {number} end - Last value in the range, inclusive


 * @return {number[]} Array of values representing the range


 */


function
 
range_
(
start
,
 
end
)
 
{


  
const
 
arr
 
=
 
[
start
];


  
let
 
i
 
=
 
start
;


  
while
 
(
i
 < 
end
)
 
{


    
i
 
+=
 
1
;


    
arr
.
push
(
i
);


  
}


  
return
 
arr
;


}



/**


 * Transposes a matrix/2d array. For cases where the rows are not the same length,


 * `fillValue` is used where no other value would otherwise be present.


 *


 * @param {Array<Array<object>>} arr - 2D array to transpose


 * @param {object} fillValue - Placeholder for undefined values created as a result


 *     of the transpose. Only required if rows aren't all of equal length.


 * @return {Array<Array<object>>} New transposed array


 */


function
 
transpose_
(
arr
,
 
fillValue
)
 
{


  
const
 
transposed
 
=
 
[];


  
for
 
(
const
 
[
rowIndex
,
 
row
]
 
of
 
arr
.
entries
())
 
{


    
for
 
(
const
 
[
colIndex
,
 
col
]
 
of
 
row
.
entries
())
 
{


      
transposed
[
colIndex
]
 
=


        
transposed
[
colIndex
]
 
||
 
fillArray_
([],
 
arr
.
length
,
 
fillValue
);


      
transposed
[
colIndex
][
rowIndex
]
 
=
 
row
[
colIndex
];


    
}


  
}


  
return
 
transposed
;


}
```
## Colaboradores
Google mantiene esta muestra con la ayuda de Expertos de Google Developers.
## Próximos pasos
- Menús personalizados en Google Workspace
- Extiende Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Verifica la exactitud de las declaraciones con un agente de IA del ADK y un modelo de Gemini

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Verifica la exactitud de las declaraciones con un agente de IA del ADK y un modelo de Gemini Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Avanzado Duración : 30 minutos Tipo de proyecto : Función personalizada
## Descripción general
Una función personalizada de verificación de datos para Hojas de cálculo de Google que se usará como un proyecto de Google Apps Script vinculado potenciado por un agente de Vertex AI y un modelo de Gemini.
En este ejemplo, se muestra cómo puedes usar dos potentes tipos de recursos de IA directamente en tus archivos de Hojas de cálculo:
- Agentes de IA para capacidades de razonamiento sofisticadas, de varios pasos y con múltiples herramientas usando agentes del ADK implementados en Vertex AI Agent Engine.
- Modelos de IA para acceder a capacidades avanzadas de comprensión, generación y resumen usando modelos de Gemini de Vertex AI
## Objetivos
- Comprender qué hace la solución
- Comprender cómo se implementa la solución
- Implementar el agente de Vertex AI
- Configurar la secuencia de comandos
- Ejecutar la secuencia de comandos
## Acerca de esta solución
La función personalizada de Hojas de cálculo se llama FACT_CHECK y funciona como una solución de extremo a extremo. Analiza una declaración, fundamenta su respuesta con la información web más reciente y muestra el resultado en el formato que necesitas:
`FACT_CHECK`
- Uso: =FACT_CHECK("Your statement here") para obtener un resultado conciso y resumido =FACT_CHECK("Your statement here", "Your output formatting instructions here") para obtener un formato de resultado específico
- =FACT_CHECK("Your statement here") para obtener un resultado conciso y resumido
`=FACT_CHECK("Your statement here")`
- =FACT_CHECK("Your statement here", "Your output formatting instructions here") para obtener un formato de resultado específico
`=FACT_CHECK("Your statement here", "Your output formatting
instructions here")`
- Razonamiento: Agente de IA del ADK de LLM Auditor (muestra de Python) .
- Formato de resultado: Modelo de Gemini .
Esta solución solicita APIs de REST de Vertex AI con UrlFetchApp .
## Arquitectura
En el siguiente diagrama, se muestra la arquitectura de los recursos de Google Workspace y Google Cloud que usa la función personalizada.
## Requisitos previos
Para usar esta muestra, necesitas los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
Un navegador web con acceso a Internet
- Requisitos previos del agente del ADK de LLM Auditor Python 3.11 o versiones posteriores: Para la instalación, sigue las instrucciones del sitio web oficial de Python . Python Poetry: Para la instalación, sigue las instrucciones del sitio web oficial de Poetry . Google Cloud CLI: Para la instalación, sigue las instrucciones del sitio web oficial de Google Cloud .
Requisitos previos del agente del ADK de LLM Auditor
- Python 3.11 o versiones posteriores: Para la instalación, sigue las instrucciones del sitio web oficial de Python .
- Python Poetry: Para la instalación, sigue las instrucciones del sitio web oficial de Poetry .
- Google Cloud CLI: Para la instalación, sigue las instrucciones del sitio web oficial de Google Cloud .
## Prepara el entorno
En esta sección, se muestra cómo crear y configurar un proyecto de Google Cloud.
### Crea un proyecto de Google Cloud
- En la consola de Google Cloud, ve a Menú menu > IAM y administración > Crear un proyecto . Ir a Crear un proyecto
Ir a Crear un proyecto
- En el campo Nombre del proyecto , ingresa un nombre descriptivo para tu proyecto. Opcional: Para editar el ID del proyecto , haz clic en Editar . El ID del proyecto no se puede cambiar después de que se crea el proyecto. Por lo tanto, elige un ID que abarque tus necesidades durante todo el ciclo de vida del proyecto.
Opcional: Para editar el ID del proyecto , haz clic en Editar . El ID del proyecto no se puede cambiar después de que se crea el proyecto. Por lo tanto, elige un ID que abarque tus necesidades durante todo el ciclo de vida del proyecto.
- En el campo Ubicación , haz clic en Explorar para mostrar las posibles ubicaciones de tu proyecto. Luego, haga clic en Seleccionar .
- Haz clic en Crear . La consola de Google Cloud navega a la página Panel y tu proyecto se crea en unos minutos.
En uno de los siguientes entornos de desarrollo, accede a Google Cloud CLI ( gcloud ):
`gcloud`
- Cloud Shell : Para usar una terminal en línea con la CLI de gcloud ya configurada, activa Cloud Shell. Activar Cloud Shell
- Shell local : Para usar un entorno de desarrollo local, instala y inicializa la gcloud CLI. Para crear un proyecto de Cloud, usa el comando gcloud projects create : gcloud projects create PROJECT_ID Reemplaza PROJECT_ID configurando el ID del proyecto que deseas crear.
`gcloud projects create`
```
gcloud projects create 
PROJECT_ID
```
### Habilita la facturación para el proyecto de Cloud
- En la consola de Google Cloud, ve a Facturación . Haz clic en el Menú menu > Facturación > Mis proyectos . Ir a Facturación de Mis proyectos
Ir a Facturación de Mis proyectos
- En Selecciona una organización , elige la organización asociada con tu proyecto de Google Cloud.
- En la fila del proyecto, abre el menú Acciones ( more_vert ), haz clic en Cambiar facturación y elige la cuenta de Facturación de Cloud.
- Haz clic en Establecer cuenta .
- Para ver una lista de las cuentas de facturación disponibles, ejecuta el siguiente comando: gcloud billing accounts list
```
gcloud billing accounts list
```
- Vincula una cuenta de facturación con un proyecto de Google Cloud: gcloud billing projects link PROJECT_ID --billing-account= BILLING_ACCOUNT_ID Reemplaza lo siguiente: PROJECT_ID es el ID del proyecto de Cloud para el que deseas habilitar la facturación. BILLING_ACCOUNT_ID es el ID de la cuenta de facturación que se vinculará con el proyecto de Google Cloud.
```
gcloud billing projects link 
PROJECT_ID
 --billing-account=
BILLING_ACCOUNT_ID
```
Reemplaza lo siguiente:
- PROJECT_ID es el ID del proyecto de Cloud para el que deseas habilitar la facturación.
`PROJECT_ID`
- BILLING_ACCOUNT_ID es el ID de la cuenta de facturación que se vinculará con el proyecto de Google Cloud.
`BILLING_ACCOUNT_ID`
### Habilita la API de Vertex AI
- En la consola de Google Cloud, habilita las APIs de Vertex AI y Cloud Resource Manager. Habilitar las API
En la consola de Google Cloud, habilita las APIs de Vertex AI y Cloud Resource Manager.
Habilitar las API
- Confirma que habilitas la API de Vertex AI en el proyecto de Cloud correcto y, luego, haz clic en Siguiente .
Confirma que habilitas la API de Vertex AI en el proyecto de Cloud correcto y, luego, haz clic en Siguiente .
- Confirma que habilitas la API correcta y, luego, haz clic en Habilitar .
Confirma que habilitas la API correcta y, luego, haz clic en Habilitar .
- Si es necesario, configura el proyecto de Cloud actual como el que creaste con el comando gcloud config set project : gcloud config set project PROJECT_ID Reemplaza PROJECT_ID por el ID del proyecto de Cloud que creaste.
Si es necesario, configura el proyecto de Cloud actual como el que creaste con el comando gcloud config set project :
`gcloud config set project`
```
gcloud
 
config
 
set
 
project
 
PROJECT_ID
```
Reemplaza PROJECT_ID por el ID del proyecto de Cloud que creaste.
- Habilita la API de Vertex AI con el comando gcloud services enable : gcloud services enable aiplatform.googleapis.com
Habilita la API de Vertex AI con el comando gcloud services enable :
`gcloud services enable`
```
gcloud
 
services
 
enable
 
aiplatform.googleapis.com
```
### Crea una cuenta de servicio en la consola de Google Cloud
Para crear una cuenta de servicio nueva con la función Vertex AI User , sigue estos pasos:
`Vertex AI User`
- En la consola de Google Cloud, ve a Menú menu > IAM y administración > Cuentas de servicio . Ir a Cuentas de servicio
Ir a Cuentas de servicio
- Haga clic en Crear cuenta de servicio .
- Completa los detalles de la cuenta de servicio y, luego, haz clic en Crear y continuar .
- Opcional: Asigna funciones a tu cuenta de servicio para otorgar acceso a los recursos de tu proyecto de Google Cloud. Para obtener más detalles, consulta Otorga, cambia y revoca el acceso a los recursos .
- Haz clic en Continuar .
- Opcional: Ingresa usuarios o grupos que puedan administrar esta cuenta de servicio y realizar acciones con ella. Para obtener más detalles, consulta Administra la identidad temporal como cuenta de servicio .
- Haz clic en Listo . Toma nota de la dirección de correo electrónico de la cuenta de servicio.
- Crea la cuenta de servicio: gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \ --display-name=" SERVICE_ACCOUNT_NAME "
```
gcloud iam service-accounts create 
SERVICE_ACCOUNT_NAME
 \


  --display-name="
SERVICE_ACCOUNT_NAME
"
```
- Opcional: Asigna funciones a tu cuenta de servicio para otorgar acceso a los recursos de tu proyecto de Google Cloud. Para obtener más detalles, consulta Otorga, cambia y revoca el acceso a los recursos .
La cuenta de servicio aparece en la página de cuentas de servicio. A continuación, crea una clave privada para la cuenta de servicio.
### Crea una clave privada
Para crear y descargar una clave privada para la cuenta de servicio, sigue estos pasos:
- En la consola de Google Cloud, ve a Menú menu > IAM y administración > Cuentas de servicio . Ir a Cuentas de servicio
Ir a Cuentas de servicio
- Selecciona tu cuenta de servicio.
- Haz clic en Claves > AGREGAR CLAVE > Crear clave nueva .
- Selecciona JSON y, luego, haz clic en Crear . Ya se generó y descargó el nuevo par de claves pública/privada en tu equipo como un archivo nuevo. Guarda el archivo JSON descargado como credentials.json en tu directorio de trabajo. Este archivo es la única copia de esta clave. Para obtener información sobre cómo almacenar tu clave de forma segura, consulta Cómo administrar claves para cuentas de servicio .
Ya se generó y descargó el nuevo par de claves pública/privada en tu equipo como un archivo nuevo. Guarda el archivo JSON descargado como credentials.json en tu directorio de trabajo. Este archivo es la única copia de esta clave. Para obtener información sobre cómo almacenar tu clave de forma segura, consulta Cómo administrar claves para cuentas de servicio .
`credentials.json`
- Haz clic en Cerrar .
Para obtener más información sobre las cuentas de servicio, consulta Cuentas de servicio en la documentación de Cloud IAM de Google Cloud.
## Implementa el agente de IA del ADK de LLM Auditor
- Si aún no lo hiciste, autentícate con tu cuenta de Google Cloud y configura Google Cloud CLI para usar tu proyecto de Google Cloud. gcloud auth application-default login gcloud config set project PROJECT_ID gcloud auth application-default set-quota-project PROJECT_ID Reemplaza PROJECT_ID con el ID del proyecto en la nube que creaste.
Si aún no lo hiciste, autentícate con tu cuenta de Google Cloud y configura Google Cloud CLI para usar tu proyecto de Google Cloud.
```
gcloud
 
auth
 
application-default
 
login


gcloud
 
config
 
set
 
project
 
PROJECT_ID


gcloud
 
auth
 
application-default
 
set-quota-project
 
PROJECT_ID
```
Reemplaza PROJECT_ID con el ID del proyecto en la nube que creaste.
- Descarga este repositorio de GitHub: Descargar
Descarga este repositorio de GitHub:
Descargar
- En tu entorno de desarrollo local preferido, extrae el archivo comprimido descargado y abre el directorio adk-samples/python/agents/llm-auditor . unzip adk-samples-main.zip cd adk-samples-main/python/agents/llm-auditor
En tu entorno de desarrollo local preferido, extrae el archivo comprimido descargado y abre el directorio adk-samples/python/agents/llm-auditor .
`adk-samples/python/agents/llm-auditor`
```
unzip
 
adk-samples-main.zip


cd
 
adk-samples-main/python/agents/llm-auditor
```
- Crea un nuevo bucket de Cloud Storage dedicado al agente del ADK. gcloud storage buckets create gs:// CLOUD_STORAGE_BUCKET_NAME --project = PROJECT_ID --location = PROJECT_LOCATION Reemplaza lo siguiente: CLOUD_STORAGE_BUCKET_NAME con un nombre de bucket único que deseas usar. PROJECT_ID con el ID del proyecto en la nube que creaste. PROJECT_LOCATION con la ubicación del proyecto en la nube que creaste
Crea un nuevo bucket de Cloud Storage dedicado al agente del ADK.
```
gcloud
 
storage
 
buckets
 
create
 
gs://
CLOUD_STORAGE_BUCKET_NAME
 
--project
=
PROJECT_ID
 
--location
=
PROJECT_LOCATION
```
Reemplaza lo siguiente:
- CLOUD_STORAGE_BUCKET_NAME con un nombre de bucket único que deseas usar.
- PROJECT_ID con el ID del proyecto en la nube que creaste.
- PROJECT_LOCATION con la ubicación del proyecto en la nube que creaste
- Configura las siguientes variables de entorno: export GOOGLE_GENAI_USE_VERTEXAI = true export GOOGLE_CLOUD_PROJECT = PROJECT_ID export GOOGLE_CLOUD_LOCATION = PROJECT_LOCATION export GOOGLE_CLOUD_STORAGE_BUCKET = CLOUD_STORAGE_BUCKET_NAME Reemplaza lo siguiente: CLOUD_STORAGE_BUCKET_NAME con el nombre del bucket que creaste. PROJECT_ID con el ID del proyecto en la nube que creaste. PROJECT_LOCATION con la ubicación del proyecto en la nube que creaste
Configura las siguientes variables de entorno:
```
export
 
GOOGLE_GENAI_USE_VERTEXAI
=
true


export
 
GOOGLE_CLOUD_PROJECT
=
PROJECT_ID


export
 
GOOGLE_CLOUD_LOCATION
=
PROJECT_LOCATION


export
 
GOOGLE_CLOUD_STORAGE_BUCKET
=
CLOUD_STORAGE_BUCKET_NAME
```
Reemplaza lo siguiente:
- CLOUD_STORAGE_BUCKET_NAME con el nombre del bucket que creaste.
- PROJECT_ID con el ID del proyecto en la nube que creaste.
- PROJECT_LOCATION con la ubicación del proyecto en la nube que creaste
- Instala y, luego, implementa el agente del ADK desde el entorno virtual. python3 -m venv myenv source myenv/bin/activate poetry install --with deployment python3 deployment/deploy.py --create
Instala y, luego, implementa el agente del ADK desde el entorno virtual.
```
python3
 
-m
 
venv
 
myenv


source
 
myenv/bin/activate


poetry
 
install
 
--with
 
deployment


python3
 
deployment/deploy.py
 
--create
```
- Recupera el ID del agente. Lo necesitarás más adelante para configurar la función personalizada. python3 deployment/deploy.py --list
Recupera el ID del agente. Lo necesitarás más adelante para configurar la función personalizada.
```
python3
 
deployment/deploy.py
 
--list
```
## Analiza el código de muestra
De manera opcional, antes de crear la nueva hoja de cálculo, tómate un momento para revisar y familiarizarte con el código de muestra alojado en GitHub.
Ver en GitHub
## Crea y configura en una hoja de cálculo nueva
- Para hacer una copia completa de la hoja de cálculo de muestra de Hojas de cálculo, incluido su proyecto de Apps Script vinculado al contenedor, haz clic en el siguiente botón: Copiar hoja de cálculo de Google
Para hacer una copia completa de la hoja de cálculo de muestra de Hojas de cálculo, incluido su proyecto de Apps Script vinculado al contenedor, haz clic en el siguiente botón:
Copiar hoja de cálculo de Google
- En la hoja de cálculo recién creada, ve a Extensiones > Apps Script .
En la hoja de cálculo recién creada, ve a Extensiones > Apps Script .
- En el proyecto de Apps Script, ve a Configuración del proyecto , haz clic Editar propiedades de la secuencia de comandos y, luego, en Agregar propiedad de la secuencia de comandos para agregar las siguientes propiedades de la secuencia de comandos: LOCATION con la ubicación del proyecto de Google Cloud creado en los pasos anteriores, como us-central1 GEMINI_MODEL_ID con el modelo de Gemini que deseas usar, como gemini-2.5-flash-lite REASONING_ENGINE_ID con el ID del agente del ADK de LLM Auditor implementado en los pasos anteriores, como 1234567890 SERVICE_ACCOUNT_KEY con la clave JSON de la cuenta de servicio descargada en los pasos anteriores, como { ... }
En el proyecto de Apps Script, ve a Configuración del proyecto , haz clic Editar propiedades de la secuencia de comandos y, luego, en Agregar propiedad de la secuencia de comandos para agregar las siguientes propiedades de la secuencia de comandos:
- LOCATION con la ubicación del proyecto de Google Cloud creado en los pasos anteriores, como us-central1
`LOCATION`
`us-central1`
- GEMINI_MODEL_ID con el modelo de Gemini que deseas usar, como gemini-2.5-flash-lite
`GEMINI_MODEL_ID`
`gemini-2.5-flash-lite`
- REASONING_ENGINE_ID con el ID del agente del ADK de LLM Auditor implementado en los pasos anteriores, como 1234567890
`REASONING_ENGINE_ID`
`1234567890`
- SERVICE_ACCOUNT_KEY con la clave JSON de la cuenta de servicio descargada en los pasos anteriores, como { ... }
`SERVICE_ACCOUNT_KEY`
`{ ... }`
- Haz clic en Guardar las propiedades de las secuencias de comandos
Haz clic en Guardar las propiedades de las secuencias de comandos
## Prueba la función personalizada
- Ve a la hoja de cálculo recién creada.
- Cambia las declaraciones en la columna A .
- Las fórmulas de la columna B se ejecutan y, luego, muestran los resultados de la verificación de datos.
## Limpia
Para evitar que se apliquen cargos a tu cuenta de Google Cloud por los recursos que usaste en este instructivo, te recomendamos que borres el proyecto de Cloud.
- En la consola de Google Cloud, ve a la página Administrar recursos . Haz clic en el Menú menu > IAM y administración > Administrar recursos . Ir a Resource Manager
Ir a Resource Manager
- En la lista de proyectos, selecciona el proyecto que deseas borrar y haz clic en Borrar delete .
- En el diálogo, escribe el ID del proyecto y, luego, haz clic en Cerrar para borrar el proyecto.
## Próximos pasos
- Planifica viajes con un agente de IA accesible en Google Workspace
- Compila agentes de Gemini Enterprise que estén bien integrados con los almacenes de datos, las APIs y los complementos de Workspace
- Compila agentes de Vertex AI que estén bien integrados con los almacenes de datos, las APIs y los complementos de Workspace
- Funciones personalizadas en Hojas de cálculo
- Extiende Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Enviar contenido seleccionado

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Enviar contenido seleccionado Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 20 minutos Tipo de proyecto : Automatización con un activador basado en eventos
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Si tienes varios tipos de contenido que te gustaría ofrecerle a tu público, puedes permitir que los usuarios elijan qué contenido recibir de ti con Formularios de Google. Esta solución permite que los usuarios seleccionen los temas que les interesan y, luego, les envía automáticamente por correo electrónico el contenido que eligieron.
### Cómo funciona
La secuencia de comandos instala un activador basado en eventos que se ejecuta cada vez que un usuario envía un formulario. Con cada envío de formulario, la secuencia de comandos crea y envía un correo electrónico desde una plantilla de Documentos de Google. El correo electrónico incluye el nombre del usuario y el contenido que seleccionó. El contenido que ofreces puede ser de cualquier tipo, siempre y cuando se haga referencia a él con una URL.
### Servicios de Apps Script
En esta solución, se usan los siguientes servicios:
- Servicio de secuencias de comandos : Instala el activador basado en eventos que se ejecuta cada vez que alguien envía el formulario.
- Servicio de Documentos : Abre la plantilla de Documentos que usa la secuencia de comandos para crear el correo electrónico.
- Servicio de correo electrónico : Crea y envía el correo electrónico con el nombre del usuario y la selección de contenido.
- Servicio de hojas de cálculo : Agrega una confirmación a la hoja Form responses después de que la secuencia de comandos envía el correo electrónico.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
- Haz clic en el siguiente botón para hacer una copia de la hoja de cálculo de Hojas de cálculo de Google Enviar contenido seleccionado . El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo: Crear una copia
Haz clic en el siguiente botón para hacer una copia de la hoja de cálculo de Hojas de cálculo de Google Enviar contenido seleccionado . El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo:
Crear una copia
- En la hoja de cálculo que copiaste, haz clic en Extensiones > Apps Script .
En la hoja de cálculo que copiaste, haz clic en Extensiones > Apps Script .
- En el menú desplegable de funciones, selecciona installTrigger .
En el menú desplegable de funciones, selecciona installTrigger .
- Haz clic en Ejecutar .
Haz clic en Ejecutar .
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
Importante : Si ejecutas installTrigger más de una vez, la secuencia de comandos crea varios activadores que envían un correo electrónico cada vez que un usuario envía el formulario. Para borrar los activadores adicionales y evitar los correos electrónicos duplicados, haz clic en Activadores alarm . Haz clic con el botón derecho en cada activador adicional y, luego, en Borrar activador .
## Ejecuta la secuencia de comandos:
- Vuelve a la hoja de cálculo y haz clic en Herramientas > Administrar formulario > Ir al formulario activo .
- Completa el formulario y haz clic en Enviar .
- Revisa tu correo electrónico para encontrar un mensaje con vínculos al contenido que seleccionaste.
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/automations/content-signup



/*


Copyright 2022 Google LLC



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



// To use your own template doc, update the below variable with the URL of your own Google Doc template.


// Make sure you update the sharing settings so that 'anyone'  or 'anyone in your organization' can view.


const
 
EMAIL_TEMPLATE_DOC_URL
 
=


  
"https://docs.google.com/document/d/1enes74gWsMG3dkK3SFO08apXkr0rcYBd3JHKOb2Nksk/edit?usp=sharing"
;


// Update this variable to customize the email subject.


const
 
EMAIL_SUBJECT
 
=
 
"Hello, here is the content you requested"
;



// Update this variable to the content titles and URLs you want to offer. Make sure you update the form so that the content titles listed here match the content titles you list in the form.


const
 
topicUrls
 
=
 
{


  
"Google Calendar how-to videos"
:


    
"https://www.youtube.com/playlist?list=PLU8ezI8GYqs7IPb_UdmUNKyUCqjzGO9PJ"
,


  
"Google Drive how-to videos"
:


    
"https://www.youtube.com/playlist?list=PLU8ezI8GYqs7Y5d1cgZm2Obq7leVtLkT4"
,


  
"Google Docs how-to videos"
:


    
"https://www.youtube.com/playlist?list=PLU8ezI8GYqs4JKwZ-fpBP-zSoWPL8Sit7"
,


  
"Google Sheets how-to videos"
:


    
"https://www.youtube.com/playlist?list=PLU8ezI8GYqs61ciKpXf_KkV7ZRbRHVG38"
,


};



/**


 * Installs a trigger on the spreadsheet for when someone submits a form.


 */


function
 
installTrigger
()
 
{


  
ScriptApp
.
newTrigger
(
"onFormSubmit"
)


    
.
forSpreadsheet
(
SpreadsheetApp
.
getActive
())


    
.
onFormSubmit
()


    
.
create
();


}



/**


 * Sends a customized email for every form response.


 *


 * @param {Object} event - Form submit event


 */


function
 
onFormSubmit
(
e
)
 
{


  
const
 
responses
 
=
 
e
.
namedValues
;



  
// If the question title is a label, it can be accessed as an object field.


  
// If it has spaces or other characters, it can be accessed as a dictionary.


  
const
 
timestamp
 
=
 
responses
.
Timestamp
[
0
];


  
const
 
email
 
=
 
responses
[
"Email address"
][
0
].
trim
();


  
const
 
name
 
=
 
responses
.
Name
[
0
].
trim
();


  
const
 
topicsString
 
=
 
responses
.
Topics
[
0
].
toLowerCase
();



  
// Parse topics of interest into a list (since there are multiple items


  
// that are saved in the row as blob of text).


  
const
 
topics
 
=
 
Object
.
keys
(
topicUrls
).
filter
((
topic
)
 
=
>
 
{


    
// indexOf searches for the topic in topicsString and returns a non-negative


    
// index if the topic is found, or it will return -1 if it's not found.


    
return
 
topicsString
.
indexOf
(
topic
.
toLowerCase
())
 
!==
 
-
1
;


  
});



  
// If there is at least one topic selected, send an email to the recipient.


  
let
 
status
 
=
 
""
;


  
if
 
(
topics
.
length
 > 
0
)
 
{


    
MailApp
.
sendEmail
({


      
to
:
 
email
,


      
subject
:
 
EMAIL_SUBJECT
,


      
htmlBody
:
 
createEmailBody
(
name
,
 
topics
),


    
});


    
status
 
=
 
"Sent"
;


  
}
 
else
 
{


    
status
 
=
 
"No topics selected"
;


  
}



  
// Append the status on the spreadsheet to the responses' row.


  
const
 
sheet
 
=
 
SpreadsheetApp
.
getActiveSheet
();


  
const
 
row
 
=
 
sheet
.
getActiveRange
().
getRow
();


  
const
 
column
 
=
 
e
.
values
.
length
 
+
 
1
;


  
sheet
.
getRange
(
row
,
 
column
).
setValue
(
status
);



  
console
.
log
(
`status=
${
status
}
; responses=
${
JSON
.
stringify
(
responses
)
}
`
);


}



/**


 * Creates email body and includes the links based on topic.


 *


 * @param {string} recipient - The recipient's email address.


 * @param {string[]} topics - List of topics to include in the email body.


 * @return {string} - The email body as an HTML string.


 */


function
 
createEmailBody
(
name
,
 
topics
)
 
{


  
let
 
topicsHtml
 
=
 
topics


    
.
map
((
topic
)
 
=
>
 
{


      
const
 
url
 
=
 
topicUrls
[
topic
];


      
return
 
`<li><a href="
${
url
}
"
>
${
topic
}
<
/a></li>`
;


    
})


    
.
join
(
""
);


  
topicsHtml
 
=
 
`<ul>
${
topicsHtml
}
<
/ul>`
;



  
// Make sure to update the emailTemplateDocId at the top.


  
const
 
docId
 
=
 
DocumentApp
.
openByUrl
(
EMAIL_TEMPLATE_DOC_URL
).
getId
();


  
let
 
emailBody
 
=
 
docToHtml
(
docId
);


  
emailBody
 
=
 
emailBody
.
replace
(
/{{NAME}}/g
,
 
name
);


  
emailBody
 
=
 
emailBody
.
replace
(
/{{TOPICS}}/g
,
 
topicsHtml
);


  
return
 
emailBody
;


}



/**


 * Downloads a Google Doc as an HTML string.


 *


 * @param {string} docId - The ID of a Google Doc to fetch content from.


 * @return {string} The Google Doc rendered as an HTML string.


 */


function
 
docToHtml
(
docId
)
 
{


  
// Downloads a Google Doc as an HTML string.


  
const
 
url
 
=
 
`https://docs.google.com/feeds/download/documents/export/Export?id=
${
docId
}
&
exportFormat=html`
;


  
const
 
param
 
=
 
{


    
method
:
 
"get"
,


    
headers
:
 
{
 
Authorization
:
 
`Bearer 
${
ScriptApp
.
getOAuthToken
()
}
`
 
},


    
muteHttpExceptions
:
 
true
,


  
};


  
return
 
UrlFetchApp
.
fetch
(
url
,
 
param
).
getContentText
();


}
```
```
</section>
```
## Colaboradores
Google mantiene esta muestra con la ayuda de los Google Developer Experts.
## Próximos pasos
- Activadores controlados por eventos
- Documentación de referencia sobre el servicio de Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Guía de inicio rápido de las funciones personalizadas

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Guía de inicio rápido de las funciones personalizadas Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Puedes usar Google Apps Script para escribir una función personalizada y, luego, usarla en Hojas de cálculo de Google como si fuera una función integrada.
En el siguiente ejemplo de inicio rápido, se crea una función personalizada que calcula el precio de venta de los artículos con descuento. El precio de oferta se muestra en dólares estadounidenses.
## Objetivos
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
- Crea una hoja de cálculo nueva .
- En la hoja de cálculo nueva, selecciona el elemento de menú Extensiones > Apps Script .
- Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código. Luego, haz clic en Guardar . /** * Calculates the sale price of a value at a given discount . * The sale price is formatted as US dollars . * * @ param { number } input The value to discount . * @ param { number } discount The discount to apply , such as . 5 or 50 % . * @ return The sale price formatted as USD . * @ customfunction */ function salePrice ( input, discount ) { let price = input - ( input * discount ); let dollarUS = Intl . NumberFormat ( "en-US" , { style : "currency" , currency : "USD" , }); return dollarUS . format ( price ); }
Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código. Luego, haz clic en Guardar .
```
/**


 
*
 
Calculates
 
the
 
sale
 
price
 
of
 
a
 
value
 
at
 
a
 
given
 
discount
.


 
*
 
The
 
sale
 
price
 
is
 
formatted
 
as
 
US
 
dollars
.


 
*


 
*
 
@
param
 
{
number
}
 
input
 
The
 
value
 
to
 
discount
.


 
*
 
@
param
 
{
number
}
 
discount
 
The
 
discount
 
to
 
apply
,
 
such
 
as
 
.
5
 
or
 
50
%
.


 
*
 
@
return
 
The
 
sale
 
price
 
formatted
 
as
 
USD
.


 
*
 
@
customfunction


 
*/


function
 
salePrice
(
input, discount
)
 
{


  
let
 
price
 
=
 
input
 
-
 
(
input
 
*
 
discount
);


  
let
 
dollarUS
 
=
 
Intl
.
NumberFormat
(
"en-US"
,
 
{


    
style
:
 
"currency"
,


    
currency
:
 
"USD"
,


});


  
return
 
dollarUS
.
format
(
price
);


}
```
## Ejecuta la secuencia de comandos:
- Vuelve a tu hoja de cálculo.
- En una celda, ingresa =salePrice(100,20) . El primer parámetro representa el precio original y el segundo parámetro representa el porcentaje de descuento. Si te encuentras en una ubicación que usa comas decimales, es posible que debas ingresar =salePrice(100;20) .
`=salePrice(100,20)`
`=salePrice(100;20)`
La fórmula que ingresas en la celda ejecuta la función en la secuencia de comandos que creaste en la sección anterior. La función genera un precio de oferta de $80.00 .
`$80.00`
## Próximos pasos
Para seguir aprendiendo a extender Hojas de cálculo con Apps Script, consulta los siguientes recursos:
- Funciones personalizadas de hojas de cálculo
- Menús personalizados en Google Workspace
- Extender Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Registra tiempos y actividades en el Calendario de Google y Hojas de cálculo de Google

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Registra tiempos y actividades en el Calendario de Google y Hojas de cálculo de Google Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 15 minutos Tipo de proyecto : Automatización con un menú personalizado
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura el entorno.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Hacer un seguimiento del tiempo dedicado a los proyectos de los clientes Puedes registrar el tiempo dedicado a tus proyectos en Calendario de Google y, luego, sincronizarlo con Hojas de cálculo de Google para crear una hoja de horas o importar tu actividad a otro sistema de administración de hojas de horas. Puedes categorizar tu tiempo por cliente, proyecto y tarea.
### Cómo funciona
La secuencia de comandos proporciona una barra lateral que te permite seleccionar los calendarios que quieres sincronizar, el período de sincronización y definir si quieres reemplazar los títulos y las descripciones de los eventos por la información ingresada en la hoja de cálculo. Una vez que configures esos parámetros, podrás sincronizar eventos y ver tus actividades en un panel.
La secuencia de comandos importa los eventos de los calendarios y el período que especificas desde Calendario a la hoja de cálculo. Puedes agregar clientes, proyectos y tareas a la hoja de categorías y, luego, etiquetar los eventos según corresponda en la hoja de horas . De esta manera, cuando veas la hoja del panel , podrás ver el tiempo total por cliente, proyecto y tarea.
### Servicios de Apps Script
En esta solución, se usan los siguientes servicios:
- Servicio HTML : Compila la barra lateral que se usa para configurar los parámetros de configuración de sincronización.
- Servicio de Properties : Almacena la configuración que el usuario selecciona en la barra lateral.
- Servicio de Calendar : Envía la información del evento a la hoja de cálculo.
- Servicio de hojas de cálculo : Escribe los eventos en la hoja de cálculo y, si está configurado, envía información actualizada sobre el título y la descripción al Calendario.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura tu entorno
Si planeas usar un calendario existente, puedes omitir este paso.
- Ve a calendar.google.com .
- Junto a Otros calendarios , haz clic en Agregar otros calendarios add > Crear calendario .
- Ponle un nombre al calendario y haz clic en Crear calendario .
- Agrega algunos eventos al calendario.
## Configura la secuencia de comandos
Haz clic en el siguiente botón para crear una copia de la hoja de cálculo de Hojas de cálculo de ejemplo Registrar el tiempo y las actividades :
Crear una copia
## Ejecuta la secuencia de comandos:
En las siguientes secciones, se te guiará para ejecutar la secuencia de comandos.
### Sincronizar eventos del calendario
- Haz clic en myTime > Configuración . Es posible que debas actualizar la página para que aparezca este menú personalizado.
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
- Vuelve a hacer clic en myTime > Configuración .
- En la lista de calendarios disponibles, selecciona el que creaste y cualquier otro que quieras sincronizar.
- Establece el resto de los parámetros de configuración y haz clic en Guardar .
- Haz clic en myTime > Sincronizar eventos del calendario .
### Configura el panel
- Ve a la hoja de cálculo Categories .
- Agregar clientes, proyectos y tareas
- Ve a la hoja Hours .
- Para cada evento sincronizado, selecciona el cliente, el proyecto y la tarea.
- Ve a la hoja de cálculo Panel . La primera sección proporciona los totales diarios. Para actualizar la lista de fechas de los totales diarios, cambia la fecha en la celda A1 . En la siguiente sección, se proporcionan los totales semanales y se corresponde con la fecha seleccionada en A1 . En las últimas tres secciones, se proporcionan los totales generales por tarea, proyecto y cliente.
- La primera sección proporciona los totales diarios. Para actualizar la lista de fechas de los totales diarios, cambia la fecha en la celda A1 .
`A1`
- En la siguiente sección, se proporcionan los totales semanales y se corresponde con la fecha seleccionada en A1 .
`A1`
- En las últimas tres secciones, se proporcionan los totales generales por tarea, proyecto y cliente.
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/automations/calendar-timesheet



/*


Copyright 2022 Jasper Duizendstra



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



/**


 * Runs when the spreadsheet is opened and adds the menu options


 * to the spreadsheet menu


 */


const
 
onOpen
 
=
 
()
 
=
>
 
{


  
SpreadsheetApp
.
getUi
()


    
.
createMenu
(
"myTime"
)


    
.
addItem
(
"Sync calendar events"
,
 
"run"
)


    
.
addItem
(
"Settings"
,
 
"settings"
)


    
.
addToUi
();


};



/**


 * Opens the sidebar


 */


const
 
settings
 
=
 
()
 
=
>
 
{


  
const
 
html
 
=


    
HtmlService
.
createHtmlOutputFromFile
(
"Page"
).
setTitle
(
"Settings"
);



  
SpreadsheetApp
.
getUi
().
showSidebar
(
html
);


};



/**


 * returns the settings from the script properties


 */


const
 
getSettings
 
=
 
()
 
=
>
 
{


  
const
 
settings
 
=
 
{};



  
// get the current settings


  
const
 
savedCalendarSettings
 
=
 
JSON
.
parse
(


    
PropertiesService
.
getScriptProperties
().
getProperty
(
"calendar"
)
 
||
 
"[]"
,


  
);



  
// get the primary calendar


  
const
 
primaryCalendar
 
=
 
CalendarApp
.
getAllCalendars
()


    
.
filter
((
cal
)
 
=
>
 
cal
.
isMyPrimaryCalendar
())


    
.
map
((
cal
)
 
=
>
 
({


      
name
:
 
"Primary calendar"
,


      
id
:
 
cal
.
getId
(),


    
}));



  
// get the secondary calendars


  
const
 
secundaryCalendars
 
=
 
CalendarApp
.
getAllCalendars
()


    
.
filter
((
cal
)
 
=
>
 
cal
.
isOwnedByMe
()
 && 
!
cal
.
isMyPrimaryCalendar
())


    
.
map
((
cal
)
 
=
>
 
({


      
name
:
 
cal
.
getName
(),


      
id
:
 
cal
.
getId
(),


    
}));



  
// the current available calendars


  
const
 
availableCalendars
 
=
 
primaryCalendar
.
concat
(
secundaryCalendars
);



  
// find any calendars that were removed


  
const
 
unavailebleCalendars
 
=
 
[];


  
for
 
(
const
 
savedCalendarSetting
 
of
 
savedCalendarSettings
)
 
{


    
if
 
(


      
!
availableCalendars
.
find
(


        
(
availableCalendar
)
 
=
>
 
availableCalendar
.
id
 
===
 
savedCalendarSetting
.
id
,


      
)


    
)
 
{


      
unavailebleCalendars
.
push
(
savedCalendarSetting
);


    
}


  
}



  
// map the current settings to the available calendars


  
const
 
calendarSettings
 
=
 
availableCalendars
.
map
((
availableCalendar
)
 
=
>
 
{


    
if
 
(


      
savedCalendarSettings
.
find
(


        
(
savedCalendar
)
 
=
>
 
savedCalendar
.
id
 
===
 
availableCalendar
.
id
,


      
)


    
)
 
{


      
availableCalendar
.
sync
 
=
 
true
;


    
}


    
return
 
availableCalendar
;


  
});



  
// add the calendar settings to the settings


  
settings
.
calendarSettings
 
=
 
calendarSettings
;



  
const
 
savedFrom
 
=


    
PropertiesService
.
getScriptProperties
().
getProperty
(
"syncFrom"
);


  
settings
.
syncFrom
 
=
 
savedFrom
;



  
const
 
savedTo
 
=
 
PropertiesService
.
getScriptProperties
().
getProperty
(
"syncTo"
);


  
settings
.
syncTo
 
=
 
savedTo
;



  
const
 
savedIsUpdateTitle
 
=


    
PropertiesService
.
getScriptProperties
().
getProperty
(
"isUpdateTitle"
)
 
===


    
"true"
;


  
settings
.
isUpdateCalendarItemTitle
 
=
 
savedIsUpdateTitle
;



  
const
 
savedIsUseCategoriesAsCalendarItemTitle
 
=


    
PropertiesService
.
getScriptProperties
().
getProperty
(


      
"isUseCategoriesAsCalendarItemTitle"
,


    
)
 
===
 
"true"
;


  
settings
.
isUseCategoriesAsCalendarItemTitle
 
=


    
savedIsUseCategoriesAsCalendarItemTitle
;



  
const
 
savedIsUpdateDescription
 
=


    
PropertiesService
.
getScriptProperties
().
getProperty
(


      
"isUpdateDescription"
,


    
)
 
===
 
"true"
;


  
settings
.
isUpdateCalendarItemDescription
 
=
 
savedIsUpdateDescription
;



  
return
 
settings
;


};



/**


 * Saves the settings from the sidebar


 */


const
 
saveSettings
 
=
 
(
settings
)
 
=
>
 
{


  
PropertiesService
.
getScriptProperties
().
setProperty
(


    
"calendar"
,


    
JSON
.
stringify
(
settings
.
calendarSettings
),


  
);


  
PropertiesService
.
getScriptProperties
().
setProperty
(


    
"syncFrom"
,


    
settings
.
syncFrom
,


  
);


  
PropertiesService
.
getScriptProperties
().
setProperty
(


    
"syncTo"
,


    
settings
.
syncTo
,


  
);


  
PropertiesService
.
getScriptProperties
().
setProperty
(


    
"isUpdateTitle"
,


    
settings
.
isUpdateCalendarItemTitle
,


  
);


  
PropertiesService
.
getScriptProperties
().
setProperty
(


    
"isUseCategoriesAsCalendarItemTitle"
,


    
settings
.
isUseCategoriesAsCalendarItemTitle
,


  
);


  
PropertiesService
.
getScriptProperties
().
setProperty
(


    
"isUpdateDescription"
,


    
settings
.
isUpdateCalendarItemDescription
,


  
);


  
return
 
"Settings saved"
;


};



/**


 * Builds the myTime object and runs the synchronisation


 */


const
 
run
 
=
 
()
 
=
>
 
{


  
myTime
({


    
mainSpreadsheetId
:
 
SpreadsheetApp
.
getActiveSpreadsheet
().
getId
(),


  
}).
run
();


};



/**


 * The main function used for the synchronisation


 * @param {Object} par The main parameter object.


 * @return {Object} The myTime Object.


 */


const
 
myTime
 
=
 
(
par
)
 
=
>
 
{


  
/**


   * Format the sheet


   */


  
const
 
formatSheet
 
=
 
()
 
=
>
 
{


    
// sort decending on start date


    
hourSheet
.
sort
(
3
,
 
false
);



    
// hide the technical columns


    
hourSheet
.
hideColumns
(
1
,
 
2
);



    
// remove any extra rows


    
if
 
(


      
hourSheet
.
getLastRow
()
 > 
1
 
&&

      
hourSheet
.
getLastRow
()
 < 
hourSheet
.
getMaxRows
()


    
)
 
{


      
hourSheet
.
deleteRows
(


        
hourSheet
.
getLastRow
()
 
+
 
1
,


        
hourSheet
.
getMaxRows
()
 
-
 
hourSheet
.
getLastRow
(),


      
);


    
}



    
// set the validation for the customers


    
let
 
rule
 
=
 
SpreadsheetApp
.
newDataValidation
()


      
.
requireValueInRange
(
categoriesSheet
.
getRange
(
"A2:A"
),
 
true
)


      
.
setAllowInvalid
(
true
)


      
.
build
();


    
hourSheet
.
getRange
(
"I2:I"
).
setDataValidation
(
rule
);



    
// set the validation for the projects


    
rule
 
=
 
SpreadsheetApp
.
newDataValidation
()


      
.
requireValueInRange
(
categoriesSheet
.
getRange
(
"B2:B"
),
 
true
)


      
.
setAllowInvalid
(
true
)


      
.
build
();


    
hourSheet
.
getRange
(
"J2:J"
).
setDataValidation
(
rule
);



    
// set the validation for the tsaks


    
rule
 
=
 
SpreadsheetApp
.
newDataValidation
()


      
.
requireValueInRange
(
categoriesSheet
.
getRange
(
"C2:C"
),
 
true
)


      
.
setAllowInvalid
(
true
)


      
.
build
();


    
hourSheet
.
getRange
(
"K2:K"
).
setDataValidation
(
rule
);



    
if
 
(
isUseCategoriesAsCalendarItemTitle
)
 
{


      
hourSheet


        
.
getRange
(
"L2:L"
)


        
.
setFormulaR1C1
(


          
'IF(OR(R[0]C[-3]="tbd";R[0]C[-2]="tbd";R[0]C[-1]="tbd");""; CONCATENATE(R[0]C[-3];"|";R[0]C[-2];"|";R[0]C[-1];"|"))'
,


        
);


    
}


    
// set the hours, month, week and number collumns


    
hourSheet


      
.
getRange
(
"P2:P"
)


      
.
setFormulaR1C1
(
'=IF(R[0]C[-12]="";"";R[0]C[-12]-R[0]C[-13])'
);


    
hourSheet


      
.
getRange
(
"Q2:Q"
)


      
.
setFormulaR1C1
(
'=IF(R[0]C[-13]="";"";month(R[0]C[-13]))'
);


    
hourSheet


      
.
getRange
(
"R2:R"
)


      
.
setFormulaR1C1
(
'=IF(R[0]C[-14]="";"";WEEKNUM(R[0]C[-14];2))'
);


    
hourSheet
.
getRange
(
"S2:S"
).
setFormulaR1C1
(
"=R[0]C[-3]"
);


  
};



  
/**


   * Activate the synchronisation


   */


  
function
 
run
()
 
{


    
console
.
log
(
"Started processing hours."
);



    
const
 
processCalendar
 
=
 
(
setting
)
 
=
>
 
{


      
SpreadsheetApp
.
flush
();



      
// current calendar info


      
const
 
calendarName
 
=
 
setting
.
name
;


      
const
 
calendarId
 
=
 
setting
.
id
;



      
console
.
log
(


        
`processing 
${
calendarName
}
 with the id 
${
calendarId
}
 from 
${
syncStartDate
}
 to 
${
syncEndDate
}
`
,


      
);



      
// get the calendar


      
const
 
calendar
 
=
 
CalendarApp
.
getCalendarById
(
calendarId
);



      
// get the calendar events and create lookups


      
const
 
events
 
=
 
calendar
.
getEvents
(
syncStartDate
,
 
syncEndDate
);


      
const
 
eventsLookup
 
=
 
events
.
reduce
((
jsn
,
 
event
)
 
=
>
 
{


        
jsn
[
event
.
getId
()]
 
=
 
event
;


        
return
 
jsn
;


      
},
 
{});



      
// get the sheet events and create lookups


      
const
 
existingEvents
 
=
 
hourSheet
.
getDataRange
().
getValues
().
slice
(
1
);


      
const
 
existingEventsLookUp
 
=
 
existingEvents
.
reduce
((
jsn
,
 
row
,
 
index
)
 
=
>
 
{


        
if
 
(
row
[
0
]
 
!==
 
calendarId
)
 
{


          
return
 
jsn
;


        
}


        
jsn
[
row
[
1
]]
 
=
 
{


          
event
:
 
row
,


          
row
:
 
index
 
+
 
2
,


        
};


        
return
 
jsn
;


      
},
 
{});



      
// handle a calendar event


      
const
 
handleEvent
 
=
 
(
event
)
 
=
>
 
{


        
const
 
eventId
 
=
 
event
.
getId
();



        
// new event


        
if
 
(
!
existingEventsLookUp
[
eventId
])
 
{


          
hourSheet
.
appendRow
([


            
calendarId
,


            
eventId
,


            
event
.
getStartTime
(),


            
event
.
getEndTime
(),


            
calendarName
,


            
event
.
getCreators
().
join
(
","
),


            
event
.
getTitle
(),


            
event
.
getDescription
(),


            
event
.
getTag
(
"Client"
)
 
||
 
"tbd"
,


            
event
.
getTag
(
"Project"
)
 
||
 
"tbd"
,


            
event
.
getTag
(
"Task"
)
 
||
 
"tbd"
,


            
isUpdateCalendarItemTitle
 
?
 
""
 
:
 
event
.
getTitle
(),


            
isUpdateCalendarItemDescription
 
?
 
""
 
:
 
event
.
getDescription
(),


            
event


              
.
getGuestList
()


              
.
map
((
guest
)
 
=
>
 
guest
.
getEmail
())


              
.
join
(
","
),


            
event
.
getLocation
(),


            
undefined
,


            
undefined
,


            
undefined
,


            
undefined
,


          
]);


          
return
 
true
;


        
}



        
// existing event


        
const
 
exisitingEvent
 
=
 
existingEventsLookUp
[
eventId
].
event
;


        
const
 
exisitingEventRow
 
=
 
existingEventsLookUp
[
eventId
].
row
;



        
if
 
(
event
.
getStartTime
()
 
-
 
exisitingEvent
[
startTimeColumn
 
-
 
1
]
 
!==
 
0
)
 
{


          
hourSheet


            
.
getRange
(
exisitingEventRow
,
 
startTimeColumn
)


            
.
setValue
(
event
.
getStartTime
());


        
}



        
if
 
(
event
.
getEndTime
()
 
-
 
exisitingEvent
[
endTimeColumn
 
-
 
1
]
 
!==
 
0
)
 
{


          
hourSheet


            
.
getRange
(
exisitingEventRow
,
 
endTimeColumn
)


            
.
setValue
(
event
.
getEndTime
());


        
}



        
if
 
(


          
event
.
getCreators
().
join
(
","
)
 
!==
 
exisitingEvent
[
creatorsColumn
 
-
 
1
]


        
)
 
{


          
hourSheet


            
.
getRange
(
exisitingEventRow
,
 
creatorsColumn
)


            
.
setValue
(
event
.
getCreators
()[
0
]);


        
}



        
if
 
(


          
event


            
.
getGuestList
()


            
.
map
((
guest
)
 
=
>
 
guest
.
getEmail
())


            
.
join
(
","
)
 
!==
 
exisitingEvent
[
guestListColumn
 
-
 
1
]


        
)
 
{


          
hourSheet
.
getRange
(
exisitingEventRow
,
 
guestListColumn
).
setValue
(


            
event


              
.
getGuestList
()


              
.
map
((
guest
)
 
=
>
 
guest
.
getEmail
())


              
.
join
(
","
),


          
);


        
}



        
if
 
(
event
.
getLocation
()
 
!==
 
exisitingEvent
[
locationColumn
 
-
 
1
])
 
{


          
hourSheet


            
.
getRange
(
exisitingEventRow
,
 
locationColumn
)


            
.
setValue
(
event
.
getLocation
());


        
}



        
if
 
(
event
.
getTitle
()
 
!==
 
exisitingEvent
[
titleColumn
 
-
 
1
])
 
{


          
if
 
(
!
isUpdateCalendarItemTitle
)
 
{


            
hourSheet


              
.
getRange
(
exisitingEventRow
,
 
titleColumn
)


              
.
setValue
(
event
.
getTitle
());


          
}


          
if
 
(
isUpdateCalendarItemTitle
)
 
{


            
event
.
setTitle
(
exisitingEvent
[
titleColumn
 
-
 
1
]);


          
}


        
}



        
if
 
(
event
.
getDescription
()
 
!==
 
exisitingEvent
[
descriptionColumn
 
-
 
1
])
 
{


          
if
 
(
!
isUpdateCalendarItemDescription
)
 
{


            
hourSheet


              
.
getRange
(
exisitingEventRow
,
 
descriptionColumn
)


              
.
setValue
(
event
.
getDescription
());


          
}


          
if
 
(
isUpdateCalendarItemDescription
)
 
{


            
event
.
setDescription
(
exisitingEvent
[
descriptionColumn
 
-
 
1
]);


          
}


        
}



        
return
 
true
;


      
};



      
// process each event for the calendar


      
events
.
every
(
handleEvent
);



      
// remove any events in the sheet that are not in de calendar


      
existingEvents
.
every
((
event
,
 
index
)
 
=
>
 
{


        
if
 
(
event
[
0
]
 
!==
 
calendarId
)
 
{


          
return
 
true
;


        
}



        
if
 
(
eventsLookup
[
event
[
1
]])
 
{


          
return
 
true
;


        
}



        
if
 
(
event
[
3
]
 < 
syncStartDate
)
 
{


          
return
 
true
;


        
}



        
hourSheet
.
getRange
(
index
 
+
 
2
,
 
1
,
 
1
,
 
20
).
clear
();


        
return
 
true
;


      
});



      
return
 
true
;


    
};



    
// process the calendars


    
settings
.
calendarSettings


      
.
filter
((
calenderSetting
)
 
=
>
 
calenderSetting
.
sync
 
===
 
true
)


      
.
every
(
processCalendar
);



    
formatSheet
();


    
SpreadsheetApp
.
setActiveSheet
(
hourSheet
);



    
console
.
log
(
"Finished processing hours."
);


  
}



  
const
 
mainSpreadSheetId
 
=
 
par
.
mainSpreadsheetId
;


  
const
 
mainSpreadsheet
 
=
 
SpreadsheetApp
.
openById
(
mainSpreadSheetId
);


  
const
 
hourSheet
 
=
 
mainSpreadsheet
.
getSheetByName
(
"Hours"
);


  
const
 
categoriesSheet
 
=
 
mainSpreadsheet
.
getSheetByName
(
"Categories"
);


  
const
 
settings
 
=
 
getSettings
();



  
const
 
syncStartDate
 
=
 
new
 
Date
();


  
syncStartDate
.
setDate
(
syncStartDate
.
getDate
()
 
-
 
Number
(
settings
.
syncFrom
));



  
const
 
syncEndDate
 
=
 
new
 
Date
();


  
syncEndDate
.
setDate
(
syncEndDate
.
getDate
()
 
+
 
Number
(
settings
.
syncTo
));



  
const
 
isUpdateCalendarItemTitle
 
=
 
settings
.
isUpdateCalendarItemTitle
;


  
const
 
isUseCategoriesAsCalendarItemTitle
 
=


    
settings
.
isUseCategoriesAsCalendarItemTitle
;


  
const
 
isUpdateCalendarItemDescription
 
=


    
settings
.
isUpdateCalendarItemDescription
;



  
const
 
startTimeColumn
 
=
 
3
;


  
const
 
endTimeColumn
 
=
 
4
;


  
const
 
creatorsColumn
 
=
 
6
;


  
const
 
originalTitleColumn
 
=
 
7
;


  
const
 
originalDescriptionColumn
 
=
 
8
;


  
const
 
clientColumn
 
=
 
9
;


  
const
 
projectColumn
 
=
 
10
;


  
const
 
taskColumn
 
=
 
11
;


  
const
 
titleColumn
 
=
 
12
;


  
const
 
descriptionColumn
 
=
 
13
;


  
const
 
guestListColumn
 
=
 
14
;


  
const
 
locationColumn
 
=
 
15
;



  
return
 
Object
.
freeze
({


    
run
:
 
run
,


  
});


};
```
```
</section>
<section>
  <h3>Page.html</h3>
```
```
<!DOCTYPE html>
<!--
 Copyright 2022 Google LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->

<html>

<head>
    <link rel="stylesheet" href="https://ssl.gstatic.com/docs/script/css/add-ons1.css">
    <style>
        #main {
            display: none
        }

        #categories-as-item-title {
            display: none
        }

        #show_title_warning {
            display: none
        }

        #show_description_warning {
            display: none
        }

        .red {
            color: red;
        }

        .branding-below {
            bottom: 56px;
            top: 0;
        }

        input[type=number] {
            width: 50px;
            height: 15px;
        }
    </style>
</head>

<body>
    <div class="sidebar branding-below" id="wait">
        Please wait...
    </div>
    <div class="sidebar branding-below" id="main">
        <div class="block" id="checks">
            <b>Synchronise calendars</b>
            <div>
                <span class="error" id="calendar-message"></span>
            </div>
        </div>

        <div class="block">
            <b>Synchronisation period</b>
            <br>Synchronise from the last <input type="number" name="sync-from" id="sync-from"> days
            <br>Synchronise up to the coming <input type="number" name="sync-to" id="sync-to"> days
        </div>

        <div class="block">
            <b>Update the calendar items</b><br>
            <input type="checkbox" id="is-update-calendar-item-title">
            <label for="is-update-calendar-item-title">Overwrite the calendar item title</label>
            <span class="secondary" id="show_title_warning">The calendar title will be overwritten with the values in
                title
                column of the sheet</span>
        </div>
        <div id="categories-as-item-title">
            <input type="checkbox" id="is-use-categories-as-item-title">
            <label for="is-use-categories-as-item-title">Use categories as the calendar item title</label>
        </div>
        <div class="block">
            <input type="checkbox" id="is-update-calendar-item-description">
            <label for="is-update-calendar-item-description">Overwrite the calendar item description</label>
            <span class="secondary" id="show_description_warning">The calendar description will be overwritten with the
                values in description column of the sheet</span>
        </div>
        <div class="block">
            <button class="blue" onClick="saveSettings()">Save</button>
        </div>
        <div class="block">
            <span class="error" id="generic-error"></span>
            <span class="gray" id="generic-message"></span>
        </div>

    </div>
    <div class="sidebar bottom">
        <span class="gray">
            myTime v1.2.0</span>
    </div>
</body>
<script>
    // event handler for categrories
    document.getElementById('is-update-calendar-item-title').addEventListener('change', (event) => {
        if (event.target.checked) {
            document.getElementById('categories-as-item-title').style.display = "block";
            document.getElementById('show_title_warning').style.display = "block";
        } else {
            document.getElementById('categories-as-item-title').style.display = "none";
            document.getElementById('is-use-categories-as-item-title').checked = false;
            document.getElementById('show_title_warning').style.display = "none";
        }
    })

    document.getElementById('is-update-calendar-item-description').addEventListener('change', (event) => {
        if (event.target.checked) {
            document.getElementById('show_description_warning').style.display = "block";
        } else {
            document.getElementById('show_description_warning').style.display = "none";
        }
    })

    // generic error handler
    const onFailure = (error) => {
        console.debug(error);
        document.getElementById('generic-error').innerHTML = error.message;
    }

    // receiving the settings
    const onSuccessGetSettings = (settings) => {
        console.debug(settings);

        settings.calendarSettings.forEach((calendar, index) => {
            const div = document.createElement('div');

            const check = document.createElement('input');
            check.className = 'calendar-check';
            check.className = 'calendar-check red';
            check.type = 'checkbox';
            check.id = 'calendar' + index;
            check.value = (calendar.id);
            check.name = (calendar.name);
            check.checked = (calendar.sync);

            const label = document.createElement('label')
            label.htmlFor = "calendar" + index;
            label.appendChild(document.createTextNode(calendar.name));
            if (index == 0) {
                label.className = 'red';
            }

            div.appendChild(check);
            div.appendChild(label);

            document.getElementById('checks').appendChild(div);
        });

        document.getElementById('sync-from').value = settings.syncFrom || 31;
        document.getElementById('sync-to').value = settings.syncTo || 31;
        document.getElementById('is-update-calendar-item-title').checked = settings.isUpdateCalendarItemTitle;

        if (settings.isUpdateCalendarItemTitle) {
            document.getElementById('categories-as-item-title').style.display = "block";
            document.getElementById('is-use-categories-as-item-title').checked = settings.isUseCategoriesAsCalendarItemTitle;
            document.getElementById('show_title_warning').style.display = "block";
        }

        if (settings.isUpdateCalendarItemDescription) {
            document.getElementById('is-update-calendar-item-description').checked = settings.isUpdateCalendarItemDescription;
            document.getElementById('show_description_warning').style.display = "block";
        }
        document.getElementById('wait').style.display = "none";
        document.getElementById('main').style.display = "block";


    }

    // receiving the settings saved confirmation
    const onSuccessSaveSettings = (msg) => {
        console.debug(msg);
        document.getElementById('generic-message').innerHTML = msg;
    }

    // save the settings
    const saveSettings = () => {
        document.getElementById('generic-message').innerHTML = '';
        const checks = document.getElementsByClassName('calendar-check');
        const calendarSettings = [];
        for (let check of checks) {
            if (!check.checked) {
                continue;
            }
            calendarSettings.push({
                name: check.name,
                id: check.value,
                sync: check.checked
            });
        }

        const settings = {};
        settings.calendarSettings = calendarSettings;
        settings.syncFrom = document.getElementById('sync-from').value;
        settings.syncTo = document.getElementById('sync-to').value;
        settings.isUpdateCalendarItemTitle = document.getElementById('is-update-calendar-item-title').checked;
        if (settings.isUpdateCalendarItemTitle) {
            settings.isUseCategoriesAsCalendarItemTitle = document.getElementById('is-use-categories-as-item-title').checked;
        }
        if (!settings.isUpdateCalendarItemTitle) {
            settings.isUseCategoriesAsCalendarItemTitle = false;
        }

        settings.isUpdateCalendarItemDescription = document.getElementById('is-update-calendar-item-description').checked;
        console.debug(settings)

        google.script.run
            .withFailureHandler(onFailure)
            .withSuccessHandler(onSuccessSaveSettings)
            .saveSettings(settings);
    }

    // get the initial settings
    google.script.run
        .withFailureHandler(onFailure)
        .withSuccessHandler(onSuccessGetSettings)
        .getSettings();
</script>

</html>
```
```
</section>
```
## Colaboradores
Esta muestra fue creada por Jasper Duizendstra, Cloud Architect de Google y experto en Google Developers. Encuentra a Jasper en Twitter: @Duizendstra .
Google mantiene esta muestra con la ayuda de los Google Developer Experts.
## Próximos pasos
- Menús personalizados en Google Workspace
- Documentación de referencia sobre el servicio de Calendario
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Compartir recursos con empleados nuevos

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Compartir recursos con empleados nuevos Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 20 minutos Tipo de proyecto : Automatización con un activador controlado por eventos
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Importante : Debes ser administrador de Google Workspace para usar esta solución.
Comparte recursos con los empleados nuevos en un solo paso. Esta solución usa un formulario en Formularios de Google para agregar empleados nuevos a un grupo en Grupos de Google. Si compartes recursos con la dirección de ese grupo, puedes darles a los empleados nuevos acceso a los recursos que necesitan.
Si tienes permiso para agregar usuarios a un grupo, puedes usar esta solución para distribuir la responsabilidad a otros miembros de tu equipo. Cuando envían el formulario, el activador controlado por eventos ejecuta la secuencia de comandos como tú y agrega el correo electrónico de la persona nueva al grupo.
De manera opcional, puedes activar las notificaciones para recibir un correo electrónico cada vez que alguien envíe el formulario .
### Cómo funciona
Cuando alguien envía un formulario con el correo electrónico de un usuario y el grupo al que se debe agregar, la secuencia de comandos verifica si la persona ya pertenece a ese grupo. Si es así, el usuario recibe un correo electrónico en el que se confirma que ya está en el grupo. De lo contrario, la secuencia de comandos agrega al usuario al grupo y le envía un correo electrónico de bienvenida.
### Servicios de Apps Script
En esta solución, se usan los siguientes servicios:
- Servicio de secuencias de comandos : Crea el activador que ejecuta la secuencia de comandos cada vez que alguien envía un formulario.
- Servicio de Grupos : Verifica si el correo electrónico enviado en el formulario ya es miembro del grupo.
- Servicio avanzado de Directorio del SDK de Admin : Agrega el correo electrónico enviado en el formulario al grupo.
- Servicio de correo electrónico : Envía un correo electrónico a la dirección de correo electrónico enviada en el formulario para confirmar su pertenencia a un grupo o darle la bienvenida.
- Servicio de hojas de cálculo : Agrega el estado del usuario a la hoja de cálculo de respuestas del formulario. El estado es Ya está en el grupo o Se agregó recientemente .
- Servicio de recuperación de URL : Recupera un documento de Google Docs como una cadena HTML. El documento contiene el contenido del correo electrónico que envía la secuencia de comandos.
## Requisitos previos
- Una cuenta de Google Workspace
- Debes ser administrador de Google Workspace
## Configura la secuencia de comandos
- Haz clic en el siguiente botón para copiar la hoja de cálculo Compartir recursos con empleados nuevos . El proyecto de Apps Script para esta solución está adjunto a la hoja de cálculo. Crear una copia
Haz clic en el siguiente botón para copiar la hoja de cálculo Compartir recursos con empleados nuevos . El proyecto de Apps Script para esta solución está adjunto a la hoja de cálculo.
Crear una copia
- Haz clic en Extensiones > Apps Script .
Haz clic en Extensiones > Apps Script .
- En Servicios , asegúrate de que aparezca el servicio AdminDirectory . Si es así, ve al paso 6. Si no es así, continúa con el siguiente paso.
En Servicios , asegúrate de que aparezca el servicio AdminDirectory . Si es así, ve al paso 6. Si no es así, continúa con el siguiente paso.
- Junto a Servicios , haz clic en Agregar un servicio add .
Junto a Servicios , haz clic en Agregar un servicio add .
- En el diálogo, selecciona API del SDK de Admin y haz clic en Agregar .
En el diálogo, selecciona API del SDK de Admin y haz clic en Agregar .
- En el menú desplegable de funciones, selecciona installTrigger .
En el menú desplegable de funciones, selecciona installTrigger .
- Haz clic en Ejecutar .
Haz clic en Ejecutar .
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
Importante : Si ejecutas esta función más de una vez, se generarán varios activadores y se enviarán correos electrónicos duplicados. Para borrar los activadores adicionales, sigue estos pasos:
- Haz clic en Activadores .
- Junto al activador, haz clic en Más > Borrar activador .
## Ejecuta la secuencia de comandos
- Regresa a la hoja de cálculo y haz clic en Herramientas > Administrar formulario > Ir al formulario publicado .
- Completa el formulario con tu dirección de correo electrónico y un grupo para el que tengas permiso para administrar la membresía, y haz clic en Enviar .
- Regresa a la hoja de cálculo y consulta la entrada del formulario. En la columna Estado, se muestra si tu dirección de correo electrónico se agregó al grupo o ya es miembro.
- Consulta tu correo electrónico para ver si recibiste un correo electrónico de bienvenida o una confirmación de tu membresía al grupo.
## Colaboradores
Google mantiene esta muestra con la ayuda de Expertos de Google Developers.
## Próximos pasos
- Activadores controlados por eventos
- Extiende Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Analiza la opinión de los comentarios con la API de Google Cloud Natural Language

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Analiza la opinión de los comentarios con la API de Google Cloud Natural Language Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Intermedio Duración : 20 minutos Tipo de proyecto : Automatización con un menú personalizado
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura el entorno.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Puedes analizar datos de texto, como comentarios abiertos, a gran escala. Para realizar análisis de entidades y análisis de sentimiento desde Hojas de cálculo de Google, esta solución usa el servicio UrlFetch para conectarse a la API de Google Cloud Natural Language .
### Cómo funciona
La secuencia de comandos recopila texto de la hoja de cálculo y se conecta a la API de Cloud Natural Language de Google para analizar las entidades y las opiniones presentes en la cadena. Una tabla dinámica resume la puntuación promedio de opiniones para cada entidad mencionada en todas las filas de datos de texto.
### Servicios de Apps Script
Esta solución usa los siguientes servicios:
- Servicio de hojas de cálculo : Envía los datos de texto a la API de Cloud Natural Language y marca cada fila como "Completa" una vez que se analiza su opinión.
- Servicio UrlFetch : Se conecta a la API de Cloud Natural Language de Google Cloud para realizar análisis de entidades y opiniones en el texto.
## Requisitos previos
Para usar esta muestra, necesitas los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
Un navegador web con acceso a Internet
- Un proyecto de Google Cloud con una cuenta de facturación asociada (consulta Habilita la facturación para un proyecto )
Un proyecto de Google Cloud con una cuenta de facturación asociada (consulta Habilita la facturación para un proyecto )
## Configura tu entorno
Para usar esta solución, completa los siguientes pasos de configuración.
### Abre tu proyecto de Cloud en la consola de Google Cloud
Si aún no está abierto, abre el proyecto de Cloud que deseas usar para esta muestra:
- En la consola de Google Cloud, ve a la página Seleccionar un proyecto . Selecciona un proyecto de Cloud
Selecciona un proyecto de Cloud
- Selecciona el proyecto de Google Cloud que deseas usar. O bien, haz clic en Crear proyecto y sigue las instrucciones en pantalla. Si creas un proyecto de Google Cloud, es posible que debas activar la facturación para el proyecto .
### Habilita la API de Cloud Natural Language de Google
Esta solución se conecta a la API de Cloud Natural Language de Google. Antes de usar las APIs de Google, debes activarlas en un proyecto de Google Cloud. Puedes activar una o más APIs en un solo proyecto de Google Cloud.
- En tu proyecto de Cloud, activa la API de Cloud Natural Language de Google. Activa la API
En tu proyecto de Cloud, activa la API de Cloud Natural Language de Google.
Activa la API
### Cómo configurar la pantalla de consentimiento de OAuth
Esta solución requiere un proyecto de Cloud con una pantalla de consentimiento configurada. La configuración de la pantalla de consentimiento de OAuth define lo que Google muestra a los usuarios y registra tu app para que puedas publicarla más adelante.
- En la Consola de APIs de Google, ve a Menú menu > Plataforma de autenticación de Google > Branding . Ir a Branding
Ir a Branding
- Si ya configuraste la plataforma de autenticación de Google, puedes configurar los siguientes parámetros de configuración de la pantalla de consentimiento de OAuth en Branding , Público y Acceso a los datos . Si ves un mensaje que dice Aún no se configuró la plataforma de autenticación de Google , haz clic en Comenzar :
- En Información de la app , en Nombre de la app , ingresa un nombre para la app.
- En Correo electrónico de asistencia al usuario , elige una dirección de correo electrónico de asistencia en la que los usuarios puedan comunicarse contigo si tienen preguntas sobre su consentimiento.
- Haz clic en Siguiente .
- En Público , selecciona Interno .
- Haz clic en Siguiente .
- En Información de contacto , ingresa una Dirección de correo electrónico en la que puedas recibir notificaciones sobre cualquier cambio en tu proyecto.
- Haz clic en Siguiente .
- En Finalizar , revisa la Política de Datos del Usuario de los Servicios de las APIs de Google y, si estás de acuerdo, selecciona Acepto la Política de Datos del Usuario de los Servicios de las APIs de Google .
- Haz clic en Continuar .
- Haz clic en Crear .
- Por ahora, puedes omitir la adición de permisos. En el futuro, cuando crees una app para usar fuera de tu organización de Google Workspace, debes cambiar el Tipo de usuario a Externo . Luego, agrega los permisos de autorización que requiere tu app. Para obtener más información, consulta la guía completa Configura el consentimiento de OAuth guide.
### Obtén una clave de API para la API de Cloud Natural Language
- Ve a la Consola de APIs de Google . Asegúrate de que esté abierto tu proyecto habilitado para la facturación.
- En la Consola de APIs de Google, ve a Menú menu > APIs y servicios > Credenciales . Ir a Credenciales
En la Consola de APIs de Google, ve a Menú menu > APIs y servicios > Credenciales .
Ir a Credenciales
- Haz clic en Crear credenciales > Clave de API .
Haz clic en Crear credenciales > Clave de API .
- Toma nota de tu clave de API para usarla en un paso posterior.
Toma nota de tu clave de API para usarla en un paso posterior.
## Configura la secuencia de comandos
Completa los siguientes pasos para configurar la secuencia de comandos.
### Crea el proyecto de Apps Script
- Haz clic en el siguiente botón para crear una copia de la hoja de cálculo de muestra Análisis de sentimiento para comentarios . El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo. Crear una copia
Haz clic en el siguiente botón para crear una copia de la hoja de cálculo de muestra Análisis de sentimiento para comentarios . El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo.
Crear una copia
- Haz clic en Extensiones > Apps Script .
Haz clic en Extensiones > Apps Script .
- Actualiza la siguiente variable en el archivo de secuencia de comandos con tu clave de API: const myApiKey = ' YOUR_API_KEY '; // Replace with your API key.
Actualiza la siguiente variable en el archivo de secuencia de comandos con tu clave de API:
```
const myApiKey = '
YOUR_API_KEY
'; // Replace with your API key.
```
- Haz clic en Guardar .
Haz clic en Guardar .
### Agrega datos de texto
- Vuelve a la hoja de cálculo.
- Agrega datos de texto a las columnas id y comments . Puedes usar muestras de opiniones de propiedades vacacionales de Kaggle o usar tus propios datos. Puedes agregar más columnas si es necesario, pero, para que se ejecute correctamente, la secuencia de comandos debe tener datos en las columnas id y comments .
## Ejecuta la secuencia de comandos
- En la parte superior de la hoja de cálculo, haz clic en Herramientas de opiniones > Marcar entidades y opiniones . Es posible que debas actualizar la página para que aparezca este menú personalizado.
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
- Vuelve a hacer clic en Herramientas de opiniones > Marcar entidades y opiniones .
- Cuando finalice la secuencia de comandos, cambia a la hoja Tabla dinámica para ver los resultados.
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver el código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/automations/feedback-sentiment-analysis



/*


Copyright 2022 Google LLC



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



// Sets API key for accessing Cloud Natural Language API.


const
 
myApiKey
 
=
 
"YOUR_API_KEY"
;
 
// Replace with your API key.



// Matches column names in Review Data sheet to variables.


const
 
COLUMN_NAME
 
=
 
{


  
COMMENTS
:
 
"comments"
,


  
ENTITY
:
 
"entity_sentiment"
,


  
ID
:
 
"id"
,


};



/**


 * Creates a Demo menu in Google Spreadsheets.


 */


function
 
onOpen
()
 
{


  
SpreadsheetApp
.
getUi
()


    
.
createMenu
(
"Sentiment Tools"
)


    
.
addItem
(
"Mark entities and sentiment"
,
 
"markEntitySentiment"
)


    
.
addToUi
();


}



/**


 * Analyzes entities and sentiment for each comment in


 * Review Data sheet and copies results into the


 * Entity Sentiment Data sheet.


 */


function
 
markEntitySentiment
()
 
{


  
// Sets variables for "Review Data" sheet


  
const
 
ss
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
();


  
const
 
dataSheet
 
=
 
ss
.
getSheetByName
(
"Review Data"
);


  
const
 
rows
 
=
 
dataSheet
.
getDataRange
();


  
const
 
numRows
 
=
 
rows
.
getNumRows
();


  
const
 
values
 
=
 
rows
.
getValues
();


  
const
 
headerRow
 
=
 
values
[
0
];



  
// Checks to see if "Entity Sentiment Data" sheet is present, and


  
// if not, creates a new sheet and sets the header row.


  
const
 
entitySheet
 
=
 
ss
.
getSheetByName
(
"Entity Sentiment Data"
);


  
if
 
(
entitySheet
 
==
 
null
)
 
{


    
ss
.
insertSheet
(
"Entity Sentiment Data"
);


    
const
 
entitySheet
 
=
 
ss
.
getSheetByName
(
"Entity Sentiment Data"
);


    
const
 
esHeaderRange
 
=
 
entitySheet
.
getRange
(
1
,
 
1
,
 
1
,
 
6
);


    
const
 
esHeader
 
=
 
[


      
[


        
"Review ID"
,


        
"Entity"
,


        
"Salience"
,


        
"Sentiment Score"
,


        
"Sentiment Magnitude"
,


        
"Number of mentions"
,


      
],


    
];


    
esHeaderRange
.
setValues
(
esHeader
);


  
}



  
// Finds the column index for comments, language_detected,


  
// and comments_english columns.


  
const
 
textColumnIdx
 
=
 
headerRow
.
indexOf
(
COLUMN_NAME
.
COMMENTS
);


  
const
 
entityColumnIdx
 
=
 
headerRow
.
indexOf
(
COLUMN_NAME
.
ENTITY
);


  
const
 
idColumnIdx
 
=
 
headerRow
.
indexOf
(
COLUMN_NAME
.
ID
);


  
if
 
(
entityColumnIdx
 
===
 
-
1
)
 
{


    
Browser
.
msgBox
(


      
`Error: Could not find the column named 
${
COLUMN_NAME
.
ENTITY
}
. Please create an empty column with header "entity_sentiment" on the Review Data tab.`
,


    
);


    
return
;
 
// bail


  
}



  
ss
.
toast
(
"Analyzing entities and sentiment..."
);


  
for
 
(
let
 
i
 
=
 
0
;
 
i
 < 
numRows
;
 
++
i
)
 
{


    
const
 
value
 
=
 
values
[
i
];


    
const
 
commentEnCellVal
 
=
 
value
[
textColumnIdx
];


    
const
 
entityCellVal
 
=
 
value
[
entityColumnIdx
];


    
const
 
reviewId
 
=
 
value
[
idColumnIdx
];



    
// Calls retrieveEntitySentiment function for each row that has a comment


    
// and also an empty entity_sentiment cell value.


    
if
 
(
commentEnCellVal
 && 
!
entityCellVal
)
 
{


      
const
 
nlData
 
=
 
retrieveEntitySentiment
(
commentEnCellVal
);


      
// Pastes each entity and sentiment score into Entity Sentiment Data sheet.


      
const
 
newValues
 
=
 
[];


      
for
 
(
let
 
entity
 
in
 
nlData
.
entities
)
 
{


        
entity
 
=
 
nlData
.
entities
[
entity
];


        
const
 
row
 
=
 
[


          
reviewId
,


          
entity
.
name
,


          
entity
.
salience
,


          
entity
.
sentiment
.
score
,


          
entity
.
sentiment
.
magnitude
,


          
entity
.
mentions
.
length
,


        
];


        
newValues
.
push
(
row
);


      
}


      
if
 
(
newValues
.
length
)
 
{


        
entitySheet


          
.
getRange
(


            
entitySheet
.
getLastRow
()
 
+
 
1
,


            
1
,


            
newValues
.
length
,


            
newValues
[
0
].
length
,


          
)


          
.
setValues
(
newValues
);


      
}


      
// Pastes "complete" into entity_sentiment column to denote completion of NL API call.


      
dataSheet
.
getRange
(
i
 
+
 
1
,
 
entityColumnIdx
 
+
 
1
).
setValue
(
"complete"
);


    
}


  
}


}



/**


 * Calls the Cloud Natural Language API with a string of text to analyze


 * entities and sentiment present in the string.


 * @param {String} the string for entity sentiment analysis


 * @return {Object} the entities and related sentiment present in the string


 */


function
 
retrieveEntitySentiment
(
line
)
 
{


  
const
 
apiKey
 
=
 
myApiKey
;


  
const
 
apiEndpoint
 
=
 
`https://language.googleapis.com/v1/documents:analyzeEntitySentiment?key=
${
apiKey
}
`
;


  
// Creates a JSON request, with text string, language, type and encoding


  
const
 
nlData
 
=
 
{


    
document
:
 
{


      
language
:
 
"en-us"
,


      
type
:
 
"PLAIN_TEXT"
,


      
content
:
 
line
,


    
},


    
encodingType
:
 
"UTF8"
,


  
};


  
// Packages all of the options and the data together for the API call.


  
const
 
nlOptions
 
=
 
{


    
method
:
 
"post"
,


    
contentType
:
 
"application/json"
,


    
payload
:
 
JSON
.
stringify
(
nlData
),


  
};


  
// Makes the API call.


  
const
 
response
 
=
 
UrlFetchApp
.
fetch
(
apiEndpoint
,
 
nlOptions
);


  
return
 
JSON
.
parse
(
response
);


}
```
## Colaboradores
Google mantiene esta muestra con la ayuda de Expertos de Google Developers.
## Próximos pasos
- Blog: Analiza texto en Hojas de cálculo con la API de Google Cloud Natural Language y Apps Script
- Documentación de la API de Cloud Natural Language de Google Cloud
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Guía de inicio rápido: Genera texto con Vertex AI

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Guía de inicio rápido: Genera texto con Vertex AI Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
En esta página, se explica cómo usar el servicio avanzado de Vertex AI de Google Apps Script para darle instrucciones al modelo Gemini 2.5 Flash para que genere texto.
Para obtener más información sobre el servicio avanzado de Vertex AI, consulta la documentación de referencia .
## Objetivos
- Configura el entorno.
- Crea un proyecto de Apps Script que use el servicio avanzado de Vertex AI.
- Ejecuta la secuencia de comandos para generar texto.
## Requisitos previos
- Un proyecto de Google Cloud con facturación habilitada. Para verificar que un proyecto existente tenga habilitada la facturación, consulta Verifica el estado de facturación de tus proyectos . Para crear un proyecto y configurar la facturación, consulta Crea un proyecto de Google Cloud .
## Configura tu entorno
En esta sección, se explica cómo configurar tu entorno en la consola de Google Cloud y Apps Script.
### Habilita la API de Vertex AI en tu proyecto de Cloud
- En la consola de Google Cloud, abre tu proyecto de Google Cloud y habilita la API de Vertex AI: Habilitar la API
En la consola de Google Cloud, abre tu proyecto de Google Cloud y habilita la API de Vertex AI:
Habilitar la API
- Confirma que habilitas la API en el proyecto de Cloud correcto y, luego, haz clic en Siguiente .
Confirma que habilitas la API en el proyecto de Cloud correcto y, luego, haz clic en Siguiente .
- Confirma que habilitas la API correcta y, luego, haz clic en Habilitar .
Confirma que habilitas la API correcta y, luego, haz clic en Habilitar .
### Crea y configura tu proyecto de Apps Script
Para crear y configurar tu proyecto de Apps Script, completa los siguientes pasos:
- Ve a script.google.com .
- Haz clic en Nuevo proyecto para crear un proyecto de Apps Script.
- En la parte superior izquierda, haz clic en Proyecto sin título .
- Nombra tu secuencia de comandos como Vertex AI quickstart y haz clic en Cambiar nombre .
#### Configura el servicio avanzado de Vertex AI
Para habilitar el servicio avanzado de Vertex AI y configurar el código, haz lo siguiente:
- En el editor de secuencias de comandos, ve a Servicios y haz clic en Agregar un servicio .
- En el menú desplegable, selecciona API de Vertex AI y haz clic en Agregar .
- Abre el archivo Code.gs y reemplaza el contenido por el siguiente código: /** * Main entry point to test the Vertex AI integration. */ function main () { const prompt = 'What is Apps Script in one sentence?' ; try { const response = callVertexAI ( prompt ); console . log ( `Response: ${ response } ` ); } catch ( error ) { console . error ( `Failed to call Vertex AI: ${ error . message } ` ); } } /** * Calls the Vertex AI Gemini model. * * @param {string} prompt - The user's input prompt. * @return {string} The text generated by the model. */ function callVertexAI ( prompt ) { // Configuration const projectId = ' GOOGLE_CLOUD_PROJECT_ID ' ; const region = 'us-central1' ; const modelName = 'gemini-2.5-flash' ; const model = `projects/ ${ projectId } /locations/ ${ region } /publishers/google/models/ ${ modelName } ` ; const payload = { contents : [{ role : 'user' , parts : [{ text : prompt }] }], generationConfig : { temperature : 0.1 , maxOutputTokens : 2048 } }; // Execute the request using the Vertex AI Advanced Service const response = VertexAI . Endpoints . generateContent ( payload , model ); // Use optional chaining for safe property access return response ? . candidates ? .[ 0 ] ? . content ? . parts ? .[ 0 ] ? . text || 'No response generated.' ; } Reemplaza GOOGLE_CLOUD_PROJECT_ID por el ID del proyecto de Cloud.
Abre el archivo Code.gs y reemplaza el contenido por el siguiente código:
`Code.gs`
```
/**


 * Main entry point to test the Vertex AI integration.


 */


function
 
main
()
 
{


  
const
 
prompt
 
=
 
'What is Apps Script in one sentence?'
;



  
try
 
{


    
const
 
response
 
=
 
callVertexAI
(
prompt
);


    
console
.
log
(
`Response: 
${
response
}
`
);


  
}
 
catch
 
(
error
)
 
{


    
console
.
error
(
`Failed to call Vertex AI: 
${
error
.
message
}
`
);


  
}


}



/**


 * Calls the Vertex AI Gemini model.


 *


 * @param {string} prompt - The user's input prompt.


 * @return {string} The text generated by the model.


 */


function
 
callVertexAI
(
prompt
)
 
{


  
// Configuration


  
const
 
projectId
 
=
 
'
GOOGLE_CLOUD_PROJECT_ID
'
;


  
const
 
region
 
=
 
'us-central1'
;


  
const
 
modelName
 
=
 
'gemini-2.5-flash'
;



  
const
 
model
 
=
 
`projects/
${
projectId
}
/locations/
${
region
}
/publishers/google/models/
${
modelName
}
`
;



  
const
 
payload
 
=
 
{


    
contents
:
 
[{


      
role
:
 
'user'
,


      
parts
:
 
[{


        
text
:
 
prompt


      
}]


    
}],


    
generationConfig
:
 
{


      
temperature
:
 
0.1
,


      
maxOutputTokens
:
 
2048


    
}


  
};



  
// Execute the request using the Vertex AI Advanced Service


  
const
 
response
 
=
 
VertexAI
.
Endpoints
.
generateContent
(
payload
,
 
model
);



  
// Use optional chaining for safe property access


  
return
 
response
?
.
candidates
?
.[
0
]
?
.
content
?
.
parts
?
.[
0
]
?
.
text
 
||
 
'No response generated.'
;


}
```
Reemplaza GOOGLE_CLOUD_PROJECT_ID por el ID del proyecto de Cloud.
`GOOGLE_CLOUD_PROJECT_ID`
- Haz clic en Guardar .
Haz clic en Guardar .
## Prueba la secuencia de comandos
- En el editor de secuencias de comandos, haz clic en Ejecutar para ejecutar la función main .
`main`
- Cuando se te solicite, autoriza la secuencia de comandos.
- Haz clic en Registro de ejecución para ver la respuesta de Vertex AI.
El servicio de Vertex AI muestra una respuesta a la instrucción What is Apps Script in one sentence? .
`What is Apps Script in one sentence?`
Por ejemplo, el registro de ejecución muestra una respuesta como la siguiente:
```
Response: Google Apps Script is a cloud-based, JavaScript platform that lets you
automate, integrate, and extend Google Workspace applications like Sheets, Docs,
and Gmail.
```
## Limpia
Para evitar que se apliquen cargos a tu cuenta de Google Cloud por los recursos que usaste en este instructivo, te recomendamos que borres el proyecto de Cloud.
- En la consola de Google Cloud, ve a la página Administrar recursos . Haz clic en el Menú menu > IAM y administración > Administrar recursos . Ir a Resource Manager
Ir a Resource Manager
- En la lista de proyectos, selecciona el proyecto que deseas borrar y haz clic en Borrar delete .
- En el diálogo, escribe el ID del proyecto y, luego, haz clic en Cerrar para borrar el proyecto.
Para evitar que se apliquen cargos a tu cuenta de Google Cloud por los recursos que usaste en esta guía de inicio rápido, te recomendamos que borres el proyecto de Cloud.
## Temas relacionados
- Documentación del servicio avanzado de Vertex AI
- Documentación de la plataforma de Vertex AI
- Consulta la galería de muestras de IA de Google Workspace
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Calcula un descuento de precios por niveles

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Calcula un descuento de precios por niveles Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 10 minutos Tipo de proyecto : Función personalizada
## Objetivos
- Comprender qué hace la solución
- Comprender qué hacen los servicios de Google Apps Script dentro de la solución
- Configurar la secuencia de comandos
- Ejecutar la secuencia de comandos
## Acerca de esta solución
Si ofreces un sistema de precios escalonados para tus clientes, esta función personalizada facilita el cálculo de los importes de descuento para tus precios en Hojas de cálculo de Google.
Aunque puedes usar la función integrada SUMPRODUCT para realizar un cálculo de precios escalonados, usar SUMPRODUCT es más complejo y menos flexible que la función personalizada de esta solución.
`SUMPRODUCT`
`SUMPRODUCT`
### Cómo funciona
Un modelo de precios escalonados significa que el costo de los bienes o servicios disminuye según la cantidad comprada.
Por ejemplo, imagina que tienes dos niveles: uno que va de USD 0 a USD 500 y tiene un descuento del 10%, y otro que va de USD 501 a USD 1,000 y tiene un descuento del 20%. Si el precio total para el que necesitas calcular un descuento es de USD 700, la secuencia de comandos multiplica los primeros USD 500 por el 10% y los USD 200 restantes por el 20%, lo que da un descuento total de USD 90.
Para un precio total determinado, la secuencia de comandos itera por los niveles especificados en la tabla de precios escalonados. Para cada parte del precio total que se encuentra dentro de un nivel, esa parte se multiplica por el valor porcentual asociado del nivel. El resultado es la suma del cálculo de cada nivel.
### Servicios de Apps Script
Esta solución usa el siguiente servicio:
- Servicio de hojas de cálculo : Toma el valor determinado y calcula qué parte del valor se debe multiplicar por el descuento porcentual de cada nivel.
## Requisitos previos
Para usar esta muestra, debes cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
Para crear una copia de la hoja de cálculo de la función personalizada de precios escalonados , haz clic en el siguiente botón:
Crear una copia
El proyecto de Apps Script para esta solución está adjunto a la hoja de cálculo.
## Ejecuta la secuencia de comandos
- En la hoja de cálculo copiada, la tabla de la fila 16 muestra un cálculo de precios de muestra para un producto de software como servicio (SaaS).
- Para calcular el importe del descuento, en la celda C20 , ingresa =tierPrice(C19,$B$3:$D$6) . El precio final se actualiza en la celda C21 . Si te encuentras en una ubicación que usa comas decimales, es posible que debas ingresar =tierPrice(C19;$B$3:$D$6) .
`C20`
`=tierPrice(C19,$B$3:$D$6)`
`C21`
`=tierPrice(C19;$B$3:$D$6)`
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver el código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/custom-functions/tier-pricing



/*


Copyright 2022 Google LLC



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



/**


 * Calculates the tiered pricing discount.


 *


 * You must provide a value to calculate its discount. The value can be a string or a reference


 * to a cell that contains a string.


 * You must provide a data table range, for example, $B$4:$D$7, that includes the


 * tier start, end, and percent columns. If your table has headers, don't include


 * the headers in the range.


 *


 * @param {string} value The value to calculate the discount for, which can be a string or a


 * reference to a cell that contains a string.


 * @param {string} table The tier table data range using A1 notation.


 * @return number The total discount amount for the value.


 * @customfunction


 *


 */


function
 
tierPrice
(
value
,
 
table
)
 
{


  
let
 
total
 
=
 
0
;


  
// Creates an array for each row of the table and loops through each array.


  
for
 
(
const
 
[
start
,
 
end
,
 
percent
]
 
of
 
table
)
 
{


    
// Checks if the value is less than the starting value of the tier. If it is less, the loop stops.


    
if
 
(
value
 < 
start
)
 
{


      
break
;


    
}


    
// Calculates the portion of the value to be multiplied by the tier's percent value.


    
const
 
amount
 
=
 
Math
.
min
(
value
,
 
end
)
 
-
 
start
;


    
// Multiplies the amount by the tier's percent value and adds the product to the total.


    
total
 
+=
 
amount
 
*
 
percent
;


  
}


  
return
 
total
;


}
```
## Modificaciones
Puedes editar la función personalizada tanto como quieras para que se adapte a tus necesidades. Para ver una adición opcional para actualizar manualmente los resultados de la función personalizada, haz clic en Actualizar resultados almacenados en caché :
#### Actualizar resultados almacenados en caché
A diferencia de las funciones integradas, Google almacena en caché las funciones personalizadas para optimizar el rendimiento. Por lo tanto, si cambias algo dentro de tu función personalizada, como un valor que se está calculando, es posible que no se fuerce una actualización de inmediato. Para actualizar el resultado de la función de forma manual, sigue estos pasos:
- Para agregar una casilla de verificación a una celda vacía, haz clic en Insertar > Casilla de verificación .
- Agrega la celda que tiene la casilla de verificación como un parámetro adicional de la función personalizada. Por ejemplo, si agregas una casilla de verificación a la celda D20 , actualiza la tierPrice() función en la celda C20 a =tierPrice(C19,$B$3:$D$6,D20) .
`D20`
`tierPrice()`
`C20`
`=tierPrice(C19,$B$3:$D$6,D20)`
- Marca o desmarca la casilla de verificación para actualizar los resultados de la función personalizada.
## Colaboradores
Google mantiene esta muestra con la ayuda de Expertos de Google Developers.
## Próximos pasos
- Funciones personalizadas en Hojas de cálculo
- Extiende Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Sube archivos a Google Drive desde Formularios de Google

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Sube archivos a Google Drive desde Formularios de Google Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 10 minutos Tipo de proyecto : Automatización con un activador basado en eventos
## Objetivos
Después de completar esta muestra, podrás hacer lo siguiente:
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Subir y organizar archivos de forma simultánea en Drive con Formularios El formulario incluye entradas para los archivos que se subirán y para la forma en que se deben organizar.
### Cómo funciona
Una función de configuración crea una carpeta para almacenar todos los archivos subidos y un activador que se ejecuta cada vez que alguien envía el formulario. Cuando un usuario completa el formulario, elige los archivos que se subirán y una subcarpeta para almacenarlos. Una vez que el usuario envía el formulario, la secuencia de comandos envía los archivos a la subcarpeta correspondiente. Si aún no existe la carpeta, la secuencia de comandos la creará.
### Servicios de Apps Script
En esta solución, se usan los siguientes servicios:
- Servicio de secuencias de comandos : Crea el activador que se ejecuta cada vez que alguien envía el formulario.
- Servicio de propiedades : Almacena el ID del activador que crea la secuencia de comandos durante la configuración para evitar activadores duplicados.
- Servicio de Drive : Durante la configuración, obtiene la ubicación del formulario en Drive y crea una carpeta en la misma ubicación. Cuando un usuario envía el formulario, el servicio de Drive direcciona los archivos a esa carpeta y, si se selecciona, a una subcarpeta designada. Si la subcarpeta aún no existe, la secuencia de comandos la creará.
- Servicio de Forms : Obtiene los archivos y el nombre de la carpeta que eligió el usuario después de enviar el formulario y los envía al servicio de Drive.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
### Crea el formulario
- Ve a forms.google.com y haz clic en En blanco add .
- Haz clic en Formulario sin título y cámbiale el nombre a Sube archivos a Drive .
- Haz clic en Pregunta sin título y cámbiale el nombre a Subfolder .
- En la pregunta Subcarpeta , haz clic en Más more_vert > Descripción .
- En Descripción , ingresa Selecciona la subcarpeta en la que se almacenarán tus archivos. Si seleccionas <None>, los archivos se almacenarán en la carpeta Uploaded files.
- Agrega las siguientes opciones a la pregunta Subfolder : <none> Proyecto A Proyecto B Proyecto C
- <none>
- Proyecto A
- Proyecto B
- Proyecto C
- Para que la pregunta sea obligatoria, haz clic en Obligatoria .
- Haz clic en Agregar pregunta add_circle .
- Haz clic en Opción múltiple y selecciona Subir archivo .
- Haz clic en Continuar .
- En Pregunta , ingresa Archivos para subir . Puedes elegir los tipos de archivos y la cantidad máxima de archivos que quieres permitir que suban los usuarios.
- Para que la pregunta sea obligatoria, haz clic en Obligatoria .
### Crea el proyecto de Apps Script
- En el formulario, haz clic en Más more_vert > Editor de secuencias de comandos .
- Haz clic en Untitled project y cambia el nombre del proyecto a Upload files to Drive .
- Para crear otro archivo de secuencia de comandos, haz clic en Agregar un archivo add > Secuencia de comandos . Asígnale el nombre Setup al archivo.
`Setup`
- Reemplaza el contenido de ambos archivos de secuencias de comandos por el siguiente: Code.gs Setup.gs Más solutions/automations/upload-files/Code.js Ver en GitHub // TODO Before you start using this sample, you must run the setUp() // function in the Setup.gs file. // Application constants const APP_TITLE = "Upload files to Drive from Forms" ; const APP_FOLDER_NAME = "Upload files to Drive (File responses)" ; // Identifies the subfolder form item const APP_SUBFOLDER_ITEM = "Subfolder" ; const APP_SUBFOLDER_NONE = "<None>" ; /** * Gets the file uploads from a form response and moves files to the corresponding subfolder. * * @param {object} event - Form submit. */ function onFormSubmit ( e ) { try { // Gets the application root folder. let destFolder = getFolder_ ( APP_FOLDER_NAME ); // Gets all form responses. const itemResponses = e . response . getItemResponses (); // Determines the subfolder to route the file to, if any. let subFolderName ; const dest = itemResponses . filter ( ( itemResponse ) = > itemResponse . getItem (). getTitle (). toString () === APP_SUBFOLDER_ITEM , ); // Gets the destination subfolder name, but ignores if APP_SUBFOLDER_NONE was selected; if ( dest . length > 0 ) { if ( dest [ 0 ]. getResponse () !== APP_SUBFOLDER_NONE ) { subFolderName = dest [ 0 ]. getResponse (); } } // Gets the subfolder or creates it if it doesn't exist. if ( subFolderName !== undefined ) { destFolder = getSubFolder_ ( destFolder , subFolderName ); } console . log ( `Destination folder to use: Name: ${ destFolder . getName () } ID: ${ destFolder . getId () } URL: ${ destFolder . getUrl () } ` ); // Gets the file upload response as an array to allow for multiple files. const fileUploads = itemResponses . filter ( ( itemResponse ) = > itemResponse . getItem (). getType (). toString () === "FILE_UPLOAD" , ) . map (( itemResponse ) = > itemResponse . getResponse ()) . reduce (( a , b ) = > a . concat ( b ), []); // Moves the files to the destination folder. if ( fileUploads . length > 0 ) { for ( const fileId of fileUploads ) { DriveApp . getFileById ( fileId ). moveTo ( destFolder ); console . log ( `File Copied: ${ fileId } ` ); } } } catch ( err ) { console . log ( err ); } } /** * Returns a Drive folder under the passed in objParentFolder parent * folder. Checks if folder of same name exists before creating, returning * the existing folder or the newly created one if not found. * * @param {object} objParentFolder - Drive folder as an object. * @param {string} subFolderName - Name of subfolder to create/return. * @return {object} Drive folder */ function getSubFolder_ ( objParentFolder , subFolderName ) { // Iterates subfolders of parent folder to check if folder already exists. const subFolders = objParentFolder . getFolders (); while ( subFolders . hasNext ()) { const folder = subFolders . next (); // Returns the existing folder if found. if ( folder . getName () === subFolderName ) { return folder ; } } // Creates a new folder if one doesn't already exist. return objParentFolder . createFolder ( subFolderName ) . setDescription ( `Created by ${ APP_TITLE } application to store uploaded Forms files.` , ); } solutions/automations/upload-files/Setup.js Ver en GitHub // TODO You must run the setUp() function before you start using this sample. /** * The setUp() function performs the following: * - Creates a Google Drive folder named by the APP_FOLDER_NAME * variable in the Code.gs file. * - Creates a trigger to handle onFormSubmit events. */ function setUp () { // Ensures the root destination folder exists. const appFolder = getFolder_ ( APP_FOLDER_NAME ); if ( appFolder !== null ) { console . log ( `Application folder setup. Name: ${ appFolder . getName () } ID: ${ appFolder . getId () } URL: ${ appFolder . getUrl () } ` ); } else { console . log ( "Could not setup application folder." ); } // Calls the function that creates the Forms onSubmit trigger. installTrigger_ (); } /** * Returns a folder to store uploaded files in the same location * in Drive where the form is located. First, it checks if the folder * already exists, and creates it if it doesn't. * * @param {string} folderName - Name of the Drive folder. * @return {object} Google Drive Folder */ function getFolder_ ( folderName ) { // Gets the Drive folder where the form is located. const ssId = FormApp . getActiveForm (). getId (); const parentFolder = DriveApp . getFileById ( ssId ). getParents (). next (); // Iterates through the subfolders to check if folder already exists. // The script checks for the folder name specified in the APP_FOLDER_NAME variable. const subFolders = parentFolder . getFolders (); while ( subFolders . hasNext ()) { const folder = subFolders . next (); // Returns the existing folder if found. if ( folder . getName () === folderName ) { return folder ; } } // Creates a new folder if one doesn't already exist. return parentFolder . createFolder ( folderName ) . setDescription ( `Created by ${ APP_TITLE } application to store uploaded files.` , ); } /** * Installs trigger to capture onFormSubmit event when a form is submitted. * Ensures that the trigger is only installed once. * Called by setup(). */ function installTrigger_ () { // Ensures existing trigger doesn't already exist. const propTriggerId = PropertiesService . getScriptProperties (). getProperty ( "triggerUniqueId" ); if ( propTriggerId !== null ) { const triggers = ScriptApp . getProjectTriggers (); for ( const t in triggers ) { if ( triggers [ t ]. getUniqueId () === propTriggerId ) { console . log ( `Trigger with the following unique ID already exists: ${ propTriggerId } ` , ); return ; } } } // Creates the trigger if one doesn't exist. const triggerUniqueId = ScriptApp . newTrigger ( "onFormSubmit" ) . forForm ( FormApp . getActiveForm ()) . onFormSubmit () . create () . getUniqueId (); PropertiesService . getScriptProperties (). setProperty ( "triggerUniqueId" , triggerUniqueId , ); console . log ( `Trigger with the following unique ID was created: ${ triggerUniqueId } ` , ); } /** * Removes all script properties and triggers for the project. * Use primarily to test setup routines. */ function removeTriggersAndScriptProperties () { PropertiesService . getScriptProperties (). deleteAllProperties (); // Removes all triggers associated with project. const triggers = ScriptApp . getProjectTriggers (); for ( const t in triggers ) { ScriptApp . deleteTrigger ( triggers [ t ]); } } /** * Removes all form responses to reset the form. */ function deleteAllResponses () { FormApp . getActiveForm (). deleteAllResponses (); }
Reemplaza el contenido de ambos archivos de secuencias de comandos por el siguiente:
```
// TODO Before you start using this sample, you must run the setUp()


// function in the Setup.gs file.



// Application constants


const
 
APP_TITLE
 
=
 
"Upload files to Drive from Forms"
;


const
 
APP_FOLDER_NAME
 
=
 
"Upload files to Drive (File responses)"
;



// Identifies the subfolder form item


const
 
APP_SUBFOLDER_ITEM
 
=
 
"Subfolder"
;


const
 
APP_SUBFOLDER_NONE
 
=
 
"<None>"
;



/**


 * Gets the file uploads from a form response and moves files to the corresponding subfolder.


 *


 * @param {object} event - Form submit.


 */


function
 
onFormSubmit
(
e
)
 
{


  
try
 
{


    
// Gets the application root folder.


    
let
 
destFolder
 
=
 
getFolder_
(
APP_FOLDER_NAME
);



    
// Gets all form responses.


    
const
 
itemResponses
 
=
 
e
.
response
.
getItemResponses
();



    
// Determines the subfolder to route the file to, if any.


    
let
 
subFolderName
;


    
const
 
dest
 
=
 
itemResponses
.
filter
(


      
(
itemResponse
)
 
=
>

        
itemResponse
.
getItem
().
getTitle
().
toString
()
 
===
 
APP_SUBFOLDER_ITEM
,


    
);



    
// Gets the destination subfolder name, but ignores if APP_SUBFOLDER_NONE was selected;


    
if
 
(
dest
.
length
 > 
0
)
 
{


      
if
 
(
dest
[
0
].
getResponse
()
 
!==
 
APP_SUBFOLDER_NONE
)
 
{


        
subFolderName
 
=
 
dest
[
0
].
getResponse
();


      
}


    
}


    
// Gets the subfolder or creates it if it doesn't exist.


    
if
 
(
subFolderName
 
!==
 
undefined
)
 
{


      
destFolder
 
=
 
getSubFolder_
(
destFolder
,
 
subFolderName
);


    
}


    
console
.
log
(
`Destination folder to use:


    Name: 
${
destFolder
.
getName
()
}


    ID: 
${
destFolder
.
getId
()
}


    URL: 
${
destFolder
.
getUrl
()
}
`
);



    
// Gets the file upload response as an array to allow for multiple files.


    
const
 
fileUploads
 
=
 
itemResponses


      
.
filter
(


        
(
itemResponse
)
 
=
>

          
itemResponse
.
getItem
().
getType
().
toString
()
 
===
 
"FILE_UPLOAD"
,


      
)


      
.
map
((
itemResponse
)
 
=
>
 
itemResponse
.
getResponse
())


      
.
reduce
((
a
,
 
b
)
 
=
>
 
a
.
concat
(
b
),
 
[]);



    
// Moves the files to the destination folder.


    
if
 
(
fileUploads
.
length
 > 
0
)
 
{


      
for
 
(
const
 
fileId
 
of
 
fileUploads
)
 
{


        
DriveApp
.
getFileById
(
fileId
).
moveTo
(
destFolder
);


        
console
.
log
(
`File Copied: 
${
fileId
}
`
);


      
}


    
}


  
}
 
catch
 
(
err
)
 
{


    
console
.
log
(
err
);


  
}


}



/**


 * Returns a Drive folder under the passed in objParentFolder parent


 * folder. Checks if folder of same name exists before creating, returning


 * the existing folder or the newly created one if not found.


 *


 * @param {object} objParentFolder - Drive folder as an object.


 * @param {string} subFolderName - Name of subfolder to create/return.


 * @return {object} Drive folder


 */


function
 
getSubFolder_
(
objParentFolder
,
 
subFolderName
)
 
{


  
// Iterates subfolders of parent folder to check if folder already exists.


  
const
 
subFolders
 
=
 
objParentFolder
.
getFolders
();


  
while
 
(
subFolders
.
hasNext
())
 
{


    
const
 
folder
 
=
 
subFolders
.
next
();



    
// Returns the existing folder if found.


    
if
 
(
folder
.
getName
()
 
===
 
subFolderName
)
 
{


      
return
 
folder
;


    
}


  
}


  
// Creates a new folder if one doesn't already exist.


  
return
 
objParentFolder


    
.
createFolder
(
subFolderName
)


    
.
setDescription
(


      
`Created by 
${
APP_TITLE
}
 application to store uploaded Forms files.`
,


    
);


}
```
```
// TODO You must run the setUp() function before you start using this sample.



/**


 * The setUp() function performs the following:


 *  - Creates a Google Drive folder named by the APP_FOLDER_NAME


 *    variable in the Code.gs file.


 *  - Creates a trigger to handle onFormSubmit events.


 */


function
 
setUp
()
 
{


  
// Ensures the root destination folder exists.


  
const
 
appFolder
 
=
 
getFolder_
(
APP_FOLDER_NAME
);


  
if
 
(
appFolder
 
!==
 
null
)
 
{


    
console
.
log
(
`Application folder setup.


    Name: 
${
appFolder
.
getName
()
}


    ID: 
${
appFolder
.
getId
()
}


    URL: 
${
appFolder
.
getUrl
()
}
`
);


  
}
 
else
 
{


    
console
.
log
(
"Could not setup application folder."
);


  
}


  
// Calls the function that creates the Forms onSubmit trigger.


  
installTrigger_
();


}



/**


 * Returns a folder to store uploaded files in the same location


 * in Drive where the form is located. First, it checks if the folder


 * already exists, and creates it if it doesn't.


 *


 * @param {string} folderName - Name of the Drive folder.


 * @return {object} Google Drive Folder


 */


function
 
getFolder_
(
folderName
)
 
{


  
// Gets the Drive folder where the form is located.


  
const
 
ssId
 
=
 
FormApp
.
getActiveForm
().
getId
();


  
const
 
parentFolder
 
=
 
DriveApp
.
getFileById
(
ssId
).
getParents
().
next
();



  
// Iterates through the subfolders to check if folder already exists.


  
// The script checks for the folder name specified in the APP_FOLDER_NAME variable.


  
const
 
subFolders
 
=
 
parentFolder
.
getFolders
();


  
while
 
(
subFolders
.
hasNext
())
 
{


    
const
 
folder
 
=
 
subFolders
.
next
();



    
// Returns the existing folder if found.


    
if
 
(
folder
.
getName
()
 
===
 
folderName
)
 
{


      
return
 
folder
;


    
}


  
}


  
// Creates a new folder if one doesn't already exist.


  
return
 
parentFolder


    
.
createFolder
(
folderName
)


    
.
setDescription
(


      
`Created by 
${
APP_TITLE
}
 application to store uploaded files.`
,


    
);


}



/**


 * Installs trigger to capture onFormSubmit event when a form is submitted.


 * Ensures that the trigger is only installed once.


 * Called by setup().


 */


function
 
installTrigger_
()
 
{


  
// Ensures existing trigger doesn't already exist.


  
const
 
propTriggerId
 
=


    
PropertiesService
.
getScriptProperties
().
getProperty
(
"triggerUniqueId"
);


  
if
 
(
propTriggerId
 
!==
 
null
)
 
{


    
const
 
triggers
 
=
 
ScriptApp
.
getProjectTriggers
();


    
for
 
(
const
 
t
 
in
 
triggers
)
 
{


      
if
 
(
triggers
[
t
].
getUniqueId
()
 
===
 
propTriggerId
)
 
{


        
console
.
log
(


          
`Trigger with the following unique ID already exists: 
${
propTriggerId
}
`
,


        
);


        
return
;


      
}


    
}


  
}


  
// Creates the trigger if one doesn't exist.


  
const
 
triggerUniqueId
 
=
 
ScriptApp
.
newTrigger
(
"onFormSubmit"
)


    
.
forForm
(
FormApp
.
getActiveForm
())


    
.
onFormSubmit
()


    
.
create
()


    
.
getUniqueId
();


  
PropertiesService
.
getScriptProperties
().
setProperty
(


    
"triggerUniqueId"
,


    
triggerUniqueId
,


  
);


  
console
.
log
(


    
`Trigger with the following unique ID was created: 
${
triggerUniqueId
}
`
,


  
);


}



/**


 * Removes all script properties and triggers for the project.


 * Use primarily to test setup routines.


 */


function
 
removeTriggersAndScriptProperties
()
 
{


  
PropertiesService
.
getScriptProperties
().
deleteAllProperties
();


  
// Removes all triggers associated with project.


  
const
 
triggers
 
=
 
ScriptApp
.
getProjectTriggers
();


  
for
 
(
const
 
t
 
in
 
triggers
)
 
{


    
ScriptApp
.
deleteTrigger
(
triggers
[
t
]);


  
}


}



/**


 * Removes all form responses to reset the form.


 */


function
 
deleteAllResponses
()
 
{


  
FormApp
.
getActiveForm
().
deleteAllResponses
();


}
```
## Ejecuta la secuencia de comandos:
- En el editor de secuencias de comandos, cambia al archivo Setup.gs .
`Setup.gs`
- En el menú desplegable de funciones, selecciona setUp .
`setUp`
- Haz clic en Ejecutar .
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
- Regresa al formulario y haz clic en Vista previa .
- En el formulario, selecciona una subcarpeta y sube un archivo.
- Haz clic en Enviar .
- Ve a Drive y abre la carpeta Subir archivos a Drive (respuestas de archivos) . Los archivos que subiste se encuentran en la subcarpeta que seleccionaste en el formulario.
## Colaboradores
Google mantiene esta muestra con la ayuda de los Google Developer Experts.
## Próximos pasos
- Activadores controlados por eventos
- Documentación de referencia sobre el servicio de Formularios
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Calcula la distancia en automóvil y convierte los metros a millas

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Calcula la distancia en automóvil y convierte los metros a millas Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 10 minutos Tipo de proyecto : Función personalizada y automatización con un menú personalizado
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Con las funciones personalizadas, puedes calcular la distancia en automóvil entre dos ubicaciones y convertir la distancia de metros a millas. Una automatización adicional proporciona un menú personalizado que te permite agregar instrucciones paso a paso desde la dirección de inicio hasta la dirección de destino en una hoja nueva.
### Cómo funciona
La secuencia de comandos usa dos funciones personalizadas y una automatización:
- La función drivingDistance(origin, destination) usa el servicio de Maps para calcular la ruta en auto entre dos ubicaciones y devolver la distancia entre las dos direcciones en metros.
`drivingDistance(origin, destination)`
- La función metersToMiles(meters) calcula la cantidad equivalente de millas para una cantidad determinada de metros.
`metersToMiles(meters)`
- La automatización le solicita al usuario que ingrese qué fila de direcciones de inicio y finalización se debe usar para calcular la ruta en auto y agrega la ruta en auto paso a paso a una hoja nueva.
### Servicios de Apps Script
En esta solución, se usan los siguientes servicios:
- Servicio de hojas de cálculo : Agrega el menú personalizado, agrega datos de demostración para probar esta solución y da formato a las hojas nuevas cuando la secuencia de comandos agrega rutas en auto.
- Servicio base : Usa la clase Browser para solicitarle al usuario que ingrese un número de fila para las instrucciones y alertarlo si se produce un error.
`Browser`
- Servicio de utilidades : Actualiza cadenas basadas en plantillas con información especificada por el usuario.
- Servicio de Maps : Obtiene instrucciones paso a paso de Google Maps desde la dirección de inicio hasta la dirección de destino.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
- Haz una copia de la hoja de cálculo Calculate driving distance and convert meters to miles . El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo: Crear una copia
Haz una copia de la hoja de cálculo Calculate driving distance and convert meters to miles . El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo:
Crear una copia
- Para agregar encabezados y datos de demostración a tu hoja, haz clic en Instrucciones > Preparar hoja . Es posible que debas actualizar la página para que aparezca este menú personalizado.
Para agregar encabezados y datos de demostración a tu hoja, haz clic en Instrucciones > Preparar hoja . Es posible que debas actualizar la página para que aparezca este menú personalizado.
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
- Haz clic en Cómo llegar > Preparar hoja de nuevo.
Haz clic en Cómo llegar > Preparar hoja de nuevo.
## Ejecuta la secuencia de comandos:
- En la celda C2 , ingresa la fórmula =DRIVINGDISTANCE(A2,B2) y presiona Intro . Si te encuentras en una ubicación que usa comas decimales, es posible que debas ingresar =DRIVINGDISTANCE(A2;B2) .
`C2`
`=DRIVINGDISTANCE(A2,B2)`
`=DRIVINGDISTANCE(A2;B2)`
- En la celda D2 , ingresa la fórmula =METERSTOMILES(C2) y presiona Intro .
`D2`
`=METERSTOMILES(C2)`
- (Opcional) Agrega filas adicionales de direcciones de inicio y fin, y copia las fórmulas de las columnas C y D para calcular las distancias de conducción entre varios lugares.
`C`
`D`
- Haz clic en Instrucciones sobre cómo llegar > Generar paso a paso .
- En el diálogo, ingresa el número de fila de las direcciones para las que deseas generar instrucciones sobre cómo llegar y haz clic en Aceptar .
- Revisa las indicaciones para llegar en la nueva hoja de cálculo que crea la secuencia de comandos.
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver código fuente :
#### Ver el código fuente
```
/**


 * @OnlyCurrentDoc Limits the script to only accessing the current sheet.


 */



/**


 * A special function that runs when the spreadsheet is open, used to add a


 * custom menu to the spreadsheet.


 */


function
 
onOpen
()
 
{


  
try
 
{


    
const
 
spreadsheet
 
=
 
SpreadsheetApp
.
getActive
();


    
const
 
menuItems
 
=
 
[


      
{
 
name
:
 
"Prepare sheet..."
,
 
functionName
:
 
"prepareSheet_"
 
},


      
{
 
name
:
 
"Generate step-by-step..."
,
 
functionName
:
 
"generateStepByStep_"
 
},


    
];


    
spreadsheet
.
addMenu
(
"Directions"
,
 
menuItems
);


  
}
 
catch
 
(
e
)
 
{


    
// TODO (Developer) - Handle Exception


    
console
.
log
(
`Failed with error: %s
${
e
.
error
}
`
);


  
}


}



/**


 * A custom function that converts meters to miles.


 *


 * @param {Number} meters The distance in meters.


 * @return {Number} The distance in miles.


 */


function
 
metersToMiles
(
meters
)
 
{


  
if
 
(
typeof
 
meters
 
!==
 
"number"
)
 
{


    
return
 
null
;


  
}


  
return
 
(
meters
 
/
 
1000
)
 
*
 
0.621371
;


}



/**


 * A custom function that gets the driving distance between two addresses.


 *


 * @param {String} origin The starting address.


 * @param {String} destination The ending address.


 * @return {Number} The distance in meters.


 */


function
 
drivingDistance
(
origin
,
 
destination
)
 
{


  
const
 
directions
 
=
 
getDirections_
(
origin
,
 
destination
);


  
return
 
directions
.
routes
[
0
].
legs
[
0
].
distance
.
value
;


}



/**


 * A function that adds headers and some initial data to the spreadsheet.


 */


function
 
prepareSheet_
()
 
{


  
try
 
{


    
const
 
sheet
 
=
 
SpreadsheetApp
.
getActiveSheet
().
setName
(
"Settings"
);


    
const
 
headers
 
=
 
[


      
"Start Address"
,


      
"End Address"
,


      
"Driving Distance (meters)"
,


      
"Driving Distance (miles)"
,


    
];


    
const
 
initialData
 
=
 
[


      
"350 5th Ave, New York, NY 10118"
,


      
"405 Lexington Ave, New York, NY 10174"
,


    
];


    
sheet
.
getRange
(
"A1:D1"
).
setValues
([
headers
]).
setFontWeight
(
"bold"
);


    
sheet
.
getRange
(
"A2:B2"
).
setValues
([
initialData
]);


    
sheet
.
setFrozenRows
(
1
);


    
sheet
.
autoResizeColumns
(
1
,
 
4
);


  
}
 
catch
 
(
e
)
 
{


    
// TODO (Developer) - Handle Exception


    
console
.
log
(
`Failed with error: %s
${
e
.
error
}
`
);


  
}


}



/**


 * Creates a new sheet containing step-by-step directions between the two


 * addresses on the "Settings" sheet that the user selected.


 */


function
 
generateStepByStep_
()
 
{


  
try
 
{


    
const
 
spreadsheet
 
=
 
SpreadsheetApp
.
getActive
();


    
const
 
settingsSheet
 
=
 
spreadsheet
.
getSheetByName
(
"Settings"
);


    
settingsSheet
.
activate
();



    
// Prompt the user for a row number.


    
const
 
selectedRow
 
=
 
Browser
.
inputBox
(


      
"Generate step-by-step"
,


      
"Please enter the row number of"
 
+


        
" the"
 
+


        
" addresses to use"
 
+


        
' (for example, "2"):'
,


      
Browser
.
Buttons
.
OK_CANCEL
,


    
);


    
if
 
(
selectedRow
 
===
 
"cancel"
)
 
{


      
return
;


    
}


    
const
 
rowNumber
 
=
 
Number
(
selectedRow
);


    
if
 
(


      
Number
.
isNaN
(
rowNumber
)
 
||


      
rowNumber
 < 
2
 
||


      
rowNumber
 > 
settingsSheet
.
getLastRow
()


    
)
 
{


      
Browser
.
msgBox
(


        
"Error"
,


        
Utilities
.
formatString
(
'Row "%s" is not valid.'
,
 
selectedRow
),


        
Browser
.
Buttons
.
OK
,


      
);


      
return
;


    
}



    
// Retrieve the addresses in that row.


    
const
 
row
 
=
 
settingsSheet
.
getRange
(
rowNumber
,
 
1
,
 
1
,
 
2
);


    
const
 
rowValues
 
=
 
row
.
getValues
();


    
const
 
origin
 
=
 
rowValues
[
0
][
0
];


    
const
 
destination
 
=
 
rowValues
[
0
][
1
];


    
if
 
(
!
origin
 
||
 
!
destination
)
 
{


      
Browser
.
msgBox
(


        
"Error"
,


        
"Row does not contain two addresses."
,


        
Browser
.
Buttons
.
OK
,


      
);


      
return
;


    
}



    
// Get the raw directions information.


    
const
 
directions
 
=
 
getDirections_
(
origin
,
 
destination
);



    
// Create a new sheet and append the steps in the directions.


    
const
 
sheetName
 
=
 
`Driving Directions for Row 
${
rowNumber
}
`
;


    
let
 
directionsSheet
 
=
 
spreadsheet
.
getSheetByName
(
sheetName
);


    
if
 
(
directionsSheet
)
 
{


      
directionsSheet
.
clear
();


      
directionsSheet
.
activate
();


    
}
 
else
 
{


      
directionsSheet
 
=
 
spreadsheet
.
insertSheet
(


        
sheetName
,


        
spreadsheet
.
getNumSheets
(),


      
);


    
}


    
const
 
sheetTitle
 
=
 
Utilities
.
formatString
(


      
"Driving Directions from %s to %s"
,


      
origin
,


      
destination
,


    
);


    
const
 
headers
 
=
 
[


      
[
sheetTitle
,
 
""
,
 
""
],


      
[
"Step"
,
 
"Distance (Meters)"
,
 
"Distance (Miles)"
],


    
];


    
const
 
newRows
 
=
 
[];


    
for
 
(
const
 
step
 
of
 
directions
.
routes
[
0
].
legs
[
0
].
steps
)
 
{


      
// Remove HTML tags from the instructions.


      
const
 
instructions
 
=
 
step
.
html_instructions


        
.
replace
(
/<br>|<div.*?>/g
,
 
"\n"
)


        
.
replace
(
/<.*?>/g
,
 
""
);


      
newRows
.
push
([
instructions
,
 
step
.
distance
.
value
]);


    
}


    
directionsSheet
.
getRange
(
1
,
 
1
,
 
headers
.
length
,
 
3
).
setValues
(
headers
);


    
directionsSheet


      
.
getRange
(
headers
.
length
 
+
 
1
,
 
1
,
 
newRows
.
length
,
 
2
)


      
.
setValues
(
newRows
);


    
directionsSheet


      
.
getRange
(
headers
.
length
 
+
 
1
,
 
3
,
 
newRows
.
length
,
 
1
)


      
.
setFormulaR1C1
(
"=METERSTOMILES(R[0]C[-1])"
);



    
// Format the new sheet.


    
directionsSheet
.
getRange
(
"A1:C1"
).
merge
().
setBackground
(
"#ddddee"
);


    
directionsSheet
.
getRange
(
"A1:2"
).
setFontWeight
(
"bold"
);


    
directionsSheet
.
setColumnWidth
(
1
,
 
500
);


    
directionsSheet
.
getRange
(
"B2:C"
).
setVerticalAlignment
(
"top"
);


    
directionsSheet
.
getRange
(
"C2:C"
).
setNumberFormat
(
"0.00"
);


    
const
 
stepsRange
 
=
 
directionsSheet


      
.
getDataRange
()


      
.
offset
(
2
,
 
0
,
 
directionsSheet
.
getLastRow
()
 
-
 
2
);


    
setAlternatingRowBackgroundColors_
(
stepsRange
,
 
"#ffffff"
,
 
"#eeeeee"
);


    
directionsSheet
.
setFrozenRows
(
2
);


    
SpreadsheetApp
.
flush
();


  
}
 
catch
 
(
e
)
 
{


    
// TODO (Developer) - Handle Exception


    
console
.
log
(
`Failed with error: %s
${
e
.
error
}
`
);


  
}


}



/**


 * Sets the background colors for alternating rows within the range.


 * @param {Range} range The range to change the background colors of.


 * @param {string} oddColor The color to apply to odd rows (relative to the


 *     start of the range).


 * @param {string} evenColor The color to apply to even rows (relative to the


 *     start of the range).


 */


function
 
setAlternatingRowBackgroundColors_
(
range
,
 
oddColor
,
 
evenColor
)
 
{


  
const
 
backgrounds
 
=
 
[];


  
for
 
(
let
 
row
 
=
 
1
;
 
row
 
<
=
 
range
.
getNumRows
();
 
row
++
)
 
{


    
const
 
rowBackgrounds
 
=
 
[];


    
for
 
(
let
 
column
 
=
 
1
;
 
column
 
<
=
 
range
.
getNumColumns
();
 
column
++
)
 
{


      
if
 
(
row
 
%
 
2
 
===
 
0
)
 
{


        
rowBackgrounds
.
push
(
evenColor
);


      
}
 
else
 
{


        
rowBackgrounds
.
push
(
oddColor
);


      
}


    
}


    
backgrounds
.
push
(
rowBackgrounds
);


  
}


  
range
.
setBackgrounds
(
backgrounds
);


}



/**


 * A shared helper function used to obtain the full set of directions


 * information between two addresses. Uses the Apps Script Maps Service.


 *


 * @param {String} origin The starting address.


 * @param {String} destination The ending address.


 * @return {Object} The directions response object.


 */


function
 
getDirections_
(
origin
,
 
destination
)
 
{


  
const
 
directionFinder
 
=
 
Maps
.
newDirectionFinder
();


  
directionFinder
.
setOrigin
(
origin
);


  
directionFinder
.
setDestination
(
destination
);


  
const
 
directions
 
=
 
directionFinder
.
getDirections
();


  
if
 
(
directions
.
status
 
!==
 
"OK"
)
 
{


    
throw
 
directions
.
error_message
;


  
}


  
return
 
directions
;


}
```
## Colaboradores
Google mantiene esta muestra con la ayuda de los Google Developer Experts.
## Próximos pasos
- Funciones personalizadas en Hojas de cálculo de Google
- Menús personalizados en Google Workspace
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Envía certificados de agradecimiento personalizados a los empleados

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Envía certificados de agradecimiento personalizados a los empleados Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 15 minutos Tipo de proyecto : Automatización con un menú personalizado
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura el entorno.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Personaliza automáticamente la plantilla de Certificado de empleado de Presentaciones de Google con los datos de los empleados en Hojas de Google y, luego, envía los certificados con Gmail.
### Cómo funciona
La secuencia de comandos usa la plantilla de presentación de Certificado de empleado de Presentaciones y una hoja de cálculo de Hojas con los detalles del empleado. La secuencia de comandos copia la plantilla y reemplaza los marcadores de posición con datos de la hoja de cálculo. Una vez que la secuencia de comandos crea una diapositiva para cada empleado, extrae cada diapositiva individual como un archivo adjunto en PDF y envía los certificados a los empleados.
### Servicios de Apps Script
En esta solución, se usan los siguientes servicios:
- Servicio de Google Drive : Copia la plantilla de Certificado de empleado de Presentaciones.
- Servicio de hojas de cálculo : Proporciona los detalles del empleado y actualiza el estado de cada empleado que aparece en la lista.
- Servicio de Presentaciones : Reemplaza los marcadores de posición en la presentación con los datos del empleado de la hoja de cálculo.
- Servicio de Gmail : Obtiene las diapositivas individuales como archivos PDF y las envía a los empleados.
## Requisitos previos
Para usar esta muestra, debes cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura tu entorno
- Haz clic en el siguiente botón para crear una copia de la plantilla de Presentaciones de Certificados de empleado .
Crear una copia
- Toma nota del ID de tu presentación para usarlo en un paso posterior. Puedes encontrar el ID en la URL: https://docs.google.com/presentation/d/ PRESENTATION_ID /edit
Toma nota del ID de tu presentación para usarlo en un paso posterior. Puedes encontrar el ID en la URL:
https://docs.google.com/presentation/d/ PRESENTATION_ID /edit
`https://docs.google.com/presentation/d/ PRESENTATION_ID /edit`
- En Drive, crea una carpeta nueva para contener los certificados.
En Drive, crea una carpeta nueva para contener los certificados.
- Toma nota del ID de tu carpeta para usarlo en un paso posterior. Puedes encontrar el ID en la URL: https://drive.google.com/drive/folders/ FOLDER_ID
Toma nota del ID de tu carpeta para usarlo en un paso posterior. Puedes encontrar el ID en la URL: https://drive.google.com/drive/folders/ FOLDER_ID
`https://drive.google.com/drive/folders/ FOLDER_ID`
## Configura la secuencia de comandos
- Haz clic en el siguiente botón para crear una copia de la hoja de cálculo de Hojas de ejemplo de Certificados de empleado . El proyecto de Apps Script para esta solución está adjunto a la hoja de cálculo: Crear una copia
Haz clic en el siguiente botón para crear una copia de la hoja de cálculo de Hojas de ejemplo de Certificados de empleado . El proyecto de Apps Script para esta solución está adjunto a la hoja de cálculo:
Crear una copia
- En la hoja de cálculo, abre el proyecto de Apps Script haciendo clic en Extensiones > Apps Script .
En la hoja de cálculo, abre el proyecto de Apps Script haciendo clic en Extensiones > Apps Script .
- Para la variable slideTemplateId , reemplaza PRESENTATION_ID por el ID de tu presentación.
Para la variable slideTemplateId , reemplaza PRESENTATION_ID por el ID de tu presentación.
`slideTemplateId`
`PRESENTATION_ID`
- Para la variable tempFolderId , reemplaza FOLDER_ID por el ID de tu carpeta.
Para la variable tempFolderId , reemplaza FOLDER_ID por el ID de tu carpeta.
`tempFolderId`
`FOLDER_ID`
- Haz clic en Guardar .
Haz clic en Guardar .
## Ejecuta la secuencia de comandos
- Vuelve a la hoja de cálculo y haz clic en Agradecimiento > Crear certificados . Es posible que debas actualizar la página para que aparezca este menú personalizado.
- Cuando se te solicite, autoriza la secuencia de comandos. <<../_snippets/oauth.md>>
- Vuelve a hacer clic en Agradecimiento > Crear certificados .
- Una vez que la columna de estado de todas las filas se haya actualizado a Creado , haz clic en Agradecimiento > Enviar certificados .
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver el código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/automations/employee-certificate



/*


Copyright 2022 Google LLC



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



const
 
slideTemplateId
 
=
 
"PRESENTATION_ID"
;


const
 
tempFolderId
 
=
 
"FOLDER_ID"
;
 
// Create an empty folder in Google Drive



/**


 * Creates a custom menu "Appreciation" in the spreadsheet


 * with drop-down options to create and send certificates


 */


function
 
onOpen
()
 
{


  
const
 
ui
 
=
 
SpreadsheetApp
.
getUi
();


  
ui
.
createMenu
(
"Appreciation"
)


    
.
addItem
(
"Create certificates"
,
 
"createCertificates"
)


    
.
addSeparator
()


    
.
addItem
(
"Send certificates"
,
 
"sendCertificates"
)


    
.
addToUi
();


}



/**


 * Creates a personalized certificate for each employee


 * and stores every individual Slides doc on Google Drive


 */


function
 
createCertificates
()
 
{


  
// Load the Google Slide template file


  
const
 
template
 
=
 
DriveApp
.
getFileById
(
slideTemplateId
);



  
// Get all employee data from the spreadsheet and identify the headers


  
const
 
sheet
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
().
getActiveSheet
();


  
const
 
values
 
=
 
sheet
.
getDataRange
().
getValues
();


  
const
 
headers
 
=
 
values
[
0
];


  
const
 
empNameIndex
 
=
 
headers
.
indexOf
(
"Employee Name"
);


  
const
 
dateIndex
 
=
 
headers
.
indexOf
(
"Date"
);


  
const
 
managerNameIndex
 
=
 
headers
.
indexOf
(
"Manager Name"
);


  
const
 
titleIndex
 
=
 
headers
.
indexOf
(
"Title"
);


  
const
 
compNameIndex
 
=
 
headers
.
indexOf
(
"Company Name"
);


  
const
 
empEmailIndex
 
=
 
headers
.
indexOf
(
"Employee Email"
);


  
const
 
empSlideIndex
 
=
 
headers
.
indexOf
(
"Employee Slide"
);


  
const
 
statusIndex
 
=
 
headers
.
indexOf
(
"Status"
);



  
// Iterate through each row to capture individual details


  
for
 
(
let
 
i
 
=
 
1
;
 
i
 < 
values
.
length
;
 
i
++
)
 
{


    
const
 
rowData
 
=
 
values
[
i
];


    
const
 
empName
 
=
 
rowData
[
empNameIndex
];


    
const
 
date
 
=
 
rowData
[
dateIndex
];


    
const
 
managerName
 
=
 
rowData
[
managerNameIndex
];


    
const
 
title
 
=
 
rowData
[
titleIndex
];


    
const
 
compName
 
=
 
rowData
[
compNameIndex
];



    
// Make a copy of the Slide template and rename it with employee name


    
const
 
tempFolder
 
=
 
DriveApp
.
getFolderById
(
tempFolderId
);


    
const
 
empSlideId
 
=
 
template
.
makeCopy
(
tempFolder
).
setName
(
empName
).
getId
();


    
const
 
empSlide
 
=
 
SlidesApp
.
openById
(
empSlideId
).
getSlides
()[
0
];



    
// Replace placeholder values with actual employee related details


    
empSlide
.
replaceAllText
(
"Employee Name"
,
 
empName
);


    
empSlide
.
replaceAllText
(


      
"Date"
,


      
`Date: 
${
Utilities
.
formatDate
(


        
date
,


        
Session
.
getScriptTimeZone
(),


        
"MMMM dd, yyyy"
,


      
)
}
`
,


    
);


    
empSlide
.
replaceAllText
(
"Your Name"
,
 
managerName
);


    
empSlide
.
replaceAllText
(
"Title"
,
 
title
);


    
empSlide
.
replaceAllText
(
"Company Name"
,
 
compName
);



    
// Update the spreadsheet with the new Slide Id and status


    
sheet
.
getRange
(
i
 
+
 
1
,
 
empSlideIndex
 
+
 
1
).
setValue
(
empSlideId
);


    
sheet
.
getRange
(
i
 
+
 
1
,
 
statusIndex
 
+
 
1
).
setValue
(
"CREATED"
);


    
SpreadsheetApp
.
flush
();


  
}


}



/**


 * Send an email to each individual employee


 * with a PDF attachment of their appreciation certificate


 */


function
 
sendCertificates
()
 
{


  
// Get all employee data from the spreadsheet and identify the headers


  
const
 
sheet
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
().
getActiveSheet
();


  
const
 
values
 
=
 
sheet
.
getDataRange
().
getValues
();


  
const
 
headers
 
=
 
values
[
0
];


  
const
 
empNameIndex
 
=
 
headers
.
indexOf
(
"Employee Name"
);


  
const
 
dateIndex
 
=
 
headers
.
indexOf
(
"Date"
);


  
const
 
managerNameIndex
 
=
 
headers
.
indexOf
(
"Manager Name"
);


  
const
 
titleIndex
 
=
 
headers
.
indexOf
(
"Title"
);


  
const
 
compNameIndex
 
=
 
headers
.
indexOf
(
"Company Name"
);


  
const
 
empEmailIndex
 
=
 
headers
.
indexOf
(
"Employee Email"
);


  
const
 
empSlideIndex
 
=
 
headers
.
indexOf
(
"Employee Slide"
);


  
const
 
statusIndex
 
=
 
headers
.
indexOf
(
"Status"
);



  
// Iterate through each row to capture individual details


  
for
 
(
let
 
i
 
=
 
1
;
 
i
 < 
values
.
length
;
 
i
++
)
 
{


    
const
 
rowData
 
=
 
values
[
i
];


    
const
 
empName
 
=
 
rowData
[
empNameIndex
];


    
const
 
date
 
=
 
rowData
[
dateIndex
];


    
const
 
managerName
 
=
 
rowData
[
managerNameIndex
];


    
const
 
title
 
=
 
rowData
[
titleIndex
];


    
const
 
compName
 
=
 
rowData
[
compNameIndex
];


    
const
 
empSlideId
 
=
 
rowData
[
empSlideIndex
];


    
const
 
empEmail
 
=
 
rowData
[
empEmailIndex
];



    
// Load the employee's personalized Google Slide file


    
const
 
attachment
 
=
 
DriveApp
.
getFileById
(
empSlideId
);



    
// Setup the required parameters and send them the email


    
const
 
senderName
 
=
 
"CertBot"
;


    
const
 
subject
 
=
 
`
${
empName
}
, you're awesome!`
;


    
const
 
body
 
=
 
`Please find your employee appreciation certificate attached.\n\n
${
compName
}
 team`
;


    
GmailApp
.
sendEmail
(
empEmail
,
 
subject
,
 
body
,
 
{


      
attachments
:
 
[
attachment
.
getAs
(
MimeType
.
PDF
)],


      
name
:
 
senderName
,


    
});



    
// Update the spreadsheet with email status


    
sheet
.
getRange
(
i
 
+
 
1
,
 
statusIndex
 
+
 
1
).
setValue
(
"SENT"
);


    
SpreadsheetApp
.
flush
();


  
}


}
```
```
</section>
```
## Colaboradores
Sourabh Choraria, blogger y experto en desarrolladores de Google, creó esta muestra.
- Encuentra a Sourabh en Twitter @schoraria911 .
- Lee el blog de Sourabh.
Google mantiene esta muestra con la ayuda de Expertos de Google Developers.
## Próximos pasos
- Menús personalizados en Google Workspace
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Resumir datos de varias hojas

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Resumir datos de varias hojas Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 5 minutos Tipo de proyecto : Función personalizada
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Si tienes datos estructurados de forma similar en varias hojas de una hoja de cálculo, como métricas de asistencia al cliente para los miembros del equipo, puedes usar esta función personalizada para crear un resumen de cada hoja. Esta solución se enfoca en los tickets de asistencia al cliente, pero puedes personalizarla para adaptarla a tus necesidades.
### Cómo funciona
La función personalizada, llamada getSheetsData() , resume los datos de cada hoja de la hoja de cálculo según la columna Estado de la hoja. La secuencia de comandos ignora las hojas que no deben incluirse en la agregación, como las hojas ReadMe y Summary .
`getSheetsData()`
### Servicios de Apps Script
En esta solución, se usa el siguiente servicio:
- Servicio de hojas de cálculo : Obtiene las hojas que se deben resumir y cuenta la cantidad de elementos que coinciden con una cadena especificada. Luego, la secuencia de comandos agrega la información calculada a un rango relativo a la ubicación en la que se llamó a la función personalizada en la hoja de cálculo.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
Para hacer una copia de la hoja de cálculo de la función personalizada Summarize spreadsheet data , haz clic en el siguiente botón:
Crear una copia
El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo.
## Ejecuta la secuencia de comandos:
- En la hoja de cálculo que copiaste, ve a la hoja Resumen .
- Haz clic en la celda A4 . La función getSheetsData() se encuentra en esta celda.
`A4`
`getSheetsData()`
- Ve a una de las hojas del propietario y actualiza o agrega datos a la hoja. Estas son algunas acciones que puedes probar: Agrega una fila nueva con información de muestra del ticket. En la columna Estado , cambia el estado de un ticket existente. Cambia la posición de la columna Estado . Por ejemplo, en la hoja Owner1 , mueve la columna Estado de la columna C a la columna D.
- Agrega una fila nueva con información de muestra del ticket.
- En la columna Estado , cambia el estado de un ticket existente.
- Cambia la posición de la columna Estado . Por ejemplo, en la hoja Owner1 , mueve la columna Estado de la columna C a la columna D.
- Ve a la hoja Resumen y revisa la tabla de resumen actualizada que getSheetsData() creó a partir de la celda A4 . Es posible que debas marcar la casilla de verificación en la fila 10 para actualizar los resultados almacenados en caché de la función personalizada. Google almacena en caché las funciones personalizadas para optimizar el rendimiento. Si agregaste o actualizaste filas, la secuencia de comandos actualizará los recuentos de tickets y estados. Si moviste la posición de la columna Estado , la secuencia de comandos seguirá funcionando según lo previsto con el nuevo índice de columna.
`getSheetsData()`
`A4`
- Si agregaste o actualizaste filas, la secuencia de comandos actualizará los recuentos de tickets y estados.
- Si moviste la posición de la columna Estado , la secuencia de comandos seguirá funcionando según lo previsto con el nuevo índice de columna.
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/custom-functions/summarize-sheets-data



/*


Copyright 2022 Google LLC



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



/**


 * Gets summary data from other sheets. The sheets you want to summarize must have columns with headers that match the names of the columns this function summarizes data from.


 *


 * @return {string} Summary data from other sheets.


 * @customfunction


 */



// The following sheets are ignored. Add additional constants for other sheets that should be ignored.


const
 
READ_ME_SHEET_NAME
 
=
 
"ReadMe"
;


const
 
PM_SHEET_NAME
 
=
 
"Summary"
;



/**


 * Reads data ranges for each sheet. Filters and counts based on 'Status' columns. To improve performance, the script uses arrays


 * until all summary data is gathered. Then the script writes the summary array starting at the cell of the custom function.


 */


function
 
getSheetsData
()
 
{


  
const
 
ss
 
=
 
SpreadsheetApp
.
getActiveSpreadsheet
();


  
const
 
sheets
 
=
 
ss
.
getSheets
();


  
const
 
outputArr
 
=
 
[];



  
// For each sheet, summarizes the data and pushes to a temporary array.


  
for
 
(
const
 
s
 
in
 
sheets
)
 
{


    
// Gets sheet name.


    
const
 
sheetNm
 
=
 
sheets
[
s
].
getName
();


    
// Skips ReadMe and Summary sheets.


    
if
 
(
sheetNm
 
===
 
READ_ME_SHEET_NAME
 
||
 
sheetNm
 
===
 
PM_SHEET_NAME
)
 
{


      
continue
;


    
}


    
// Gets sheets data.


    
const
 
values
 
=
 
sheets
[
s
].
getDataRange
().
getValues
();


    
// Gets the first row of the sheet which is the header row.


    
const
 
headerRowValues
 
=
 
values
[
0
];


    
// Finds the columns with the heading names 'Owner Name' and 'Status' and gets the index value of each.


    
// Using 'indexOf()' to get the position of each column prevents the script from breaking if the columns change positions in a sheet.


    
const
 
columnOwner
 
=
 
headerRowValues
.
indexOf
(
"Owner Name"
);


    
const
 
columnStatus
 
=
 
headerRowValues
.
indexOf
(
"Status"
);


    
// Removes header row.


    
values
.
splice
(
0
,
 
1
);


    
// Gets the 'Owner Name' column value by retrieving the first data row in the array.


    
const
 
owner
 
=
 
values
[
0
][
columnOwner
];


    
// Counts the total number of tasks.


    
const
 
taskCnt
 
=
 
values
.
length
;


    
// Counts the number of tasks that have the 'Complete' status.


    
// If the options you want to count in your spreadsheet differ, update the strings below to match the text of each option.


    
// To add more options, copy the line below and update the string to the new text.


    
const
 
completeCnt
 
=
 
filterByPosition
(


      
values
,


      
"Complete"
,


      
columnStatus
,


    
).
length
;


    
// Counts the number of tasks that have the 'In-Progress' status.


    
const
 
inProgressCnt
 
=
 
filterByPosition
(


      
values
,


      
"In-Progress"
,


      
columnStatus
,


    
).
length
;


    
// Counts the number of tasks that have the 'Scheduled' status.


    
const
 
scheduledCnt
 
=
 
filterByPosition
(


      
values
,


      
"Scheduled"
,


      
columnStatus
,


    
).
length
;


    
// Counts the number of tasks that have the 'Overdue' status.


    
const
 
overdueCnt
 
=
 
filterByPosition
(
values
,
 
"Overdue"
,
 
columnStatus
).
length
;


    
// Builds the output array.


    
outputArr
.
push
([


      
owner
,


      
taskCnt
,


      
completeCnt
,


      
inProgressCnt
,


      
scheduledCnt
,


      
overdueCnt
,


      
sheetNm
,


    
]);


  
}


  
// Writes the output array.


  
return
 
outputArr
;


}



/**


 * Below is a helper function that filters a 2-dimenstional array.


 */


function
 
filterByPosition
(
array
,
 
find
,
 
position
)
 
{


  
return
 
array
.
filter
((
innerArray
)
 
=
>
 
innerArray
[
position
]
 
===
 
find
);


}
```
## Modificaciones
Puedes editar la función personalizada tantas veces como quieras para que se adapte a tus necesidades. Para ver una adición opcional para actualizar manualmente los resultados de la función personalizada, haz clic en Actualizar resultados almacenados en caché :
#### Actualiza los resultados almacenados en caché
A diferencia de las funciones integradas, Google almacena en caché las funciones personalizadas para optimizar el rendimiento. Esto significa que, si cambias algo en tu función personalizada, como un valor que se está calculando, es posible que no se fuerce una actualización de inmediato. Para actualizar el resultado de la función de forma manual, sigue estos pasos:
- Para agregar una casilla de verificación a una celda vacía, haz clic en Insertar > Casilla de verificación .
- Agrega la celda que tiene la casilla de verificación como parámetro de la función personalizada, por ejemplo, getSheetsData(B11) .
`getSheetsData(B11)`
- Marca o desmarca la casilla de verificación para actualizar los resultados de la función personalizada.
## Colaboradores
Google mantiene esta muestra con la ayuda de los Google Developer Experts.
## Próximos pasos
- Funciones personalizadas en Hojas de cálculo
- Extensión de Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### Guía de inicio rápido de la biblioteca

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Guía de inicio rápido de la biblioteca Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Crea una biblioteca de Google Apps Script que puedas usar para quitar filas duplicadas en los datos de la hoja de cálculo.
## Objetivos
- Configurar la secuencia de comandos
- Ejecutar la secuencia de comandos
## Requisitos previos
Para usar esta muestra, necesitas los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
Para compilar la biblioteca, haz lo siguiente:
- Accede a tu Cuenta de Google.
- Para abrir el editor de secuencias de comandos, ve a script.google.com .
- En la esquina superior izquierda, haz clic en Nuevo proyecto .
- Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código. sheets/removingDuplicates/removingDuplicates.gs Ver en GitHub /** * Removes duplicate rows from the current sheet. */ function removeDuplicates () { const sheet = SpreadsheetApp . getActiveSheet (); const data = sheet . getDataRange (). getValues (); const uniqueData = {}; for ( const row of data ) { const key = row . join (); uniqueData [ key ] = uniqueData [ key ] || row ; } sheet . clearContents (); const newData = Object . values ( uniqueData ); sheet . getRange ( 1 , 1 , newData . length , newData [ 0 ]. length ). setValues ( newData ); }
Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código.
```
/**


 * Removes duplicate rows from the current sheet.


 */


function
 
removeDuplicates
()
 
{


  
const
 
sheet
 
=
 
SpreadsheetApp
.
getActiveSheet
();


  
const
 
data
 
=
 
sheet
.
getDataRange
().
getValues
();


  
const
 
uniqueData
 
=
 
{};


  
for
 
(
const
 
row
 
of
 
data
)
 
{


    
const
 
key
 
=
 
row
.
join
();


    
uniqueData
[
key
]
 
=
 
uniqueData
[
key
]
 
||
 
row
;


  
}


  
sheet
.
clearContents
();


  
const
 
newData
 
=
 
Object
.
values
(
uniqueData
);


  
sheet
.
getRange
(
1
,
 
1
,
 
newData
.
length
,
 
newData
[
0
].
length
).
setValues
(
newData
);


}
```
- Haz clic en Guardar .
Haz clic en Guardar .
- En la esquina superior izquierda, haz clic en Proyecto sin título .
En la esquina superior izquierda, haz clic en Proyecto sin título .
- Nombra tu secuencia de comandos como Quitar filas duplicadas y haz clic en Cambiar nombre .
Nombra tu secuencia de comandos como Quitar filas duplicadas y haz clic en Cambiar nombre .
- Haz clic en Implementar > Nueva implementación .
Haz clic en Implementar > Nueva implementación .
- Junto a Seleccionar tipo , haz clic en Habilitar los tipos de implementación > Biblioteca .
Junto a Seleccionar tipo , haz clic en Habilitar los tipos de implementación > Biblioteca .
- Ingresa una descripción de la biblioteca, como Quitar filas duplicadas . Cualquier persona con acceso a la biblioteca puede ver esta descripción.
Ingresa una descripción de la biblioteca, como Quitar filas duplicadas . Cualquier persona con acceso a la biblioteca puede ver esta descripción.
- Haz clic en Implementar .
Haz clic en Implementar .
- A la izquierda, haz clic en Configuración del proyecto .
A la izquierda, haz clic en Configuración del proyecto .
- En IDs , copia el ID de la secuencia de comandos para usarlo en un paso posterior.
En IDs , copia el ID de la secuencia de comandos para usarlo en un paso posterior.
## Ejecuta la secuencia de comandos
Para usar una biblioteca, debes tener al menos permisos de visualización para su proyecto de Apps Script. Como creaste la biblioteca, tienes los permisos necesarios para usarla. Si quieres permitir que otros usuarios usen la biblioteca, otórgales permiso de lectura para el proyecto de Apps Script.
Para usar la biblioteca, haz lo siguiente:
- Abre una hoja de cálculo de Hojas de cálculo de Google que tenga datos con filas duplicadas. Para usar una hoja de cálculo de muestra, haz una copia de la hoja de cálculo Filas duplicadas de muestra .
- Haz clic en Extensiones > Apps Script .
- Junto a Bibliotecas , haz clic en Agregar una biblioteca add .
- En la sección ID de secuencia de comandos , pega el ID de la secuencia de comandos del proyecto de Apps Script de la biblioteca que copiaste en la sección anterior.
- Haz clic en Buscar .
- En la sección Versión , selecciona 1 .
- Haz clic en Agregar .
- Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código. function runLibrary () { Removeduplicaterows . removeDuplicates (); }
Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código.
```
function
 
runLibrary
()
 
{


 
Removeduplicaterows
.
removeDuplicates
();


}
```
- En el menú desplegable de funciones, selecciona runLibrary .
En el menú desplegable de funciones, selecciona runLibrary .
- Haz clic en Ejecutar .
Haz clic en Ejecutar .
- Vuelve a la hoja de cálculo para ver los datos actualizados sin filas duplicadas.
Vuelve a la hoja de cálculo para ver los datos actualizados sin filas duplicadas.
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver código fuente :
#### Ver el código fuente
Primero, la secuencia de comandos realiza una sola llamada a la hoja de cálculo para recuperar todos los datos. Puedes elegir leer la hoja fila por fila, pero las operaciones de JavaScript son mucho más rápidas que hablar con otros servicios como Hojas de cálculo. Cuantas menos llamadas realices, más rápido se ejecutará. Esto es importante porque cada ejecución de secuencia de comandos tiene un tiempo de ejecución máximo de 6 minutos.
```
const
 
sheet
 
=
 
SpreadsheetApp
.
getActiveSheet
();


const
 
data
 
=
 
sheet
.
getDataRange
().
getValues
();
```
La variable data es un array bidimensional de JavaScript que contiene todos los valores de la hoja. newData es un array vacío en el que la secuencia de comandos coloca todas las filas no duplicadas.
`data`
`newData`
```
const
 
newData
 
=
 
Object
.
values
(
uniqueData
);
```
El primer bucle for itera sobre cada fila del array bidimensional data . Para cada fila, el segundo bucle prueba si ya existe otra fila con datos coincidentes en el array newData . Si no es un duplicado, la fila se inserta en el array newData .
`for`
`data`
`newData`
`newData`
```
uniqueData
[
key
]
 
=
 
uniqueData
[
key
]
 
||
 
row
;
```
Por último, la secuencia de comandos borra el contenido existente de la hoja y, luego, inserta el contenido del array newData .
`newData`
```
sheet
.
clearContents
();


const
 
newData
 
=
 
Object
.
values
(
uniqueData
);


sheet
.
getRange
(
1
,
 
1
,
 
newData
.
length
,
 
newData
[
0
].
length
).
setValues
(
newData
);
```
## Modificaciones
Puedes editar la biblioteca tanto como quieras para que se adapte a tus necesidades. La siguiente sección contiene una modificación opcional.
#### Quita las filas con datos coincidentes en algunas columnas
En lugar de quitar las filas que coinciden por completo, es posible que quieras quitar las filas con datos coincidentes en solo una o dos de las columnas. Para ello, puedes cambiar la instrucción condicional.
En el código de muestra, actualiza la siguiente línea:
```
    
if
(
row
.
join
()
 
==
 
newData
[
j
]
.
join
())
{


      
duplicate
 
=
 
true
;


    
}
```
Reemplaza la línea con el siguiente código:
```
    
if
(
row
[
0
]
 
==
 
newData
[
j
][
0
]
 
&&
 
row
[
1
]
 
==
 
newData
[
j
][
1
]
)
{


      
duplicate
 
=
 
true
;


    
}
```
La instrucción condicional anterior encuentra duplicados cada vez que dos filas tienen los mismos datos en la primera y la segunda columna de la hoja.
## Colaboradores
Romain Vialard, experto en desarrolladores de Google, creó esta muestra. Sigue a Romain en Twitter @romain_vialard .
Google mantiene esta muestra con la ayuda de Expertos de Google Developers.
## Próximos pasos
- Bibliotecas
- Crea y administra implementaciones
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### prueba esta automatización sencilla

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Guía de inicio rápido de automatización Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Crea y ejecuta una automatización que cree un documento de Documentos de Google y te envíe por correo electrónico un vínculo a él.
## Objetivos
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
Para crear la automatización, haz lo siguiente:
- Para abrir el editor de secuencias de comandos de Google Apps, ve a script.google.com . Si es la primera vez que visitas script.google.com , haz clic en Ver panel .
`script.google.com`
`script.google.com`
- Haz clic en Proyecto nuevo .
- Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código. templates/standalone/helloWorld.gs Ver en GitHub /** * Creates a Google Doc and sends an email to the current user with a link to the doc. */ function createAndSendDocument () { try { // Create a new Google Doc named 'Hello, world!' const doc = DocumentApp . create ( "Hello, world!" ); // Access the body of the document, then add a paragraph. doc . getBody () . appendParagraph ( "This document was created by Google Apps Script." ); // Get the URL of the document. const url = doc . getUrl (); // Get the email address of the active user - that's you. const email = Session . getActiveUser (). getEmail (); // Get the name of the document to use as an email subject line. const subject = doc . getName (); // Append a new string to the "url" variable to use as an email body. const body = `Link to your doc: ${ url } ` ; // Send yourself an email with a link to the document. GmailApp . sendEmail ( email , subject , body ); } catch ( err ) { // TODO (developer) - Handle exception console . log ( "Failed with error %s" , err . message ); } }
Borra cualquier código que haya en el editor de secuencias de comandos y pega el siguiente código.
```
/**


 * Creates a Google Doc and sends an email to the current user with a link to the doc.


 */


function
 
createAndSendDocument
()
 
{


  
try
 
{


    
// Create a new Google Doc named 'Hello, world!'


    
const
 
doc
 
=
 
DocumentApp
.
create
(
"Hello, world!"
);



    
// Access the body of the document, then add a paragraph.


    
doc


      
.
getBody
()


      
.
appendParagraph
(
"This document was created by Google Apps Script."
);



    
// Get the URL of the document.


    
const
 
url
 
=
 
doc
.
getUrl
();



    
// Get the email address of the active user - that's you.


    
const
 
email
 
=
 
Session
.
getActiveUser
().
getEmail
();



    
// Get the name of the document to use as an email subject line.


    
const
 
subject
 
=
 
doc
.
getName
();



    
// Append a new string to the "url" variable to use as an email body.


    
const
 
body
 
=
 
`Link to your doc: 
${
url
}
`
;



    
// Send yourself an email with a link to the document.


    
GmailApp
.
sendEmail
(
email
,
 
subject
,
 
body
);


  
}
 
catch
 
(
err
)
 
{


    
// TODO (developer) - Handle exception


    
console
.
log
(
"Failed with error %s"
,
 
err
.
message
);


  
}


}
```
- Haz clic en Guardar .
Haz clic en Guardar .
- Haz clic en Proyecto sin título .
Haz clic en Proyecto sin título .
- Ingresa un nombre para tu secuencia de comandos y haz clic en Cambiar nombre .
Ingresa un nombre para tu secuencia de comandos y haz clic en Cambiar nombre .
## Ejecuta la secuencia de comandos:
Para ejecutar la secuencia de comandos, haz lo siguiente:
- Haz clic en Ejecutar .
- Cuando se te solicite, autoriza la secuencia de comandos. <<../samples/_snippets/oauth.md>>
- Cuando finalice la ejecución de la secuencia de comandos, revisa tu carpeta Recibidos de Gmail para ver el correo electrónico.
- Abre el correo electrónico y haz clic en el vínculo para abrir el documento que creaste.
## Próximos pasos
- Extender Docs
- Extiende Hojas de cálculo de Google
- Extiende Presentaciones de Google
- Funciones básicas de JavaScript
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

### prueba esta solución popular de combinación de correo electrónico

- Página principal
- Google Workspace
- Apps Script
- Ejemplos
# Crea una combinación de correo electrónico con Gmail y Hojas de cálculo de Google Organiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.
Nivel de programación : Principiante Duración : 10 minutos Tipo de proyecto : Automatización con un menú personalizado
## Objetivos
- Comprende qué hace la solución.
- Comprende qué hacen los servicios de Apps Script dentro de la solución.
- Configura la secuencia de comandos.
- Ejecuta la secuencia de comandos.
## Acerca de esta solución
Completa automáticamente una plantilla de correo electrónico con datos de Hojas de cálculo. Los correos electrónicos se envían desde tu cuenta de Gmail para que puedas responder a los correos de los destinatarios.
Importante : Esta muestra de combinación de correo electrónico está sujeta a los límites de correo electrónico que se describen en Cuotas para los servicios de Google .
### Cómo funciona
Creas una plantilla de borrador de Gmail con marcadores de posición que corresponden a los datos de una hoja de cálculo de Hojas de cálculo. Cada encabezado de columna en una hoja representa una etiqueta de marcador de posición. La secuencia de comandos envía la información de cada marcador de posición de la hoja de cálculo a la ubicación de la etiqueta de marcador de posición correspondiente en el borrador de tu correo electrónico.
### Servicios de Apps Script
En esta solución, se usan los siguientes servicios:
- Servicio de Gmail : Obtiene, lee y envía el borrador del correo electrónico que quieres enviar a tus destinatarios. Si tu correo electrónico incluye caracteres Unicode, como emojis, usa el servicio de correo en su lugar. Obtén más información para actualizar el código y agregar caracteres Unicode a tu correo electrónico .
- Si tu correo electrónico incluye caracteres Unicode, como emojis, usa el servicio de correo en su lugar. Obtén más información para actualizar el código y agregar caracteres Unicode a tu correo electrónico .
- Servicio de hojas de cálculo : Completa los marcadores de posición de correo electrónico con la información personalizada de cada destinatario.
## Requisitos previos
Para usar esta muestra, necesitas cumplir con los siguientes requisitos previos:
- Una Cuenta de Google (es posible que las cuentas de Google Workspace requieran la aprobación del administrador)
- Un navegador web con acceso a Internet
## Configura la secuencia de comandos
Completa los siguientes pasos para configurar la secuencia de comandos.
### Crea el proyecto de Apps Script
- Haz clic en el siguiente botón para crear una copia de la hoja de cálculo de ejemplo de la combinación de correspondencia de Gmail/Hojas de cálculo . El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo. Crear una copia
Haz clic en el siguiente botón para crear una copia de la hoja de cálculo de ejemplo de la combinación de correspondencia de Gmail/Hojas de cálculo . El proyecto de Apps Script para esta solución se adjunta a la hoja de cálculo.
Crear una copia
- En la hoja de cálculo que copiaste, actualiza la columna Recipients con las direcciones de correo electrónico que quieras usar en la combinación de correspondencia.
En la hoja de cálculo que copiaste, actualiza la columna Recipients con las direcciones de correo electrónico que quieras usar en la combinación de correspondencia.
- (Opcional) Agrega, edita o quita columnas para personalizar los datos que deseas incluir en tu plantilla de correo electrónico.
(Opcional) Agrega, edita o quita columnas para personalizar los datos que deseas incluir en tu plantilla de correo electrónico.
Si cambias el nombre de las columnas Recipient o Email Sent , debes actualizar el código correspondiente en el proyecto de Apps Script. Para abrir el proyecto de Apps Script desde la hoja de cálculo, selecciona Extensiones > Apps Script .
### Crea una plantilla de correo electrónico
- En tu cuenta de Gmail, crea un borrador de correo electrónico. Para incluir datos de la hoja de cálculo en tu correo electrónico, usa marcadores de posición que correspondan a los nombres de las columnas entre llaves, como {{First name}} . Si le aplicas formato al texto del correo electrónico, también debes hacerlo con los corchetes de los marcadores de posición. Los marcadores de posición distinguen entre mayúsculas y minúsculas, y deben coincidir exactamente con los encabezados de las columnas.
`{{First name}}`
- Si le aplicas formato al texto del correo electrónico, también debes hacerlo con los corchetes de los marcadores de posición.
- Los marcadores de posición distinguen entre mayúsculas y minúsculas, y deben coincidir exactamente con los encabezados de las columnas.
- Copia la línea de asunto del borrador de tu correo electrónico.
## Ejecuta la secuencia de comandos:
- En la hoja de cálculo, haz clic en Combinar correspondencia > Enviar correos electrónicos . Es posible que debas actualizar la página para que aparezca este menú personalizado.
- Cuando se te solicite, autoriza la secuencia de comandos. Si la pantalla de consentimiento de OAuth muestra la advertencia Esta app no está verificada , selecciona Opciones avanzadas > Ir a {Nombre del proyecto} (no seguro) para continuar.
Cuando se te solicite, autoriza la secuencia de comandos.
Si la pantalla de consentimiento de OAuth muestra la advertencia Esta app no está verificada , selecciona Opciones avanzadas > Ir a {Nombre del proyecto} (no seguro) para continuar.
- Haz clic en Combinar correspondencia > Enviar correos electrónicos de nuevo.
Haz clic en Combinar correspondencia > Enviar correos electrónicos de nuevo.
- Pega la línea de asunto de la plantilla de correo electrónico y haz clic en Aceptar .
Pega la línea de asunto de la plantilla de correo electrónico y haz clic en Aceptar .
Si aplicaste un filtro a la hoja, la secuencia de comandos seguirá enviando correos electrónicos a los participantes filtrados, pero no agregará la marca de tiempo.
## Revisa el código
Para revisar el código de Apps Script de esta solución, haz clic en Ver código fuente :
#### Ver el código fuente
```
// To learn how to use this script, refer to the documentation:


// https://developers.google.com/apps-script/samples/automations/mail-merge



/*


Copyright 2022 Martin Hawksey



Licensed under the Apache License, Version 2.0 (the "License");


you may not use this file except in compliance with the License.


You may obtain a copy of the License at



    https://www.apache.org/licenses/LICENSE-2.0



Unless required by applicable law or agreed to in writing, software


distributed under the License is distributed on an "AS IS" BASIS,


WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


See the License for the specific language governing permissions and


limitations under the License.


*/



/**


 * @OnlyCurrentDoc


 */



/**


 * Change these to match the column names you are using for email


 * recipient addresses and email sent column.


 */


const
 
RECIPIENT_COL
 
=
 
"Recipient"
;


const
 
EMAIL_SENT_COL
 
=
 
"Email Sent"
;



/**


 * Creates the menu item "Mail Merge" for user to run scripts on drop-down.


 */


function
 
onOpen
()
 
{


  
const
 
ui
 
=
 
SpreadsheetApp
.
getUi
();


  
ui
.
createMenu
(
"Mail Merge"
).
addItem
(
"Send Emails"
,
 
"sendEmails"
).
addToUi
();


}



/**


 * Sends emails from sheet data.


 * @param {string} subjectLine (optional) for the email draft message


 * @param {Sheet} sheet to read data from


 */


function
 
sendEmails
(
subjectLine
,
 
sheet
 
=
 
SpreadsheetApp
.
getActiveSheet
())
 
{


  
// option to skip browser prompt if you want to use this code in other projects


  
let
 
processedSubjectLine
 
=
 
subjectLine
;


  
if
 
(
!
processedSubjectLine
)
 
{


    
processedSubjectLine
 
=
 
Browser
.
inputBox
(


      
"Mail Merge"
,


      
"Type or copy/paste the subject line of the Gmail "
 
+


        
"draft message you would like to mail merge with:"
,


      
Browser
.
Buttons
.
OK_CANCEL
,


    
);



    
if
 
(
processedSubjectLine
 
===
 
"cancel"
 
||
 
processedSubjectLine
 
===
 
""
)
 
{


      
// If no subject line, finishes up


      
return
;


    
}


  
}



  
// Gets the draft Gmail message to use as a template


  
const
 
emailTemplate
 
=
 
getGmailTemplateFromDrafts_
(
processedSubjectLine
);



  
// Gets the data from the passed sheet


  
const
 
dataRange
 
=
 
sheet
.
getDataRange
();


  
// Fetches displayed values for each row in the Range HT Andrew Roberts


  
// https://mashe.hawksey.info/2020/04/a-bulk-email-mail-merge-with-gmail-and-google-sheets-solution-evolution-using-v8/#comment-187490


  
// @see https://developers.google.com/apps-script/reference/spreadsheet/range#getdisplayvalues


  
const
 
data
 
=
 
dataRange
.
getDisplayValues
();



  
// Assumes row 1 contains our column headings


  
const
 
heads
 
=
 
data
.
shift
();



  
// Gets the index of the column named 'Email Status' (Assumes header names are unique)


  
// @see http://ramblings.mcpher.com/Home/excelquirks/gooscript/arrayfunctions


  
const
 
emailSentColIdx
 
=
 
heads
.
indexOf
(
EMAIL_SENT_COL
);



  
// Converts 2d array into an object array


  
// See https://stackoverflow.com/a/22917499/1027723


  
// For a pretty version, see https://mashe.hawksey.info/?p=17869/#comment-184945


  
const
 
obj
 
=
 
data
.
map
((
r
)
 
=
>

    
heads
.
reduce
((
o
,
 
k
,
 
i
)
 
=
>
 
{


      
o
[
k
]
 
=
 
r
[
i
]
 
||
 
""
;


      
return
 
o
;


    
},
 
{}),


  
);



  
// Creates an array to record sent emails


  
const
 
out
 
=
 
[];



  
// Loops through all the rows of data


  
obj
.
forEach
((
row
,
 
rowIdx
)
 
=
>
 
{


    
// Only sends emails if email_sent cell is blank and not hidden by a filter


    
if
 
(
row
[
EMAIL_SENT_COL
]
 
===
 
""
)
 
{


      
try
 
{


        
const
 
msgObj
 
=
 
fillInTemplateFromObject_
(
emailTemplate
.
message
,
 
row
);



        
// See https://developers.google.com/apps-script/reference/gmail/gmail-app#sendEmail(String,String,String,Object)


        
// If you need to send emails with unicode/emoji characters change GmailApp for MailApp


        
// Uncomment advanced parameters as needed (see docs for limitations)


        
GmailApp
.
sendEmail
(
row
[
RECIPIENT_COL
],
 
msgObj
.
subject
,
 
msgObj
.
text
,
 
{


          
htmlBody
:
 
msgObj
.
html
,


          
// bcc: 'a.bcc@email.com',


          
// cc: 'a.cc@email.com',


          
// from: 'an.alias@email.com',


          
// name: 'name of the sender',


          
// replyTo: 'a.reply@email.com',


          
// noReply: true, // if the email should be sent from a generic no-reply email address (not available to gmail.com users)


          
attachments
:
 
emailTemplate
.
attachments
,


          
inlineImages
:
 
emailTemplate
.
inlineImages
,


        
});


        
// Edits cell to record email sent date


        
out
.
push
([
new
 
Date
()]);


      
}
 
catch
 
(
e
)
 
{


        
// modify cell to record error


        
out
.
push
([
e
.
message
]);


      
}


    
}
 
else
 
{


      
out
.
push
([
row
[
EMAIL_SENT_COL
]]);


    
}


  
});



  
// Updates the sheet with new data


  
sheet
.
getRange
(
2
,
 
emailSentColIdx
 
+
 
1
,
 
out
.
length
).
setValues
(
out
);



  
/**


   * Get a Gmail draft message by matching the subject line.


   * @param {string} subject_line to search for draft message


   * @return {object} containing the subject, plain and html message body and attachments


   */


  
function
 
getGmailTemplateFromDrafts_
(
subject_line
)
 
{


    
try
 
{


      
// get drafts


      
const
 
drafts
 
=
 
GmailApp
.
getDrafts
();


      
// filter the drafts that match subject line


      
const
 
draft
 
=
 
drafts
.
filter
(
subjectFilter_
(
subject_line
))[
0
];


      
// get the message object


      
const
 
msg
 
=
 
draft
.
getMessage
();



      
// Handles inline images and attachments so they can be included in the merge


      
// Based on https://stackoverflow.com/a/65813881/1027723


      
// Gets all attachments and inline image attachments


      
const
 
allInlineImages
 
=
 
draft
.
getMessage
().
getAttachments
({


        
includeInlineImages
:
 
true
,


        
includeAttachments
:
 
false
,


      
});


      
const
 
attachments
 
=
 
draft


        
.
getMessage
()


        
.
getAttachments
({
 
includeInlineImages
:
 
false
 
});


      
const
 
htmlBody
 
=
 
msg
.
getBody
();



      
// Creates an inline image object with the image name as key


      
// (can't rely on image index as array based on insert order)


      
const
 
img_obj
 
=
 
allInlineImages
.
reduce
((
obj
,
 
i
)
 
=
>
 
{


        
obj
[
i
.
getName
()]
 
=
 
i
;


        
return
 
obj
;


      
},
 
{});



      
//Regexp searches for all img string positions with cid


      
const
 
imgexp
 
=
 
/<img.*?src="cid:(.*?)".*?alt="(.*?)"[^\>]+>/g;


      
const
 
matches
 
=
 
[...
htmlBody
.
matchAll
(
imgexp
)];



      
//Initiates the allInlineImages object


      
const
 
inlineImagesObj
 
=
 
{};


      
for
 
(
const
 
match
 
of
 
matches
)
 
{


        
inlineImagesObj
[
match
[
1
]]
 
=
 
img_obj
[
match
[
2
]];


      
}



      
return
 
{


        
message
:
 
{


          
subject
:
 
subject_line
,


          
text
:
 
msg
.
getPlainBody
(),


          
html
:
 
htmlBody
,


        
},


        
attachments
:
 
attachments
,


        
inlineImages
:
 
inlineImagesObj
,


      
};


    
}
 
catch
 
(
e
)
 
{


      
throw
 
new
 
Error
(
"Oops - can't find Gmail draft"
);


    
}



    
/**


     * Filter draft objects with the matching subject linemessage by matching the subject line.


     * @param {string} subject_line to search for draft message


     * @return {object} GmailDraft object


     */


    
function
 
subjectFilter_
(
subject_line
)
 
{


      
return
 
(
element
)
 
=
>
 
{


        
if
 
(
element
.
getMessage
().
getSubject
()
 
===
 
subject_line
)
 
{


          
return
 
element
;


        
}


      
};


    
}


  
}



  
/**


   * Fill template string with data object


   * @see https://stackoverflow.com/a/378000/1027723


   * @param {string} template string containing {{}} markers which are replaced with data


   * @param {object} data object used to replace {{}} markers


   * @return {object} message replaced with data


   */


  
function
 
fillInTemplateFromObject_
(
template
,
 
data
)
 
{


    
// We have two templates one for plain text and the html body


    
// Stringifing the object means we can do a global replace


    
let
 
template_string
 
=
 
JSON
.
stringify
(
template
);



    
// Token replacement


    
template_string
 
=
 
template_string
.
replace
(
/{{[^{}]+}}/g
,
 
(
key
)
 
=
>
 
{


      
return
 
escapeData_
(
data
[
key
.
replace
(
/[{}]+/g
,
 
""
)]
 
||
 
""
);


    
});


    
return
 
JSON
.
parse
(
template_string
);


  
}



  
/**


   * Escape cell data to make JSON safe


   * @see https://stackoverflow.com/a/9204218/1027723


   * @param {string} str to escape JSON special characters from


   * @return {string} escaped string


   */


  
function
 
escapeData_
(
str
)
 
{


    
return
 
str


      
.
replace
(
/[\\]/g
,
 
"\\\\"
)


      
.
replace
(
/[\"]/g
,
 
'\\"'
)


      
.
replace
(
/[\/]/g
,
 
"\\/"
)


      
.
replace
(
/[\b]/g
,
 
"\\b"
)


      
.
replace
(
/[\f]/g
,
 
"\\f"
)


      
.
replace
(
/[\n]/g
,
 
"\\n"
)


      
.
replace
(
/[\r]/g
,
 
"\\r"
)


      
.
replace
(
/[\t]/g
,
 
"\\t"
);


  
}


}
```
## Modificaciones
Puedes editar la automatización de combinación de correspondencia para que se ajuste a tus necesidades. En los siguientes ejemplos, se muestran algunos cambios opcionales que puedes realizar en el código fuente.
#### Agrega parámetros de correo electrónico de Cco, Cc, ReplyTo o From
El código de muestra incluye varios parámetros adicionales, que están comentados, que te permiten controlar el nombre de la cuenta desde la que se envía el correo electrónico, responder a las direcciones de correo electrónico, así como las direcciones de correo electrónico de Cco y Cc.
Para activar los parámetros que deseas agregar, quita las barras diagonales // que se encuentran delante de cada uno.
`//`
En el siguiente ejemplo, se muestra un fragmento de la función sendEmails que activa la mayoría de los parámetros de correo electrónico:
`sendEmails`
```
GmailApp
.
sendEmail
(
row
[
RECIPIENT_COL
]
,
 
msgObj
.
subject
,
 
msgObj
.
text
,
 
{


         
htmlBody
:
 
msgObj
.
html
,


         
bcc
:
 
'bcc@example.com'
,


         
cc
:
 
'cc@example.com'
,


         
from
:
 
'from.alias@example.com'
,


         
name
:
 
'name of the sender'
,


         
replyTo
:
 
'reply@example.com'
,


        
//
 
noReply
:
 
true
,
 
//
 
if
 
the
 
email
 
should
 
be
 
sent
 
from
 
a
 
generic
 
no
-
reply
 
email
 
address
 
(
not
 
available
 
to
 
gmail
.
com
 
users
)
```
En el ejemplo anterior, el parámetro noReply sigue comentado porque se configuró el parámetro replyTo .
`noReply`
`replyTo`
#### Incluye caracteres Unicode en tus correos electrónicos
Si deseas incluir caracteres Unicode, como emojis, en tus correos electrónicos, debes actualizar el código para usar el servicio de correo en lugar del servicio de Gmail.
En el código de muestra, actualiza la siguiente línea:
```
GmailApp
.
sendEmail
(
row
[
RECIPIENT_COL
]
,
 
msgObj
.
subject
,
 
msgObj
.
text
,
 
{
```
Reemplaza la línea por el siguiente código:
```
MailApp
.
sendEmail
(
row
[
RECIPIENT_COL
]
,
 
msgObj
.
subject
,
 
msgObj
.
text
,
 
{
```
## Colaboradores
La muestra fue creada por Martin Hawksey, jefe de Diseño y Tecnología de Aprendizaje en el Edinburgh Futures Institute, bloguero y experto de Google Developers.
- Encuentra a Martin en Twitter @mhawksey .
- Lee las publicaciones de blog de Martin relacionadas con Apps Script.
- Mira el programa de Martin en YouTube, Totally Unscripted .
Google mantiene esta muestra con la ayuda de los Google Developer Experts.
## Próximos pasos
- Menús personalizados en Google Workspace
- Extender Hojas de cálculo
Salvo que se indique lo contrario, el contenido de esta página está sujeto a la licencia Atribución 4.0 de Creative Commons , y los ejemplos de código están sujetos a la licencia Apache 2.0 . Para obtener más información, consulta las políticas del sitio de Google Developers . Java es una marca registrada de Oracle o sus afiliados.
Última actualización: 2026-04-23 (UTC)

---

