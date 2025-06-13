# ************* PYTHON PISCINE - DAY 0 *************

# ******************* Exercice 8 *******************


def ft_tqdm(lst: range) -> None:
    """
    This function prints a loading bar on the output.
    """
    length = len(lst)
    progress = 0
    total = 100
    for element in lst:
        filled_length = int(total * progress // length)
        bar = "█" * filled_length + " " * (total - filled_length)
        print(f"\r{bar} {progress+1}/{length} ({(progress+1)/length*100:.2f}%)", end="")
        yield progress
        progress += 1
    print()


# Ici, la boucle sert principalement a relancer le yield, yield permet
# en effet d'envoyer a la fonction appelante, un resultat en temps reel,
# avant que la fonction executée ne soit terminée.
