"""
# avocado
Historical data on avocado prices and sales volume in multiple US markets


Context
It is a well known fact that Millenials LOVE Avocado Toast. It's also a well known fact that all Millenials live
in their parents basements.

Clearly, they aren't buying home because they are buying too much Avocado Toast!

But maybe there's hope... if a Millenial could find a city with cheap avocados, they could live out the
Millenial American Dream.

Content
This data was downloaded from the Hass Avocado Board website in May of 2018 & compiled into a single CSV. 
Here's how the Hass Avocado Board describes the data on their website:

The table below represents weekly 2018 retail scan data for National retail volume (units) and price. 
Retail scan data comes directly from retailers’ cash registers based on actual retail sales of Hass avocados. 
Starting in 2013, the table below reflects an expanded, multi-outlet retail data set. Multi-outlet 
reporting includes an aggregation of the following channels: grocery, mass, club, drug, dollar and military. 
The Average Price (of avocados) in the table reflects a per unit (per avocado) cost, even when multiple 
units (avocados) are sold in bags. The Product Lookup codes (PLU’s) in the table are only for Hass avocados. 
Other varieties of avocados (e.g. greenskins) are not included in this table.

Some relevant columns in the dataset:

Date - The date of the observation
AveragePrice - the average price of a single avocado
type - conventional or organic
year - the year
Region - the city or region of the observation
Total Volume - Total number of avocados sold
4046 - Total number of avocados with PLU 4046 sold
4225 - Total number of avocados with PLU 4225 sold
4770 - Total number of avocados with PLU 4770 sold
Acknowledgements
Many thanks to the Hass Avocado Board for sharing this data!!

http://www.hassavocadoboard.com/retail/volume-and-price-data

Inspiration
In which cities can millenials have their avocado toast AND buy a home?

Was the Avocadopocalypse of 2017 real?

"""
import os 
import pandas as pd

"""
AVOCADO_PATH = os.path.join("avocado")

def load_avocado_data(avocado_path = AVOCADO_PATH):
    csv_path = os.path.join(avocado_path,"avocado.csv")
    return pd.read_csv(csv_path)


avocado_dataframe = load_avocado_data()
"""
# Carga de la data
avocado_dataframe = pd.read_csv("avocado.csv") 

# Visualizo los primeros 5 registros del dataframe
head_avocado = avocado_dataframe.head()
print(head_avocado)
#rename, rename_axis ????

# Descripcion de la data
print(avocado_dataframe.info())

# Nombro columna que aparece como Unnamed: 0 - Colimna sin encabezado
#print(dir(avocado_dataframe)) # Listo Funciones, Metodos que puedo usar
avocado_dataframe.rename(columns={'Unnamed: 0':'semana'}, inplace = True)
# Listo nombres de columnas
print(avocado_dataframe.columns)


# Verifico si algunos campos son variables categoricas
print(avocado_dataframe["type"].value_counts())
print(avocado_dataframe["year"].value_counts())
print(avocado_dataframe["region"].value_counts())
#print(avocado_dataframe["semana"].value_counts())
print(avocado_dataframe["semana"].sort_values(ascending = False))
print(avocado_dataframe["semana"].unique())


# Resumen de los atributos de datos numericos
print(avocado_dataframe.describe())







