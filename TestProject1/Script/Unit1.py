
def Connect_Android_Appium():
  server = "http://localhost:4723/wd/hub"
  capabilities = {
    "deviceName": "Pixel_3a_API_33_x86_64",
    "platformVersion": "13",
    "platformName": "android",
    "automationName": "UIAutomator2",
    "app": "C:\\Users\\jaroslaw.kuklis\\Downloads\\tvc.apk"
  }

  Mobile.ConnectDevice(server, capabilities)
  
  

