class api_lista_usuario:
    def __init__(self):
        self.api_lista_usuario=[]
    
    def guardar_autores(self,lista_autor):
        self.api_lista_usuario.append(lista_autor)
    
    def extender_autores(self,nueva_lista):
        self.api_lista_usuario.extend(nueva_lista)
    
    def insertar_autores(self,pos_index,autor):
        self.api_lista_usuario.insert(pos_index,autor)
    
    def remover_autores(self,lista_autor):
        self.api_lista_usuario.remove(lista_autor)
    
    def eliminar_autores(self,pos_index):
        self.api_lista_usuario.pop(pos_index)
    
    def buscar_autores(self,nombre_lista):
        self.api_lista_usuario.index(nombre_lista)
    
    def ordenar_autores(self):
        self.api_lista_usuario.sort()
    
    def invertir_autores(self):
        self.api_lista_usuario.reverse()
    
    def valor_lista(self):
        self.api_lista_usuario.count()

    def mostrar_lista_autores(self):
        for i in range(len(self.api_lista_usuario)):
            print("imprimir por posicion ")
            print(self.api_lista_usuario[i])

            for j in range(len(self.api_lista_usuario[i])):
                print("imprimir por posicion de las hijas")
                print(self.api_lista_usuario[i][j])
            
