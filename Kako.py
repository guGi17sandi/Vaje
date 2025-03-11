import json

employee = {
    "name": "Sandi",
    "age": 30,
    "job": "it"
}

file_path ="C:/Users/Sandi/OneDrive/Desktop/output.json"

try:
    with open(file_path, "w") as file:
      json.dump(employee, file, indent=4)
    print(f"json file {file_path} was created")

except FileExistsError:
    print("That file already exists!")