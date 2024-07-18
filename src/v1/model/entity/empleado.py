class Empleado():
    def __init__(self):
        self._nombre=None
        self._apellidopaterno=None
        self._apellidomaterno=None
        self._direccion=None
        self._codigopostal=None
        self._telefono=None
        self._curp=None
        self._nss=None
        self._keyx=None
        self._fechaalta=None
        self._numeroempleado=None
        self._puesto=None
        self._fechabaja=None
        self._estatus=None
        self._causabaja=None
    # Getter
    @property
    def nombre(self):
        return self._nombre
    @property
    def apellidopaterno(self):
        return self._apellidopaterno
    @property
    def apellidomaterno(self):
        return self._apellidomaterno
    @property
    def direccion(self):
        return self._direccion
    @property
    def codigopostal(self):
        return self._codigopostal
    @property
    def telefono(self):
        return self._telefono
    @property
    def curp(self):
        return self._curp
    @property
    def nss(self):
        return self._nss
    @property
    def keyx(self):
        return self._keyx
    @property
    def fechaalta(self):
        return self._fechaalta
    @property
    def numeroempleado(self):
        return self._numeroempleado
    @property
    def puesto(self):
        return self._puesto
    @property
    def fechabaja(self):
        return self._fechabaja
    @property
    def estatus(self):
        return self._estatus
    @property
    def causabaja(self):
        return self._causabaja
    # Setter
    @nombre.setter
    def nombre(self,value):
        self._nombre=value
    @apellidopaterno.setter
    def apellidopaterno(self,value):
        self._apellidopaterno=value
    @apellidomaterno.setter
    def apellidomaterno(self,value):
        self._apellidomaterno=value
    @direccion.setter
    def direccion(self,value):
        self._direccion=value
    @codigopostal.setter
    def codigopostal(self,value):
        self._codigopostal=value
    @telefono.setter
    def telefono(self,value):
        self._telefono=value
    @curp.setter
    def curp(self,value):
        self._curp=value
    @nss.setter
    def nss(self,value):
        self._nss=value
    @keyx.setter
    def keyx(self,value):
        self._keyx=value
    @fechaalta.setter
    def fechaalta(self,value):
        self._fechaalta=value
    @numeroempleado.setter
    def numeroempleado(self,value):
        self._numeroempleado=value
    @puesto.setter
    def puesto(self,value):
        self._puesto=value
    @fechabaja.setter
    def fechabaja(self,value):
        self._fechabaja=value
    @estatus.setter
    def estatus(self,value):
        self._estatus=value
    @causabaja.setter
    def causabaja(self,value):
        self._causabaja=value