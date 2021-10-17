import os

vhd_files=[]
y=[]
objeto=os.listdir()
for i in objeto:
    if i.endswith(".vhd"):
        #print(i)
        vhd_files.append(i)
name= vhd_files[0][:-4]
f=open(vhd_files[0], 'r')

mensaje=f.readlines()
port=0
cont=0
puertos=[]
for t in mensaje:
    t=t.replace("\n", "")
    t=t.replace(";", "")
    t=t.replace(" ", "")
    y.append([t])
    
    #print(t + "\n")
    if t.find("port(") != -1:
        #print("encontrado")
        port=1
    
    if port==1:
        cont+=t.count("(")
        cont-=t.count(")")
       # print(cont)
        puertos.append([t])
    if cont==0:
        port=0

#print(puertos)
nombre=[]
tipo =[]
formato=[]
MSB =[]
LSB= []
for pue in puertos[1:]:
    aux=pue[0].split(":", -1)
    nombre.append(aux[0])
    aux2=aux[1].split("in", 1)
    if len(aux2)==2:
        tipo.append("in")
        aux3=aux2[1]
    else:
        tipo.append("out")
        aux3=aux2[0][3:]
   # print(aux3)
    aux3=aux3.replace("(", "")
    aux3=aux3.replace(")", "")
    if aux3.find("std_logic_vector") != -1:
        aux3=aux3[16:]
        if aux3.find("downto"):
            aux4=aux3.split("downto", -1)
            MSB.append(int(aux4[0]))
            LSB.append(int(aux4[1]))
        else:
            aux4=aux3.split("to", -1)
            MSB.append(int(aux4[1]))
            LSB.append(int(aux4[0]))
        formato.append("std_logic_vector")
    elif aux3=="std_logic":
        formato.append("std_logic")
        MSB.append(0)
        LSB.append(0)
      #  print(aux3)
   # print(pue)
#print(nombre)
#print(tipo)
#print(formato)
#print(MSB)
#print(LSB)

port_in=[]
port_out=[]
i=0
for j in tipo:
    if j=="in":
        port_in.append([nombre[i], formato[i], MSB[i], LSB[i]])
    elif j=="out":
        port_out.append([nombre[i], formato[i], MSB[i], LSB[i]])
    i+=1

#print("port_in: " ,port_in)
#print("port_out: ", port_out)


def generar_testbench():
    
    wr="library IEEE; \nuse IEEE.STD_LOGIC_1164.ALL;\nuse ieee.numeric_std.all;\n\nentity " + name + "_tb is\nend " + name + "_tb;\n\narchitecture arch_" + name + "_tb of " + name + "_tb is\n"
    cont=0
    wr += "component "+ name + " is\n\t"
    wr +="port ( \n\t\t"
    for h in port_in:
        if h[1] == "std_logic":
            wr += h[0] + " : in " + h[1] 
        elif h[1]== "std_logic_vector":
            wr += h[0] + " : in " + h[1] +"("+ str(h[2]) + " downto " + str(h[3]) + ")"
        if cont != len(nombre)-1:
            wr += ";\n\t\t"
            cont+=1
        else:
            wr += "\n\t\t"
    for r in port_out:
        if r[1] == "std_logic":
            wr +=   r[0] + " : out " + r[1]
        elif r[1]== "std_logic_vector":
            wr +=   r[0] + " : out " + str(r[1]) +"("+ str(r[2]) + " downto " +r[3] + ")"
        if cont != len(nombre)-1:
            wr += ";\n\t\t"
            cont+=1
        else:
            wr += "\n\t"
    wr +=");"
    wr += "\nend component;\n"
    wr += generador_senales("")
    wr += "\nbegin"
    wr +=component()
    wr +="\nend architecture;"

    return wr

def generador_senales(fin=""):
    sn =""
    for h in port_in:
        if h[1] == "std_logic":
            sn += "signal " + h[0] + fin + " : " + h[1] + ";\n"
        else:
            sn += "signal " + h[0] + fin + " : " + h[1] + "(" + str(h[2]) + " downto "+ str(h[3]) + ");\n"
    for r in port_out:
        if r[1] == "std_logic":
            sn += "signal " + r[0] + fin + " : " + r[1] + ";\n"
        else:
            sn += "signal " + r[0] + fin + " : " + r[1] + "(" + str(r[2]) + " downto "+ str(r[3]) + ");\n"
    
    return sn

def component():
    cont=0
    cmp="\nDUT : entity work." + name
    cmp+="\n\tport map("
    for h in port_in:
        cmp+="\n\t\t"+ h[0] + " => " + h[0] 
        if cont != len(nombre)-1:
            cmp += ""
            cont+=1
    for h in port_out:
        cmp+="\n\t\t"+ h[0] + " => " + h[0] 
        if cont != len(nombre)-1:
            cmp += ","
            cont+=1
    cmp+="\n\t);"
    return cmp

print(generar_testbench())
fil=name+"_tb.vhd"
file=open(fil,"w")
file.write(generar_testbench())
file.close()
  #  print(t.find("port("))
#print(y.find("port"))
