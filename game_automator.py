import time
from ppadb.client import Client as AdbClient
from PIL import Image



client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("RZ8W403AZBD")

s_t1 = time.time()

n = 0

for i in range(10):

    s_t = time.time()

    time.sleep(2)

    device.shell("am kill com.edengames.GTSpirit");print("killing gt")
    time.sleep(1)

    device.shell("am start -n com.ghisler.android.TotalCommander/com.ghisler.android.TotalCommander.TotalCommander");print("starting tc")
    time.sleep(1)

    device.shell("input tap 975 301");print("refreshing")
    time.sleep(1)

    device.shell("input swipe 500 413 499 413 500");print("holding")
    time.sleep(0.3)

    device.shell("input tap 489 1472");print("touching delete")
    time.sleep(1)

    device.shell("input tap 681 1425");print("touching yes")
    time.sleep(1)

    device.shell("monkey -p com.edengames.GTSpirit -c android.intent.category.LAUNCHER 1");print("starting gt")
    print("waiting");time.sleep(45)

    device.shell("input tap 1802 336");print("touching renew")
    time.sleep(2)

    device.shell("input tap 2305 965");print("touching back")
    time.sleep(3)

    device.shell("input tap 2305 965");print("touching garage")
    print("waiting");time.sleep(20)

    device.shell("input tap 1435 221");print("touching car")
    time.sleep(2.5)

    device.shell("input tap 1553 305");print("touching ws")
    time.sleep(2.5)

    print("taking screenshot");device.shell("screencap /sdcard/screenshot.png")

    print("pulling screenshot");device.pull("/sdcard/screenshot.png", "screenshot.png")

    image = Image.open("screenshot.png")

    pixel_color = image.getpixel((1943, 603))

    if pixel_color == (93, 229, 87, 255):
        device.shell("input tap 1997 165");
        print("g touching upper")
    else:
        device.shell("input tap 2055 708");
        print("ng touching lower")

    time.sleep(1)
    device.shell("input tap 2116 965");print("touching install")
    time.sleep(6.5)

    device.shell("input tap 1402 175");print("touching ff")
    time.sleep(2)

    device.shell("input tap 2039 66");print("touching achive")
    time.sleep(3)

    device.shell("input tap 1650 367");print("touching golds1")
    time.sleep(1)

    device.shell("input tap 1650 527");print("touching golds2")
    time.sleep(3)

    device.shell("am start -a android.intent.action.MAIN -c android.intent.category.HOME");print("going home")

    n += 1
    print("done", n,"----------------------------------------------------------------------------------------------------------------------------------")

    e_t = time.time()

    elapsed_time = e_t - s_t
    x=0
    for i in range(3):
        if elapsed_time > 60:
            x += 1
            elapsed_time = elapsed_time - 60

        else:
            break

    print('Execution time:', x, 'minutes', elapsed_time, 'seconds')

time.sleep(3)
device.shell("monkey -p com.sec.android.app.clockpackage -c android.intent.category.LAUNCHER 1");print("starting gt")
time.sleep(3)

device.shell("input tap 530 2084");print("touching alarm")

e_t1 = time.time()

elapsed_time1 = e_t1 - s_t1
x=0

elt = elapsed_time1 / 60

for i in range(elt):
    if elapsed_time1 > 60:
        x += 1
        elapsed_time1 = elapsed_time1 - 60

    else:
        break

print('Execution time:', x, 'minutes', elapsed_time1, 'seconds')


