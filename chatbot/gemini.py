# 구글 제미나이 AI
from google import genai
def aiai(text):
    client = genai.Client(api_key="AIzaSyBR_dnrtYqshdDSub10WR56QCkY6DxPsB8")
    response = client.models.generate_content(model="gemini-2.0-flash",contents=text + ";짱구처럼 말해줘")
    answer = response.text
    print(answer)
    return answer


if __name__=="__main__":
    aiai("gpt에 대해 설명해")