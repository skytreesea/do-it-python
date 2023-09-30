import requests 
from bs4 import BeautifulSoup
api_key = "7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D"  # 발급받은 API 키로 변경해야 합니다.
 

base_url = f"http://apis.data.go.kr/9760000/WinnerInfoInqireService2/getWinnerInfoInqire?sgId=20170509&sgTypecode=1&sdName=전국&sggName=대한민국&pageNo=1&numOfRows=10&resultType=xml&serviceKey=" + api_key 
    
url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade'
params ={'serviceKey' : '서비스키', 'LAWD_CD' : '11110', 'DEAL_YMD' : '201512' }

response = requests.get(url, params=params)
print(response.content)