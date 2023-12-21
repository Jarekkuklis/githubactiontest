def getTime():
  BuiltIn.SendMail("jaroslaw.kuklis@smartbear.com", "jaroslaw.kuklis@smartbear.com", "", "jaroslaw.kuklis@smartbear.com", "KeywordTestLog", "Attached are the log results", "C:\\Work\\Log.mht")

  
def Test():
    if SendMail("jaroslaw.kuklis@gmail.com", "gmail.com", "aa", "wworkk1996@gmail.com", "KeywordTestLog", "Attached are the log results", "C:\\Work\\Log.mht"):
      Log.Message("Mail was sent")
    else:
      Log.Warning("Mail was not sent")