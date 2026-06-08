#Etapa 1- Calculo do IMC
def calc_imc(a,p):
    imc = peso/ (altura*peso)
    return imc

#Etapa 2- Classificação do IMC
def classificar_imc(resultado):
    if  resultado >= 24:
         return "ACIMA DO PESO"
    else:
        return "PESO NORMAL"
#Etapa 3- Mensagem de Retorno
def mensagem(status):
    if status == "ACIMA DO PESO: "
        return "🆘 Atenção! Procure um Médico"
    else:
        return "👍 Seu Peso está normal! Continue Assim"
    
#Etapa 4- Integração do Código
valor_peso = float(input("Digite o seu peso: "))
valor_altura = float(input("Digite sua Altura: "))

valor_imc = calc_imc(valor_peso,valor_altura)
resultado_imc = classificar_imc(valor_imc)
saída = mensagem(resultado_imc)

print("="*50)
print("RESULTADO DO SEU IMC")
print(f\n Seu IMC é:(valor_imc))
print(f\n {saida})
print