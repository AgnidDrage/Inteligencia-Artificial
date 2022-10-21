from math import e

def capaInicial(r,sd,w,neuronas):
    lista = [1]
    for i in range(0, neuronas):
        lista.append(perceptron(r, sd, w[i]))
    return lista

# def capaOculta(lista_entP,sd, w, neuronas):
#     lista = [1]
#     cantidadDeCapasOcultas = 1
#     val = 0
#     while val != cantidadDeCapasOcultas:
#         for i in range(neuronas-1, neuronas+2):
#             lista.append(perceptron(lista_entP, sd, w[i])[0])
#         lista_entP = lista
#         neuronas += neuronas
#         val += 1
#     return lista_entP

def capaFinal(lista_entO,sd, w, neuronas):
    lista = [1]
    for i in range(neuronas+2, neuronas+3):
        lista.append(perceptron(lista_entO, sd, w[i]))
    return lista
    

def perceptron(r, sd, w):
    i = len(r)-1 #para lista original 
    j = 0 #para pesos
    suma = 0
    for i in range(i-(len(r)-1), i+1):
        suma += r[i] * w[j]
        j += 1
    y = 1 / (1 + e**-suma)
    calc_error = sd - y
    delta = y*(1-y)*calc_error
    for z in range(0, len(w)):
        w[z] = w[z] + 0.1*r[z]*delta
    return y

def modificarLista(lista):
    lista.insert(0,lista[-1])
    lista.pop()

def backpropagation(weight, ent, val):
    for i in range(0, len(weight)):
        weight[i] = weight[i] + 0.9*ent[i]*val


r = [
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
    ]
sd = [0,1,1,0]
weights = [
          [0.9,0.7,0.5],
          [0.3,-0.9,-1],
          [0.8,0.35,0.1],
          [-0.23,-0.79,0.56,0.6]
          ]
iteracion = 0
iteracion_r = 0
iteracion_sd = 0
listaP = []
while iteracion != 10000:
    listaInicial = capaInicial(r[iteracion_r],sd[iteracion_sd],weights,3)
    #listaMedia = capaOculta(listaInicial, sd,weights,3)
    listaFinal = capaFinal(listaInicial, sd[iteracion_sd], weights, 1)
    listaNew = listaInicial + listaFinal
    while (1 in listaNew) is True:
        listaNew.remove(1)
    modificarLista(listaNew)
    modificarLista(weights)
    listaP.append(listaNew[0])
    for i in range (0, len(weights)):
        if i == 0:
            error = sd[iteracion_sd] - listaNew[i]
            deltaMinuscula = listaNew[i]*(1-listaNew[i])*error
            backpropagation(weights[i], listaInicial, deltaMinuscula)
        else:
            listaInicial = r[iteracion_r]
            deltaMayuscula = listaNew[i]*(1-listaNew[i])*deltaMinuscula
            backpropagation(weights[i], listaInicial, deltaMayuscula)
    iteracion_r += 1
    weights.insert(len(weights), weights[0])
    weights.pop(0)
    iteracion_sd += 1
    iteracion += 1
    if iteracion_r == 4:
        iteracion_r = 0
        iteracion_sd = 0


print(listaP[-4:])