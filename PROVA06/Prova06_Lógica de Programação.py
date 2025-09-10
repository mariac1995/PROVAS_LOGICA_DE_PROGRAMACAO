
usuario_correto = "admin"
senha_correta = "1234"


tentativas_restantes = 3


while tentativas_restantes > 0:

     usuario = input("Digite o nome de usuário: ")
     senha = input("Digite a senha: ")
    
    
     if usuario == usuario_correto and senha == senha_correta:
         print("Bem-vindo!")
         break
     else:
         tentativas_restantes -= 1
         print(f"Credenciais incorretas. Você tem {tentativas_restantes} tentativa(s) restante(s).")


         if tentativas_restantes == 0:
             for i in range(3):
                 print("Acesso bloqueado.")
