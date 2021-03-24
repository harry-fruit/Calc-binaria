import PySimpleGUI as sg







#altera a cor do background
sg.theme('Darkbrown3')
bases = ('Decimal','Hexadecimal','Octal', 'Binario')
um = (1)

# Define the window's contents
Layout = [  
            [sg.Text('Conversor de bases', size=(100,2), background_color = 'black', font=('Arial', 30), justification='center', text_color="#DAA520")],
            [sg.Text('Criado por: Isaque D, Marcos Q, Guilherme', font=('Arial'), pad=((450,0),(0,60)), text_color="black", background_color="#D3D3D3")],

            [sg.Text('Selecione as bases que você deseja converter.', background_color = 'black', font=('Arial', 20), text_color="#DAA520",pad=((110,0),(0,40)))],

            [sg.Text('(X)', pad=((290,0),(0,0))), sg.Text('(Y)', pad=((160,0),(0,0)))],
            [sg.Combo(bases, size=(15, 4), key="-FROMbases-", pad=((245, 0),(0,0))), sg.Text('➜', font=('Arial', 20), pad=((10,0),(0,0))), sg.Combo(bases, size=(15, 4), key="-TObases-", pad=(10, 0))],
            [sg.Text("Insira um valor 'X'", size=(30,1),pad=((165,0),(60,0))), sg.Text("Valor em 'Y'", size=(30,1), pad=((20,0),(60,0)))],

            [sg.Input(key='-X-', size=(30,2), pad=((165,0),(0,0
            ))), sg.Text('➜',pad=((15,15),(0,0)) ), sg.Text(key='-Y-', size=(30,1),font=('Arial'), pad=((0,0),(0,0)), background_color="#BDB76B", justification="center", )],
            [sg.Button('Calcular',pad=((310,0),(50,0)), size=(15,2), font=('Arial', 15))]

        ]

# Create the window
window = sg.Window('Conversor de Bases', Layout, size=(800,600))     # Part 3 - Window Defintion

def tratarParam2(referenteY):
    param2 = ''
    if referenteY == 'Decimal':
        param2 = 'd'
        return param2
    elif referenteY == 'Hexadecimal':
        param2 = 'X'
        return param2
    elif referenteY == 'Octal':
        param2 = 'o'
        return param2
    elif referenteY == 'Binario':
        param2 = 'b'
        return param2

def calcularResultado (valor, param2):
    resultado = (format(valor, param2)).upper()
    return resultado



# Display and interact with the Window
while True:
    event, values = window.read() # Part 4 - Event loop or Window.read call
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break    
    if event == "Calcular" :
        baseX = values['-FROMbases-']
        baseY = values['-TObases-']
        valorX = values['-X-']
        #window['-Y-'].update(values['-X-'])
        def tratarParam1(valorX, baseX):
            if baseX == 'Decimal':
                valorX = int(valorX)
                return valorX
            elif baseX == 'Hexadecimal':
                valorX = eval('0x'+valorX)
                return valorX
            elif baseX == 'Octal':
                valorX = eval('0o'+valorX)
                return valorX
            elif baseX == 'Binario':
                valorX = eval('0b'+valorX)
                return valorX
        window['-Y-'].update(calcularResultado(tratarParam1(valorX,baseX), tratarParam2(baseY)))
