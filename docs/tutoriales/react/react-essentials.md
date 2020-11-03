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

### 1.3 Conditionals    
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

### 1.5 Scope
La variable es una parte fundamental en la programación. Declaramos las variables para almacenar datos, pero estos pueden tener un alcance global, local o window.   
Cuando usamos let y const, el alcance es de bloque (local), sin embargo, si la variable es declarada fuera de los curly brackets ({}), la variable pasa a ser global.

### 1.6 Object
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

### 1.7 Functions
Una función es un bloque de código reutilizable diseñado para realizar una tarea en específico. Una función es declarada con un nombre y seguido de un paréntesis (). El paréntesis puede tomar parámetros (llamados argumentos) o no. Para extraer valores de una función, esta debe tener **return**, y para obtener el valor debemos llamar o invocar a la funcion.   
Las funciones hacen el código, limpio y fácil de leer, reutilizable y fácil de testear.   
Las funciones pueden ser declaradas o creadas de distintas maneras:
# PROFUNDIZAR!!!!!!!!!!!!!!!!!!!!!!


### 1.8 Higher order function
### 1.9 Destructuring and spreading
### 1.10 Functional programming
### 1.11 Classes
### 1.12 Document object model (DOM)