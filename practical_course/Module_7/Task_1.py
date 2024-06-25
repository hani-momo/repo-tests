import requests
from bs4 import BeautifulSoup

# get exchange rate from the website at different points in time
url = 'https://myfin.by/currency/cb-rf/cny'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser') # parser
    datatable = soup.find('table')

    if datatable is not None:
        rows = datatable.find_all('tr')  # rows in html table 

        for row in rows:
            cells = row.find_all('td') # cells in this html row
            if len(cells) >= 2: # checking amount of data (at least date and exchange rate)
                date = cells[0].text
                exrate = cells[1].text
                print(f'On {date} yuan exchange rate was {exrate}₽ for 1元')
            
            '''else:
                print('Not enough data to collect')  '''  
    else:
        print('No table with data found')
else:
    print(response.status_code)
