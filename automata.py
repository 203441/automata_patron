import tkinter as tk

estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'} 
alfabeto = {'1', '2', '3', '-', 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', 
            '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'}

transiciones = {
    'q0': {'1': 'q1', '2': 'q1', '3': 'q1'},
    'q1': {'-': 'q2'},
    'q2': {'A': 'q3'},
    'q3': {'A': 'q4', 'B': 'q4', 'C': 'q4', 'D': 'q4', 'E': 'q4', 'F': 'q4'},
    'q4': {'-': 'q5'},
    'q5': {'0': 'q7', '1': 'q6', '2': 'q6', '3': 'q6', '4': 'q6', '5': 'q6', '6': 'q6', '7': 'q6', '8': 'q6', '9': 'q7'},
    'q6': {'1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'},
    'q7': {'1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'},
    'q8': {'A': 'q9', 'B': 'q9', 'C': 'q9', 'D': 'q9', 'E': 'q9', 'F': 'q9', 'G': 'q9', 'H': 'q9', 'I': 'q9', 'J': 'q9', 
           'K': 'q9', 'L': 'q9', 'M': 'q9', 'N': 'q9', 'O': 'q9', 'P': 'q9'},
    'q9': {}
}

def validar_cadena(cadena):
    estado_actual = 'q0'
    recorrido = ['q0']

    for simbolo in cadena:
        if simbolo not in alfabeto:
            return False, recorrido
        
        if simbolo in transiciones[estado_actual]:
            estado_actual = transiciones[estado_actual][simbolo]
            recorrido.append(estado_actual)
        else:
            return False, recorrido
    
    return estado_actual == 'q9', recorrido

def verificar_cadena():
    cadena = entrada.get()
    resultado, recorrido = validar_cadena(cadena)

    if resultado:
        resultado_label.config(text="Cadena válida")
    else:
        resultado_label.config(text="Cadena inválida")

    recorrido_label.config(text=" -> ".join(recorrido))

ventana = tk.Tk()
ventana.title("automata")
ventana.geometry("400x200")

entrada_label = tk.Label(ventana, text="Ingrese una cadena:")
entrada_label.pack()

entrada = tk.Entry(ventana)
entrada.pack()

verificar_button = tk.Button(ventana, text="Verificar", command=verificar_cadena)
verificar_button.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

recorrido_label = tk.Label(ventana, text="")
recorrido_label.pack()

ventana.mainloop()
