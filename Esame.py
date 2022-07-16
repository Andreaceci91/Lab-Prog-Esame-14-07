#==============================
#  Classe per file CSV
#==============================

from pickle import FALSE, TRUE

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
            if not self.can_read:
                
                print('Errore, file non aperto o illeggibile')
                return None 
            else:

                file = open('data.csv', 'r')

                values = []

                for line in file:
                    line = line.strip()
                    values.append(line)
        
                for line in values:
                    print(line)

                return(values)

time_series_file = CSVTimeSeriesFile(name='data.csv')

time_series = time_series_file.get_data()

print(time_series[1])