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
        self.entity, self.architecture=self.nameVHDL(name)
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
            type : tipo de los datos, por defecto std_logic
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
            type : tipo de los datos, por defecto std_logic
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
            type : tipo de los datos, por defecto std_logic
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
            type : tipo de los datos, por defecto std_logic
        '''
        if type is None:
            if bits==0:
                type="std_logic"
            elif bits>0:
                type="std_logic_vector"
        elif type == "u":
            type="unsigned"
        self.list_ports(signal, self.signals, bits, MSB, LSB, invert, type)

    def nameVHDL(self, name=None):
        if name is None:
            name=self.name
        else:
            self.entity=""
            self.architecture=""
            for i in range(len(name)):
                if name[i]=='.':
                    break
                self.entity=self.entity+name[i]
        self.architecture="arch_"+self.entity
        return self.entity, self.architecture
    
    def nameArchitecture(self, name=None):
        if name is None:
            name="arch_"+self.nameVHDL()
        self.architecture=name
        return self.architecture

    #Convertir el codigo VHDL
    def conv_library(self):
        wLib=""
        for i in range(len(self.libraries)):
            wLib=wLib+"library "+self.libraries[i]+"\n"
        return wLib

    def conv_uses(self):
        wUse=""
        for i in range(len(self.uses)):
            wUse = wUse + "use " + str(self.uses[i][1]) + "." + str(self.uses[i][0]) + "." + str(self.uses[i][2]) + ";\n"
        return wUse

    def conv_ports(self):
        wPort="port("
        lonEnt=len(self.inPorts)
        lonSal=len(self.outPorts)
        lonEntSal=len(self.inoutPorts)
        longitud=lonEnt+lonSal+lonEntSal
        #Puertos de entrada
        for i in range(len(self.inPorts)):
            if self.inPorts[i][2]==self.inPorts[i][3]:
                wPort=wPort+"\n\t"+self.inPorts[i][0]+ "\t : \t in \t" + self.inPorts[i][1] 
            else:
                wPort+="\n\t"+self.inPorts[i][0]+ "\t :\t in \t" + str(self.inPorts[i][1])+ "(" + str(self.inPorts[i][2])
                if self.inPorts[i][2]>self.inPorts[i][3]:
                    wPort+=" downto "
                else:
                    wPort += " to "
                wPort+=str(self.inPorts[i][3])+ ")"
            if i<longitud-1:
                wPort=wPort+";"
        #puertos de salida
        for i in range(len(self.outPorts)):
            if self.outPorts[i][2]==self.outPorts[i][3]:
                wPort=wPort+"\n\t"+self.outPorts[i][0]+ " : out " + self.outPorts[i][1] 
            else:
                wPort+="\n\t"+self.outPorts[i][0]+ " : out " + str(self.outPorts[i][1])+ "(" + str(self.outPorts[i][2])
                if self.outPorts[i][2]>self.outPorts[i][3]:
                    wPort+=" downto "
                else:
                    wPort += " to "
                wPort+=str(self.outPorts[i][3])+ ")"
            if i<longitud-lonEnt-1:
                wPort=wPort+";"
        #puertos de entrada/salida
        for i in range(len(self.inoutPorts)):
            if self.inoutPorts[i][2]==self.inoutPorts[i][3]:
                wPort=wPort+"\n\t"+self.inoutPorts[i][0]+ " : inout " + self.inoutPorts[i][1] 
            else:
                wPort+="\n\t"+self.inoutPorts[i][0]+ " : inout " + str(self.inoutPorts[i][1])+ "(" + str(self.inoutPorts[i][2])
                if self.inoutPorts[i][2]>self.inoutPorts[i][3]:
                    wPort+=" downto "
                else:
                    wPort += " to "
                wPort+=str(self.inoutPorts[i][3])+ ")"
            if i<longitud-lonEnt-lonSal-1:
                wPort=wPort+";"
        wPort+="\n);"
        return wPort

    def conv_signal(self):
        if self.signals is not None:
            wSignal=""
            for i in range(len(self.signals)):
                if self.signals[i][2]==self.signals[i][3]:
                    wSignal+="\nsignal "+self.signals[i][0]+ " : " + self.signals[i][1] 
                else:
                    wSignal+="\nsignal "+self.signals[i][0]+ " : " + str(self.signals[i][1])+ "(" + str(self.signals[i][2])
                    if self.signals[i][2]>self.signals[i][3]:
                        wSignal+=" downto "
                    else:
                        wSignal += " to "
                    wSignal+=str(self.inoutPorts[i][3])+ ")"
                wSignal=wSignal+";"
        return wSignal

    def conv_entity(self):
        if self.entity is None:
            self.nameVHDL()
        wEntity="entity "+ self.entity + " is\n"  + self.conv_ports() + "\nend entity " + self.entity +";\n"
        return wEntity

    def conv_architecture(self):
        wArch="architecture " + self.architecture + " of " + self.entity +  " is " + self.conv_signal()+ "\nbegin" + "\nend architecture;"
        return wArch

    def conv_VHDL(self):
        wVHDL=self.conv_library()+self.conv_uses()+self.conv_entity()+self.conv_architecture()
        return wVHDL


if __name__=="__main__":
    v=pyVHDL("PWM_generator.vhd")
    v.use("numeric_std")
    v.port_in("rst")
    v.port_in("periodo",MSB=25, type="u")
    v.port_in("ciclo_trabajo", 23)
    v.port_in("clk")
    v.port_out("pwm")
    v.port_inout("final_pwm")
    v.signal("senal_portadora", 23) 
    v.signal("final_pwm_int")
    v.nameVHDL("hola")
    v.nameArchitecture("Pasando")
    print(v.conv_VHDL())