import time
from plyer import notification   # pip install plyer


for i in range(5):
    print("Drink some water!")
    notification.notify(title="Please drink some water",
        message="you need to drink water")
    time.sleep(5)