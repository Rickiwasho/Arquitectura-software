# React Essentials      
### Contenidos:
- [Javascript](##Javascript)
- [JSX](##JSX)
- [Primeros pasos en React](##React)
## 1. Javascript     
### 1.1 Variables    
Usamos **var**, **let** y **const** para declarar una variable. El alcance de var son las funciones, pero let y const son de alcance de bloque.     

### 1.2 Arrays     
En contraste a las variables, un arreglo puede almacenar multiples valores. Cada valor en un arreglo tiene un índice, y cada indice tiene una referencia a una dirección de memoria. Se puede acceder a cada valor del arreglo mediante el uso de su índice. El índice de un arreglo comienza en cero, y termina en n-1.    

Un arreglo puede ser una colección de distintos tipos, de datos ordenados y puede reordenarse. También permite almacenar datos duplicados o no almacenar dato alguno.   

#### Creando un arreglo    
Los arreglos se pueden crear de distintas formas. Es muy común usar const, en vez de let para declarar un arreglo, en este caso, no se podrá usar nuevamente el nombre del arreglo para crear variables.    
``` js
const arr1 = [] 
//creando un arreglo vacío.   
   
const arr2 = ['h','o','l','a'] 
//creando un arreglo con elementos.   
```
#### Métodos para manipular arreglos     
    
Existen diferentes métodos para manipular arreglos, Estos son algunos de los métodos más comunes:   
- **Array()**, crea un arreglo.      
- **length**, para saber el tamaño del arreglo.   
- **concat(arr)**, para concatenar dos arreglos.   
- **indexOf(n)**, para saber si un elemento está en el arreglo, entrega el índice en caso que esté, y en caso contrario, entrega -1.   
- **lastIndexOf(n)**, entrega el índice del último elemento que coincida con el parametro ingresado, si el parametro no se encuentra en el arreglo, entrega -1.   
- **slice(a,b)**, entrega una porción del arreglo. Recibe como parametros dos valores, el comienzo y el final.   
- **splice**,   
- **join**,   
- **toString**, convierte un arreglo en string.   
- **includes**,    
- **isArray**,   
- **fill**,    
- **push(a)**, agrega un elemento al final del arreglo.   
- **pop()**, remueve un elemento del final del arreglo.  
- **reverse()**, invierte el orden del arreglo.    
- **shift()**, remueve el primer elemento del arreglo.   
- **unshift(a)**, agrega un elemento al comienzo del arreglo.   

### 1.3 Condicionales    
Las declaraciones condicionales son usadas para hacer decisiones basadas en condiciones. Por defecto, las declaraciones en un script de Javascript son ejecutadas secuencialmente desde arriba hacia abajo.   
- if(condition){}
- if(condition){} else{}
- if(condition){} else if(condition){} else{}
- switch(case-value){case 1://break case 2: // break default: }
- ternary operator   

### 1.4 Loops    
En programación usamos diferentes tipos de loops para realizar tareas repetitivas. El loop se cumple hasta que la condición deje de cumplirse, pero a veces, nos gustaría interrumpirlo o saltar cierta iteración, por esta razón usamos 'break' para salir del loop y 'continue' para saltar una iteración. Javascript  tiene diferentes tipos de loops:   
- for
- while
- do while
- for of
- forEach
- for in

### 1.5 Alcance
La variable es una parte fundamental en la programación. Declaramos las variables para almacenar datos, pero estos pueden tener un alcance global, local o window.   
Cuando usamos let y const, el alcance es de bloque (local), sin embargo, si la variable es declarada fuera de los curly brackets ({}), la variable pasa a ser global.

### 1.6 Objetos
Todo puede ser un objeto. Los objetos tienen propiedades y las propiedades tienen valores, por lo que un objeto es un par clave-valor. El orden de la llave no está reservado o no hay orden. 

#### Creando un objeto
Para crear un objeto literal, usamos curly brackets.   

```js    
const person = {
    // objeto vacío
}     
const rectangle = { length:20, width:20,}
```
#### Obteniendo valores de un arreglo
Podemos acceder a los valores de un objeto usando dos métodos:
- Usando **.** seguido del nombre clave.
- Usando square brackets
 
```js
const person = {
    firstName: 'Louis',
}
console.log(person.firstName)
console.log(person['firstName'])
```

#### Creando métodos objeto
Generalmente se emplean los métodos objeto dentro de la descripción del objeto con la finalidad de modificar u obtener los atributos del objeto.
Ej:  
```js
const person = {
    firstName = 'Louis',
    lastName = 'Litt',
    //Obteniendo información
    getFullName: function(){
        return `${this.firstName} ${this.lastName}`
    },
}
```
#### Métodos objeto
Existen diferentes métodos para manipular un objeto. Algunos de los más populares son:
- Object.assign
- Object.keys
- Object.values
- Object.entries
- hasOwnProperty

### 1.7 Funciones
Una función es un bloque de código reutilizable diseñado para realizar una tarea en específico. Una función es declarada con un nombre y seguido de un paréntesis (). El paréntesis puede tomar parámetros (llamados argumentos) o no. Para extraer valores de una función, esta debe tener **return**, y para obtener el valor debemos llamar o invocar a la funcion.   
Las funciones hacen el código, limpio y fácil de leer y testear, reutilizable, etc.   
Las funciones pueden ser declaradas o creadas de distintas maneras:
- _Declaration function_
- _Expression funcion_
- _Anonymous function_
- _Arrow function_

# PROFUNDIZAR!!!!!!!!!!!!!!!!!!!!!!

### 1.8 Funciones de alto nivel
Las funciones de alto nivel son fincione s que toman a otras funciones como sus parámetros o  que retornan a una función como valor de retorno.
La función pasada como parámetro es llamada _Callback_.   

```js
const callback = (n) => {
    return n ** 2
}
function cube(callback, n){
    return callback(n) * n 
}
```
#### Ejecutando actividades en tiempo real
- **setInterval:**
Podemos usar setInterval con funciones de alto nivel para hacer actividades continuamente en ciertos intervalos de tiempo. El método setInterval (globalscope) toma una función callback y la duración(tiempo) como parámetros, esta duración es en milisegundos y el callback será llamado en ese intervalo de tiempo.
```js
function sayHello(){ // funcion callback
    console.log('Hello') // acción de la funcion
}
setInterval(sayHello, 2000) //imprime hello cada 2 segundos
```
- **setTimeout:**
Podemos usar setTimeout con funciones de alto nivel para ejecutar acciones en algún tiempo futuro. El método toma una función callback y la duración como parámetros. La duracion es en milisegundos y la función callback espera esa cantidad de tiempo.

```js
function sayHello(){
    console.log('Hello')
}
setTimeout(sayHello,2000) //imprime hello después de esperar 2 segundos
```

### 1.9 Desestructuración y propagación
#### Desestructuración:
La desestrocturación es una forma de descomprimir arreglos y objetos, y asignarlos a una variable distinta. La desestructuración nos permite escriibir código limpio y legible.
- **desestructurar arreglos:**
Los arreglos son una lista de diferentes tipos de datos ordenados por su índice. 
Podemos acceder a cada ítem del arreglo utilizando su índice e iterando con un loop.
Si el tamaño del arreglo es pequeño es mejor acceder a sus elementos de la siguiente forma:

```js
const countries = ['Chile', 'Argentina', 'Perú']
const [chi,arg,pe] = countries
console.log(chi,arg,pe) // Chile, Argentina, Perú
```
Otros casos:

```js
const fullStack = [
    ['HTML','CSS','JS','React'],
    ['Node', 'Django', 'MongoDB']
]
const[frontend, backend] = fullstack
console.log(frontend,backend)
```
Y si no estamos interesados en cada uno de los ítems del arreglo, podemos omitir alguno usando una coma en ese índice.

```js
const countries = ['chile', 'argentina', 'peru', 'bolivia']
const [chi, arg, , bol] =  countries // se omite peru
```
También, podemos almacenar ciertos datos del arreglo en variables y el resto almacenarlo en un subarreglo
```js
const countries = [
    'Chile',
    'Argentina',
    'Peru',
    'Bolivia',
]
const [chi, ...rest] = countries
console.log(chi, rest) //Chile, ["Argentina","Peru","Bolivia"]
```
- **Desestructurar objetos:**
# FALTA PROFUNDIZAR!!!!

#### Operador de propagación(spread) o Rest
Cuando desestructuramos un arreglo usamos el operador de propagación(...) para obtener el resto de los elementos del arreglo.
Podemos copiar un arreglo con spread (...)
```js
const nums = [0,1,2,3,4,5,6,7,8,9]
const unidades = [...nums]
```
También, podemos copiar un objeto:
```js
const user = {
    name: 'James',
    age: '10 years',
    genre: 'Male',
}
const copiedUser = {...user}
```
# FALTA PROFUNDIZAR!!!!

### 1.10 Programación funcional
La _programación funcional_ nos permite escribir un código más corto, limpio, y también resolver problemas complejos que serían complejos de resolver de forma convencional.

#### 1. forEach
Usamos forEach cuando queremos iterar 
### 1.11 Classes
### 1.12 Document object model (DOM)