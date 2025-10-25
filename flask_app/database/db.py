from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Region, Comuna, AvisoAdopcion, Foto, ContactarPor, Comentario

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)


def get_Avisos(cant):
	session = SessionLocal()
	avisos = session.query(AvisoAdopcion).order_by(AvisoAdopcion.id.desc()).limit(cant)
	session.close()
	return avisos

def create_aviso(listInfo):
	session = SessionLocal()
	nuevoAviso = AvisoAdopcion(
		fecha_ingreso = listInfo[0],
		comuna_id = listInfo[1],
		sector = listInfo[2],
		nombre = listInfo[3],
		email = listInfo[4],
		celular = listInfo[5],
		tipo = listInfo[6],
		cantidad = listInfo[7],
		edad = listInfo[8],
		unidad_medida = listInfo[9],
		fecha_entrega = listInfo[10],		 
		descripcion = listInfo[11]
	)
	
	fotos = listInfo[12]
	for fotoInfo in fotos:
		foto = Foto(ruta_archivo=fotoInfo[0], nombre_archivo=fotoInfo[1])
		nuevoAviso.fotos.append(foto)

	if len(listInfo)==14:
		contactos = listInfo[13]	
		if contactos:
			for contactoInfo in contactos:
				contacto = ContactarPor(nombre=contactoInfo[0], identificador=contactoInfo[1])
				nuevoAviso.contactos.append(contacto)

	session.add(nuevoAviso)
	session.commit()
	session.close()

def get_fotos_by_id(idAviso):
	session = SessionLocal()
	fotos = session.query(Foto).filter_by(aviso_id=idAviso).all()
	session.close()
	return fotos

def get_contactos_by_id(idAviso):
	session = SessionLocal()
	contactos = session.query(ContactarPor).filter_by(aviso_id=idAviso).all()
	session.close()
	return contactos

def get_region_by_id(idRegion):
	session = SessionLocal()
	region = session.query(Region).filter_by(id=idRegion).first()
	session.close()
	return region

def get_comuna_by_id(idComuna):
	session = SessionLocal()
	comuna= session.query(Comuna).filter_by(id=idComuna).first()
	session.close()
	return comuna

def get_avisos_per_page(page_num,per_page):
	session = SessionLocal()
	avisos = session.query(AvisoAdopcion).order_by(AvisoAdopcion.id.desc()).offset((page_num-1)*per_page).limit(per_page)
	cant_avisos = session.query(AvisoAdopcion).count()
	session.close()
	return avisos, cant_avisos

def get_fechas():
	session = SessionLocal()
	avisos = session.query(AvisoAdopcion).order_by(AvisoAdopcion.fecha_ingreso.desc()).all()
	fechas = []
	for aviso in avisos:
		fecha = str(aviso.fecha_ingreso).split()[0]
		if fecha not in fechas:
			cant = session.query(AvisoAdopcion).filter(AvisoAdopcion.fecha_ingreso.like(f'%{fecha}%')).count()
			fechas.append([fecha,cant])
	session.close()
	return fechas

def get_cant_avisos_per_type():
	session = SessionLocal()
	cant_p = session.query(AvisoAdopcion).filter_by(tipo = 'perro').count()
	cant_g = session.query(AvisoAdopcion).filter_by(tipo = 'gato').count()
	session.close()
	return cant_p, cant_g

def avisos_porTipo_mes():
	session = SessionLocal()
	avisos = session.query(AvisoAdopcion).order_by(AvisoAdopcion.fecha_ingreso.desc()).all()
	data = {}
	for aviso in avisos:
		fecha = str(aviso.fecha_ingreso).split()[0]
		mes = fecha[:-3]
		if mes not in data:
			data[mes] = {
				'perro': 0,
				'gato': 0
			}
		data[mes][aviso.tipo] += 1
	session.close()
	return data

def get_comentarios_by_id(idAviso):
	session = SessionLocal()
	comentarios = session.query(Comentario).filter_by(aviso_id=idAviso).all()
	session.close()
	return comentarios

def add_comentario(nombre,comentario,fecha,idAviso):
	session = SessionLocal()
	aviso = session.query(AvisoAdopcion).filter_by(id=idAviso).first()
	newComentario = Comentario(nombre=nombre,texto=comentario,fecha=fecha)
	aviso.comentarios.append(newComentario)
	session.commit()
	session.close()