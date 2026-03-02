from libro_modelo import libro_modelos
from autor_modelo import registrar_autor
from libro_bd import base_dato_libro
from api_autores import api_lista_usuario

obj_api=api_lista_usuario()
obj_bd=base_dato_libro()

# Crear autor
autor= registrar_autor("joel","23","eeuu","vivo")

# Crear lista autor
autor2=["bryan","Arias","23 nov/2005","colombia "]
lista=[autor,autor2]

# se agrega nuevo elemento
obj_api.guardar_autores("pedro")

# se agrega un nuevo elemento ala lista
obj_api.extender_autores(lista)

# insertar un elemento
obj_api.insertar_autores(0,"maria")
# elimina un elemento de la lista
obj_api.eliminar_autores(1)

obj_api.remover_autores("joel")

print(obj_api.buscar_autores(autor))
print(obj_api.valor_lista("joel"))

obj_api.ordenar_autores()
obj_api.invertir_autores()
print(obj_api)

object_libro=libro_modelos("23 noviembre","300 hojas","accion")

# Guardar autor
obj_api.guardar_autores(autor)
obj_api.guardar_autores(autor2)
# Guardar libro
obj_bd.guardar_libro(object_libro)

# Mostrar libros
print("LIBROS REGISTRADOS")
obj_bd.mostrar_info()

# Mostrar autores
print("AUTORES REGISTRADOS")
obj_api.mostrar_lista_autores()

# Pedir cantidad
dato_cantidad= input("escriba la cantidad de hojas")
object_libro.set_cantidad_hojas(dato_cantidad)

# Mostrar cantidad
print(object_libro.mostrar_cantidad_hojas())

# Mostrar autor del libro
print(object_libro.info_autor(autor))