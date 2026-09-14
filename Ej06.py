salarioBruto = int(input("Indique su salario bruto: "))
IRPF = int(input("Indique su porcentaje del IRPF: "))

salarioNeto = salarioBruto - (salarioBruto * IRPF / 100)

print("Su salario neto es de:", salarioNeto, "€")