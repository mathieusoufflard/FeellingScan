# FeellingScan

## table des matières

* [Description](#Description)
* [Prérequi Mac OS M1](#Prérequi-Mac-OS-M1)
* [Instalation Miniforge](#Instalation-Miniforge)
* [Avoir la bonne version Python](#Avoir-la-bonne-verssion-Python)
* [Instalation de jupyter et crée l’environnement](#Instalation-de-jupyter-et-crée-l’environnement)
* [Enregistrer l’environnement et tester](#Enregistrer-l’environnement-et-tester)
* [pour plus d'infomation](#pour-plus-d'infomation)
* [Démarrer le projet](#Démarrer-le-projet)

## Description

projet product management. Miroir connectée/scanner de sentiment. Grâce à une caméra intégrée, une photo est prise et une IA détecte une émotion et Lance sur Youtube une music et un jeu de lumière adaptée.

## Prérequi Mac OS M1

- Python, TensorFlow, IDE (Jupyter, TensorFlow, autres)
- Miniforge

### Instalation Miniforge

l'instalation est via Homebrew https://brew.sh/ via le terminal 
Après installation ouvrer un nouveau terminal

```
$ xcode-select --install

```

Si la commande suivante donne une erreur. l'instalation peux se faire sur l'app store

```
$ brew install miniforge
```

Noubliez pas de noter le repertoire.

### Avoir la bonne version Python

Des précédentes installations de pythons peuvent générer cette erreur :

```
Collecting package metadata (repodata.json): done
Solving environment: failed

ResolvePackageNotFound: 
  - tensorflow-deps
```

Verifier votre version 

```
$ which python
```

la commande devrait répondre quelque chose comme ça
```
/opt/homebrew/Caskroom/miniforge/base/bin/python
```
vous devrier voire "homebrew" et "miniforge". si vous voyez "anaconda" or "miniconda" votre path pointe vers le movais Python.
vous devez modifier votre .zshrc avec

*/usr/local/Caskroom/miniforge/base
*/opt/homebrew/Caskroom/miniforge/base

### Instalation de jupyter et crée l’environnement

```
$ conda install -y jupyter
```

```
$ conda deactivate
$ conda env create -f tensorflow-apple-metal.yml -n tensorflow
$ conda activate tensorflow
$ conda install nb_conda
```

### Enregistrer l’environnement et tester

```
$ python -m ipykernel install --user --name tensorflow --display-name "Python 3.9 (tensorflow)"
$ jupyter notebook
```

Executer le code suivant

```
import sys

import tensorflow.keras
import pandas as pd
import sklearn as sk
import tensorflow as tf

print(f"Tensor Flow Version: {tf.__version__}")
print(f"Keras Version: {tensorflow.keras.__version__}")
print()
print(f"Python {sys.version}")
print(f"Pandas {pd.__version__}")
print(f"Scikit-Learn {sk.__version__}")
gpu = len(tf.config.list_physical_devices('GPU'))>0
print("GPU is", "available" if gpu else "NOT AVAILABLE")
```

pour avoir ce resultat

```
Init Plugin
Init Graph Optimizer
Init Kernel
Tensor Flow Version: 2.5.0
Keras Version: 2.5.0

Python 3.9.6 | packaged by conda-forge | (default, Jul  6 2021, 08:51:19) 
[Clang 11.1.0 ]
Pandas 1.3.0
Scikit-Learn 0.24.2
GPU is available
```
## pour plus d'infomation
https://brew.sh/
https://github.com/jeffheaton/t81_558_deep_learning/blob/master/install/tensorflow-install-mac-metal-jul-2021.ipynb
https://www.youtube.com/watch?v=_CO-ND1FTOU

## Démarrer le projet

executer le script main.py Attention a modifier les lien present dans les fichiers.

