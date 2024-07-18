CREATE TABLE IF NOT EXISTS tbcatempleadosprueba(
  keyx INT GENERATED ALWAYS AS IDENTITY,
  nombre VARCHAR(50),
  apellidopaterno VARCHAR(50),
  apellidomaterno VARCHAR(50),
  direccion VARCHAR(60),
  codigopostal VARCHAR(5),
  telefono VARCHAR(10),
  curp VARCHAR(18),
  nss VARCHAR(11),
  fechaalta DATE,
  numeroempleado INTEGER PRIMARY KEY,
  puesto INTEGER,
  fechabaja DATE DEFAULT '1900-01-01',
  estatus SMALLINT DEFAULT 1,
  causabaja VARCHAR DEFAULT ''
);

CREATE TABLE IF NOT EXISTS tbcatpuestosprueba(
    keyx INT GENERATED ALWAYS AS IDENTITY, 
    fechaalta DATE,
    idpuesto INTEGER PRIMARY KEY NOT NULL,
    descripcion VARCHAR(100),
    estatus INTEGER DEFAULT 1,
    fechabaja DATE DEFAULT '1900-01-01',
    empleadoregistra INTEGER NOT NULL,
    empleadobaja INTEGER NOT NULL 
);