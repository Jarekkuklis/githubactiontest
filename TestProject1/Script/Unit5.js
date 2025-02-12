// Testing URL: https://www.w3schools.com/html/default.asp

Options.Run.ObjectSearchStrategy = "Breadth-first";

function test1()
{
    var link = Sys.Browser("chrome").Page("https://www.w3schools.com/html/default.asp").Panel("belowtopnav").Panel(0).Panel("main").Panel(3).Panel(14).Link(0);
    Sys.HighlightObject(link);
}

function test2()
{
    var link = Sys.Browser("chrome").Find("FullName", "*.Page(\"https://www.w3schools.com/html/default.asp\").Panel(\"belowtopnav\").Panel(0).Panel(\"main\").Panel(3).Panel(14).Link(0)", 8);
    Sys.HighlightObject(link);   
}

function test3()
{
    var page = Sys.Browser("chrome").Page("*");
    var link = page.Find("FullName", "*.Panel(\"belowtopnav\").Panel(0).Panel(\"main\").Panel(3).Panel(14).Link(0)", 6);
    Sys.HighlightObject(link);
}

function test4()
{
    var page = Sys.Browser("chrome").Page("https://www.w3schools.com/html/default.asp");
    var link = page.Find("FullName", "*.Panel(\"belowtopnav\").Panel(0).Panel(\"main\").Panel(3).Panel(14).Link(0)", 6);
    Sys.HighlightObject(link);
}

function test5()
{
    var page = Sys.Browser("chrome").Page("https://www.w3schools.com/html/default.asp");
    var nav = page.Find("FullName", "*.Panel(\"belowtopnav\")", 1);
    var link = nav.Find("FullName", "*.Panel(0).Panel(\"main\").Panel(3).Panel(14).Link(0)", 5);
    Sys.HighlightObject(link);
}

function test6()
{
    var page = Sys.Browser("chrome").Page("https://www.w3schools.com/html/default.asp");
    var nav = page.Find("Name", "Panel(\"belowtopnav\")", 1);
    var panel = nav.Find("Name", "Panel(14)", 4);
    var link = panel.Find("Name", "Link(0)", 1);
    Sys.HighlightObject(link);
}

function test7()
{
    var page = Sys.Browser("chrome").Page("*");
    var nav = page.Find("FullName", "*.Panel(\"belowtopnav\")", 1);
    var link = nav.Find("FullName", "*.Panel(0).Panel(\"main\").Panel(3).Panel(14).Link(0)", 5);
    Sys.HighlightObject(link);
}

function test8()
{
    var page = Sys.Browser("chrome").Page("https://www.w3schools.com/html/default.asp");
    var nav = page.Find("Name", "Panel(\"belowtopnav\")", 1);
    var panel = nav.FindChild("Name", "Panel(14)", 3);
    var link = panel.FindChild("Name", "Link(0)", 1);
    Sys.HighlightObject(link);
}

function test9()
{
    var page = Sys.Browser("chrome").Page("*");
    var nav = page.Find("Name", "Panel(\"belowtopnav\")", 1);
    var panel = nav.FindChild("Name", "Panel(14)", 3);
    var link = panel.FindChild("Name", "Link(0)", 1);
    Sys.HighlightObject(link);
}