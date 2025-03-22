import numpy as np 
co2_emissions = np.round(np.random.uniform(4, 20, 200), 2)

print(co2_emissions)

# Nome del file di output
output_file = "emissioni.txt"

# Salvataggio su file
np.savetxt(output_file, co2_emissions, fmt="%.2f")

# Restituisco il percorso del file
print(output_file)