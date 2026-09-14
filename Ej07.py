segundosTotales = int(input("Escribe un número de segundos: "))

horas = segundosTotales // 3600
restoHora = (segundosTotales % 3600)

minutos = restoHora // 60
segundos = segundosTotales % 60

print("Son:", horas, "horas,", minutos, "minutos y", segundos, "segundos")