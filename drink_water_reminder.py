from winotify import Notification,audio

a = Notification(app_id= "Drink Water",
                 title= "It's been 2 Hours",
                 msg="Hey Smit! Drink Some Water!",
                 duration="long",
                 icon=r"C:\Users\smit\Desktop\Pyhton\6774894.png")

a.set_audio(audio.LoopingAlarm,loop=True)

a.show()
