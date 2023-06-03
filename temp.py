import csv
import os
import shutil

csv_file = "LocationData.csv"
desc_file = "desc.txt"
image_folder = "static/locationpictures/"

# Remove rows 89-187 and row 16 from the CSV
rows_to_remove = list(range(89, 188)) + [16]
remaining_rows = []

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        if index not in rows_to_remove:
            remaining_rows.append(row)

# Update the image filenames to match the modified CSV file
new_rows = []
for index, row in enumerate(remaining_rows):
    # Update the image filename
    old_image_filename = f"img{index + 1}.jpg"
    new_image_filename = f"img{index}.jpg"
    row[0] = row[0].replace(old_image_filename, new_image_filename)
    new_rows.append(row)

# Save the modified CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_rows)

# Remove the corresponding rows from the desc.txt file
with open(desc_file, 'r') as file:
    lines = file.readlines()

remaining_lines = [line for index, line in enumerate(lines) if index not in rows_to_remove]

with open(desc_file, 'w') as file:
    file.writelines(remaining_lines)

# Delete the corresponding images and renumber the remaining images
for index in rows_to_remove:
    image_filename = f"img{index}.jpg"
    image_path = os.path.join(image_folder, image_filename)
    if os.path.exists(image_path):
        os.remove(image_path)

# Renumber the remaining images
for index, row in enumerate(new_rows):
    old_image_filename = f"img{index + len(rows_to_remove)}.jpg"
    new_image_filename = f"img{index}.jpg"
    old_image_path = os.path.join(image_folder, old_image_filename)
    new_image_path = os.path.join(image_folder, new_image_filename)
    if os.path.exists(old_image_path):
        shutil.move(old_image_path, new_image_path)

print("CSV, desc.txt, and corresponding images updated successfully.")
