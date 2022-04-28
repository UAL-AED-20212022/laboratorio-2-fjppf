
from models.LinkedList import LinkedList

def criar_linked_list():
    return LinkedList()

def inserir_inicio(lista_ligada, pais):
    lista_ligada.insert_at_start(pais)
    return lista_ligada

def inserir_fim(lista_ligada, pais):
    lista_ligada.insert_at_end(pais)
    return lista_ligada

def registar_pais_depois(lista_ligada, pais_1, pais_2):
    lista_ligada.insert_after_item(pais_2, pais_1)
    return lista_ligada

def registar_pais_antes(lista_ligada, pais_1, pais_2):
    lista_ligada.insert_before_item(pais_2, pais_1)
    return lista_ligada

def registar_pais_determinado_indice(lista_ligada, pais, indice):
    lista_ligada.insert_at_index(pais, indice)
    return lista_ligada

def verificar_numero_elementos_lista(lista_ligada):
    numero =lista_ligada.get_count() 
    return numero

def verificar_pais_na_lista(lista_ligada, pais):
    resultado = lista_ligada.search_item(pais)
    return resultado
    
def eliminar_primeiro(lista_ligada):
    nome = lista_ligada.start_node.item
    lista_ligada.delete_at_start()
    return nome

def eliminar_ultimo(lista_ligada):
    nome = lista_ligada.delete_at_end
    lista_ligada.delete_at_end()
    return nome


def eliminar_determinado_pais(lista_ligada, pais):
    resultado = lista_ligada.delete_element_by_value(pais)
    
    return resultado

