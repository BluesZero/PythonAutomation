import os

def findFilesAndSizes(folder):
    # Dictionary to store file names and their sizes
    filesAndSizes = {}

    # Traverse the folder and subfolders
    try:
        for root, dirs, files in os.walk(folder):
            for fileName in files:
                # Get the full path of the file
                fullPath = os.path.join(root, fileName)

                # Get the file size
                size = os.path.getsize(fullPath)

                # Add the file and its size to the dictionary
                filesAndSizes[fullPath] = size

        # If no files were found
        if not filesAndSizes:
            return None, "No files were found in the folder."

        # Sort the files by size, from largest to smallest
        sortedFiles = sorted(filesAndSizes.items(), key=lambda x: x[1], reverse=True)

        return sortedFiles, None
    except Exception as e:
        return None, str(e)

def saveToTxt(sortedFiles, txtFileName):
    # Open the txt file for writing
    with open(txtFileName, 'w') as file:
        # Write each file and its size to the txt
        for  path, size in sortedFiles:
            head, tail = os.path.split(path)
            file.write(f"Name: {tail}\nSize: {size} bytes\n")

# Get the path of the folder where the program is running
currentFolder = os.getcwd()

# Get the files and their sizes
filesAndSizes, error = findFilesAndSizes(currentFolder)

# Check if there was an error
if filesAndSizes is None:
    errorMessage = error
else:
    # Save the information in a txt file
    txtFileName = os.path.join(currentFolder, "sizes.txt")
    saveToTxt(filesAndSizes, txtFileName)
    errorMessage = None

errorMessage, txtFileName
