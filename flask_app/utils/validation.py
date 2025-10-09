import re
import filetype
from database import db

def validar_select(select):
    if select:
        return True
    return False

def validar_nombre(name):
    return name and len(name)>=3 and len(name)<=200

def validar_email(email):
    return (email and len(email)<=100 and 
            bool(re.search(r'^[\w\.-]+@[\w\.-]+\.\w+$',email)))

def validar_celular(num):
    return bool(re.search(r'^\+569\d{8}$',num))

def validar_edad(edad):
    return edad and edad>0

def validar_contacto(contacto):
    return len(contacto)>3 and len(contacto)<=500

def validate_conf_img(conf_img):

    # check if a file was submitted
    if conf_img is None:
        return False
        
    # check if the browser submitted an empty file
    if conf_img.filename == "":
        return False

    ftype_guess = filetype.guess(conf_img)
    # check mimetype
    if not ftype_guess.mime.startswith("image/"):
        return False
    return True

def validar_obligatorio(region_id,comuna_id,name,email,tipo,cantidad,edad,um,foto):
    return (db.get_region_by_id(region_id) and db.get_comuna_by_id(comuna_id) and validar_nombre(name) and
            validar_email(email) and validar_select(tipo) and
            cantidad>0 and validar_edad(edad) and 
            validar_select(um) and validate_conf_img(foto))
