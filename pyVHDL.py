class pyVHDL:
    '''
Esta clase es la que permite crear los ficheros vhdl
    '''
    def __init__(self, name=None):
        '''
En el constructor se declaran las listas en las que se almacenarán los elementos que luego
compondrán el fichero vhdl
        '''
        self.libraries=["ieee"]
        self.uses=[["std_logic_1164", self.libraries[0], 'all']]
        self.signals=[]
        self.process=[]
        self.name=name
        self.entity=""
        self.architecture=""
        self.inPorts=[]
        self.outPorts=[]
        self.generics=[]
        self.constants=[]
        self.inoutPorts=[]

    def library(self, library=None):
        '''
        Este método permite intruducir las clases que fuese necesario incluir
        '''
        if library is not None:
            self.libraries.append(library)
    
    def use(self, use=None, library="ieee", count="all"):
        '''Este método permite introducir los use que se utilizarán en el fichero

        Parameters
        ----------
        use : nombre del use que se va a introduci
        library : nombre de la libreria al que pertenece el use
        count : numero de fichero que se introducen

        '''
        if use is not None:
            self.uses.append([use, library, count])
    
    def list_ports(self ,input, output, bits, MSB, LSB, invert, type):
        ''' Método para cuadrar el numero de bits en las listas

        Parameters
        ----------
        input : nombre de entrada
        output : lista en la que se almacenará
        bits : número de bits que incluye el fichero
        MSB : bit de mayor peso
        LSB : bit de menor peso
        invert : para invertir el orden de los bits
            '0': para orden descente
            '1': para orden ascendente
        type : tipo de los datos
        '''
        if invert==0:
            if bits ==0:
                MSB_l=MSB
                LSB_l=MSB
            elif bits>0 and MSB==0 and LSB==0:
                LSB_l=0
                MSB_l=bits-1
            elif MSB>0:
                MSB_l=MSB
                LSB_l=MSB-bits
                if(LSB_l<0):
                    print("Error en LSB")
                    LSB_l=0
            elif LSB>0:
                LSB_l=LSB
                MSB_l=LSB+bits
        elif invert==1:
            if bits ==0:
                MSB_l=MSB
                LSB_l=MSB
            elif bits>0 and MSB==0 and LSB==0:
                LSB_l=bits-1
                MSB_l=0
            elif MSB>0:
                MSB_l=MSB
                LSB_l=MSB+bits
            elif LSB>0:
                LSB_l=LSB
                MSB_l=LSB-bits
                if(MSB_l<0):
                    print("Error en LSB")
                    MSB_l=0
        output.append([input, type, MSB_l, LSB_l])

    def port_in(self, port=None, bits=0, MSB=0, LSB=0, invert=0, type=None):
        ''' Método para introducir los puertos de entrada

            Parameters
            ----------
            port : nombre del puerto de entrada
            bits : número de bits que incluye el fichero
            MSB : bit de mayor peso
            LSB : bit de menor peso
            invert : para invertir el orden de los bits
                '0': para orden descente
                '1': para orden ascendente
            type : tipo de los datos
        '''
        if type is None:
            if bits==0:
                type="std_logic"
            elif bits>0:
                type="std_logic_vector"
        elif type == "u":
            type="unsigned"
        self.list_ports(port, self.inPorts, bits, MSB, LSB, invert, type)
        
    def port_out(self, port=None, bits=0, MSB=0, LSB=0, invert=0, type=None):
        ''' Método para introducir los puertos de salida

            Parameters
            ----------
            port : nombre del puerto de salida
            bits : número de bits que incluye el fichero
            MSB : bit de mayor peso
            LSB : bit de menor peso
            invert : para invertir el orden de los bits
                '0': para orden descente
                '1': para orden ascendente
            type : tipo de los datos
        '''
        if type is None:
            if bits==0:
                type="std_logic"
            elif bits>0:
                type="std_logic_vector"
        elif type == "u":
            type="unsigned"
        self.list_ports(port, self.outPorts, bits, MSB, LSB, invert, type)

    def port_inout(self, port=None, bits=0, MSB=0, LSB=0, invert=0, type=None):
        ''' Método para introducir los puertos de entrada_salida

            Parameters
            ----------
            port : nombre del puerto de entrada_salida
            bits : número de bits que incluye el fichero
            MSB : bit de mayor peso
            LSB : bit de menor peso
            invert : para invertir el orden de los bits
                '0': para orden descente
                '1': para orden ascendente
            type : tipo de los datos
        '''
        if type is None:
            if bits==0:
                type="std_logic"
            elif bits>0:
                type="std_logic_vector"
        elif type == "u":
            type="unsigned"
        self.list_ports(port, self.inoutPorts, bits, MSB, LSB, invert, type)

    def signal(self, signal=None, bits=0, MSB=0, LSB=0, invert=0, type=None):
        ''' Método para introducir las señales

            Parameters
            ----------
            signal : nombre de la señal
            bits : número de bits que incluye el fichero
            MSB : bit de mayor peso
            LSB : bit de menor peso
            invert : para invertir el orden de los bits
                '0': para orden descente
                '1': para orden ascendente
            type : tipo de los datos
        '''
        if type is None:
            if bits==0:
                type="std_logic"
            elif bits>0:
                type="std_logic_vector"
        elif type == "u":
            type="unsigned"
        self.list_ports(signal, self.signals, bits, MSB, LSB, invert, type)

    def constant(self, constant=None):
        if constant is not None:
            self.constants.append(constant)
    


if __name__=="__main__":
    v=pyVHDL("PWM_generator.vhd")
    #v.library("ieee") ###libreria por defecto
    #v.use("std_logic_1164") ###libreria por defecto
    v.use("numeric_std")
    print(v.uses)
    v.port_in("rst")
    v.port_in("clk")
    v.port_in("periodo",MSB=25, type="u")
    v.port_in("ciclo_trabajo", 23)
    v.port_out("pwm")
    v.port_out("final_pwm")
    print("Puertos de entrada: ", v.inPorts)
    print("Puertos de salida: ", v.outPorts)
    v.signal("senal_portadora", 23) 
    v.signal("final_pwm_int")
    print("Signals", v.signals)