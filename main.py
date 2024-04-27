import pandas as pd

# Load the original CSV data to split into multiple CSV files for different tables
data_path = 'ICE-Fuente.csv'
data = pd.read_csv(data_path)

# Splitting data into multiple CSVs for the respective tables
# Example simplified transformation, real transformation may need additional steps

# Zones
zones = data[['PAIS', 'REGION', 'DEPTO', 'MUNICIPIO']].drop_duplicates().reset_index(drop=True)
# Assuming 'PAIS' as top-level zone without a parent (ID_Padre for 'PAIS' is NULL)
# For the sake of the example, let's assign arbitrary IDs manually. Real scenario needs a proper method to assign unique IDs.
zones['ID_Zona'] = range(1, len(zones) + 1)
zones['ID_Padre'] = [None] * len(zones)  # Placeholder, real values depend on actual hierarchical relationships
zones.to_csv('zonas.csv', index=False)

# Parties
parties = data[['PARTIDO', 'NOMBRE_PARTIDO']].drop_duplicates().reset_index(drop=True)
parties['ID_Partido'] = range(1, len(parties) + 1)
parties.to_csv('partidos.csv', index=False)

# Elections (assuming a relationship with zones and simplified transformation)
elections = data[['NOMBRE_ELECCION', 'AÑO_ELECCION', 'PAIS']].drop_duplicates().reset_index(drop=True)
elections['ID_Eleccion'] = range(1, len(elections) + 1)
elections['ID_Zona'] = 1  # Placeholder, should match real zone IDs
elections.to_csv('elecciones.csv', index=False)

# Election Results (assuming simplified relationships)
results = data[['PARTIDO', 'ANALFABETOS']].drop_duplicates().reset_index(drop=True)  # Placeholder columns
results['ID_Resultado'] = range(1, len(results) + 1)
results['ID_Eleccion'] = 1  # Placeholder, should match real election IDs
results['ID_Partido'] = 1  # Placeholder, should match real party IDs
results.to_csv('resultados.csv', index=False)

# Demographics (assuming simplified and placeholder transformations)
demographics = data[['PAIS', 'SEXO', 'RAZA', 'ANALFABETOS', 'ALFABETOS']].drop_duplicates().reset_index(drop=True)
demographics['ID_Demografia'] = range(1, len(demographics) + 1)
demographics['ID_Zona'] = 1  # Placeholder, should match real zone IDs
demographics.to_csv('demografia.csv', index=False)
