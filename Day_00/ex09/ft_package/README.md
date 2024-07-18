# Comment réaliser cet exercice :

## Répondre a la commande pip show -v ft_package :

**Name**: Le nom du package. Cela correspond à l'argument name dans *setup.py*.

**Version**: La version du package. Cela correspond à l'argument version dans *setup.py*.

**Summary**: Une courte description du package. Cela correspond à l'argument description dans
*setup.py*.

**Home-page**: L'URL de la page d'accueil du projet, souvent un dépôt GitHub. Cela correspond
à l'argument url dans *setup.py*.

**Author**: Le nom de l'auteur du package. Cela correspond à l'argument author dans *setup.py*.

**Author-email**: L'email de l'auteur du package. Cela correspond à l'argument author_email
dans *setup.py*.

**License**: La licence sous laquelle le package est distribué. Cela correspond à l'argument
license dans *setup.py*.

**Location**: L'emplacement où le package est installé sur le système de fichiers local.
Cette information est déterminée par pip lors de l'installation du package.

**Requires**: Les dépendances du package. Cela correspond à l'argument install_requires
dans *setup.py*. Si vide, cela signifie que le package n'a pas de dépendances ou que pip
n'a pas pu les résoudre.

**Required-by**: Les autres packages qui dépendent de ce package. Cette information est
déterminée par pip en fonction des autres packages installés.

**Metadata-Version**: La version du format de métadonnées utilisé pour stocker les
informations du package. Cette information est gérée par setuptools et pip.

**Installer**: L'outil utilisé pour installer le package. Dans ce cas, c'est pip.

**Classifiers**: Une liste de classificateurs qui décrivent le package, comme son statut
de développement, son environnement, sa licence, etc. Cela correspond à l'argument
classifiers dans *setup.py*.

**Entry-points**: Les points d'entrée du package, utilisés pour exposer des commandes
CLI ou des extensions. Cela correspond à l'argument entry_points dans *setup.py*.

## Vérifier la présence de tous les documents nécessaires et ceux requis :

- pyproject.py :
- README et LICENSE

Ensuite, run la commande suivante à la racine du package:
`python -m build`
le package est alors construit.

Ensuite on l'installe :
`pip install /chemin/du/package`

On peut ensuite vérifier l'installation avec :
`pip show -v ft_package`

Si problemes lors de l'installation :
python3 -m venv env
source env/bin/activate
pip install --upgrade pip setuptools wheel
pip install ./dist/ft_package-0.0.1.tar.gz
