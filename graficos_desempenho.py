import numpy as np
import matplotlib.pyplot as plt


perguntas = [1,2,3,4,5,6,7,8,9]
tempo = [22,24,14,47,23,14,21,25,17]
acertos = [1,2,3,3,4,5,6,7,8]

#fig, axes = plt.subplots(ncols = 3, figsize = (20,5))
fig, ax1 = plt.subplots()

color = 'gray'
ax1.set_xlabel('Pergunta')
ax1.set_ylabel('Tempo de Resposta', color=color)
ax1.bar(perguntas, tempo, color=color)
plt.yticks([5,10,15,20,25,30,35,40,45, 47])

ax2 = ax1.twinx() 

color = 'black'
ax2.set_ylabel('Acertos Acumulados', color=color) 
ax2.plot(perguntas, acertos, color=color)
plt.yticks([1,2,3,4,5,6,7,8,9], color = 'white')

ax3 = ax1.twinx() 


ax3.plot(perguntas, [1,2,3,4,4,4,4,5,5], color='green')
plt.yticks([1,2,3,4,5,6,7,8,9])

plt.title('S2 - LB1 Pré Módulo', fontsize = 15, fontweight = 'bold')
plt.show()




perguntas = [1,2,3,4,5,6,7,8,9]
tempo = [46,142,10,13,12,28,17,13,8]
acertos = [1,1,2,3,4,5,6,7,8]


fig, ax1 = plt.subplots()

color = 'gray'
ax1.set_xlabel('Pergunta')
ax1.set_ylabel('Tempo de Resposta', color=color)
ax1.plot(perguntas, tempo, color=color)
plt.yticks([20,40,60,80,100,120,142])

ax2 = ax1.twinx() 

color = 'black'
ax2.set_ylabel('Acertos Acumulados', color=color) 
ax2.plot(perguntas, acertos, color=color)
plt.yticks([1,2,3,4,5,6,7,8,9])


plt.title('S2 - Módulo 1', fontsize = 15, fontweight = 'bold')
plt.show()


import numpy as np
import matplotlib.pyplot as plt


perguntas = [1,2,3,4,5,6,7,8,9]
tempo = [28,23,16,43,21,14,20,12,19]
acertos = [1,2,3,4,5,6,7,8,9]

fig, ax1 = plt.subplots()

color = 'gray'
ax1.set_xlabel('Pergunta')
ax1.set_ylabel('Tempo de Resposta', color=color)
ax1.plot(perguntas, tempo, color=color)
plt.yticks([5,10,15,20,25,30,35,40,43])

ax2 = ax1.twinx() 

color = 'black'
ax2.set_ylabel('Acertos Acumulados', color=color) 
ax2.plot(perguntas, acertos, color=color)
plt.yticks([1,2,3,4,5,6,7,8,9])



plt.title('S2 - LB1 Pós Módulo', fontsize = 15, fontweight = 'bold')

plt.show()
