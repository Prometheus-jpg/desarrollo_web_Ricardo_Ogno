from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Region, Comuna, AvisoAdopcion, Foto, ContactarPor

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
		fechaIngreso = listInfo[0],
		idComuna = session.query(Comuna).filter_by(nombre=listInfo[1]).first(),
		sector = listInfo[2],
		nombre = listInfo[3],
		email = listInfo[4],
		celular = listInfo[5],
		tipo = listInfo[6],
		cantidad = listInfo[7],
		edad = listInfo[8],
		unidadMediad = listInfo[9],
		fechaEntrega = listInfo[10],		 
		descripcion = listInfo[11]
	)
	
	fotos = listInfo[12]
	for fotoInfo in fotos:
		foto = Foto(ruta_archivo=fotoInfo[0], nombre_archivo=fotoInfo[1])
		nuevoAviso.fotos.append(foto)

	contactos = listInfo[13]	
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