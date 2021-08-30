from PIL import Image
from PIL.ExifTags import TAGS
import tkinter as tk
import tkinter.filedialog as tkFileDialog

def main():

    root = tk.Tk()
    root.withdraw()    


    def browsefunc():
        filename =tkFileDialog.askopenfilename(filetypes=(('image files', ('.png', '.jpg')), ("All files","*.*")))
        return filename

    imagename = browsefunc()#r"C:\Users\nisha\Desktop\010 dog.jpg"

    image = Image.open(imagename)

    exifdata = image.getexif()

    for tag_id in exifdata:
        
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        
        if isinstance(data, bytes):
            data = data.decode('UTF8', 'replace')
        print(f"{tag:25}: {data}")

if __name__ == '__main__':
    main()