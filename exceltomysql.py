import pandas as pd
excel_file = 'datos.xlsx'
sheet_name = 'Hoja 1'

# Cargar datos desde el archivo Excel
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Generar la parte del INSERT INTO
def generate_sql_insert(df):
    sql_insert = "INSERT INTO REGISTROS (TELEFONO, FECHA_REGISTRO,TURNO) VALUES "
    value_statements = []

    for index, row in df.iterrows():
        # Obtener los valores de cada fila
        telefono = str(row.get('CELULAR', 'null'))
        fecha = str(row.get('FECHA', 'null'))
        turno = str(row.get('TURNO', 'null'))
       

        # Formar una tupla de valores para esta fila
        values_tuple = f"('{telefono}', '{fecha}', '{turno}')"
        value_statements.append(values_tuple)

    # Combinar todas las tuplas en una única sentencia INSERT
    sql_insert += ",\n ".join(value_statements) + ";"

    return sql_insert

# Generar la sentencia SQL de inserción
sql_insert_query = generate_sql_insert(df)

# Imprimir la sentencia SQL generada
print(sql_insert_query)