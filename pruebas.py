import VHDL 

##Opcion 1
v=VHDL("PWM_generator.vhd")
v.library(["ieee"])
v.use([["std_logic_1164"], ["numeric_std"]])
v.port([["rst", "clk", "hab_pwm", ["periodo", 23,0], ["ciclo_trabajo",23, 0]], ["pwm", "final_pwm"]])
v.signal([["senal_portadora", 23], ["final_pwm_int"]])
v.constant([["cero", 24, 0, 'u']])

##Opcion 2
v=VHDL("PWM_generator.vhd")
#v.library("ieee") ###libreria por defecto
#v.use("std_logic_1164") ###libreria por defecto
v.use("numeric_std")
v.port_in("rst")
v.port_in("clk")
v.port_in("periodo", bits=24)
v.port_in("ciclo_trabajo", 23)
v.port_out("pwm")
v.port_out("final_pwm")
v.signal("senal_portadora", 23)
v.signal("final_pwm_int")
v.constant("cero", 24, 0, type='u')

