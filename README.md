# RPA

-Tomar en cuenta cambiar los credenciales para cada servicio.

-La base de datos usada para el servicio REST es mariadb, el cual viene con el programa XAMMP(https://www.apachefriends.org/es/index.html) y tiene la siguiente estructura

create database simulacion;
use simulacion;
 
create table datos_rest(
	id int not null auto_increment primary key,
	employee_name varchar(100),
	employee_age int,
	profile_image text
);

El String de conexion para la actividad en UiPath tiene la siguiente estructura
"Server=ip/domain;Port=numberOfPortDatabase;Database=nameOfDatabase;Uid=username;Pwd=password;"

