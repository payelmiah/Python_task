
input_files = ["Pos_0.png.json", "Pos_10010.png.json", "Pos_10492.png.json"]
combined_data = {"objects": []}

for input_file in input_files:
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)
        combined_data["objects"].extend(data.get("objects", []))


for obj in combined_data["objects"]:
    class_title = obj.get("classTitle")
    if class_title == "Vehicle":
        obj["classTitle"] = "Car"
    elif class_title == "License Plate":
        obj["classTitle"] = "Number"


output_file = "combined_data.json"
with open(output_file, 'w') as json_file:
    json.dump(combined_data, json_file, indent=4)

print(f"Combined JSON saved as {output_file}")
