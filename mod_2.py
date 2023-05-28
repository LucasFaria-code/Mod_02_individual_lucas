# aqui inicia o meu trabalho individual do modulo 2 

def titulo(msg):
        print(f'{msg}')  

#aqui inicia a parte lógica do meu código.
       
def listCandidato(candidato):
    global result, listAprovados
    for i in range(len(candidato)):
        e = candidato[i][0]
        t = candidato[i][1]
        p = candidato[i][2]
        s = candidato[i][3]

        result.append(f'{i+1}° Candidato: e{e}_t{t}_p{p}_s{s}')
        
    titulo('Lista de Candidatos:')  
#esse imprime a lista de Candidatos que deram entrada no programa.   
    for c in range(len(result)):
        print(f'{result[c][:13]:.<18}', end='')
        print(f'{result[c][13:]}')

# aqui se da a entrada dos critérios.

def aprov(criterios, candidato):
    for g in range(len(candidato)):
        cont = 0
        for i in range(0, 4):
            if 0 < criterios[i] <= candidato[g][i]:
                cont += 1
            if cont == 4:
                listAprovados.append(f'{g+1}ª Candidato e_{candidato[g][0]}_t{candidato[g][1]}_p{candidato[g][2]}_s{candidato[g][3]}')

# aqui, abaixo, mostra a lista de candidatos aprovados e reprovados.

    titulo('Aprovados:')
     
    for ap in range(len(listAprovados)):
        print(f'{listAprovados[ap][:13]:.<18}', end='')
        print(f'{listAprovados[ap][13:]}')
    if len(listAprovados) == 0:
        print('Nenhum aprovado!')

listAprovados = []
candidato = []
result = []
posicao = 1
  
titulo('Insira as notas')
   
#aqui é o algoritimo, que recebe os valores inteiros, para cada nota atribuida aos candidatos.

while True:
    print(f'{posicao}° Candidato:')
    notas = [
        int(input('Digite a nota Entrevista: ')),
        int(input('Digite a nota Teste Teorico: ')),
        int(input('Digite a nota Teste Prático: ')),
        int(input('Digite a nota Soft Skill: '))
            ]
    candidato.append(notas[:])
    notas.clear

    resposta = input('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nDeseja adicionar mais algum cadidato a lista? \nPara Continuar com a entrada de notas do próximo candidato, digite [s] ou [n] para prosseguir para os critérios das notas de cada candidato.\nDigite aqui: ').lower()[0]
    print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    if resposta == 'n':
        break
    posicao +=1

# aqui entra a nota minima dos criterios, para saber se o cadidato será aprovado ou reprovado.
titulo('Quais são os Critérios:')
   
criterios = [
    int(input('Qual a nota de critério para a Entrevista: ')),
    int(input('Qual a nota de critério para o Teste Teórico: ')),
    int(input('Qual a nota de critério para o Teste Prático: ')),
    int(input('Qual a nota de critério para o Soft Skill: '))
            ]

listCandidato(candidato)
aprov(criterios, candidato)

# aqui termina o código.