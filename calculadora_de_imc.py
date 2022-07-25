# Calculadora de IMC
# IMC = peso / (Altura x Altura)
# < 19 : delgadez
# entre 20 y 25 : normal
# entre 26 y 30 : sobrepeso
# > de 30: Obesidad

#def calcularIMC():
#    print('Calculadora de ICM')

#calcularIMC()

#peso = float(input('Ingrese su peso en kg'))
#alturaEnCM = int(input('Ingrese su altura en cm'))
#alturaEnMetros = alturaEnCM / 100
#imc = peso / (alturaEnMetros * alturaEnMetros)

#print('Su IMC es de ' + str(imc))
#if imc < 20:
#    print('Estado de delgadez')
#if imc >= 20 and imc < 26:
#    print('Estado de normal')
#if imc >= 26 and imc < 30:
#    print('Estado de sobrepeso')
#if imc >= 30:
#    print('Estado de obesidad')
def run():
    def velocidad(distancia, tiempo):
        resultado = ""

        velocidad = distancia / tiempo

        a = round((float(velocidad) * 3600), 6)

        b = round((float(velocidad) * 1000), 6)

        resultado = str(a) + " " "km/h" " " "o" " " + str(b) + " " "m/s"
        print("La velocidad es", str(resultado))

        return resultado

    # Con distancia en km y tiempo en segundos

    distancia = 0.01

    tiempo = 1

    velocidad(distancia, tiempo)


if __name__ == '__main__':
    run()