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
outPorts=[[\<nombre\>, \<tipo\>, \<MSB\>, \<LSB\>], [...]]
- port_inout
inoutPorts=[[\<nombre\>, \<tipo\>, \<MSB\>, \<LSB\>], [...]]
- signal
signals=[[\<nombre\>, \<tipo\>, \<MSB\>, \<LSB\>],[...]]
- generic
generics=[[\<nombre\>, \<tipo\>, \<valor\>], [...]]

## Funciones
- *library(\<libreria\>)*: 
Este método permite incluir librerias al proyecto. La librería _IEEE_ ya está incluida en el proyecto
- *use(\<use\>)*: 
Este método permite incluir _uses_ al proyecto. El _use_ std_logic_1164 de la librería _IEEE_ ya está incluido en el proyecto
- *port_in(\<puertos_de_entrada\>, \<bits\>, \<MSB\>, \<LSB\>, \<invert\>, \<type\>)*: 
Este método permite incluir puertos de entrada en el proyecto.
    - **_bits_**: permite elegir el número de bits que tendrá la cadena
    - **_MSB_**: permite elegir el bit de más peso
    - **_LSB_**: permite elegir el bit de menor peso
    - **_invert_**: permite elegir el sentido de los bits
        - '0': para orden descente
        - '1': para orden ascendente
    - **_type_**: permite elegir el tipo de los datos. El tipo por defecto es **_std_logic(_vector)**
    El tipo 'u' --> "unsigned"

- *port_out(\<puertos_de_salida\>, \<bits\>, \<MSB\>, \<LSB\>, \<invert\>, \<type\>)*: 
Este método permite incluir puertos de salida en el proyecto.
    - **_bits_**: permite elegir el número de bits que tendrá la cadena
    - **_MSB_**: permite elegir el bit de más peso
    - **_LSB_**: permite elegir el bit de menor peso
    - **_invert_**: permite elegir el sentido de los bits
        - '0': para orden descente
        - '1': para orden ascendente
    - **_type_**: permite elegir el tipo de los datos. El tipo por defecto es **_std_logic(_vector)**
    El tipo 'u' --> "unsigned"

- *port_inout(\<puertos_de_entrada_salida\>, \<bits\>, \<MSB\>, \<LSB\>, \<invert\>, \<type\>)*: 
Este método permite incluir puertos de entrada\salida en el proyecto.
    - **_bits_**: permite elegir el número de bits que tendrá la cadena
    - **_MSB_**: permite elegir el bit de más peso
    - **_LSB_**: permite elegir el bit de menor peso
    - **_invert_**: permite elegir el sentido de los bits
        - '0': para orden descente
        - '1': para orden ascendente
    - **_type_**: permite elegir el tipo de los datos. El tipo por defecto es **_std_logic(_vector)**
    El tipo 'u' --> "unsigned"

- *signal(\<señal\>, \<bits\>, \<MSB\>, \<LSB\>, \<invert\>, \<type\>)*: 
Este método permite incluir señales en el proyecto.
    - **_bits_**: permite elegir el número de bits que tendrá la cadena
    - **_MSB_**: permite elegir el bit de más peso
    - **_LSB_**: permite elegir el bit de menor peso
    - **_invert_**: permite elegir el sentido de los bits
        - '0': para orden descente
        - '1': para orden ascendente
    - **_type_**: permite elegir el tipo de los datos. El tipo por defecto es **_std_logic(_vector)**
    El tipo 'u' --> "unsigned"

- *generic(\<generic\>, \<tipo\>="integer", \<valor\>)*:
Este método permite incluir en los genéricos en el proyeto
    - **_tipo_**: permite elegir el tipo del genérico, por defecto es _integer_
    - **_valor_**: el valor del generico, es opcional

## Ejemplo:
``` python
import pyVHDL
v=pyVHDL("Prueba.vhd")
v.use("numeric_std")
v.generic("generico", "integer", 32)
v.port_in("puerto_entrada1")
v.port_in("puerto_entrada2", 23)
v.port_in("puerto_entrada3", 23, invert=1)
v.port_in("puerto_entrada4", bits=4, LSB=2)
v.port_out("puerto_salida")
v.port_inout("puerto_entrada_salida")
v.signal("senal", 8)
```
Equivalente:
``` vhdl
library ieee;
use ieee.std_logic_1164.all;
use iee.numeric_std.all;

entity Prueba is
generic(
    generico : integer := 32
);
port(
    puerto_entrada1 : in std_logic;
    puerto_entrada2 : in std_logic_vector(22 downto 0);
    puerto_entrada3 : in std_logic_vector(0 to 22);
    puerto_entrada4 : in std_logic_vector(6 downto 2);
    puerto_salida : out std_logic;
    puerto_entrada_salida : inout std_logic
);

end Prueba;

architecture arch_Prueba of Prueba is
signal senal : std_logic_vector(7 downto 0);
begin


end architecture;
```