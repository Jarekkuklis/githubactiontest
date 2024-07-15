
def Connect_Android_Appium():
  server = "http://localhost:4723/wd/hub"
  capabilities = {
    "deviceName": "Pixel_3a_API_33_x86_64",
    "platformVersion": "13",
    "platformName": "android",
    "automationName": "UIAutomator2",
<<<<<<< HEAD
    "app": "C:\\Users\\jaroslaw.kuklis\\Downloads\\tvc.apk"
=======
    "app": "C:\\Users\\Public\Documents\\TestComplete 15 Samples\\Mobile\\Android\\Orders\\Orders Application\\bin\\Orders.apk"
>>>>>>> 3a1af7d13643f5246ee4f71cd688107ff8f4b028
  }

  Mobile.ConnectDevice(server, capabilities)
  
  

<<<<<<< HEAD
=======
##def Test1():
#    #Mobile.ConnectDevice("https://appium-us.bitbar.com/wd/hub/", '{\"platformName\":\"ANDROID\",\"bitbar_target\":\"android\",\"bitbar_findDevice\":false,\"bitbar_device\":\"Samsung Galaxy S22 SM-S901U1 -US\",\"deviceName\":\"Samsung Galaxy S22 SM-S901U1 -US\",\"automationName\":\"UiAutomator2\",\"bitbar_app\":\"176886747\"}', 600)
#    
#
#def Test1():
#  capabilities = {
#    "automationName": "UIAutomator2", 
#    "deviceName": "Pixel_3a_API_33_x86_64", 
#    "platformName": "android", 
#    "platformVersion": "13"
#  }
#  server = "http://localhost:4723/wd/hub"
#  Mobile.ConnectDevice(server, capabilities, 180)
#  Aliases.Device.processGoogleAndroidAppsNexuslauncher.recyclerViewAppsListView.textViewIcon.Touch()
>>>>>>> 3a1af7d13643f5246ee4f71cd688107ff8f4b028
