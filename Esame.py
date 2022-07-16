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
            my_file = open(self.name, 'r')

            for line in my_file:
                
                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')
                
                # Posso anche pulire il carattere di newline 
                # dall'ultimo elemento con la funzione strip():
                elements[-1] = elements[-1].strip()
                
                # p.s. in realta' strip() toglie anche gli spazi
                # bianchi all'inizio e alla fine di una stringa.
    
                # Se NON sto processando l'intestazione...
                if elements[0] != 'epoch':
                    
                    # Aggiungo alla lista gli elementi di questa linea
                    data.append(elements)
            
            # Chiudo il file
            my_file.close()

            return(data)

#def compute_daily_max_difference(values):
    
    #for line in values[1:len(values)]:


time_series_file = CSVTimeSeriesFile(name='data.csv')

time_series = time_series_file.get_data()

print('********************************')

#compute_daily_max_difference(time_series)


time_series[1]

#print(x[0] - (x[0] % 86400))