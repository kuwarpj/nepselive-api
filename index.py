
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def main():
    import requests

    from bs4 import BeautifulSoup
    import pandas as pd
    import json
    
    url = 'https://www.sharesansar.com/live-trading'
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    table = soup.find('table', class_="table")

    table_heading = [heading.text for heading in table.find_all('th')]
    table_data = [j for j in table.find_all('tr')]

    results = [{table_heading[index]:cell.text.strip() for index, cell in enumerate(
        row.find_all('td'))} for row in table_data]
    
  

    df = pd.DataFrame(results)
    df.rename(columns={'S.No': 'S_no', 'Symbol': 'symbol', 'LTP': 'ltp', 'Point Change': 'point_change', '% Change': 'change_per',
              'Open': 'open_price', 'High': 'high_price', 'Low': 'low_price', 'Volume': 'volume', 'Prev. Close': 'prev_close'}, inplace=True)

    jsn = json.loads(df.to_json(orient='records'))
    return jsonify(jsn)



if __name__ == '__main__':
    app.run(debug=True)
