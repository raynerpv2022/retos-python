import os
from PIL import Image
import pillow_heif

def heic_to_jpg(heic, jpg):
    try:
        heif_file = pillow_heif.read_heif(heic)
        image = Image.frombytes(heif_file.mode,heif_file.size,heif_file.data,"raw",)
        image.save(jpg, "JPEG")
    except:
        print("ERROR : " + "source file :" + f"{heic}" )
        return
    print("source file :" + f"{heic}")
    print(f"{jpg} *** " + "OK")
    
    
def convert_heic_jpg(dir_heic, dir_jpg):
    # if not exist then create
    if not os.path.exists(dir_jpg):
        os.makedirs(dir_jpg)

    for file in os.listdir(dir_heic):
        # get name nd extention for file
        name,ext = os.path.splitext(dir_heic+"/"+file)
        
        # if heic file then ...
        if ext in [".heic"]:
            # get heic file path 
            heic_file = os.path.join(dir_heic,file)
            # get only name of heic file
            file_name = os.path.splitext(file)[0] 
            # get output file path
            jpg_file = os.path.join(jpg_dir,file_name+".jpg")
            heic_to_jpg(heic_file,jpg_file)

if __name__ == "__main__":
    #  get pwd
     current_dir = os.getcwd() 
    #  set output dir
     jpg_dir = os.path.join(current_dir,"jpg")
     convert_heic_jpg(current_dir,jpg_dir)
