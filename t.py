# iterate through all files (and folders' files, recursively) in the `*/biomes` folder.
# load the contents of all .json files as a json object, and then iterate through all
# on each iteration check the 'customDerivitives' key, which returns an array, iterate through all elements
# for each of those elements print the `id` key which returns a string.

import os
import json
import regex

# get the current working directory
cwd = os.getcwd()

# valid id regex
valid_id_regex = regex.compile(r'^[a-z0-9_-]+$')

# get the path to the biomes folder
biomes_path = os.path.join(cwd, 'biomes')

# iterate through all files in the biomes folder
for root, dirs, files in os.walk(biomes_path):
    for file in files:
        # get the path to the current file
        file_path = os.path.join(root, file)

        # open the file
        with open(file_path, 'r') as f:
            # load the file contents as a json object
            json_object = json.load(f)

            # check if the json object has a 'customDerivitives' key
            if not 'customDerivitives' in json_object:
                # print('no customDerivitives key in file: ' + file_path)
                continue

            # get the customDerivitives key, which returns an array
            custom_derivitives = json_object['customDerivitives']

            # iterate through all elements in the array
            for element in custom_derivitives:

                # check if the element has an 'id' key
                if not 'id' in element:
                    # print('no id key in file: ' + file_path)
                    continue

                # print the id key, which returns a string
                # print(file_path + " -> " + element['id'])

                # for each id check if it is a valid id
                if not valid_id_regex.match(element['id']):
                    print('invalid id: ' + element['id'])

print("Done")