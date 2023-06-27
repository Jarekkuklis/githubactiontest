"""@calculator
def Test8():
    #Clicks the 'TrayButton' object.
    Aliases.explorer.wndShell_SecondaryTrayWnd.TrayButton.Click(21, 18)
    #Enters 'ca' in the 'wndSearch' object.
    Aliases.CortanaUI.wndSearch.Keys("ca")
    #Enters 'l' in the 'Search_box' object.
    Aliases.CortanaUI.wndSearch.Search_box.Keys("l")
    #Clicks the 'panelApp' object.
    Aliases.CortanaUI.pageBing.panelApp.Click(83, 8)
    #Clicks the 'Five' object.
    Aliases.Microsoft_WindowsCalculator.Calculator.NavView.LandmarkTarget.Number_pad.Five.Click()
    #Closes the 'wndCalculator' window.
    Aliases.ApplicationFrameHost.wndCalculator.Close()"""

@given("The tested app is running")
def step_impl():
    #Clicks the 'TrayButton' object.
    Aliases.explorer.wndShell_SecondaryTrayWnd.TrayButton.Click(21, 18)
    #Enters 'ca' in the 'wndSearch' object.
    Aliases.CortanaUI.wndSearch.Keys("ca")
    #Enters 'l' in the 'Search_box' object.
    Aliases.CortanaUI.wndSearch.Search_box.Keys("l")
    #Clicks the 'panelApp' object.
    Aliases.CortanaUI.pageBing.panelApp.Click(83, 8)
    #Clicks the 'Five' object.
    Aliases.Microsoft_WindowsCalculator.Calculator.NavView.LandmarkTarget.Number_pad.Five.Click()
    #Closes the 'wndCalculator' window.
    Aliases.ApplicationFrameHost.wndCalculator.Close()

