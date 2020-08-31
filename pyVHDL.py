class pyVHDL:
    def __init__(self, name=None):
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

    def library(self, library=None):
        if library is not None:
            self.libraries.append(library)
    
    def use(self, use=None, library="ieee", count="all"):
        if use is not None:
            self.uses.append([use, library, count])
    
    def list_ports(self,input, output, bits, MSB, LSB, invert, type):
        if invert==0:
            if bits ==0:
                MSB_l=0
                LSB_l=0
                type="std_logic"
            elif bits>0 and MSB==0 and LSB==0:
                LSB_l=0
                MSB_l=bits-1
                type="std_logic_vector"
            elif MSB>0:
                MSB_l=MSB
                LSB_l=MSB-bits
                type="std_logic_vector"
                if(LSB_l<0):
                    print("Error en LSB")
                    LSB_l=0
            elif LSB>0:
                LSB_l=LSB
                MSB_l=LSB+bits
                type="std_logic_vector"
        elif invert==1:
            if bits ==0:
                MSB_l=0
                LSB_l=0
                type="std_logic"
            elif bits>0 and MSB==0 and LSB==0:
                LSB_l=bits-1
                MSB_l=0
                type="std_logic_vector"
            elif MSB>0:
                MSB_l=MSB
                LSB_l=MSB+bits
                type="std_logic_vector"
            elif LSB>0:
                LSB_l=LSB
                MSB_l=LSB-bits
                type="std_logic_vector"
                if(MSB_l<0):
                    print("Error en LSB")
                    MSB_l=0
        output.append([input, type, MSB_l, LSB_l])

    def port_in(self, port=None, bits=0, MSB=0, LSB=0, invert=0, type="std_logic"):
        self.list_ports(port, self.inPorts, bits, MSB, LSB, invert, type)
        
    def port_out(self, port=None):
        if port is not None:
            self.outPorts.append(port)

    def signal(self, signal=None):
        if signal is not None:
            self.signals.append(signal)

    def constant(self, constant=None):
        if constant is not None:
            self.constants.append(constant)
    