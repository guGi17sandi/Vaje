import json
import csv

employee = (["Name", "Age", "Job"],
            ["Sandi", 30, "it"],
            ["Maureen", 27, "Caregiver"],
            ["Laureen",26,"Nurse"],)

file_path ="C:/Users/Sandi/OneDrive/Desktop/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)
        print(f"csv file {file_path} was created")

except FileExistsError:
    print("That file already exists!")