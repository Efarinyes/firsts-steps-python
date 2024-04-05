CREATE DATABASE IF NOT EXISTS curs_python;
use curs_python;
CREATE TABLE usuaris(
    id int(25) auto_increment NOT NULL,
    nom varchar(100) NOT NULL,
    cognoms varchar(150) NOT NULL,
    email varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    data date NOT NULL,
    CONSTRAINT pk_usuaris PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE todos(
    id int(25) auto_increment NOT NULL,
    usuari_id int(25) NOT NULL,
    titol varchar(255) NOT NULL,
    contingut MEDIUMTEXT,
    data_creacio date NOT NULL,
    CONSTRAINT pk_todos PRIMARY KEY(id),
    CONSTRAINT fk_todo_usuari FOREIGN KEY(usuari_id) REFERENCES usuaris(id)

)ENGINE=InnoDb;

