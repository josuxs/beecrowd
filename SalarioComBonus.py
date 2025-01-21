nome=input("")
salario = float(input(""))
totalDeVendas = float (input(""))

comissao = totalDeVendas * 0.15

total = comissao + salario
print(f"TOTAL = R$ {total:.2f}")