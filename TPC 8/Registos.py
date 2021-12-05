import matplotlib.pyplot as plt


def getEMD(linha):
    novaLinha=linha.strip("\n")
    emd=[]
    campos=novaLinha.split(",")
    emd.append("emd" + str(int(campos[1])+1))
    for i in range (2,len(campos)):
        emd.append(campos[i])
    return emd

def lerDataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd = []
    f.readline()
    for linha in f:
        emd=getEMD(linha)
        bd.append(emd)
    return bd

def chaveOrd(exame):
    return exame[1]

def apto(b):
    if b=="true":
        return "sim"
    else:
        return "não"

def listarDataset(bd):
    bd.sort(key=chaveOrd, reverse=True)
    lista=[]
    for a in bd:
       lista.append(a[0] + " | " + a[1] + " | " + a[3] + " " + a[2] + "     | " + apto(a[11]))
    
    return lista

def consultarDataset(bd, id):
    i=0
    while bd[i][0]!=id:
        i=i+1
    return bd[i]       

def modalidades(bd):
    modalidade=[]
    for emd in bd:
        if emd[7] not in modalidade:
            modalidade.append(emd[7])
    
    return modalidade
    #for mod in modalidade:
        #print (mod)

def chaveOrd2(exame):
    return exame[7]
    
def distribPorModalidade(bd):
    bd.sort(key=chaveOrd2)
    modalidades={}
    for exame in bd:
        if exame[7] in modalidades.keys():
            modalidades[exame[7]]+=1
        
        else:
            modalidades[exame[7]]=1
    return modalidades

def distribPorClube(bd):
    distribuicao={}
    for emd in bd:
        if emd[8] in distribuicao.keys():
            distribuicao[emd[8]]+=1
        
        else:
            distribuicao[emd[8]]=1
    
    return distribuicao

def distribPorAno(bd):
    distribuicao={}
    for emd in bd:
        if emd[1][0:4] in distribuicao.keys():
            distribuicao[emd[1][0:4]]+=1
        
        else:
            distribuicao[emd[1][0:4]]=1
    
    return distribuicao

def distrib(p,bd):
    distribuicao={}
    for emd in bd:
        if emd[p] in distribuicao.keys():
            distribuicao[emd[p]]+=1
        
        else:
            distribuicao[emd[p]]=1
    
    return distribuicao


def plotDistribPorModalidade(d):
    x_axis=[]

    y_axis=[]

    label=[]

    for mod in d.keys():
        y_axis.append(mod)
        x_axis.append(d[mod])
    
    plt.barh(y_axis,x_axis)
    plt.title('Distribuição de registos por modalidade')
    plt.ylabel('Modalidades')
    plt.xlabel('Nº de Registos')
    plt.show()

def plotDistrib(d):
    x_axis=[]

    y_axis=[]

    label=[]

    for mod in d.keys():
        y_axis.append(mod)
        x_axis.append(d[mod])
    
    plt.barh(y_axis,x_axis)
    plt.title('Distribuição')
    
    plt.xlabel('Nº de Registos')
    plt.show()
      