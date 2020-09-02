# pyVHDL
 Librería para programar en VHDL usando Python

El funcionamiento de la libreria se basa en almacenar las cosas en listas de la siguiente manera:
 - Library
 libraries=[[\<libreria\>], [...]]
 - use
 uses=[["nombre", "tipo", "cantidad"],[...]]
 - port_in
 inPorts=[["nombre", "tipo", "MSB", "LSB"], [...]]
- port_out
outPorts=[["nombre", "tipo", "MSB", "LSB"], [...]]
- signal
signals=[["nombre", "tipo", "MSB", "LSB"],[...]]


## Funciones
- library(\<libreria\>)
- use("use")
- port_in("puertos de entrada")