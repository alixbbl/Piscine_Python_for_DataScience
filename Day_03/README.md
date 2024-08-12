# DAY 03 : CLASSES ET HÉRITAGE DE CLASSES

Il s'agit des mêmes méthodes de POO qu'en C++. On retrouve les constructeurs et destructeurs, ici sous la forme des méthodes "magic" init() et die(). Les lois de l'héritage sont les mêmes.
Attention ici aux notions de "décorateurs"'

## Les différents décorateurs :

`@abstractmethod` : Indique qu'une méthode est une méthode abstraite, c'est-à-dire une méthode qui doit être implémentée par les classes filles. Elle ne possède pas d'implémentation dans la classe abstraite où elle est déclarée. Son utilisation assure que toutes les classes dérivées implémentent cette méthode, ce qui est crucial pour l'héritage et la polymorphisme dans la programmation orientée objet.

`@classmethod` : Ce décorateur modifie une méthode pour qu'elle devienne une méthode de classe. Cela signifie que la méthode reçoit la classe elle-même comme premier argument au lieu d'une instance de cette classe (traditionnellement nommé `cls`). Cela est utile pour créer des méthodes qui doivent opérer sur la classe elle-même, plutôt que sur des instances de la classe.

`@staticmethod` : Ce décorateur transforme une méthode en méthode statique, ce qui signifie qu'elle ne reçoit ni une instance de la classe (`self`), ni la classe elle-même (`cls`) comme premier argument. Elle est essentiellement comme une fonction normale qui vit dans l'espace de noms de la classe, et elle est utilisée pour des opérations qui ne nécessitent pas d'accéder aux attributs ou méthodes de la classe ou de ses instances.

On retrouve des setters et des getters permettant de set ou d'acceder aux attributs des instances des classes.
Une fonction définie au sein d'une classe, sans décorateur, concernera une instance de classe.
