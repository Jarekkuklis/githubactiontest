function Test1()
{
  Sys.Browser("chrome").Page("https://www.google.com/search*").Panel("main").Panel("cnt").Panel("rcnt").Click()
}