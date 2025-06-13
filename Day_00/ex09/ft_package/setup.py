from setuptools import find_packages, setup

setup(
    name="ft_package",
    version="0.0.1",
    author="eagle",
    author_email="eagle@42.fr",
    description="A sample test package",
    url="https://github.com/eagle/ft_package",  # `url` au lieu de `Homepage`
    license="MIT",  # Assurez-vous que la licence correspond à ce que vous voulez
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        # Configuration des points d'entrée si nécessaire, ici vide
    },
    install_requires=[
        # Liste des dépendances nécessaires
    ],
)
