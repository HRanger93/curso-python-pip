import csv

def read_csv(path):
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    print(type(reader))

    #array para las llaves.
    header = next(reader)
    #print(header)
    data = []
    for row in reader: 
      iterable = zip(header,row)
      country_dict = {key:value for key,value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data =read_csv('./App/data.csv')
  print(data[0])

#Transformando lo siguiente en un array de diccionario...
#[
#  {
#    'Country':'Colombia',
#    'Capital': 'Bogota'
#    '2022 Population': 3000,
#    'World Population Percentage': 0.12
#  }
#]
