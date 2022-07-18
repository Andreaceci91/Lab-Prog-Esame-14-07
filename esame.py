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

def compute_daily_max_difference(time_series):
    values = []
    lung = len(time_series)

    for i in range(lung):

        trovato = FALSE
        temp = 0

        if(i != lung-1):

            j = i

            if(i != 0):
                prec = (time_series[i-1][0] - (time_series[i-1][0] % 86400))

            att = time_series[i][0] - (time_series[i][0] % 86400)
            succ = (time_series[i+1][0] - (time_series[i+1][0] % 86400))

            if(i == 0 and att != succ):
                #print(att ,"vs", succ)
                trovato = TRUE
                temp = None

            if(i != 0 and att != succ and prec != att):
                #print(prec, att, succ)
                trovato = TRUE
                temp = None
            else:
                #print(att, succ)
                while(j != lung-1 and ( (time_series[j][0] - (time_series[j][0] % 86400)) == (time_series[j+1][0] - (time_series[j+1][0] % 86400)))):
                    #print(j, "vs", j+1)
                    if abs(time_series[j][1] - time_series[j+1][1]) > temp:
                        temp = abs(time_series[j][1] - time_series[j+1][1])
                        trovato = TRUE
 
                    j = j + 1
        
            if trovato == TRUE:
                #print(temp)
                values.append(temp)
                trovato = FALSE

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

print("Cambiamenti rievati:",len(results))

for item in results:
    print(item)

