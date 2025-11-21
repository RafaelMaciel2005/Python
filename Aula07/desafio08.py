medida = float(input("Digite a medida em metros: "))
km = medida/1000
cm = medida*100
mm = medida*1000
pol = medida*39.37
print("A medida em quilometros é: {}".format(km))
print("A medida em centímetros é: {}".format(cm))
print("A medida em milímetros é: {}".format(mm))
print("A medida em polegadas é: {}".format(pol))