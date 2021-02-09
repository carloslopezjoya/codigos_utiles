import os

Carpeta=input('Ingrese ruta ')
Formato=input('Ingrese formato del nombre ')

contenido = os.listdir(Carpeta)

for i in range(1,(len(contenido)+1),1):
    #nombre_nuevo = f'E:\Oscar\Renombrador\Carpeta1\Foto_1118_001_{i}.mat'
    nombre_nuevo = f'{Carpeta}\{Formato}{i}.mat'
    path=f'{Carpeta}\{contenido[i-1]}'

    try:
        os.rename(path, nombre_nuevo)
    except:
        print(f'Numero {i} Ha fallado')
        continue
    
print('Proceso finalizado.')