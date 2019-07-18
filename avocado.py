import os 
import pandas as pd

"""
AVOCADO_PATH = os.path.join("avocado")

def load_avocado_data(avocado_path = AVOCADO_PATH):
    csv_path = os.path.join(avocado_path,"avocado.csv")
    return pd.read_csv(csv_path)


avocado_dataframe = load_avocado_data()
"""
avocado_dataframe = pd.read_csv("avocado.csv") 

head_avocado = avocado_dataframe.head()
print(head_avocado)

#print("info", avocado_dataframe.info()) 







