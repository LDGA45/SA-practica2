# SA-practica2
practica 2 software avanzado

## Docker y sus componentes

Docker es una plataforma de código abierto diseñada para facilitar la creación, implementación y ejecución de aplicaciones en entornos contenerizados. Los contenedores son entornos ligeros y portátiles que encapsulan una aplicación junto con sus dependencias y configuraciones, permitiendo que se ejecute de manera consistente en diferentes entornos.

#### componontes:

Docker Engine: Es el componente central de Docker y es responsable de la creación y ejecución de contenedores. Incluye el demonio de Docker (dockerd), una API para interactuar con Docker y una interfaz de línea de comandos (docker).

Imagen: Una imagen de Docker es un paquete ligero y autónomo que incluye todo lo necesario para ejecutar una aplicación, incluyendo el código, el entorno de ejecución, las bibliotecas, las variables de entorno y las configuraciones. Las imágenes son la base para la creación de contenedores.

Contenedor: Un contenedor es una instancia en tiempo de ejecución de una imagen de Docker. Puedes pensar en un contenedor como un proceso en ejecución que está aislado del sistema y tiene su propio sistema de archivos, espacio de red y configuraciones. Los contenedores son portátiles y se pueden ejecutar de manera consistente en diferentes entornos.

Dockerfile: Es un archivo de texto que contiene instrucciones para construir una imagen de Docker. Define el entorno, las dependencias y la configuración de una aplicación. A partir de un Dockerfile, puedes construir una imagen utilizando el comando docker build.

Registro (Registry): Es un repositorio centralizado de imágenes de Docker. Docker Hub es un registro público donde se pueden encontrar y compartir imágenes de Docker, pero también puedes utilizar registros privados o locales. Al construir una imagen, esta se puede enviar a un registro para que otros la descarguen y utilicen.

Docker Compose: Una herramienta que permite definir y gestionar aplicaciones multi-contenedor. Con Docker Compose, puedes describir las dependencias, servicios, redes y volúmenes de una aplicación en un archivo docker-compose.yml y luego iniciar toda la aplicación con un solo comando.

Red: Docker proporciona redes que permiten la comunicación entre contenedores. Las redes pueden ser utilizadas para aislar contenedores o para permitir la comunicación entre ellos.

## Kubernetes
Kubernetes (también conocido como K8s) es una plataforma de código abierto diseñada para la orquestación y gestión de contenedores en entornos distribuidos. Facilita la implementación, escalabilidad y operación de aplicaciones en contenedores. A continuación, se describen los componentes clave de Kubernetes:

#### componentes de kubernetes:
Nodo (Node): Un nodo es una máquina física o virtual en el clúster de Kubernetes. Cada nodo ejecuta el software necesario para comunicarse con el clúster y puede alojar uno o varios contenedores.

Pod: El pod es la unidad más pequeña en Kubernetes y representa un entorno de ejecución para un contenedor o un conjunto de contenedores. Los contenedores dentro de un pod comparten el mismo espacio de red y almacenamiento local. Los pods son escalables y pueden ser replicados para garantizar la disponibilidad y resistencia.

Control Plane: También conocido como plano de control, es el conjunto de componentes que gestionan y controlan el estado del clúster de Kubernetes. Incluye los siguientes componentes:

Kube-API Server: Actúa como la interfaz principal para la gestión del clúster. Las operaciones y las configuraciones se envían al servidor API, que luego interactúa con otros componentes para llevar a cabo las acciones solicitadas.

Etcd: Un almacén de datos distribuido que almacena la configuración del clúster, el estado y los metadatos. Es altamente consistente y proporciona una fuente única de verdad para el estado del clúster.

Control Manager: Gestiona y supervisa el estado de los recursos en el clúster. Por ejemplo, el Control Manager asegura que el número correcto de réplicas de un pod esté en funcionamiento.

Scheduler: Decide en qué nodo se debe ejecutar un pod, teniendo en cuenta los requisitos y restricciones definidos.

Kubelet: Es un agente que se ejecuta en cada nodo del clúster y se comunica con el API Server. Es responsable de asegurarse de que los contenedores en los pods estén en ejecución y en buen estado.

Kube Proxy: Mantiene las reglas de red en los nodos. Facilita la comunicación de red entre los pods y asegura que las solicitudes se enruten correctamente.

Service: Define una abstracción que expone aplicaciones o servicios implementados en los pods. Un servicio proporciona un punto de acceso estable mediante el cual otros servicios pueden comunicarse con las aplicaciones.

Ingress: Gestiona las reglas de enrutamiento externo al clúster, permitiendo el acceso a servicios desde fuera del clúster.

ConfigMap y Secret: Recursos para gestionar la configuración de la aplicación y secretos, respectivamente, de forma separada del código fuente.

Namespace: Proporciona un ámbito para recursos de clúster, permitiendo la división lógica y el aislamiento de aplicaciones y servicios.

## Contratos de microservicios

  Contrato de Microservicios body { font-family: 'Arial', sans-serif; line-height: 1.6; padding: 20px; } h1 { color: #333; } h2 { color: #555; } code { background-color: #f4f4f4; border: 1px solid #ddd; padding: 5px 10px; display: block; margin: 10px 0; } pre { background-color: #f4f4f4; border: 1px solid #ddd; padding: 10px; overflow-x: auto; }

Contrato de Microservicio de Gestión de Productos (Product Service)
===================================================================

1\. API de Productos:
---------------------

*   **Endpoint:** `/productos`
*   **Métodos Permitidos:** `GET`, `POST`
*   **GET:** Devuelve una lista de productos disponibles.
*   **POST:** Crea un nuevo producto.
    *   Parámetros: `{ "nombre": "Nombre del Producto", "precio": 19.99, "stock": 100 }`
    *   Retorna el producto creado.

2\. Contrato de Mensajes para el Servicio de Productos:
-------------------------------------------------------

    `Mensaje de Evento: Producto Agregado       {         "evento": "producto_agregado",         "producto_id": "123",         "nombre": "Nombre del Producto",         "precio": 19.99,         "stock": 100       }`
    
  

Contrato de Microservicio de Gestión de Pedidos (Order Service)
===============================================================

1\. API de Pedidos:
-------------------

*   **Endpoint:** `/pedidos`
*   **Métodos Permitidos:** `GET`, `POST`
*   **GET:** Devuelve una lista de pedidos realizados.
*   **POST:** Crea un nuevo pedido.
    *   Parámetros: `{ "productos": [{ "producto_id": "123", "cantidad": 2 }] }`
    *   Retorna el resumen del pedido.

2\. Contrato de Mensajes para el Servicio de Pedidos:
-----------------------------------------------------

    `Mensaje de Evento: Pedido Realizado       {         "evento": "pedido_realizado",         "pedido_id": "456",         "productos": [{ "producto_id": "123", "cantidad": 2 }],         "total": 39.98       }`
    
  

Notas:
------

*   Estos contratos son simplificados y se centran en las interacciones esenciales entre los microservicios.
*   Pueden incluirse detalles adicionales, como autenticación, manejo de errores, y detalles de formato de datos.
*   Los contratos de eventos (mensajes) son cruciales para la comunicación asincrónica entre microservicios.