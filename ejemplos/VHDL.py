from tkinter import *
class VHDL:
    def __init__(self, name=None):
        self.libraries=["ieee"]
        self.uses=[["std_logic_1164", 'std', 'all']]
        self.signals=[]
        self.process=[]
        self.name=name
        self.entity=""
        self.architecture=""
        self.inPorts=[]
        self.outPorts=[]
        self.generics=[]

        ### Catch the values and input in lists
    def library(self, library=None):
        if library!=None:
            for i in range(len(library)):
                self.libraries.append(library[i])
        return self.libraries
    
    def use(self, use=None):
        if use!=None:
            for i in range(len(use)):
                if len(use[i])==1:
                    self.uses.append([use[i][0], "ieee", "all"])
                elif len(use[i])==2:
                    self.uses.append([use[i][0], use[i][1], "all"])
                elif len(use[i])==3:
                    if(use[i][1]=="_")|(use[i][1]==""):
                        self.uses.append([use[i][0], "ieee", use[i][2]])
                    else:
                        self.uses.append(use[i])
                else:
                    print("Error enough arguments in method \" use \" ")
        return self.uses

    def signal(self, signal=None):
        self.add(signal, self.signals)  
        return self.signals
    
    def nameVHDL(self, name=None):
        if name==None:
            name=self.name
        for i in range(len(name)):
            if name[i]=='.':
                break
            self.entity=self.entity+name[i]
        return self.entity

    def nameArchitecture(self, name=None):
        if name==None:
            name="arch_"+self.nameVHDL()
        self.architecture=name
        return self.architecture

    def port(self, inPorts=None, outPorts=None):
        self.add(inPorts, self.inPorts)
        self.add(outPorts, self.outPorts)

    def generic(self, generic=None):
        if generic!=None:
            self.generics.append(generic)

        ### Change the list to a VHDL code
    def convPorts(self):
        wPort="port(\n\t"
        longitudEntrada=len(self.inPorts)
        longitudSalida=len(self.outPorts)
        longitud=longitudEntrada+longitudSalida
        for i in range(len(self.inPorts)):
            wPort=wPort+self.inPorts[i][0]+ " : in std_logic"
            if(self.inPorts[i][1]==0):
                if i<longitud-1:
                    wPort=wPort+";\n\t"
                else:
                    wPort=wPort+"\n\t"
            else:
                wPort=wPort+"_vector("+str(self.inPorts[i][1]) + " downto 0);\n\t"
        for i in range(len(self.outPorts)):     #reestructurarlo : ; al final
            wPort=wPort+self.outPorts[i][0]+ " : out std_logic"
            if(self.outPorts[i][1]==0):
                if i+longitudEntrada<longitud-1:
                    wPort=wPort+";\n\t"
                else:
                    wPort=wPort+"\n\t"
            elif(self.outPorts[i][1][1]==None) :
                wPort=wPort+"_vector("+str(self.outPorts[i][1]) + " downto 0);\n\t"
            else:
                if(self.outPorts[i][1][0]>self.outPorts[i][1][1]):
                    direct=" downto "
                else:
                    direct=" to "
                wPort=wPort+"_vector("+str(self.outPorts[i][1][0]) + direct + str(self.outPorts[i][1][1])  + ");\n\t"
        wPort=wPort+");"
        return wPort

    def convEntity(self):   #faltan genericos
        if self.entity==None:
            self.nameVHDL()
        wEntity="entity "+ self.entity + " is\n"  + str(self.convGeneric) + str(self.convPorts()) + "\nend entity " + self.entity +";\n"
        return wEntity

    def convArchitecture(self):
        if self.entity==None:
            self.nameVHDL()
        wArchitecture="architecture "+ self.architecture + " of " + self.entity + " is\n " + self.convSignals() + " begin\n\t" \
            + "end " + self.architecture+ ";"
        return wArchitecture

    def convSignal(self):
        wSign=""
        for i in range(len(self.signals)):
            wSign= wSign + "\tsignal " + str(self.signals[i][0]) + " : std_logic_vector(" + str(self.signals[i][1]) +");\n"
        return wSign

    def convLib(self):
        wLib=""
        for i in range(len(self.libraries)):
            wLib=wLib+"library "+self.libraries[i]+"\n"
        return wLib
    
    def convUses(self):
        wUse=""
        for i in range(len(self.uses)):
            wUse = wUse + "use " + str(self.uses[i][1]) + "." + str(self.uses[i][0]) + "." + str(self.uses[i][2]) + ";\n"
        return wUse

        ### Method for transform data into list more especific
    def add(self, input, output):   #intentar para listas unitarias
        if input!=None:
            for i in range(len(input)):
                if len(input[i])==1:
                    self.oneArg(input[i], output)
                elif len(input[i])==2:
                    output.append(input[i])
                else:
                    self.error(input[i][0])

    def error(self, input):
        print("Error enough arguments for \"", input, "\"")

    def oneArg(self, input, output):
        newInput=[input[0], 0]
        output.append(newInput)
        return output

    def show(self):
        w=Tk()
        w.geometry('350x200')
        lbl = Label(w, text=self.convLib())
        lbl.grid(column=0, row=0)
        w.title(self.nameVHDL())
        w.configure(bg='blue')
        w.mainloop()

if __name__=="__main__":
    
    v=VHDL("primero.vhd")
    v.library(["eee", "rr", "ttrtr", "fgf"])
    print(v.libraries)
  #  v.generic([["hola", 32]])
 #   print(v.generics)
    


    print(v.convLib())
    v.use([["arithm"], ["uses",  "", "std"]])
    print(v.uses)
    print(v.convUses())
    
   # v.signal([["hola", 32], ["para_atras", 23]])
   # print(v.signals)
   # print(v.convSignal())
#
  #  v.port([["fsrfe"]], [["fasfa", [4,0]],["rere"]])
  #  print(v.inPorts)
 #   print(v.outPorts)
    
    # print("\t\t\t\t",v.signals)
    # v.signal([["nuevas", 4]])
    # print(v.inPorts)
   # print(v.convEntity())
    #