REM Clears the screen
CLS
@ECHO OFF

REM Launches TestExecute
REM executes the specified project
REM and closes TestExecute when the run is over
"C:\Program Files (x86)\SmartBear\TestExecute 15\Bin\TestExecute.exe" "C:\Users\dipanshu.raj\Documents\TestComplete 15 Projects\WebTestingTC\WebTestingTC.pjs" /r /e /AccessKey:3948bf6a-97eb-40f5-952f-be289451c8df /SilentMode /Timeout:1200 /ns /ErrorLog:%cd%\logs\error.log /ExportLog:%cd%\logs\runlog.html /ExportSummary:%cd%\logs\runlog.xml
:OkEnd
