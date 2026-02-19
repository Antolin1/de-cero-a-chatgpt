# De cero a ChatGPT

Este repositorio contiene los materiales del curso "De cero a ChatGPT" impartido en el CIFP Carlos III.

Organización del README:
- **Requisitos básicos** que es necesario **tener instalados antes de la primera sesión**.
- **Entorno de Python para los contenidos de deep learning** (días 1,2,3 y primera parte del día 4). Sería ideal tenerlo listo antes de la primera sesión, pero no es imprescindible.
- **Entorno de Python para los contenidos de agentes** (segunda parte del día 4). Sería ideal tenerlo listo antes de la cuarta sesión, pero no es imprescindible. Se recomienda encarecidamente tener instalado Ollama antes de la cuarta sesión.
- **Tabla con los notebooks** y sus links a colab. Esto es como una contigencia que solo aplica en algunos casos por si alguien tiene problemas para configurar su entorno local.




## Requisitos


### Sistema operativo

Se recomienda usar Linux. Si usáis Windows, se recomienda usar WSL2 con Ubuntu.

### VS Code

Instalar [Visual Studio Code](https://code.visualstudio.com/). Se recomienda instalar las siguientes extensiones:
- Python
- Jupyter
- WSL (si usáis WSL2)
- GitHub Copilot

### Conda

Conda es un sistema de gestión de paquetes y entornos virtuales. Se recomienda instalar [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (Anaconda también es una opción, pero Miniconda es más ligera). Cuando esté instalado, debe salir en un terminal el mensaje `(base)`, lo que indica que el entorno base de conda está activo.

### Docker

Instalar [Docker Desktop](https://docs.docker.com/get-docker/). Docker se usará para ejecutar Ollama y servidores MCP.

### Cuenta de Ollama y API KEY

Crear una cuenta en [Ollama](https://ollama.com/). Ollama expone en la nube varios modelos que podemos usar para hacer pruebas. Sacad también un [token de acceso](https://docs.ollama.com/cloud#authentication).

### Gemini API KEY

Sacad una [API KEY](https://ai.google.dev/gemini-api/docs/api-key) para usar Gemini desde código. Este LLM lo usaremos para agentes.

### Habilita el GitHub Copilot en el VS Code

Tenéis que [activar](https://code.visualstudio.com/docs/copilot/overview#_getting-started) el GitHub Copilot de vuestro VS Code. Creo que hay un plan gratuito limitado. Sin embargo, os recomiendo encarecidamente que cojáis la versión pro. Los docentes tienen acceso gratuito si se aplica a [GitHub Education](https://docs.github.com/en/education/about-github-education/github-education-for-teachers/about-github-education-for-teachers). Una vez aplicado, se puede solicitar el acceso a GitHub Copilot [aquí](https://docs.github.com/en/copilot/how-tos/manage-your-account/get-free-access-to-copilot-pro#about-free-github-copilot-pro-access).



## Entorno para contenidos de deep learning (días 1,2,3 y primera parte del día 4)

Vamos a manejar dos entornos de Python: uno para los contenidos de deep learning y otro para los contenidos relacionados con agentes. Esto es así debido a conflictos de dependencias entre las librerías usadas en cada uno de los tópicos.

Los entornos

1. Crear el entorno de deep learning:

```bash
conda create -n deep_learning python=3.11 -y
```

2. Activar el entorno:

```bash
conda activate deep_learning
```

3. Instalar Pytorch siguiendo las instrucciones de la [página oficial](https://pytorch.org/get-started/locally/). Si tenéis GPU Nvidia, instalar la versión con soporte CUDA. Seleccionad Stable, Linux, pip, Python, y vuestra versión de CUDA (si tenéis GPU Nvidia; se puede checkear con `nvidia-smi`) o CPU en su defecto. Ejecutar el comando que se genera en la terminal para instalar Pytorch.

4. Instalar las dependencias:

```bash
pip install -r requirements-dl.txt
```

5. Instalar Jupyter:

```bash
conda install -c conda-forge notebook
```

6. Configurar el intérprete de Python en VS Code para que use el entorno `deep_learning`. Para ello, abrir la paleta de comandos (Ctrl+Shift+P), escribir "Python: Select Interpreter" y seleccionar el entorno `deep_learning`.

## Entorno para contenidos de agentes (segunda parte del día 4)

1. Crear el entorno de agentes:

```bash
conda create -n agents python=3.11 -y
```

2. Activar el entorno:

```bash
conda activate agents
```

3. Instalar las dependencias:

```bash
pip install -r requirements-agents.txt
```

4. Instalar Jupyter:

```bash
conda install -c conda-forge notebook
```

5. Descargar la imagen de Ollama siguiendo las instrucciones de la [página oficial](https://hub.docker.com/r/ollama/ollama). Asegurarse de que Docker está corriendo antes de iniciar Ollama. Si tenéis GPU, seguid las instrucciones para correr Ollama con soporte GPU.

6. Configurar el intérprete de Python en VS Code para que use el entorno `agents`. Para ello, abrir la paleta de comandos (Ctrl+Shift+P), escribir "Python: Select Interpreter" y seleccionar el entorno `agents`.

Si se va a utilizar Ollama el contenedor debe estar corriendo. Si se ha terminado con Ollama, recomiendo pausar el contenedor.

## Tabla con notebooks y contenidos

### Día 1

Los siguientes notebooks pertenecen al Día 1:

| Notebook | Open in Colab |
|----------|---------------|
| [Gradiente Descendente](dia1/1_gradiente_descendente.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia1/1_gradiente_descendente.ipynb) |
| [Los Tres Ingredientes](dia1/2_los_tres_ingredientes.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia1/2_los_tres_ingredientes.ipynb) |
| [Regularización](dia1/3_regularizacion.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia1/3_regularizacion.ipynb) |
| [Ejercicio Final](dia1/4_ejercicio_final.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia1/4_ejercicio_final.ipynb) |

### Día 2

Los siguientes notebooks pertenecen al Día 2:

| Notebook | Open in Colab |
|----------|---------------|
| [Tokenizer, RNN, LSTM, GRU](dia2/tokenizer_rnn_lstm_gru.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia2/tokenizer_rnn_lstm_gru.ipynb) |

### Día 3

Los siguientes notebooks pertenecen al Día 3:

| Notebook | Open in Colab |
|----------|---------------|
| [Encoder](dia3/1_encoder.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia3/1_encoder.ipynb) |
| [Encoder Random](dia3/2_encoder_random.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia3/2_encoder_random.ipynb) |
| [Ejercicio Encoder](dia3/3_ejercicio_encoder.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia3/3_ejercicio_encoder.ipynb) |
| [Transformer](dia3/transformer.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia3/transformer.ipynb) |

### Día 4.1

Los siguientes notebooks pertenecen al Día 4.1:

| Notebook | Open in Colab |
|----------|---------------|
| [Decoder](dia4-1/4_decoder.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia4-1/4_decoder.ipynb) |
| [Decoder SFT 1](dia4-1/5_decoder_sft_1.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia4-1/5_decoder_sft_1.ipynb) |
| [Decoder SFT LoRA](dia4-1/5_decoder_sft_lora.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia4-1/5_decoder_sft_lora.ipynb) |
| [Número Parámetros](dia4-1/6_numero_parametros.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia4-1/6_numero_parametros.ipynb) |

### Día 4.2

Los siguientes notebooks pertenecen al Día 4.2:

| Notebook | Open in Colab |
|----------|---------------|
| [0. Ollama](dia4-2/0_ollama.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia4-2/0_ollama.ipynb) |
| [1. Smolagents](dia4-2/1_smolagents.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia4-2/1_smolagents.ipynb) |
| [2. Langchain Agent](dia4-2/2_langchain_agent.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Antolin1/de-cero-a-chatgpt/blob/main/dia4-2/2_langchain_agent.ipynb) |

El enunciado del ejercicio MCP se encuentra [aquí](dia4-2/MCP-Ejercicio.md).