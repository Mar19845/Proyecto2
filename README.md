# Proyecto2
Sistema de recomendacion musical

# ChatBotPythones
ChatBot AI utilizando el Procesador de Lenguaje Natual "Dialogflow" integrado en Facebook Messenger, programado en Node.js. 

## Webhook
El archivo index.js ejecuta el servidor que funciona como  webhook en el Port 5000. Este sirve como intermediario entre Facebook Messenger y Dialogflow.
```
node index.js
```

## Rutina de Carga de Conocimiento
El archivo carga.js consulta todos los intents y sus respectivos mensajes a la base de datos MySQL y crea dentro de Dialogflow los mismos intents.
```
node carga.js
```
El archivo UpdateDB.js identifica mensajes dentro de los intents de Dialogflow que no estan almacenados en la base de datos. Inmediatamente inserta estos valores en la base de datos.
```
node UpdateDB.js
```

## Aspectos Relevantes para la Configuración en Intergación
### Iniciar e Integrar Webhook
En la línea de comandos de ngrok ejectar el servidor del webhook.
```
ngrok http 5000
```
Luego se mostrará el link al tunel del servidor. Este será ingresado en fbdev dentro de la configuración de webhook.
//Insertar imagen de configuración fvdeb.

### Conexión con la Base de Datos
Dentro del archivo [conexion.js](https://github.com/wsaldana/ChatBotPythones/blob/master/conexion.js) configurar los parametros de conexión
```
var con = mysql.createConnection({
  host: "<HOST>",
  user: "<USUARIO>",
  password: "<CONTRASEÑA>",
  database: "<NOMBRE DE LA BASE DE DATOS>"
});
```
### Dialogflow en la Rutina de Carga
El POST que se realiza para cargar el conocimiento de la base de datos a Dialogflow se encuentra en el archivo [PostNewData.js](https://github.com/wsaldana/ChatBotPythones/blob/master/PostNewData.js), y el GET por el cual obtenemos la información de los intents de Dialogflow se ubica en el archivo [UpdateDB.js](https://github.com/wsaldana/ChatBotPythones/blob/master/UpdateDB.js). En ambos se deberá de especificar el token de autorización específico del agente de Dialogflow con el que trabajaremos. Este parámetro lo encontraremos en el header del método.
```
headers: {
            'Authorization': 'Bearer <TOKEN DE AUTORIZACIÓN API DE DIALOGFLOW>',
            'Content-Type': 'application/json; charset=UTF-8'
        }
```
### Configuraciones del Webhook
Se debe de realizar la misma declaración del Token de autorización del API de Dialogflow en el header que se encuentra en el archivo [index.js](https://github.com/wsaldana/ChatBotPythones/blob/master/index.js).
Además, en el mismo archivo se debe de especificar el Token de autorización de Facebook developer.
```
var clientServerOptions2={
          uri: "https://graph.facebook.com/v4.0/me/messages?access_token=<<TOKEN DE AUTORIZACIÓN DE FBDEV>>",
          body: ResMsg,
          method: 'POST',
          headers: {
              'Content-Type': 'application/json; charset=UTF-8'
          }
```

Si no conocemos el token del API de Dialogflow, se puede encontrar en la configuración de nuestro agente en Dialogflow.
