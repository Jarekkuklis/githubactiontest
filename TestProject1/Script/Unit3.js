function measureExecutionTime() {
    // Start time
    var startTime = aqDateTime.Time();
    
    Options.Run.Timeout = 10000
    Sys.Process("EXCEL").UIAObject("Book1_Excel").Window("EXCEL2", "", 2).UIAObject("Ribbon").UIAObject("Ribbon").Window("NUIPane", "", 1).Window("NetUIHWND", "", 1).MSAAObject("property_page_Ribbon").MSAAObject("pane_Lower_Ribbon").MSAAObject("property_page_Formulas").MSAAObject("tb_Function_Library").MSAAObject("drop_down_button_Math_Trig").WaitProperty("VisibleOnScreen",true,-1)
  

    // End time
    var endTime = aqDateTime.Time();
    
    // Calculate execution time in seconds
    var executionTime = aqDateTime.TimeInterval(endTime, startTime) / 1000;  // Converts ms to seconds
    Log.Message("Execution Time: " + executionTime.toFixed(2) + " seconds");
}

