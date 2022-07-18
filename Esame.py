#==============================
#  Classe per file CSV
#==============================

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
    
    values  = []
    

    for i in range(len(time_series)):
        temp = 0
        j = i
        while (time_series[i][0] - (time_series[j][0] % 86400)) == time_series[i][0]:
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

#print(time_series[25][0])
#print((time_series[25][0] % 86400))
#day_start_epoch = time_series[25][0] - (time_series[25][0] % 86400)
#print(day_start_epoch)

#compute_daily_max_difference(time_series)

x = time_series[1][0] - time_series[1][0] % 86400


print(time_series[0][0])
print(time_series[1][0] - time_series[1][0] % 86400)
if time_series[0][0] == x:
    print("Uguali")

#day_start_epoch = epoch - (epoch % 86400)
