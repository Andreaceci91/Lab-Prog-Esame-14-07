
# Import the libraries
from audioop import add
from lib2to3.pgen2.token import EQUAL
from operator import truediv
from pickle import FALSE, TRUE
from time import time

# Create the class ExamExeption
class ExamException(Exception):
    pass

# Create Class CSVTimeSeriesFile
class CSVTimeSeriesFile:

    # Use magic method __ini__ to initialize the attribute of class
    def __init__(self, name):
        self.name = name

        # Try to open the file
        try:
            file = open(name, 'r')
            file.readline()
        
        # If i can't open the file, I raise an exception 
        except:
            raise ExamException('Impossibile aprire il file')
            #print('Errore in apertura del file: "{}"'.format(error))
    
# Create a function get_data
    def get_data(self):  
            
            #Create a empty list
            data = []
    
            # Open the file
            file = open(self.name, 'r')


            for line in file:
                
                # Split the element on "," that separates the value
                elements = line.split(',')
                
                # Remove the newline character and black space
                elements[-1] = elements[-1].strip()
                
                #If the element in first position is different by epoch i will add at the list
                if elements[0] != 'epoch':
                    
                    data.append(elements)
            
            # Close the file
            file.close()

            # Raise an exception if the file is empty
            if len(data) == 0:
                raise ExamException('Il file non ha valori al suo interno')

            # Try to convert data else raise an exception
            for i in range(len(data)):
                try:
                    data[i][0] = int(data[i][0])
                    data[i][1] = float(data[i][1])
                except:
                    raise ExamException("Errore nella conversione dei dati")

            # Check if epoch are sorted correctly
            for i in range(len(data)-1):
                j = i+1    
                while j != len(data):
                    
                    if data[i][0] >= data[j][0]:
                        raise ExamException("Epoch non ordinati correttamente")
                        None

                    j += 1
                    
            # If all the check are ok, return data
            return(data)

# Create function to control the difference of values of temperature
def compute_daily_max_difference(time_series):

    # Declare variables
    values = []
    lung = len(time_series)

    prec = 0
    succ = 0

    singolo = FALSE

    i = 0
    j = 0

    # Create a cycle in which I slide the elements in the list
    while i < lung:
        
        # Use a variable to check if there are a single measure
        singolo = FALSE

        temp = 0

        # Calculate the value before if the i is different by 0
        if i != 0:
            prec = (time_series[i-1][0] - (time_series[i-1][0] % 86400))

        # Calculate the current value
        attu = (time_series[i][0] - (time_series[i][0] % 86400))

        # Calculate the next value
        if i != lung-1:
            succ = (time_series[i+1][0] - (time_series[i+1][0] % 86400))

        if attu != succ and i == 0:
            temp = None
            singolo = TRUE

        if prec != attu and attu != succ and i != 0:
            temp = None
            singolo = TRUE

        if prec != attu and i == lung-1 :
            temp = None
            singolo = TRUE
            
        if singolo == FALSE:
            j = i

            # Create a Cycle to check the difference of Temperature in the Liste
            while (j < lung and ((time_series[j][0] - (time_series[j][0] % 86400)) == attu)):
                if abs(time_series[i][1] - time_series[j][1]) > temp:
                    temp = abs(time_series[i][1] - time_series[j][1])
                j+=1

            i = j-1

        i += 1

        # Attach temp at the list
        values.append(temp)

    # Return list of values
    return(values)

#==============================
#  Corpo del programma
#==============================

time_series_file = CSVTimeSeriesFile(name='data_2.csv')

# Use function Getdata and save value in Time_series
time_series = time_series_file.get_data()

# Invoce function below to calculare difference of temperature
results = compute_daily_max_difference(time_series)

#print("\n***  Lista  ***")
#for item in results:
#    print(item)
#    None

#print("Cambiamenti rievati:",len(results))

