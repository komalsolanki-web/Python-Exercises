def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)
    
def speak2(intro):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(intro)
    
if __name__ == "__main__":
    import requests
    import json
    import time
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=in&category=health&'
           'apiKey=ba4e36d81b7649359e90cadf204b4bc4')
    
    news = requests.get(url)
    text = news.text
    js = json.loads(text)
    intro = "Todays breaking news are"
    print("Now you are listing news by our news anchors")
    speak2(intro)
    time.sleep(1)
    for i in range(1, 11):
        speak(js['articles'][i]['title'])