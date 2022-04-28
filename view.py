
import controller as c


def main():
    
    lista_ligada = c.criar_linked_list()
    
    
    while True:
        commands = input().split(" ")
        
        if commands[0] == "RPI":
            if c.inserir_inicio(lista_ligada, commands[1]):
                lista_ligada.traverse_list()
                
        elif commands[0] == "RPF":
            if c.inserir_fim(lista_ligada, commands[1]):
                lista_ligada.traverse_list()

        elif commands[0] == "RPDE":
            if c.registar_pais_depois(lista_ligada, commands[1], commands[2]):
                lista_ligada.traverse_list()
            

        elif commands[0] == "RPAE":
            if c.registar_pais_antes(lista_ligada, commands[1], commands[2]):
                lista_ligada.traverse_list()
            

        elif commands[0] == "RPII":
            if c.registar_pais_determinado_indice(lista_ligada, int(commands[2]), commands[1]): #### commands[2], commands[1]
                lista_ligada.traverse_list()
           

        elif commands[0] == "VNE":
            
            numero = c.verificar_numero_elementos_lista(lista_ligada)
                
            print(f"O número de elementos são {numero}.")
            

        elif commands[0] == "VP":
            if c.verificar_pais_na_lista(lista_ligada, commands[1]):
                print(f"O país {commands[1]} encontra-se na lista.")
            else:
                print(f"O país {commands[1]} não encontra se  na lista.")
                

        elif commands[0] == "EPE":
            nome = c.eliminar_primeiro(lista_ligada)
            if nome:
                print(f"O país {nome} foi eliminado da lista.")
          

        elif commands[0] == "EUE":
            nome = c.eliminar_ultimo(lista_ligada)
            if nome:
                print(f"O país {nome} foi eliminado da lista.")
           

        elif commands[0] == "EP":
            
            if c.eliminar_determinado_pais(lista_ligada, commands[1]):
                print(f"O país {commands[1]} foi eliminado da lista.")
            else:
                print(f"O país {commands[1]} não se encontra na lista.")
                
               
                
        


        