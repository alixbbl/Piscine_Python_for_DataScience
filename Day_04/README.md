# DAY 04 - Les essentiels à retenir

## Les arguments *args et **kwargs:
Lorsqu'une fonction prend un ensemble d'arguments de natures variées, comme avec
ft_statistics (des int, des float, des strings assignées...). On peut dstinguer
deux types d'arguments.

**Les *args:**
Ce sont les arguments positionnels, c'est à dire des valeurs directement entrées
dans la fonction. Leur position est importante.
**Les **kwargs:**
Ce sont les arguments nommés, il s'agit de paires key/value. Ce sont les noms des
fonctions de stats dans ft_statistics.
Pour parcourir la liste de kwargs, on utilise la méthode items(), en effet, il s'agit
d'un dictionnaire, ou liste de paires de clefs/valeurs.
`for key, value in kwargs.items():`

L'utilisation de cette syntaxe permet une grande souplesse pour la fonction.

## Les fonctions "lambda" :
Une lambda est une petite fonction définie par le mot-clef. Elles peuvent être utiles
comme dans le cas d'un dictionnaire de key/value : string/fonction, pour retarder l'exec.
Ce sont de petites fonctions anonymes, utiles pour des opérations courtes ou pour mettre des
fonctions en argument d'autres fonctions plus lourdes.
En termes de syntaxe :
 - Utilisation traditionnelle avec def
`def add(x, y):`
    `return x + y`

- Équivalent en utilisant une lambda
`add_lambda = lambda x, y: x + y`

- Utilisation
`print(add(2, 3))  # Affiche 5`
`print(add_lambda(2, 3))  # Affiche 5`

Autre propriété, sans lambda, la fonction est exécutée immédiatement :
`result = np.mean([1, 2, 3])`

Mais avec une lambda (dans un dict par exemple), la fonction n'est exécutée que lorsqu'on appelle la lambda :
`lazy_mean = lambda: np.mean([1, 2, 3])`
Pour exécuter la fonction, on appelle la lambda :
`result = lazy_mean()`

Dans le cas de ft_statistics, cela permet d'ecrire le dictionnaire sans appeler directement les fonctions :
`arguments = np.array(args) # on met les arguments positionnels dans un array`
`STATS_FUNCTIONS = {`
`	'mean' : lambda: np.mean(arguments),`
`	'median' : lambda: np.median(arguments),`
`	'quartile' : lambda: np.percentile(arguments, 25),`
`	'std' : lambda: np.std(arguments),`
`	'var' : lambda: np.var(arguments)`
`}'`

Il est possible de créer son propre décorateur de fonction (cf. ex02 Day04).

## Les modules "random" et "string"
**random** contient des fonctionnalités permettant de générer des nombres aléatoires et de réaliser des sélections aléatoires.
**string** contient des outils pou manipuler les chaines de caractères.
