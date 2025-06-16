@echo off
set TEST_EXECUTE_ACCESS_KEY=%1
set PROJECT=%2
"C:\Program Files (x86)\SmartBear\TestExecute 15\Bin\TestExecute.exe" /run /project:"%PROJECT%" /accesskey:"%TEST_EXECUTE_ACCESS_KEY%"

