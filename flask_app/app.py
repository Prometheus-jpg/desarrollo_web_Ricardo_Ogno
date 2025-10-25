from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from flask_cors import cross_origin
from database import db
from utils.validation import *
from werkzeug.utils import secure_filename
from datetime import datetime
from math import ceil
import hashlib
import filetype
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/formAdopcion", methods=["GET", "POST"])
def add_adopcion():
    if request.method == "POST":
        email = request.form.get("email")
        nombre = request.form.get("nombre")
        num = request.form.get("tel")
        edad = int(request.form.get("edad"))
        region = request.form.get("select_region")
        comuna = int(request.form.get("select_comuna"))
        tipo = request.form.get("tipo")
        cantidad = int(request.form.get("cantidad"))
        um = request.form.get("unidad_edad")
        descripcion = request.form.get("descripcion")
        sector = request.form.get("sector")
        fecha_ingreso = datetime.now()
        fecha_entrega = request.form.get("fecha_entrega")
        contactos_raw = []
        for i in range(5):
            nameApp = request.form.get(f"contacto{i}")
            identificador = request.form.get(f"textContacto{i}")
            contactos_raw.append([nameApp,identificador])
        imgs = []
        for i in range(5):
            imgs.append(request.files[f'foto{i}'])
        error = ""

        if validar_obligatorio(region,comuna,nombre,email,tipo,cantidad,edad,um,imgs[0]):
            if num and not validar_celular(num):
                error += "Numero celular incorrecto"
            if sector and len(sector)>100:
                error += "Texto en sector demasiado largo, maximo 100 caracteres"        

            if error == "":
                aviso = [fecha_ingreso,comuna,sector,nombre,email,num,tipo,cantidad,edad,um,fecha_entrega,descripcion]
                fotos = []
                for foto in imgs:
                    if foto is not None and foto.filename!="":
                        if validate_conf_img(foto):
                            # 1. generate random name for img
                            _filename = hashlib.sha256(
                                secure_filename(foto.filename) # nombre del archivo
                                .encode("utf-8") # encodear a bytes
                                ).hexdigest()
                            _extension = filetype.guess(foto).extension
                            img_filename = f"{_filename}.{_extension}"
                            img_name = foto.filename
                            # 2. save img as a file
                            foto.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
                            fotos.append([f"uploads/{img_filename}",img_name])
                aviso.append(fotos)

                contactos = []
                for contacto in contactos_raw:
                    if contacto[0] is not None and contacto[0]!="" and contacto[1] is not None and contacto[1]!="":
                        contactos.append(contacto)
                if contactos:
                    aviso.append(contactos)
                db.create_aviso(aviso)
                return redirect( url_for('index') )
            else:
                print(error)
                return render_template("formulario/formAdopcion.html", error=error)
            
        else:
            error += "Uno de los campos obligatorios es erroneo "
            print(error)
            return render_template("formulario/formAdopcion.html", error=error)

    elif request.method == "GET":
        return render_template("formulario/formAdopcion.html")

@app.route("/", methods=["GET"])
def index():
    
    data = []
    for aviso in db.get_Avisos(5):

        foto = db.get_fotos_by_id(aviso.id)[0]
        img_filename = foto.ruta_archivo
        um = aviso.unidad_medida
        if um == 'm':
            um = 'mes'
        else:
            um = 'año'
        data.append({
            "date": aviso.fecha_ingreso,
            "comuna": aviso.comuna.nombre,
            "sector": aviso.sector,
            "cantidad": aviso.cantidad,
            "tipo": aviso.tipo,
            "edad": aviso.edad,
            "um": um,
            "path_image": url_for('static', filename=img_filename)
        })
    
    return render_template("info/portada.html", data=data)

@app.route("/lisAvisos/<int:page_num>", methods=["GET"])
def list_avisos(page_num):
    avisos, cant_avisos = db.get_avisos_per_page(page_num,5)
    cant_pages = ceil(cant_avisos/5)
    avisos_in_page = min(5,cant_avisos-(5*(page_num-1)))
    data = []
    modal_ids = []
    fila_ids = []
    close_ids = []
    img_ids = []
    cant_imgs = []
    aviso_ids = []
    i=0
    for aviso in avisos:

        fotos = db.get_fotos_by_id(aviso.id)
        img_filenames = []
        img_aviso = []
        j=0
        for foto in fotos:
            img_filename = foto.ruta_archivo
            img_filenames.append(url_for('static', filename=img_filename))
            img_aviso.append(f"img-modal{i}{j}")
            j+=1
        cant_imgs.append(j)
        
        contactos = db.get_contactos_by_id(aviso.id)
        contactos_info = []
        if contactos:
            for contacto in contactos:
                nameApp = contacto.nombre
                identificador = contacto.identificador
                contactos_info.append([nameApp,identificador])

        um = aviso.unidad_medida
        if um == 'm':
            um = 'mes'
        else:
            um = 'año'

        data.append({
            "fecha_ingreso": aviso.fecha_ingreso,
            "fecha_entrega": aviso.fecha_entrega,
            "comuna": aviso.comuna.nombre,
            "sector": aviso.sector,
            "cantidad": aviso.cantidad,
            "tipo": aviso.tipo,
            "edad": aviso.edad,
            "um": um,
            "nombre": aviso.nombre,
            "email": aviso.email,
            "celular": aviso.celular,
            "contactos": contactos_info,
            "path_image": img_filenames
        })
        modal_ids.append(f"myModal{i}")
        fila_ids.append(f"fila{i}")
        close_ids.append(f"close{i}")
        img_ids.append(img_aviso)
        aviso_ids.append(aviso.id)
        i+=1

    return render_template("info/listAvisos.html", data=data, avisos_in_page=avisos_in_page,
    page_num=page_num, cant_avisos=cant_avisos, cant_imgs=cant_imgs,
    cant_pages=cant_pages,ids=[modal_ids,fila_ids,close_ids,img_ids,aviso_ids])

@app.route("/estadisticas", methods=['GET'])
def estadistica():
    return render_template("info/estadisticas.html")

@app.route("/get-stats-data", methods=["GET"])
@cross_origin(origin="127.0.0.1", supports_credentials=True)
def get_stats_data():
    fechas = db.get_fechas()
    cant_p, cant_g = db.get_cant_avisos_per_type()
    
    dataFechas = [{
        "date": fecha[0],
        "count": fecha[1],  
    } for fecha in fechas]

    dataTipos = [{
        "cant_p": cant_p,
        "cant_g": cant_g
    }]

    dataTiposMes = [{
        'meses': [],
        'perros': [],
        'gatos': []
    }]
    for k,v in db.avisos_porTipo_mes().items():
        dataTiposMes[0]['meses'].append(k)
        dataTiposMes[0]['perros'].append(v['perro'])
        dataTiposMes[0]['gatos'].append(v['gato'])

    return jsonify(dataFechas,dataTipos,dataTiposMes)

@app.route("/get-comentarios", methods=["GET"])
@cross_origin(origin="127.0.0.1", supports_credentials=True)
def get_comentarios():
    aviso_id = request.args.get("idAviso", type=int)
    comentarios = db.get_comentarios_by_id(aviso_id)
    data=[]
    for comentario in comentarios:
        data.append({
            'nombre': comentario.nombre,
            'comentario': comentario.texto,
            'fecha': comentario.fecha
        })
    return jsonify(data)

@app.route("/add-comentario", methods=["POST"])
@cross_origin(origin="127.0.0.1", supports_credentials=True)
def add_comentario():
    data = request.get_json()
    nombre = data.get("nombre", "").strip()
    comentario = data.get("comentario", "").strip()
    fecha = datetime.now()
    aviso_id = data.get("idAviso")

    if not nombre or not comentario:
        return jsonify({"status": "error", "data": "Faltan campos"}), 400
    
    db.add_comentario(nombre,comentario,fecha,aviso_id)
    return jsonify({"status": "ok"})