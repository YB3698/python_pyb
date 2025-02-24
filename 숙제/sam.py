import requests as req
    url = "https://finance.naver.com/sise/sise_market_sum.naver"
    web = req.get(url)
    html = web.text
def sam(jong = '삼성전자'):
    f2 = html.find('<td class="number">')
print(f'{jong} :'+html[f2:f2+25].replace('<td class="number">',''))

if __name__ == '__main__':
    print(sam())