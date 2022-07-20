
from audioop import add
from lib2to3.pgen2.token import EQUAL
from operator import truediv
from pickle import FALSE, TRUE
from time import time

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

        self.can_read = TRUE
        try:
            file = open(name, 'r')
            file.readline()
        except Exception as error:
            self.can_read = FALSE
            print('Errore in apertura del file: "{}"'.format(error))
    
    def get_data(self):  
            
            data = []
    
            # Apro il file
            file = open(self.name, 'r')

            for line in file:
                
                elements = line.split(',')
                
                elements[-1] = elements[-1].strip()
                
                if elements[0] != 'epoch':
                    
                    data.append(elements)
            
            file.close()

            return(data)
# (time_series[i][0] - (time_series[j][0] % 86400))

def compute_daily_max_difference(time_series):

    # Dichiariazione variabili
    values = []
    lung = len(time_series)

    prec = 0
    succ = 0

    singolo = FALSE

    i = 0
    j = 0

    print("i prima del while:",i)


    while i < lung:
        print("**********")
        
        print("i:",i)
        
        singolo = FALSE
        print("- singolo:",singolo)

        temp = 0
        print("temp",temp)

        if i != 0:
            prec = (time_series[i-1][0] - (time_series[i-1][0] % 86400))
            print("prec",time_series[i-1][0])
            print("prec pulito",prec)

        attu = (time_series[i][0] - (time_series[i][0] % 86400))
        print("attu",time_series[i][0])
        print("attu pulito",attu)

        print(i)
        #print("-- Prova:", time_series[54][0])
        if i != lung-1:
            succ = (time_series[i+1][0] - (time_series[i+1][0] % 86400))
            print("succ",time_series[i+1][0])
            print("succ pulito",succ)

        #print("prec:",prec, "attu:",attu, "succ:",succ)

        if attu != succ: 
            print("attu maggiore di succ")

        # Controllo giorni singoli
        #if i == 0 and attu != succ:
        #    print("singolo")
        #    temp = None
        #    singolo = TRUE
        #    j += 1

        if attu != succ and i == 0:
            print("Singolo: attu != succ and i == 0")
            temp = None
            singolo = TRUE

        if prec != attu and attu != succ and i != 0:
            print("Singolo: prec != attu and attu != succ and i != 0")
            temp = None
            singolo = TRUE
            #j += 1

        if prec != attu and i == lung-1 :
            print("Singolo: prec != attu and attu != succ and i != 0")
            temp = None
            singolo = TRUE
            
        # Ciclo giorni non singoli
        if singolo == FALSE:
            print("Sono in: IF singolo == FALSE")
            j = i

            while (j < lung and ((time_series[j][0] - (time_series[j][0] % 86400)) == attu)):
                if abs(time_series[i][1] - time_series[j][1]) > temp:
                    temp = abs(time_series[i][1] - time_series[j][1])
                j+=1
            #print("-i:",i,"time:", time_series[i][0])
            #print("-j:",j,"time:", time_series[j][0])
            i = j-1
            #i += 1
        #print("Esco")

        
        i += 1
        print("i+=1:", i)
        print("temp in append",temp)
        values.append(temp)

        print("\nlung", lung)

    return(values)

#==============================
#  Corpo del programma
#==============================

time_series_file = CSVTimeSeriesFile(name='data.csv')

time_series = time_series_file.get_data()

print('********************************')

for i in range(len(time_series)):
    time_series[i][0] = int(time_series[i][0])
    time_series[i][1] = float(time_series[i][1])

#compute_daily_max_difference(time_series)
results = compute_daily_max_difference(time_series)

print("\n*** Lista ***")
for item in results:
    print(item)
    None

print("Cambiamenti rievati:",len(results))

