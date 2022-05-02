import time
import json
from serpapi import GoogleSearch
import validators 
import os
from dotenv import load_dotenv
load_dotenv()  

def senator_scrape():
    API_KEY = os.environ.get('API')

    while True:
        time.sleep(1.0)
        f = open("./senator.txt", "r")
        line = f.read()
        f.close()

        if line != "" and not validators.url(f"{line}"):
            params = {
                "q": f"{line}",
                "tbm": "isch",
                "start": 0,
                "engine": "google",
                "num": 1,
                "api_key": API_KEY
            }
            try:
                search = GoogleSearch(params)
                results = search.get_dict()
                image_link = json.dumps(results['images_results'][0]["original"], indent=2, ensure_ascii=False)
                with open("./senator.txt", "w") as fr:
                    fr.truncate()
                    fr.write("{}".format(eval(image_link)))
                    fr.flush()
                    time.sleep(5)
                
            except:
                print("request failed")
        else:
            print("waiting on new input")
            continue 

if __name__ == '__main__':
    senator_scrape()