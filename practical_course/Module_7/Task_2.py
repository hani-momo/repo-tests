import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as graph

# get exchange rate from the website at different points in time
url = 'https://myfin.by/currency/cb-rf/cny'
response = requests.get(url)

dates = [] # for future graph
rates = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser') # parser
    datatable = soup.find('table')

    if datatable is not None:
        rows = datatable.find_all('tr')  # rows in html table 

        for row in rows:
            cells = row.find_all('td') # cells in this html row
            if len(cells) >= 2: # checking amount of data (at least date and exchange rate)
                date = cells[0].text
                exchange_rate = cells[1].text
                print(f'On {date} yuan exchange rate was {exchange_rate}₽ for 1元')

                dates.append(date)
                rates.append(exchange_rate)
            
            '''else:
                print('Not enough data to collect')  '''  
    else:
        print('No table with data found')
else:
    print(response.status_code)


graph.figure(figsize=(14, 7))  # size in inch
graph.plot(dates, rates, marker='.', linestyle='-', color='r')

graph.title('Yuan exchange rate')
graph.xlabel('Date')  
graph.ylabel('Yuan')
graph.grid(True)  # cell

graph.savefig('yuan_test.png')  # save as png
graph.show()
