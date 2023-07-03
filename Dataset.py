import os
import csv
import shutil
import scipy.io


def create_dictionary(mat_file, txt_file):
    # Load the MATLAB .mat file
    data = scipy.io.loadmat(mat_file)

    # Access the fields inside the struct
    ilsvrc_ids = data['synsets']['ILSVRC2012_ID'][:1000]
    wnid_values = data['synsets']['WNID'][:1000]
    wnid_ids = []
    for wnid in wnid_values:
        wnid_id = wnid[0][0]
        wnid_ids.append(wnid_id)

    # Read the .txt file and create the dictionary
    txt_dictionary = {}
    with open(txt_file, 'r') as file:
        for idx, line in enumerate(file):
            wnid = line.strip().split()[0]
            row_number = idx + 1
            txt_dictionary[wnid] = row_number

    final_dict = {}
    for idx, wnid in enumerate(wnid_ids):
        final_dict[str(idx+1)] = str(txt_dictionary[wnid])
    return final_dict


def create_csv(labels_file, images_folder, output_csv):
    # Read labels from the file
    with open(labels_file, 'r') as file:
        labels = [int(line.strip()) for line in file.readlines()]

    # Get a list of all image names in the images folder
    image_names = sorted(os.listdir(images_folder))

    # Create and save the CSV file
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Image', 'Label'])
        for i, label in enumerate(labels):
            image_name = os.path.basename(image_names[i])
            writer.writerow([image_name, label])


def create_validation_folder(output_folder, csv_file, source_folder, translation_dict):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            image = row[0]
            label = translation_dict[row[1]]

            # Create a folder for the label if it doesn't exist
            label_folder = os.path.join(output_folder, f"{label}")
            os.makedirs(label_folder, exist_ok=True)

            # Copy the image to the label folder
            source_path = os.path.join(source_folder, image)
            destination_path = os.path.join(label_folder, image)
            shutil.copyfile(source_path, destination_path)

            # Optionally, you can also copy the label file to the label folder
            # if it exists and you want to keep track of the labels.
            label_file = f"{label}.txt"
            label_source_path = os.path.join(source_folder, label_file)
            label_destination_path = os.path.join(label_folder, label_file)
            if os.path.isfile(label_source_path):
                shutil.copyfile(label_source_path, label_destination_path)


def change_names(translation_dict, directory_path):
    # Iterate over the folders in the directory
    for folder_name in os.listdir(directory_path):
        folder_path = os.path.join(directory_path, folder_name)

        # Check if the folder is a directory
        if os.path.isdir(folder_path):
            # Get the translated name from the dictionary
            translated_name = str(translation_dict.get(folder_name))

            # Rename the folder if a translation exists
            if translated_name:
                new_folder_path = os.path.join(directory_path, translated_name)
                os.rename(folder_path, new_folder_path)
                print(f"Renamed folder '{folder_name}' to '{translated_name}'")
            else:
                print(f"No translation found for folder '{folder_name}'")


# for some reason relative paths didn't work - try however you want
validation_path = r'C:\Users\matan\Desktop\CvT_huggingface\ILSVRC2012_img_val'
labels_path = r'./datafiles/ILSVRC2012_validation_ground_truth.txt'
output_csv_path = r'./datafiles/validation.csv'
output_path = r'./imagenet_val'
mat_meta = r'./datafiles/meta.mat'
synset_dict = r'./datafiles/synset_words.txt'
imagenet_correction_dict = r'./datafiels/imagenet_dict.csv'

# create_csv(labels_file=labels_path, images_folder=validation_path, output_csv=output_csv_path)
dictionary_cc = create_dictionary(mat_file=mat_meta, txt_file=synset_dict)
create_validation_folder(output_folder=output_path, csv_file=output_csv_path, source_folder=validation_path, translation_dict=dictionary_cc)
print('finished noder')
