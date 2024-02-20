def Sample_Run_Browser():
  Browsers.Item["chrome"].RunOptions = "--disable-web-security --user-data-dir=C:\\Users\\jaroslaw.kuklis\\AppData\\Local\\Google\\Chrome\\User Data\\Default --disable-site-isolation-trials"
  Browsers.Item["chrome"].Run()
