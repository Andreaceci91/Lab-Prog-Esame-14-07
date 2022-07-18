#==============================
#  Classe per file CSV
#==============================

from audioop import add
from lib2to3.pgen2.token import EQUAL
from operator import truediv
from pickle import FALSE, TRUE
from time import time

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

        self.can_read = TRUE
        try:
            file = open('data.csv', 'r')
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

    values = []
    lung = len(time_series)

    prec = 0
    succ = 0

    singolo = FALSE

    #k = 0

    for i in range(lung):

        # Controllo giorni singoli
        print("**********")
        if i != 0:
            prec = (time_series[i-1][0] - (time_series[i-1][0] % 86400))
            #print("i:",i, "prec:", prec)

        attu = (time_series[i][0] - (time_series[i][0] % 86400))
        #print("i:",i,"attu:", attu,"time:",time_series[i][0])

        if i != lung-1:
            succ = (time_series[i+1][0] - (time_series[i+1][0] % 86400))
            #print("i:",i, "succ:", succ)

        temp = 0

        if i == 0 and attu != succ:
            print("singolo")
            temp = None
            singolo = TRUE

        if i != 0 and prec != attu and attu != succ:
            print("singolo")
            temp = None
            singolo = TRUE

        if singolo == FALSE:

            j = i

            while (j < lung-1 and ((time_series[j][0] - (time_series[j][0] % 86400)) == attu)):
                if abs(time_series[i][1] - time_series[j][1]) > temp:
                    temp = abs(time_series[i][1] - time_series[j][1])
                j+=1
    
        values.append(temp)

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

for item in results:
    print(item)

print("Cambiamenti rievati:",len(results))

