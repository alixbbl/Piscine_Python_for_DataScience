import pandas as pd
import os

def load(path: str) -> pd.DataFrame:
	"""
	This function takes a CSV format file and load the data, returns it on dataset format.
	Here, dataset format is DataFrame (dataset with several rows and columns), and Series
	(for unidimensional data), both can be used to perform modifications and operations.
	"""
	if not os.path.exists(path):
		print("File doesn't exist.")
		return None
	_, extension = os.path.splitext(path)
	if extension.lower() != ".csv":
		print("Bad file extension")
		return ()
	try:
		dataset = pd.read_csv(path)
		# dataset = dataset.drop(columns=id)
		print(f"Loading file of dimensions : {dataset.shape}")
	except Exception as e:
		print(f"Error opening this file : {e}")
		return None
	return dataset

# RAPPEL :
# size va donner le nombre d'éléments et shape les dimensions de l'objet.
