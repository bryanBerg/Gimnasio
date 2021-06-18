select * from usuario;
insert into usuario (correousuario, telefono, nombre, apellidop, apellidom) values ('bryanberg640@gmail.com','5573054247','Bryan Enrique', 'Ramirez', 'Gonzalez');
insert into usuario values ('marioAvila@gmail.com','1234567896','Jesus Mario', 'Sierra', 'Avila');
insert into usuario values ('jesusGarcia@gmail.com','3698520147','Jesus', 'Garcia', 'Perez');

select * from membresia;
insert into membresia (nombre, costo, areas) values ('Bronze', 100, 'regaderas, locker');
insert into membresia (nombre, costo, areas) values ('Silver', 200, 'regaderas, locker, zumba');
insert into membresia (nombre, costo, areas) values ('Gold', 300, 'crossfit, alberca, zumba, regaderas, locker, sauna');

select * from suscripcion
insert into suscripcion (idusuario, idmembresia, fechapago, fechaconclusion) values ('bryanberg640@gmail.com', 1, '2021-06-05', '2021-07-05');
insert into suscripcion (idusuario, idmembresia, fechapago, fechaconclusion) values ('marioAvila@gmail.com', 3, '2021-06-01', '2021-08-01');
insert into suscripcion (idusuario, idmembresia, fechapago, fechaconclusion) values ('jesusGarcia@gmail.com', 2, '2021-06-11', '2021-08-11');

