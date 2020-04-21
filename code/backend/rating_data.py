import pandas as pd
import numpy as np
import logging
from .data import Data
from .filepaths import rating_dataset_filepath
from .canadas_coordinates import *
from .dataset_columns import  rating_columns #rating_dataset_site_names,

class RatingData(Data):
	def __init__(self):
		Data.__init__(self)

		# Load the rating_dataset csv file into a DataFrame and retain only the relevant columns
		self.dataset_df = pd.read_csv(rating_dataset_filepath)
		# self.sites = full_dataset_site_names
		# self.df = self.dataset_df[full_dataset_site_names]
		self.target = self.dataset_df[rating_columns]
		# self.longitudes = []
		# self.latitudes = []
		# for site in full_dataset_site_names:
		# 	self.longitudes.append(self.dataset_df[site + '_lon'][0])
		# 	self.latitudes.append(self.dataset_df[site + '_lat'][0])
