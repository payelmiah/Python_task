import json


input_file_name = "pos_0.png.json"
output_file_name = "formatted_" + input_file_name

try:
   
    with open(input_file_name, "r") as input_file:
        input_data = json.load(input_file)


    formatted_data = {}
    for key, value in input_data.items():
        formatted_data["formatted_" + key] = value

  
    with open(output_file_name, "w") as output_file:
        json.dump(formatted_data, output_file, indent=4)

    print(f"Conversion successful. Output saved to {output_file_name}")

except FileNotFoundError:
    print(f"Input file '{input_file_name}' not found.")
except json.JSONDecodeError:
    print(f"Error decoding JSON data in '{input_file_name}'")
except Exception as e:
    print(f"An error occurred: {str(e)}")
