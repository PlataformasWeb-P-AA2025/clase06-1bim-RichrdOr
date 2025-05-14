from sqlalchemy.orm import sessionmaker

from crear_base import Saludo
from configuracion import engine

import pandas as pd

Session = sessionmaker(bind=engine)
session = Session()

miSaludo2 = Saludo()
miSaludo2.mensaje = "Buenas tardes"
miSaludo2.tipo = "formal"



df = pd.read_csv("./data/saludos_mundo.csv")

print(df)