import pandas as pd
from pandas import ExcelWriter

consultar=""
Rut_cliente=[]
nombre_cliente=[]
apellido_cliente=[]
direccion_cliente=[]
telefono_cliente=[]

nuevo_Rut_cliente=input()
Rut_cliente.append(nuevo_Rut_cliente)

nuevo_nombre_cliente=input()
nombre_cliente.append(nuevo_nombre_cliente)

nuevo_apellido_cliente=input()
apellido_cliente.append(nuevo_apellido_cliente)

nuevo_direccion_cliente=input()
direccion_cliente.append(nuevo_direccion_cliente)

nuevo_telefono_cliente=input()
telefono_cliente.append(nuevo_telefono_cliente)

data= {'RUT': Rut_cliente,
            'Nombre': nombre_cliente,
            'Apellido':apellido_cliente,
            'Direccion':direccion_cliente,
            'Telefono':telefono_cliente}
print (data)

df = pd.DataFrame(data)

escritor = pd.ExcelWriter('C:/Users/Nicolas/Desktop/Respaldo/Desarrollo agil de Software/Datos.xlsx', engine='xlsxwriter')

df.to_excel(escritor, sheet_name="Usuario") 

escritor.save()
print("data entered succefully")