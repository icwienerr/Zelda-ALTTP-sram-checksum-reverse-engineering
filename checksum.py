contador=0
result="0000"
with open("/home/debian/Downloads/ALttP/zelda.srm", 'rb') as f:
    while contador<=638:
        byte_s = f.read(2)
        if not byte_s:
            break
        result = hex(int(result, 16) + int.from_bytes(byte_s, byteorder='little'))
        if len(result[2:])>4:
            result = result[3:7]
        else:
            result = result[2:6]
        contador+=1
if int(result, 16) > 23130:
    resultado=int(result, 16)-23130
    resultado=65535-(resultado-1)
else:
    resultado=23130-int(result, 16)
resultado=hex(resultado)[2:6]
if len(resultado)<4:
    resultado= "0"+resultado
print(resultado[2]+resultado[3]+resultado[0]+resultado[1])
