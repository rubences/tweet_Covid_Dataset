'''
"# Introducción\n",
DESCRIPCION BREVE DEL DATASET Y LOS OBJETIVOS A CUMPLIR.\n",
"\n"
        "Contenido: \n",
        "\n",
        "1. [Cargar y chequear datos](#1)\n",
        "1. [Descripción de variables](#2)\n",
        "    * [Analísis univariado de variables](#3)\n",
        "        * [Variables categóricas](#4)\n",
        "        * [Variables numéricas](#5)\n",
        "1. [Análisis básico de datos](#6)\n",
        "1. [Detección de outliers](#7)\n",
        "1. [Valores perdidos](#8)\n",
        "    * [Encontrar valores perdidos](#9)\n",
        "    * [Rellenar valores perdidos](#10)\n",
        "1. [Visualización](#11)\n",
        "    * [Correlación entre variables](#12)\n",
        "    * [DATOS A COMPARAR DEL DATASET -- DATOS_ANALIZADOS_DATASET](#13)\n",
        "    * [SON LAS DIFERENTES VARIABLES QUE APARECEN EN LA PRIMERA FILA DEL DATASET](#12)\n",
        "    * [Rellenar perdidos: DEL DATASET](#20)\n",
        "1. [Ingeniería de características](#21)\n",
        "    * [VALORES DEL DATASET](#22)\n",
        "    * [TODOS LOS VALORES](#23)\n",
        "    * [Eliminar VALORES NO DESEADOS DEL DATASET](#28)\n",
        "1. [Modeling](#29)\n",
        "    * [Train - Test Split](#30)\n",
        "    * [Simple Logistic Regression](#31)\n",
        "    * [Hyperparameter Tuning -- Grid Search -- Cross Validation](#32) \n",
        "    * [Ensemble Modeling](#33)\n",
        "    * [Prediction and Submission](#34)"

#Cargar librerías necesarias \n",
        "import numpy as np # algebra lineal\n",
        "import pandas as pd # procesado de datos, ficheros CSV\n",
        "import math\n",
        "\n",
        "import matplotlib.pyplot as plt\n",
        "plt.style.use(\"seaborn-whitegrid\")\n",
        "\n",
        "import seaborn as sns\n",
        "\n",
        "from collections import Counter\n",
        "\n",
        "import warnings\n",
        "warnings.filterwarnings(\"ignore\")"

CARGA DE FICHEROS

 "train_df = pd.read_csv(\"/content/gdrive/My Drive/alberto_tests/titanic_train.csv\")\n",
        "test_df = pd.read_csv(\"/content/gdrive/My Drive/alberto_tests/titanic_test.csv\")\n",
        "test_PassengerId = train_df[\"PassengerId\"]"

'''