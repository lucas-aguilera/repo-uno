ingreso_mensual =90000
gasto_mensual=7000

if ingreso_mensual>10000:
    if ingreso_mensual -gasto_mensual <0:
        print("ahora estas bien")
    elif ingreso_mensual - gasto_mensual >3000:
        print("bien pa, ahora si estas bien")    
    else:
        ("y pa, estas gastando mucho fijate con los gasto")
    
else:
    print("sos pobre")