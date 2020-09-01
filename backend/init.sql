CREATE TABLE accesos (	
id serial,	
usuario VARCHAR ( 50 ) UNIQUE NOT NULL,	
password VARCHAR ( 50 ) NOT NULL,	
email VARCHAR ( 255 ) UNIQUE NOT NULL,	
fecha_ini TIMESTAMP NOT NULL,        
login TIMESTAMP 
);
ALTER TABLE accesos OWNER TO postgres;
insert into accesos(usuario,password,email,fecha_ini) values('jfabiancz','1234567','jfabiancz@gmail.com',current_timestamp);
insert into accesos(usuario,password,email,fecha_ini) values('mariorg','1234567','mariorg@gmail.com',current_timestamp);

