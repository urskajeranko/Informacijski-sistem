import random 

polje = {'zgoraj-Levo': ' ', 'zgoraj-Sredina': ' ', 'zgoraj-Desno': ' ', 
         'sredina-Levo':' ','sredina-Sredina': ' ','sredina-Desno' : ' ', 
         'spodaj-Levo': ' ','spodaj-Sredina' : ' ', 'spodaj-Desno' : ' '} 
                                                                        
                                                    
                                                    
mogoce_poteze = list(polje.keys()) 
                                  
                                
                                  

def print_navodila():
    print('Možne poteze:')
    for i in mogoce_poteze:
        print(i) 
    print() 

def print_polje(): 
    print(polje['zgoraj-Levo'] + '|' + polje['zgoraj-Sredina'] + '|' + polje['zgoraj-Desno']) 
    print(polje['sredina-Levo'] + '|' + polje['sredina-Sredina'] + '|' + polje['sredina-Desno']) 
    print(polje['spodaj-Levo'] + '|' + polje['spodaj-Sredina'] + '|' + polje['spodaj-Desno'])



def preveri_konec(navrsti): 
    if(polje['zgoraj-Levo'] == navrsti and polje['zgoraj-Sredina'] == navrsti and polje['zgoraj-Desno'] == navrsti):
        return True 
    elif(polje['sredina-Levo'] == navrsti and polje['sredina-Sredina'] == navrsti and polje['sredina-Desno'] == navrsti):
        return True 
    elif(polje['spodaj-Levo'] == navrsti and polje['spodaj-Sredina'] == navrsti and polje['spodaj-Desno'] == navrsti):
        return True 
    elif(polje['zgoraj-Levo'] == navrsti and polje['sredina-Levo'] == navrsti and polje['spodaj-Levo'] == navrsti):
        return True 
    elif(polje['zgoraj-Sredina'] == navrsti and polje['sredina-Sredina'] == navrsti and polje['spodaj-Sredina'] == navrsti):
        return True 
    elif(polje['zgoraj-Desno'] == navrsti and polje['sredina-Desno'] == navrsti and polje['spodaj-Desno'] == navrsti):
        return True 
    elif(polje['zgoraj-Levo'] == navrsti and polje['sredina-Sredina'] == navrsti and polje['spodaj-Desno'] == navrsti):
        return True 
    elif(polje['zgoraj-Desno'] == navrsti and polje['sredina-Sredina'] == navrsti and polje['spodaj-Levo'] == navrsti):
        return True 
    else:
        return False 

def racunalnik_poteza():
    for i in mogoce_poteze: 
        if polje[i] == ' ': 
            polje[i] = 'O'
            if(preveri_konec('O') == True): 
                return i 
            else: 
                polje[i] = ' '
            
    for i in mogoce_poteze: 
        if polje[i] == ' ':
                                    
            polje[i] = 'X' 
            if(preveri_konec('X') == True): 
                return i 
            else:
                polje[i] = ' '
    
    poteza = random.choice(mogoce_poteze) 
    while(polje[poteza] != ' '): 
           poteza = random.choice(mogoce_poteze)
    return poteza 

def polno_polje(): 
    for i in mogoce_poteze: 
        if polje[i] == ' ': 
            return False 
    return True 

def ponovna_igra(): 
    print('Ponovna igra?(DA / NE)') 
    if(input().lower().startswith('d')): 
       return True 
    else: 
       return False 

def mogoca_poteza(poteza): 
    if poteza in mogoce_poteze: 
        if polje[poteza] == ' ': 
            return True 
    return False 



while True: 
    for v in polje: 
       polje[v] = ' ' 
    print_navodila()
    print('Vnesi 1 za igro proti računalniku')
    print('Vnesi 2 za igro z 2 igralcema')
    izbira = input() 
    if(izbira == '1'): 
        navrsti = 'X' 
        igra = True 
        print_polje() 
        while igra: 
            if(navrsti == 'X'): 
                poteza = input(navrsti + ': ') 
                if(mogoca_poteza(poteza) == False): 
                    print('nepravilna poteza') 
                    continue 
                polje[poteza] = navrsti 
                if(preveri_konec(navrsti)):
                    print_polje() 
                    print('Zmagal je igralec')
                    break 
                else: 
                   if(polno_polje()): 
                       print_polje() 
                       print('Igra je izenačena') 
                       break 
                   else:
                       navrsti = 'O' 
            else: 
                poteza = racunalnik_poteza()
                print('O: ' + poteza)
                polje[poteza] = navrsti 
                print_polje() 
                if(preveri_konec(navrsti)): 
                   print('Zmagal je računalnik')
                   igra = False 
                else:
                   if(polno_polje()): 
                       print_polje() 
                       print('Igra je izenačena')
                       break
                   else: 
                       navrsti = 'X'
        
    elif(izbira == '2'): 
        navrsti = 'X' 
        igra = True
        while(igra): 
            print_polje() 
            print('Na vrsti je ' + navrsti) 
            poteza = input(navrsti + ': ') 
            if(mogoca_poteza(poteza) == False): 
                print('nepravilna poteza')
                continue 
            polje[poteza] = navrsti 
            if(preveri_konec(navrsti)): 
                print_polje()
                print('Zmagal je ' + navrsti) 
                break 
            if(polno_polje()): 
                print('Izenaceno')
                break
            if navrsti == 'X': 
                navrsti = 'O' 
            else:
                navrsti = 'X' 
    else:
        print('neveljavna izbira') 

    if ponovna_igra() == False: 
       break
