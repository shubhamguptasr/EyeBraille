import pyinotify
wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm)
wm.add_watch('./Text_File.txt',pyinotify.ALL_EVENTS)
notifier.loop()
