import requests
import json
url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=P8BCEwczI7rfxdaAnhmW8Cwkom2XBoEb&data=AP01'
res = requests.get(url).text
data = json.loads(res)
print(type(data))
result = data[-1]['deal_bas_r']
# print(result,type(result))
#result2 = result.replace(",","").replace(".","")
print('='*40)
print(f'오늘의 환율은 1달러에 {result}원 입니다.')
print('='*40)
# print(result2,type(result2))
# exc = int(result2)/10