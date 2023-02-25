Set oShell = Wscript.CreateObject("WScript.Shell")
CommandLine = "%COMSPEC% /c C:\Users\a.kalinkin\Desktop\MailTemplate\venv\Scripts\python.exe C:\Users\a.kalinkin\Desktop\MailTemplate\manage.py runserver 192.168.123.19:8080"
oShell.Run CommandLine, 0, 0