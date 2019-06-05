import csv
import Atributes

# funcao para escrever a primeira linha do csv
def write(vet): 
    # endereco do .csv (ja processado) na maquina.
    f = open('/home/murilo/Documentos/GitHub/Preprocessing/Processed.csv','w')
    try:
        writer = csv.writer(f)
        writer.writerow(vet)
    finally:
        f.close()

# funcao apra adicionar as proximas linhas do csv
def append(vet): 
    # endereco do .csv (ja processado) na maquina.
    f = open('/home/murilo/Documentos/GitHub/Preprocessing/Processed.csv','a')
    try:
        writer = csv.writer(f)
        writer.writerow(vet)
    finally:
        f.close()

 # funcao para fazer o pre-processamento dos dados (atributos).
def preprocessing(vet): 
    vet[1] = Atributes.revenue(vet[1])
    vet[2] = Atributes.units(vet[2])
    vet[3] = Atributes.ls_date(vet[3])
    vet[4] = Atributes.tsls(vet[4])
    vet[8] = Atributes.completed(vet[8])
    vet[9] = Atributes.completed_post(vet[9])
    vet[10] = Atributes.win_rate(vet[10])
    vet[11] = Atributes.tries(vet[11])
    vet[13] = Atributes.tbs(vet[13])
    return vet

cont = 0
# endereco do .csv (a ser processado) na maquina.
f = open('/home/murilo/Documentos/GitHub/Preprocessing/Original_Data.csv','r') 
try:
    leitor = csv.reader(f)
    for linha in leitor:
        # Para tirar o espaco da primeira linha do csv, basta usar nesta o metodo 'w' ao inves de 'a'.
        if cont == 0:  
            write(linha)  
        else:    
            vet = preprocessing(linha)
            append(vet)
        cont += 1        
finally:
    f.close()
