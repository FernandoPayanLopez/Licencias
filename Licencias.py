import numpy as np
import random
from rich.table import Table
from rich.console import Console

#Inserción de Datos y Verificación
LicenciasCompradas = [100,150,200,250,300]
ProbabilidadLicencias = [0.30,0.20,0.30,0.15,0.05]
NAleaGen = 0.0
MediaUtilidad = 0
VarianzaUtilidad = 0
Utilidades = []

N = int(input("Ingrese el número de veces que desea realizar la simulación: "))
opcion = input("Escoja una de las siguientes cantidades como el número de licencias que desea comprar: \na)100\nb)150\nc)200\nd)250\ne)300\nIngrese su opción: ").lower()
if opcion == "a":
    CantidadEventos = int(1)
elif opcion == "b":
    CantidadEventos = int(2)
elif opcion == "c":
    CantidadEventos = int(3)
elif opcion == "d":
    CantidadEventos = int(4)
elif opcion == "e":
    CantidadEventos = int(5)      
else:
    print("Numero Invalido")

print(LicenciasCompradas)

#Generar Datos para la Tabla

#AleatorioGenerado
def NAleatorioGenerado(TotalEventos, NumeroAleatorio):
  global NAleaGen
  valorAnterior = 0
  ProbabilidadMaxima = 0
  numUniforme = NumeroAleatorio
  for j in range (TotalEventos):
      ProbabilidadMaxima = ProbabilidadLicencias[j] + ProbabilidadMaxima
  while numUniforme > ProbabilidadMaxima:
      numUniforme = random.random()
      NAleaGen = numUniforme
  for i in range(TotalEventos):
    if((numUniforme>=valorAnterior)&(numUniforme<=(ProbabilidadLicencias[i] + valorAnterior))):
      return i
    else:
        valorAnterior=ProbabilidadLicencias[i] + valorAnterior
  return TotalEventos-1

#Tabla a Generar
table = Table()
table.add_column("N")
table.add_column("     #aleagen")
table.add_column("Licencias\nVendidas")
table.add_column("Licencias\nDevueltas")
table.add_column("Costo")
table.add_column("Ing X \n Vta")
table.add_column("Ing X \n Dev")
table.add_column("Utilidad")

for row in range(N):
    NAleaGen = random.random()
    LicenciasVendidas = LicenciasCompradas[NAleatorioGenerado(CantidadEventos, NAleaGen)]
    LicenciasDevueltas = LicenciasCompradas[CantidadEventos-1]-LicenciasVendidas
    Costo = 75*LicenciasCompradas[CantidadEventos-1]
    IngresoVenta = 100*LicenciasVendidas
    IngresoDevoluciones = 25 * LicenciasDevueltas
    Utilidad = (IngresoVenta + IngresoDevoluciones) - Costo
    MediaUtilidad = (MediaUtilidad + Utilidad)
    Utilidades.append(Utilidad)
    table.add_row(f"{row+1}", str(NAleaGen), str(LicenciasVendidas), str(LicenciasDevueltas), str(Costo), str(IngresoVenta), str(IngresoDevoluciones), str(Utilidad))
console = Console()
console.print(table)
print("La media de la Utilidad es: " , MediaUtilidad/N)
for k in range(N):
    VarianzaUtilidad = (VarianzaUtilidad + ((Utilidades[k] - (MediaUtilidad/N))**2))
print("La varianza de las Utilidades es igual a: ", VarianzaUtilidad/(N-1))         
