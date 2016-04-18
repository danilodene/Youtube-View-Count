import time
import lcddriver
import threading
import json
import requests

lcd = lcddriver.lcd()

channelId = "put_your_channel_id"
apiKey = "put_your_api_key"

subscriberCount = 0
viewCount = 0


def checkSubscribers():
    global subscriberCount
    global viewCount
    # ############################################### ws
    url = ("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channelId + "&key=" + apiKey)
    print (url)
    headers = {'content-type': 'text/plain'}
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        print("Failed to connect to server " + str(response.status_code))
    else:
        returnObj = json.loads(response.content)
        # print("Result >>>> " + str(returnObj))
        print("OK "),

        subscriberCount = str(returnObj['items'][0]['statistics']['subscriberCount'])
        viewCount = str(returnObj['items'][0]['statistics']['viewCount'])

    threading.Timer(60.0, checkSubscribers).start()


if __name__ == "__main__":
    checkSubscribers()
    while True:
        lcd.lcd_display_string("SubscriberCount", 1)
        lcd.lcd_display_string("" + subscriberCount + "   ", 2)
        time.sleep(3)
        lcd.lcd_display_string("View Count", 1)
        lcd.lcd_display_string("" + viewCount + "   ", 2)
        time.sleep(3)




