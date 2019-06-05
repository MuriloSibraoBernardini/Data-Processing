def user(x): # vet[0]
    return x  

def revenue(x): # vet[1]
    if x == 'NULL':
        return 0
    else:
        return x

def units(x): # vet[2]
    if x == 'NULL':
        return 0
    else:
        return x

def ls_date(x): # vet[3]
    if x == 'NULL':
        return 0
    else:
        y = '-'
        for i in range(0,len(y)):
            x = x.replace(y[i],"")
        x = int(x)
    return x

def tsls(x): # vet[4] 
    if x == 'NULL':
        return 0
    else:
        return x

def rating(x): # vet[5]
    return x

def ttp(x): # vet[6]
    return x

def total_sessions(x): # vet[7]
    return x

def completed(x): # vet[8]
    if x == 'NULL':
        return 0
    else:
        return x

def completed_post(x): # vet[9]
    if x == 'NULL':
        return 0
    else:
        return x

def win_rate(x): # vet[10]
    if x == 'NULL':
        return 0
    else:
        return x    

def tries(x): # vet[11]
    if x == 'NULL':
        return 0
    else:
        return x  

def device(x): # vet[12]
    return x  

def tbs(x): # vet[13] 
    if x == 'NULL':
        return 0
    else:
        return x  

def tsad(x): # vet[14]
    return x                             
