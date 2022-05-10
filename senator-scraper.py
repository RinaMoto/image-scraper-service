import time
from bing_image_urls import bing_image_urls
import re
import time

def image_scraper():
    while True:
        time.sleep(1.0)
        f = open("./senator.txt", "r")
        keywords = [keyword.strip() for keyword in f.readlines()]
        f.close()

        if keywords != [] and not ('url' in keywords[0]):
            urls = []
            print(keywords)
            valid = False
            for key in keywords:
                if re.search('[a-zA-Z]', key):
                    url = bing_image_urls(key + " wikipedia", limit=1)[0]
                    urls.append({"keyword": key, "url": url})
                    valid = True
                else:
                    print("invalid keyword")
            
            if valid == True:
                with open("./senator.txt", "w") as fr:
                    fr.write("{}".format(urls))
                    fr.flush()
                    fr.close()
                    print("added urls")
                    time.sleep(5)
            else:
                print("no valid keywords")
        else:
            print("waiting on keywords")

if __name__ == '__main__':
    image_scraper()