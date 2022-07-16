# Import CSV file and extract the values from file
file = open('data.csv', 'r')

values = []

for line  in file:

    values.append(line)

time = []
value = []

# Check if the CSV file has a str header

if values[0].split(',')[0] == 'epoch':
    for line in values[1:len(values)]:
        x = line.split(',')
        time.append(x[0])
        value.append(x[1])
else:
        for line in values:
            x = line.split(',')
            time.append(x[0])
            value.append(x[1])

file.close() 

print(time[0])







