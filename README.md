# Dani-Control-Version  
  
Sistema de control de versiones simplificado similar a Git, implementado en Python.  
  
## Instalación   
pip install -e .

### Uso
mygit init  
echo "Hola mundo" > test.txt  
mygit hash-object test.txt  
mygit cat-file <hash>

### Arquitectura
CLI: mygit/cli.py - interfaz de comandos
Data: mygit/data.py - almacenamiento de objetos
Setup: setup.py - configuración del paquete
