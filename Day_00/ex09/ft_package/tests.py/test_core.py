# ici on met des tests, ils sont optionnels mais recommandés
from ft_package import count_in_list

def test_count_in_list():
	assert count_in_list(["toto", "tata", "toutou", "toto"], "toto") == 2
	assert count_in_list(["toto", "tata", "toutou", "titi"], "toto") == 0
