

last_name = ["JPG", "BMP", "GIF"," PNG", "PSD", "TIFF", "RAW", "HEIF","JFIF"
           ]

def check_extention(attachment):
    attachment = attachment.split(".")
    for name in last_name:
        if attachment[-1] == name.lower() :
            return True
     







