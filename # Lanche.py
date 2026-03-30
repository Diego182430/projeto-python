# Calculadora de lanche
preço = int(input("Digite o valor do lanche"))
if preço <= 10:
  print("Preço justo")
elif preço <= 20:
    print("Está ficando caro!")
else:
   print("Muito caro, melhor levar de casa!")