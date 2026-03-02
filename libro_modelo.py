class libro_modelos:
    def __init__(self,fecha,cantidad,tematica):
        self.fecha = fecha
        self.cantidad = cantidad
        self.tematica = tematica
        
    # -------- GETTERS ----------
    def get_cantidad_hojas(self):
        return self.cantidad
    
    def get_tematica(self):
        return self.tematica

    def get_fecha(self):
        return self.fecha

    # -------- SETTERS ----------
    def set_cantidad_hojas(self, cantidad):
        self.cantidad = cantidad

    def set_tematica(self, tematica):
        self.tematica = tematica

    def set_fecha(self, fecha):
        self.fecha = fecha

    # -------- MENSAJES ----------
    def mostrar_cantidad_hojas(self):
         return "El libro tiene " + self.get_cantidad_hojas() + " hojas"

    def mostrar_tematica(self):
        return self.get_tematica()
    
    def info_autor(self, autor):
        return f"Autor: {autor.nombre} - Nacionalidad: {autor.nacionalidad}"

    


    