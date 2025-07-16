from sqlalchemy import create_engine, inspect, text
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False)
inspector = inspect(engine)

# Listar tablas
tablas = inspector.get_table_names()
print("Tablas en la DB:", tablas)

# Mostrar primeras 3 filas de 'Artist'
with engine.connect() as conn:
    result = conn.execute(text("SELECT ArtistId, Name FROM Artist LIMIT 3"))
    for row in result:
        print(row)

