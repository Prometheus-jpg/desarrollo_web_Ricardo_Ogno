from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)

Base = declarative_base()

class Region(Base):
	__tablename__ = "region"
	__table_args__ = {"autoload_with": engine}

	comunas = relationship("Comuna", back_populates="region")


class Comuna(Base):
	__tablename__ = "comuna"
	__table_args__ = {"autoload_with": engine}

	region = relationship("Region", back_populates="comunas")
	avisos = relationship("AvisoAdopcion", back_populates="comuna")


class AvisoAdopcion(Base):
	__tablename__ = "aviso_adopcion"
	__table_args__ = {"autoload_with": engine}

	comuna = relationship("Comuna", back_populates="avisos")
	fotos = relationship("Foto", back_populates="aviso")
	contactos = relationship("ContactarPor", back_populates="aviso")


class Foto(Base):
	__tablename__ = "foto"
	__table_args__ = {"autoload_with": engine}

	aviso = relationship("AvisoAdopcion", back_populates="fotos")


class ContactarPor(Base):
	__tablename__ = "contactar_por"
	__table_args__ = {"autoload_with": engine}

	aviso = relationship("AvisoAdopcion", back_populates="contactos")