@echo off
set TEST_EXECUTE_ACCESS_KEY=b12f4231-34da-4ccd-9be8-25b2b17ba825
set PROJECT="C:\Users\jaroslaw.kuklis\Documents\TestComplete 15 Projects\TestProject1\TestProject1.pjs"
"C:\Program Files (x86)\SmartBear\TestExecute 15\Bin\TestExecute.exe" /run /project:"%PROJECT%" /accesskey:"%TEST_EXECUTE_ACCESS_KEY%"
