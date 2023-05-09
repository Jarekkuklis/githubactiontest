
def Connect_Android_Appium():
  server = "http://localhost:4723/wd/hub"
  capabilities = {
    "deviceName": "Pixel 6 API 33",
    "platformVersion": "13",
    "platformName": "android",
    "automationName": "UIAutomator2",
    "app": "C:\\Users\\jaroslaw.kuklis\\Downloads\\tvc.apk"
  }

  Mobile.ConnectDevice(server, capabilities)
  
  


def mobile():
  Log.Message("test")
    #Compares the viewGroupNavigationLayout Stores item with the image of the Regions.CreateRegionInfo(Aliases.Device.processStreitdatentechnikSDTMonteurPlus.viewGroupNavigationLayout, 131, 20, 1842, 791, False) object.
    #Regions.viewGroupNavigationLayout.Check(Regions.CreateRegionInfo(Aliases.Device.processStreitdatentechnikSDTMonteurPlus.viewGroupNavigationLayout, 131, 20, 1842, 791, False))