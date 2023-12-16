import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

tech = pd.read_json('https://raw.githubusercontent.com/sahilrahman12/Technology-Lookup-Web-Application/main/technologies.json')
#cats = pd.read_json('https://raw.githubusercontent.com/AliasIO/wappalyzer/master/src/technologies.json')


data_tech = tech.copy()
print(data_tech.head())

data_tech = data_tech.T
print(data_tech.head())

print(data_tech.info())