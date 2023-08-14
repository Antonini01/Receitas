
print('As quantidades serão dadas em gramas ou ml')

receitas = {
    
    "omelete": {"ovo": 200, "leite": 100, "sal": 1,"manteiga": 100, "pimenta": 100},
    "pizza": {"massa de pizza": 100, "molho de tomate": 100, "queijo": 100, "tomate": 100, "azeitona": 100},
    "pao de queijo": {"polvilho doce": 100, "queijo": 100, "ovo": 200, "manteiga": 100},
    "bolo de cenoura": {"cenoura": 200, "acucar": 200, "farinha de trigo": 300, "oleo": 100, "ovo": 400},
    "arroz com feijao": {"arroz": 200, "feijao": 100, "cebola": 100, "alho": 200},
    "macarrao com molho branco": {"macarrao": 100, "leite": 100, "manteiga": 100, "farinha de trigo": 100, "queijo": 100},
    "sopa de legumes": {"batata": 200, "cenoura": 200, "cebola": 100, "alho": 200, "agua": 400}
}

def ler_ingredientes(): # Essa função serve para receber os ingredientes e quantidades que o usuário tem, e guarda essas 
                        # informações no dicionário ingredientes
    n_ingredientes = int(input("Digite a quantidade de ingredientes: ")) 
    ingredientes = {}  
    
    for i in range(n_ingredientes):
        
        
        ingrediente = input(f"Digite o nome do ingrediente {i+1}: ")
        ingrediente = ingrediente.lower()
        quantidade = int(input(f"Digite a quantidade do ingrediente {i+1}: "))
        ingredientes[ingrediente] = quantidade # Associamos o valor quantidade à chave ingrediente e guardamos no dicionário
      
           
    print()  
    return ingredientes
   
def encontrar_receitas(ingredientes): # Essa função analisa se o usuário digitou todos os ingredientes e quantidades necessários
                                      # para fazer alguma receita. A lista receitas_encontradas será muito importante para o 
                                      # funcionamento do próximo def
    
    receitas_encontradas = []
  
    for receita, receita_ingredientes in receitas.items(): # separamos o dicionário receitas em chave e valor 
        ingredientes_encontrados = True # Se um ingrediente está faltando ou não está na quantidade correta, 
                                        # o booleano é definido como False, indicando que a receita não pode ser feita. 
                                                       
    
        for ingrediente, quantidade in receita_ingredientes.items(): # separamos o dicionário receita_ingredientes em chave e valor 
            if ingrediente not in ingredientes: 
                ingredientes_encontrados = False # ingrediente faltando
                    
            elif ingredientes[ingrediente] < quantidade: 
                
                    ingredientes_encontrados = False # quantidade faltando
        
        if ingredientes_encontrados == True: # Se o booleano continuar verdadeiro, a receita encontrada será incluída na lista
                receitas_encontradas.append(receita) 
            
    return receitas_encontradas
    
def imprimir_informacoes(receitas_encontradas, ingredientes): # Esse é o ponto crítico, a função mais importante e complexa do código!!
    if len(receitas_encontradas) == 1: # Quando o comprimento da lista criada no def anterior for equivalente a 1
       print(f"A receita encontrada é {receitas_encontradas[0]}.") # a receita será mostrada ao usuário e, além disso, analisaremos
                                                                   # se há ingredientes extras a serem retirados.
       ingredientes_receita = receitas[receitas_encontradas[0]] # Guarda na variável ingredientes_receita
                                                                # os ingredientes e as quantidades (do dicionário receitas) 
                                                                # da receita encontrada 
       ingredientes_extras = [] 
       for ingrediente in ingredientes:   # Itera o dicionário ingredientes
           if ingrediente not in ingredientes_receita:    # Encontra os ingredientes que não constam no dicionário ingredientes_receita
               ingredientes_extras.append(ingrediente) 
    
       if ingredientes_extras != []: # Condicional importante para não executar sempre o print abaixo. 
                                     # Será executado apenas quando tiver ingredientes extras
           print(f"É necessário retirar: {', '.join(ingredientes_extras)}.")
           
   # ------------------------------------------------------------------------------------------------------------------

    elif len(receitas_encontradas) == 0:  # Sem dúvidas, essa parte é o cerne do código. A maioria das informações inseridas pelo usuário
                                          # chegam aqui. Esse condicional analisa ingredientes faltantes, ingredientes extras 
                                          # e as quantidades necessárias para cada receita.
                                          # Será analisado receita a receita.
                                          # Quando o comprimento da lista criada no def anterior for equivalente a 0
                                          
        ingredientes_faltantes = [] 
        ingredientes_extras = []
        
        for receita,receita_ingredientes in receitas.items(): 
            intersecao_ingredientes = [] # Essa lista é muito importante. Ela irá evitar que as passagens seguintes sejam executadas
                                         # caso o usuário não tenha digitado nenhum ingrediente que conste no banco de dados.
                                         # Vamos supor que o usuário digitou rúcula. O comprimento dessa lista será 0, pulando todas
                                         # as passagens dentro do if da linha 93 indo direto para o if da linha 131
            
            for ingrediente in receita_ingredientes:
                if ingrediente in ingredientes:
                    intersecao_ingredientes.append(ingrediente)        
            
            if len(intersecao_ingredientes) > 0: # O usuário digitou algum ingrediente que consta no banco de dados
            
                ingredientes_faltantes = []
                for ingrediente, quantidade in receita_ingredientes.items(): # Itera o dicionário receita_ingredientes, separando-o
                                                                             # em chave e valor
                    if ingrediente not in ingredientes: # Analisa se o ingrediente do dicionário receita_ingredientes não consta 
                                                        # no dicionário feito pelo usuário
                        ingredientes_faltantes.append(ingrediente) 
  
                    elif ingredientes[ingrediente] < quantidade: # Além disso, se a quantidade digitada for menor que a do banco
                                                                 # de dados, o ingrediente também será considerado como faltante
                        ingredientes_faltantes.append(ingrediente)
   
                ingredientes_extras = []   # Essa passagem é bem simples
                for ingrediente in ingredientes: # Iteramos o dicionário do usuário e,
                    if ingrediente not in intersecao_ingredientes: # se tiver algum ingrediente que não conste no banco de dados
                                                                   # daquela receita,
                        ingredientes_extras.append(ingrediente) # ele será armazenado na lista ingredientes extras
                        
                        
                # Agora, será analisado as duas listas criadas acima:
                if len(ingredientes_extras) > 0: 
                    print(f"Para fazer {receita}, é necessário retirar: {', '.join(ingredientes_extras)}.")
                
                
                if len(ingredientes_faltantes) > 0: # Caso tenham ingredientes faltantes
                    print("A receita de " + receita + " pode ser feita se adicionar os seguintes ingredientes:")
                    
                    for i in ingredientes_faltantes: # Iterando a lista
                        quantidade_faltante = receita_ingredientes[i] # Quantidade do ingrediente do banco de dados da receita
                       
                        if i in ingredientes: # Se o ingrediente estiver no dicionário ingredientes e ao mesmo tempo na lista
                                              # ingredientes_faltantes,
                            quantidade_faltante -= ingredientes[i] # faz a diferença entre a quantidade do banco de dados e a quantidade
                                                                   # digitada pelo usuário e guarda na variável
                        print(" - " + i + ", Falta: " + str(quantidade_faltante))
                    print()

        if len(ingredientes_faltantes) == 0: # se a lista intersecao_ingredientes for vazia, a lista ingredientes_faltantes também será
            print("\nNão encontramos uma receita que possa ser feita com esses ingredientes. \n")
                
    else:    # A execução dessa passagem é similar ao if da linha 62. Aqui considera a lista receitas_encontradas > 1
        for i in range(len(receitas_encontradas)):
            print(f"\nA receita encontrada é {receitas_encontradas[i]}.")
            ingredientes_receita = receitas[receitas_encontradas[i]]
            
        
            ingredientes_extras = [] 
            for ingrediente in ingredientes:   
                if ingrediente not in ingredientes_receita:    
                    ingredientes_extras.append(ingrediente) 
         
            if ingredientes_extras != []:
                print(f"É necessário retirar: {', '.join(ingredientes_extras)}.\n")
        
def imprimir_receitas_prontas():

    for receita, ingredientes in receitas.items():
        ingredientes_str = [ ]
        for ingrediente, quantidade in ingredientes.items():
            ingredientes_str.append(ingrediente + " " + str(quantidade))
        print(receita + ": " + ', '.join(ingredientes_str))

def consultar_ingrediente():
    banco_ingredientes=["ovo","sal","manteiga","pimenta","arroz","alho",
                          "batata","massa de pizza","molho de tomate","queijo",
                          "tomate","polvilho doce","feijao","macarrao","agua",
                          "cenoura","acucar","farinha de trigo","oleo","cebola"]
    tem_esse=input("digite o ingrediente que você deseja saber se tem uma receita com ele: ")
    if tem_esse in banco_ingredientes:
        print ("Existe alguma receita com o ingrediente", tem_esse)
    else:
        print ("Não existe receita com o ingrediente", tem_esse)



def main():   
    ingredientes = {}
    primeira_execucao = True # Booleano criado para executar o primeiro condicional uma vez, depois abre o menu
    while True: # Loop criado para sempre mostrar o menu, até que o usuário decida "Sair"
        if primeira_execucao == True:
            print("\nAdicione os ingredientes que você tem em casa \n")
            ingredientes = ler_ingredientes() # Executa o primeiro def e 
            primeira_execucao = False # depois encerra o condicional
        else:
            print("1. Consultar ingrediente")
            print("2. Encontrar receitas")
            print("3. Comprar mais ingredientes (Mercadinho)")
            print("4. Receitas prontas")
            print("5. Sair")
            escolha = input("Escolha uma opção: ")
            
            if escolha == '1':
                consultar_ingrediente()
                print()
            elif escolha == '2':
                receitas_encontradas = encontrar_receitas(ingredientes)
                imprimir_informacoes(receitas_encontradas, ingredientes)

                
            elif escolha == '3': # Funcionamento do Mercadinho
                novos_ingredientes = ler_ingredientes() # O primeiro def será executado de novo.
                                                        # Será criado um novo dicionário ingredientes chamado novos_ingredientes
                for ingrediente, quantidade in novos_ingredientes.items(): # que será dividido na chave ingrediente e valor quantidade.
                    if ingrediente in ingredientes: # Se o novo ingrediente constar no dicionário feito inicialmente,
                        ingredientes[ingrediente] += quantidade # a quantidade antiga será somada com a nova.
                        
                    else: # Senão, será adicionado no dicionário ingredientes a nova quantidade que será associada ao novo ingrediente
                        ingredientes[ingrediente] = quantidade 
                        
                print("Total de ingredientes: ", ingredientes)
            elif escolha == '4':
                print()
                imprimir_receitas_prontas()
                print()
            elif escolha == '5':
                return
            
            else:
                print('\nDigite um número válido\n')


main()
