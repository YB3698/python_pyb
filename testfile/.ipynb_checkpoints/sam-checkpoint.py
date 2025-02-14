import requests as req
import sys
url = "https://finance.naver.com/sise/sise_market_sum.naver"
web = req.get(url)
html = web.text

# 인자 받기
args = sys.argv
print(args[1])

# 출력함수 만들기
def sam(jong):
    f2 = html.find('<td class="number">')
print(f'{jong} :'+html[f2:f2+25].replace('<td class="number">',''))

if __name__ == '__main__':
    print(sam())