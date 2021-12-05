import PySimpleGUI as sg
import Registos as emd

# Painel de 2 colunas
# Coluna 1- Menu (menu_list_column)
# Coluna 2- Resultados (data_viewer_column)


def janelaListar(L):
    layout2=[
        [sg.Text("id          data              nome                  apto")],
        [sg.Listbox(values=L, size=(60,20), key="_Listar_")]
    ]


    window2 = sg.Window(title="Listar").Layout(layout2)

    stop = False
    while not stop:
        event, values = window2.read()  
        if event == sg.WIN_CLOSED:
            stop = True
    
    window.close()


sg.theme('LightGreen6')

menu_list_column=[
    [sg.Button("Carregar")],
    [sg.Button("Modalidades")],
    [sg.Button("Por ano")],
    [sg.Button("Por clube")],
    [sg.Button("Listar")],
]

listar=[]

data_viewer_column=[
    [sg.Text("Painel de Dados", key="_Dados_")],
    
]


layout = [
    [
        sg.Column(menu_list_column),
        sg.VSeperator(),
        sg.Column(data_viewer_column),
        
    ]
]

window= sg.Window("Registos Médicos", layout)
window.Size=(800,400)


stop = False
while not stop:
    event, values = window.read()
    BD=emd.lerDataset("emd.csv")
    if event == "Carregar":
        c=0
        for reg in BD:
            c+=1
        window['_Dados_'].Update("Foram carregados " + str(c)+ " registos.")
    
    elif event == "Modalidades":
        mod=emd.modalidades(BD)
        modal=" "
        for i in range (len(mod)):
            modal=modal + mod[i] + "\n "
        window['_Dados_'].Update("Modalidades:\n" + modal)
        window['_Dados_'].Update(emd.plotDistribPorModalidade(emd.distribPorModalidade(BD)))
    
    elif event == "Por ano":
        window['_Dados_'].Update(emd.plotDistrib(emd.distribPorAno(BD)))
    
    elif event == "Por clube":
        window['_Dados_'].Update(emd.plotDistrib(emd.distribPorClube(BD)))
    
    elif event == "Listar":
        listar=emd.listarDataset(BD)
        janelaListar(listar)

    elif event == sg.WIN_CLOSED:
        stop = True

window.close()