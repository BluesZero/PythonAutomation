from PIL import Image
import os

downloadsFolder= "Your/Downloads/Folder"
picturesFolder = ""

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)
        
        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+ filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            
        if extension in [".mp3"]:
            musicFolder = ""
            os.rename(downloadsFolder + filename, musicFolder + filename)