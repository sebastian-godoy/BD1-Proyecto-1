import os
def parse_csv_file(filename):
    # Initialize an empty list to store the data
    data = []
    script_directory = os.path.dirname(__file__)  # Obtener el directorio del script Flask
    # Open the file for reading
    ruta_absoluta = os.path.join(script_directory, "ciudadanos.csv")  # Construir la ruta relativa
    with open(ruta_absoluta, 'r', encoding='utf-8-sig') as file:
        # Read the lines from the file
        lines = file.readlines()


        # Iterate over each line in the file
        for line in lines:
            line = line.lstrip('\ufeff')
            # Split the line into fields using ',' as the delimiter
            fields = line.strip().split(',')

            # Append the fields to the data list
            data.append(fields)

    # Return the parsed data
    return data

# Specify the filename of the CSV file
filename = 'your_csv_file.csv'

# Call the parse_csv_file function
parsed_data = parse_csv_file(filename)

i = -1
# Print the parsed data
for row in parsed_data:
    print(row[0])
    if i>30:
        break
    print(row)
    i = i + 1