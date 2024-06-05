def StartCloudBrowser(scrumTeam, testName):

Logger.CreateLogEntry("Starting","Open_Browser","StartCloudBrowser")

server = ProjectSuite.Variables.BrowserStack
caps = RemoteBrowserConfigs.WindowsBrowsersBrowserStack(scrumTeam, testName)

Browsers.RemoteItem[server, caps[0]].Run(ProjectSuite.Variables.Test_Environment)

sessionId = BS_APIs.GetSessionId(ProjectSuite.Variables.BuildName, scrumTeam + " - " + testName)

Log.Message("Session Id is : " + sessionId)
Logger.CreateLogEntry("Completed","Open_Browser","StartCloudBrowser")
return sessionId