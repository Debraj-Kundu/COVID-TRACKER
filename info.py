import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

source = requests.get('https://www.worldometers.info/coronavirus/country/india/#:~:text=India%20Coronavirus%3A%204%2C566%2C726%20Cases%20and%2076%2C336%20Deaths%20%2D%20Worldometer').text

soup = BeautifulSoup(source, 'lxml')
cases = soup.find('div', class_='maincounter-number').text.strip()
death_lst = soup.find('div', class_='col-md-8')
div_death = death_lst.find_all('div', id='maincounter-wrap')[1]
deaths = div_death.span.text.strip()
div_reco = death_lst.find_all('div', id='maincounter-wrap')[2]
recovered = div_reco.span.text.strip()
toaster = ToastNotifier()
toaster.show_toast('COVID INFO', f'Cases: {cases}, Deaths: {deaths}\n Recovered: {recovered}',duration=100)



