import csv

date = []

def demo_row(row):
  EMP_ID = line[0]
  EMP_NAME = int(line[1])
  Experience = line[2]
  
  return [

         EMP_ID,

         EMP_NAME,

         Experience,

        None,

         ]

#Read CSV File

with open('team.csv','rb') as f:
     reader = csv.reader(f)
     header = reader.next()
     for line in reader:
        if not line: continue 
        data.append(demo_row(line))

#write CSV file

with open('output.csv','w') as f:
     writer = csv.writer(f, delimiter=',')
     writer.writerow([
     'EMP_ID',
     'EMP_NAME',
     'Experience',
     None,

])

#write our data to the file 
writer.writerows(data)

