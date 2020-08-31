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
        if type is None:
            if bits==0:
                type="std_logic"
            elif bits>0:
                type="std_logic_vector"
        self.list_ports(port, self.inPorts, bits, MSB, LSB, invert, type)
        
    def port_out(self, port=None, bits=0, MSB=0, LSB=0, invert=0, type="std_logic"):
        self.list_ports(port, self.outPorts, bits, MSB, LSB, invert, type)

    def signal(self, signal=None, bits=0, MSB=0, LSB=0, invert=0, type="std_logic"):
        self.list_ports(signal, self.signals, bits, MSB, LSB, invert, type)

    def constant(self, constant=None):
        if constant is not None:
            self.constants.append(constant)
    


if __name__=="__main__":
    v=pyVHDL("PWM_generator.vhd")
    #v.li   brary("ieee") ###libreria por defecto
    #v.use("std_logic_1164") ###libreria por defecto
    v.use("numeric_std")
    v.port_in("rst")
    v.port_in("clk")
    v.port_in("periodo",MSB=25, type="unsigned")
    v.port_in("ciclo_trabajo", 23)
    v.port_out("pwm")
    v.port_out("final_pwm")
    print(v.inPorts)
    print(v.outPorts)
    v.signal("senal_portadora", 23) 
    v.signal("final_pwm_int")
    print(v.signals)