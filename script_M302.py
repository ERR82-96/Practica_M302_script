import xml.etree.ElementTree as ET
import requests
import json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

headers = {'accept': 'application/json'}
r = requests.get('https://zenodo.org/api/records/3608959',headers)
record = json.loads(r.text)
url = record['files'][0]["links"]["self"]
data = pd.read_csv(url)

plt.figure(figsize=(10,8))
plt.scatter(x=data.X,y=data.Y,s=data.Poblacion/10000)
plt.show()