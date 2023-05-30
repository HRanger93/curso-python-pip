import utils as u
import read_csv
import chart




def run():
  data = read_csv.read_csv('./data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  chart.generate_pie_chart(countries, percentages)
  
  
  country = input('Type country = ')
  print(country)

  result=u.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = u.get_population(country)
    chart.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()

