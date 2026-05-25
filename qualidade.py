#Multiplas Funções--Exercicio Controle de Qualidade--
def cabcalho():
  print("\n"+ "=" *30)
  print("SISTEMAS DE QUALIDADE")
def verificar_status(peso):
   if peso >= 50 and peso <=100:
      return "Aprovada"
   else:
      return "Reprovada"
cabcalho()
peso_item = float(input("Digite o peso do Item em Gramas:"))
status = verificar_status(peso_item)
print(f"Resultado da Inspeção: {status}")
print("=" * 30)
                  

