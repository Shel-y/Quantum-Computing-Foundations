# ⚛️ Simulador Cuántico Serverless en AWS

Este repositorio contiene el código fuente y la arquitectura de la demostración técnica **"De lo Clásico a lo Cuántico con AWS"**, presentada en el AWSome Women Summit LATAM 2026.

El proyecto es un micro-simulador cuántico que demuestra matemáticamente la **Superposición** (aplicando la compuerta de Hadamard) utilizando álgebra lineal. Todo el proyecto está construido con una arquitectura 100% Serverless utilizando el Free Tier de AWS.

## 📐 Arquitectura del Proyecto

El simulador se divide en dos componentes principales:
1. **Frontend (Visualizador):** Una interfaz web interactiva alojada estáticamente en **AWS Amplify**.
2. **Backend (Motor Cuántico):** Una función de **AWS Lambda** (Python + NumPy) expuesta a través de una Lambda Function URL pública, encargada de realizar la multiplicación de matrices del vector de estado.

---

## 🚀 Guía de Despliegue en AWS (Paso a Paso)

Si deseas replicar este simulador en tu propia cuenta de AWS sin salir de la capa gratuita, sigue estos pasos:

### Fase 1: El Backend (AWS Lambda)

1. Entra a la consola de AWS y ve al servicio **Lambda**.
2. Haz clic en **Crear función** > **Crear desde cero**.
3. Nómbrala `SimuladorCuantico` y selecciona el Runtime **Python 3.12** (o superior).
4. En *Configuración avanzada*, marca **Habilitar la URL de la función**.
5. Tipo de autenticación: **NONE**.
6. Marca la casilla **Configurar el uso compartido de recursos entre orígenes (CORS)** y crea la función.
7. **Agrega la Capa de NumPy:**
   * En la página de tu función, baja a la sección **Capas** (Layers) y haz clic en **Añadir capa**.
   * Selecciona *Capas de AWS* > `AWSSDKPandas-Python3...` (asegúrate de que coincida con tu versión de Python) > Selecciona la última versión > **Añadir**.
8. Ve a la pestaña **Código**, borra el contenido por defecto y pega el código que se encuentra en `backend/lambda_function.py`.
9. Haz clic en **Deploy** (Implementar).
10. Copia tu **URL de la función** (Function URL).

### Fase 2: El Frontend (AWS Amplify)

1. Abre el archivo `frontend/index.html` en tu editor de código favorito.
2. Busca la variable `LAMBDA_URL` en la sección del `<script>` y reemplázala con la URL que copiaste en el paso anterior:
   ```javascript
   const LAMBDA_URL = '[https://tu-lambda-url.on.aws/](https://tu-lambda-url.on.aws/)';
   ```
3. Guarda el archivo y comprímelo en un archivo ZIP (ej. simulador.zip).

4. Ve a la consola de AWS y busca el servicio AWS Amplify.

5. Selecciona Deploy without Git (Despliegue manual) para crear una nueva aplicación.

6. Nombra tu entorno (ej. prod o staging).

7. Arrastra y suelta tu archivo simulador.zip y haz clic en Guardar e implementar.

    ¡Listo! AWS te proporcionará un enlace HTTPS seguro y público para interactuar con tu simulador cuántico.

💻 Ejecución Local

Si solo deseas ver la interfaz visual sin desplegarla en la nube:

    Clona este repositorio.

    Abre el archivo frontend/index.html directamente en tu navegador web.

    (Opcional) Si tu Lambda no está activa, puedes comentar la petición fetch en el código JavaScript y descomentar la respuesta simulada para ver la animación CSS.

Desarrollado por Shel | Creado para la comunidad y la democratización de la computación cuántica.
