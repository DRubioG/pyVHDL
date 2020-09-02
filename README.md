# pyVHDL
 Librería para programar en VHDL usando Python

El funcionamiento de la libreria se basa en almacenar las cosas en listas de la siguiente manera:
 - Library
 libraries=[[\<libreria\>], [...]]
 - use
 uses=[[\<nombre\>, \<tipo\>, \<cantidad\>],[...]]
 - port_in
 inPorts=[[\<nombre\>, \<tipo\>, \<MSB\>, \<LSB\>], [...]]
- port_out
outPorts=[[\<nombre\>, \<tipo\>, \<MSB\>, \<LSB"], [...]]
- signal
signals=[[\<nombre\>, \<tipo\>, \<MSB\>, \<LSB\>],[...]]


## Funciones
- _library_(\<libreria\>)
Este método permite incluir librerias al proyecto. La librería _IEEE_ ya está incluida en el proyecto
- _use_(\<use\>)
Este método permite incluir _uses_ al proyecto. El _use_ std_logic_1164 de la librería _IEEE_ ya está incluido en el proyecto
- *port_in*(\<puertos_de_entrada\>, \<bits\>, \<MSB\>, \<LSB\>, \<invert\>, \<type\>)
Este método permite incluir puertos de entrada en el proyecto.
**_bits_**: permite elegir el número de bits que tendrá la cadena
**_MSB_**: permite elegir el bit de más peso
**_LSB_**: permite elegir el bit de menor peso
**_invert_**: permite elegir el sentido de los bits
**_type_**: permite elegir el tipo de los datos. El tipo por defecto es **_std_logic(_vector)**


Ejemplo:
``` python
port_in("puerto_entrada1")
port_in("puerto_entrada2", 23)
port_in("puerto_entrada3", 23, invert=1)
port_in("puerto_entrada4", bits=4, LSB=2)
```
Equivalente:
``` vhdl
port(
    puerto_entrada1 : in std_logic;
    puerto_entrada2 : in std_logic_vector(22 downto 0);
    puerto_entrada3 : in std_logic_vector(0 to 22);
    puerto_entrada4 : in std_logic_vector(6 downto 2)
)
```