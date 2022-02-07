from VHDL import VHDL

class top:
    def __init__(self, top_name, *bottom_files):
        self.document = top_name
        self.bottom_files = bottom_files
        self.num_files = len(bottom_files)
        self.port_in = []
        self.port_out = []
        self.generics = []
        self.component = []
        self.implement = []
    
    def generate(self):
        for i in range(self.num_files):
            self.vhdl = VHDL(self.bottom_files[i])
            self.vhdl.analizar()
            self.port_in = self.vhdl.port_in
            self.port_out = self.vhdl.port_out
            self.generics = self.vhdl.generics
            self.name = self.vhdl.name
            self.component.append(self.generate_component())
            self.implement.append(self.generate_impl())


    def generate_impl(self):
        wr = "\n" + self.name + "_impl : entity work." + self.name
        if self.generics is not None:
            wr += "\n\tgeneric map("
            cont = 0
            for gen in self.generics:
                wr += "\n\t\t" + gen[0] + " => " + gen[0] + "_top"
                if cont != len(self.generics)-1:
                    wr += ","
            wr += "\n\t)"

        num_port = len(self.port_in) + len(self.port_out)
        wr += "\n\tport map("
        cont = 0
        for port in self.port_in:
            wr += "\n\t\t" + port[0] + " => " + port[0] + "_top"
            if cont != num_port-1:
                wr += ","
                cont += 1
        for port in self.port_out:
            wr += "\n\t\t" + port[0] + " => " + port[0] + "_top"
            if cont != num_port-1:
                wr += ","
                cont += 1
        wr += "\n\t);"

        print(wr)

        
    
    def generate_component(self):
        wr = "\ncomponent " + self.name + " is"
        if self.generics is not None:
            wr += "\ngeneric("
            cont = 0
            for gen in self.generics:
                wr += "\n\t" + gen[0] + " : " + gen[1] + " := " + gen[2]
                if cont != len(self.generics)-1:
                    wr +=";"
                    cont += 1
                else: 
                    wr += "\n\t);"
        
        wr += "\nport ("
        num_port = len(self.port_in) + len(self.port_out)
        cont=0
        for port in self.port_in:
            wr += "\n\t" + port[0] + " : " + port[1] + " " + str(port[2])
            if port[2] == "std_logic_vector":
                wr += "("
                if port[4] == "0":
                    wr += port[3] + " downto 0)"
                elif port[3].isnumeric() and port[4].isnumeric():
                    if int(port[3]) > int(port[4]):
                        wr += port[3] + " downto " + port[4]
                    else:
                        wr += port[3] + " to " + port[4]
            if cont != num_port-1:
                cont += 1
                wr += ";"

        for port in self.port_out:
            wr += "\n\t" + port[0] + " : " + port[1] + " " + str(port[2])
            if port[2] == "std_logic_vector":
                wr += "("
                if port[4] == "0":
                    wr += port[3] + " downto 0)"
                elif port[3].isnumeric() and port[4].isnumeric():
                    if int(port[3]) > int(port[4]):
                        wr += port[3] + " downto " + port[4]
                    else:
                        wr += port[3] + " to " + port[4]
            if cont != num_port-1:
                cont += 1
                wr += ";" 
                    
        wr += "\n\t);\nend component;"
        print(wr)
        

if __name__=="__main__":
    top = top("hola", "PWM_generator.vhd")

    top.generate()