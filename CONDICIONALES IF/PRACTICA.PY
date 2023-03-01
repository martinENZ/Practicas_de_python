segundos = 125
minutos = segundos // 60
segundos_sobrantes = segundos % 60  # Residuo de dividir entre 60
print("Minutos: {}, segundos: {}".format(minutos, segundos_sobrantes))


segundos = 125
minutos, segundos_sobrantes = divmod(segundos, 60)
print("Minutos: {}, segundos: {}".format(minutos, segundos_sobrantes))