import sys

def traducir(letra):
    notas = {"A":"La","B":"Si","C":"Do","D":"Re","E":"Mi","F":"Fa","G":"Sol"}
    try:
        return notas[letra]
    except KeyError:
        return letra

while True:
    try:
        linea = input()
    except EOFError:
        sys.exit(0)
    if linea.startswith("{define: "):
        print(linea[:9] + traducir(linea[len("{define: ")]) + linea[10:])
        

