class base_dato_libro:
    def __init__(self):
        self.base_dato_libro=[]

    def guardar_libro(self,obj_libro):
        self.base_dato_libro.append(obj_libro)
     
    
    def extender_libro(self, nueva_lista):
        self.base_dato_libro.extend(nueva_lista)
    
    def insertar_libro(self,obj_libro,pos_index):
        self.base_dato_libro.insert(pos_index,obj_libro)
    
    def remove_libro(self,obj_libro):
        self.base_dato_libro.remove(obj_libro)
    
    def eliminar_libros(self,pos_index):
        self.base_dato_libro.pop(pos_index)    
    
    def buscar_libros(self,nombre_obj):
        self.base_dato_libro.index(nombre_obj)
    
    def contar_libros(self,valor):
        self.base_dato_libro.count(valor)
# la lista existe no debe tener parametros 
    def ordenar_libros(self):
        self.base_dato_libro.sort()
    
    def invertir_libro(self):
        self.base_dato_libro.reverse()
    
    def ver_array(self):
        print(self,base_dato_libro)

    def mostrar_info(self):
        for i in range(len(self.base_dato_libro)):
            tematica=self.base_dato_libro[i].get_tematica()
            fecha=self.base_dato_libro[i].get_fecha()
            cantidad=self.base_dato_libro[i].get_cantidad_hojas()
            print(f"tematica libro: {tematica}- fecha libro:{fecha} ,-cantidad hojas:{cantidad}")

