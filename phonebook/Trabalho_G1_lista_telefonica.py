import csv
lista_contatos=[]

def cadastrar_contato():

   while True:
      nome= input("Insira o seu Nome: ") 
      if len(nome) < 3:
         print("Insira novamente o nome") 
         continue
      else:
         print("Nome cadastrado")
         break 
      
   while True:
      numero= input("Insira o seu numero: ")
       
      if not numero.isdigit() or len(numero) < 8 or len(numero) > 15 :       
         print("Formato de numero incorreto, por favor insira novamente") 
         continue
      else:
         print("Telefone Cadastrado")
         break

   while True:
      email= input("Insira o seu email: ")

      if "@" not in email or not email.endswith(".com"):

         print("Email inválido, digite novamente: ") 
         continue
      else:
         print("Email Cadastrado")
         break
   
   pessoa = {"nome": nome, "numero": numero, "email": email}
   lista_contatos.append(pessoa)
   print("Contato cadastrado com sucesso!")

def exibir_contatos():
   if not lista_contatos:
      print("Nenhum contato registrado")

   else:
      for contato in lista_contatos:
         print(f"NOME: {contato['nome']}")
         print(f"TELEFONE: {contato['numero']}")
         print(f"EMAIL: {contato['email']}")
         print("-" * 10)

def buscar_contato(nome):
    encontrados = []
    # Procura o nome na lista de contatos
    for contato in lista_contatos:
        
        # Converte todos os caracteres para lowercase caso haja erro na digitação do usuário

        if nome.lower() in contato["nome"].lower():
            encontrados.append(contato)

    # Printa os contatos encontrados se houver correspondência 
       
    if encontrados:
        print(f"{len(encontrados)} contato(s) encontrado(s):")
        for contato in encontrados:
            print(f"NOME: {contato['nome']}")
            print(f"TELEFONE: {contato['numero']}")
            print(f"EMAIL: {contato['email']}")
            print("-" * 10)
    else:
        print("Não há nenhum contato encontrado com esse nome")

def salvar_contatos():
    nome_arquivo = "agenda.csv"
    
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
   
        campos = ["nome", "numero", "email"]
        
        escreve = csv.DictWriter(arquivo_csv, fieldnames=campos)
        
        escreve.writeheader()
        
        escreve.writerows(lista_contatos)
    
    print(f"Contatos salvos no arquivo '{nome_arquivo}' com sucesso!")

def carregar_contatos():
   nome_arquivo = "agenda.csv"
   
   with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
         leitor = csv.DictReader(arquivo_csv)
            
         # Limpa a lista atual de contatos para evitar duplicados
         lista_contatos.clear()
            
         # Percorre cada linha do arquivo e adiciona à lista de contatos
         for linha in leitor:
                # Converte a linha (dicionário) para o formato correto
               contato = {
                  "nome": linha["nome"],
                  "numero": linha["numero"],
                  "email": linha["email"]
                }
               lista_contatos.append(contato)
            
   print("Contatos carregados com sucesso! \n")
   

def menu_principal():
   while True:
      
      print("\nMenu\n1 - Cadastro\n2 - Exibir contatos\n3 - Buscar Contato\n4 - Salvar contatos\n5 - Carregar Contatos\n6 - Sair \n")
      carregar_contatos()
      try:
         opcao= int(input("Digite a opção: "))
      except ValueError:
         print("Valor inválido")
   
      match opcao:

         case 1:
            cadastrar_contato()
            salvar_contatos()
            continue

         case 2:
            exibir_contatos()
            continue

         case 3:
            nome= input("Digite o nome à ser procurado: ")
            buscar_contato(nome)
            continue

         case 4:
            salvar_contatos()
            continue

         case 6:
            salvar_contatos()
            break
         case _:
          print("Unknown Class")
            # nome= input("Digite o nome a ser procurado:")
            # if len(nome) < 3:
            #    print("Insira o nome novamente")
            # else:
            #    buscar_contato(nome)
            # continue
         
         # case 4:
         #    salvar_contatos()


menu_principal()