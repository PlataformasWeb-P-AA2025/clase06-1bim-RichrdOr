from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine
import pandas as pd

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Leer el CSV
df = pd.read_csv("./data/saludos_mundo.csv", sep='|')

# Iterar sobre cada fila del DataFrame
for index, row in df.iterrows():
    miSaludo2 = Saludo2()
    miSaludo2.mensaje = row['saludo']
    miSaludo2.tipo = row['tipo']
    miSaludo2.origen = row['origen']
    
    session.add(miSaludo2)

# Guardar los cambios en la base de datos
session.commit()
