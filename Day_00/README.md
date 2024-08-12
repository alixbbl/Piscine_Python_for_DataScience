# PYTHON : Day 00, les eléments à retenir

Les ensembles les plus utilisés :

- **tuple** : un tuple, une fois assigné, n'est pas modifiable, il peut toutfois être parcouru grâce à un index. Format : (.., .., ..).
- **liste** : une liste est indexable, et modifiable. Son format est en crochets : [.., .., .., ..].
- **set** : Il s'agit d'un ensemble non ordonné, donc non indexable. On le parcourt et on le modifie via des fonctions (clear, remove, add ...). Le format est : {.., .., .., ..}.
- **dictionnaire** : les dictionnaires sont des containers de type clef-valeur, on peut les modifier mais ils ne sont pas indexables. On les modifie en accédant aux valeurs via les clefs. Le format est {clef1 : valeur1, clef2, valeur2, .., clefn : valeurn}.

Pour identifier un type facilement, il existe une fonction de base : isistance(object, type)
qui retourne un booléen. C'est un builtin de Python, aucune lib n'est nécessaire.

## Pour récupérer des arguments depuis la ligne de commande :
`arguments = sys.argv`
"import sys" est nécessaire afin de pouvoir utiliser le mot-clef.

## Faire appel au main se fait de cette manière :
`def main():`
`	code..`
`if __name__ == "__main__":`
`	main()`

## Comment recuperer et ouvrir un fichier en Python :
` if len(sys.argv) > 1:`
`     filename = sys.argv[1]`
`     with open(filename, 'r') as file:`
`         content = file.read()`
`         print(content)`

## Évaluation dynamique d'une fonction avec eval() :
avec cette fonction builtin, on évalue la "valeur" ou la véracité d'une fonction en tant que chaine de caractères,
Exemple : "eval(functino)" avec "function = lambda x: x % 2 == 0", est testée, or c'est bien une expression valide sous forme de string.
Cette fonction eval() doit etre utilisée avec précaution car elle va évaluer et donc exécuter n'importe quel code soumis, elle peut donc présenter une importante brèche de sécurité.

## Les listes de compréhension :
C'est un moyen de créer une liste sur la base d'une opération appliquée à chaque elément d' une liste de départ. Comme une sorte de filtre:
`nouvelle_liste = [nouvel_element for element in liste_de_base if condition_remplie]`
