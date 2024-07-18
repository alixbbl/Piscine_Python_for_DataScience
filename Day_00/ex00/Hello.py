# ************* PYTHON PISCINE - DAY 0 *************

# ******************* Exercice 0 *******************

ft_list = ["Hello", "tata!"]
# la liste est indexable et modifiable (listes ou tableaux)

ft_tuple = ("Hello", "toto!")
# A línverse, un tuple n'est pas modifiable une fois assigné
# on peut cependant recuperer ses valeurs via un index

ft_set = {"Hello", "tutu!"}
# il s'agit d'un ensemble, non ordonné, on utilise donc des 
# fonctions pour acceder aux valeurs (clear, remove, add ...)

ft_dict = {"Hello" : "titi!"}
# les dict sont des containers de type clef-valeur

ft_list[1] = 'World!'
ft_tuple = ("Hello", "France!")
ft_set.clear()
ft_set.add('Paris!')
ft_set.add('Hello')
ft_dict["Hello"] = '42Paris!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)