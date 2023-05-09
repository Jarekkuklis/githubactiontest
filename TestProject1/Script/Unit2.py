def Main_RunMobileTests_Parallel():
  
   capabilities = [
    {
      "automationName": "XCUITest",
      "bitbar_device": "Apple iPhone 12 A2403 14.3",
      "bitbar_findDevice": "false",
      "bitbar_target": "ios",
      "deviceName": "Apple iPhone 12 A2403 14.3",
      "newCommandTimeout": "3600",
      "platformName": "iOS"
    },

    {
      "automationName": "XCUITest",
      "bitbar_device": "Apple iPhone 13 Pro A2638 15.2",
      "bitbar_findDevice": "false",
      "bitbar_target": "ios",
      "deviceName": "Apple iPhone 13 Pro A2638 15.2",
      "newCommandTimeout": "3600",
      "platformName": "iOS"
    }
   ]
   
   server = "https://appium.bitbar.com/wd/hub/"
   tests = ['Script|Unit2|MyTest1', 'Script|Unit2|MyTest2']
   Parallel.RunMobileTests(tests, capabilities, server)
   
def MyTest1():
  Log.Message("it is test1")

def MyTest2():
  Log.Message("it is test2")
