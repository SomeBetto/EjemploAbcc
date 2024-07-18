class Puesto():
    def __init__(self):
        self._keyx=None
        self._fechaalta=None
        self._idpuesto=None
        self._descripcion=None
        self._estatus=None
        self._fechabaja=None
        self._empleadoregistra=None
        self._empleadobaja=None
    # Getter
    @property
    def keyx(self):
        return self._keyx
    @property
    def fechaalta(self):
        return self._fechaalta
    @property
    def idpuesto(self):
        return self._idpuesto
    @property
    def descripcion(self):
        return self._descripcion
    @property
    def estatus(self):
        return self._estatus
    @property
    def fechabaja(self):
        return self._fechabaja
    @property
    def empleadoregistra(self):
        return self._empleadoregistra
    @property
    def empleadobaja(self):
        return self._empleadobaja
    # Setter
    @keyx.setter
    def keyx(self,value):
        self._keyx=value    
    @fechaalta.setter
    def fechaalta(self,value):
        self._fechaalta=value            
    @idpuesto.setter
    def idpuesto(self,value):
        self._idpuesto=value        
    @descripcion.setter
    def descripcion(self,value):
        self._descripcion=value        
    @estatus.setter
    def estatus(self,value):
        self._estatus=value        
    @fechabaja.setter
    def fechabaja(self,value):
        self._fechabaja=value        
    @empleadoregistra.setter
    def empleadoregistra(self,value):
        self._empleadoregistra=value        
    @empleadobaja.setter
    def empleadobaja(self,value):
        self._empleadobaja=value        