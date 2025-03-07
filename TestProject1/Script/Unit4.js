const BrowsersName = [ "chrome", "edge", "firefox", "iexplore"];

function TestWaitBrowser()
{
  Options.Run.Timeout = 100
  Sys.WaitBrowser("edge",100)
//  for (let BrowserName of BrowsersName)
//  {
//    // Why the timeout setted to 0 is not applied according to your documentation?
//    // https://support.smartbear.com/testcomplete/docs/reference/test-objects/members/sys/waitbrowser-method-sys-object.html?sbsearch=WaitBrowser
//    let oBrowser = Sys.WaitBrowser(BrowserName, 0);
//    if (oBrowser.Exists)
//      oBrowser.Close();
//  }
}

Given("some precondition", function (){
  throw new NotImplementedError();
});

When("an action is performed", function (){
  throw new NotImplementedError();
});

Then("validate a condition", function (){
  throw new NotImplementedError();
});
