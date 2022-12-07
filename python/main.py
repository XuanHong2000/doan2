import time
from firebase import firebase

firebase = firebase.FirebaseApplication("https://do-an-2-ute-default-rtdb.firebaseio.com/", None)
path = ["BED_ROOM/nhiet_do", "BED_ROOM/do_am", "BED_ROOM/khi_ga", "BED_ROOM/cb_as", "BED_ROOM/ti_vi", "BED_ROOM/may_lanh", "BED_ROOM/den"]

while (true):
        data = firebase.get('BED_ROOM/data', None).split('-')
        
        if (data[4] != str(firebase.get(path[3], None))):
                firebase.put("/", path[3], int(data[4]))
        if (data[5] != str(firebase.get(path[4], None))):
                firebase.put("/", path[3], int(data[5]))
        if (data[6] != str(firebase.get(path[5], None))):
                firebase.put("/", path[3], int(data[6]))
        if (data[7] != str(firebase.get(path[6], None))):
                firebase.put("/", path[3], int(data[7]))

        for i in range(3):
                firebase.put("/", path[i], int(data[i + 1]))

        time.sleep(2)
