create database Gym;

create table usuario(
	CorreoUsuario varchar(60) primary key,
	Telefono varchar(10) not null,
	Nombre varchar(20) not null,
	ApellidoP varchar(20) not null,
	ApellidoM varchar(20) not null);

create table membresia(
	IdMembresia serial primary key,
	Nombre varchar(20) not null,
	Costo float not null,
	Areas varchar(100) not null);

create table suscripcion(
	IdSuscripcion serial primary key,
	IdUsuario varchar(60) not null,
	IdMembresia int not null,
	FechaPago date not null,
	FechaConclusion date not null);

alter table suscripcion
	ADD CONSTRAINT FK_suscripcion_usuario
	FOREIGN KEY (IdUsuario)
	REFERENCES usuario(CorreoUsuario)
	ON UPDATE cascade;

alter table suscripcion
	ADD CONSTRAINT FK_suscripcion_membresia
	FOREIGN KEY (IdMembresia)
	REFERENCES membresia(IdMembresia)
	ON UPDATE cascade;


