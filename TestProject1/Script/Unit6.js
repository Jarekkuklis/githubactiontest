function Test11()
{
  let filename = "C:\\Windows\\System32\\notepad.exe";
  Log.Message("FileName" + filename);
  
  let VerInfo = aqFileSystem.GetFileInfo(filename).VersionInfo
  
  //It works fine
  Log.Message("Check Type = "+VerInfo.FileType);
  Log.Message("Check File Major version ="+VerInfo.FileMajorVersion);
  Log.Message("Check File Minor version =" +VerInfo.FileMinorVersion);
  Log.Message("Check Product Languages = "+VerInfo.Languages);
  Log.Message("Check Product MinorVersion = "+VerInfo.ProductMinorVersion);
  // Convert to string to avoid JavaScript errors
  
  Log.Message("Check Product Legal Copyright = " + JSON.stringify(VerInfo.LegalCopyright) || "N/A");
  Log.Message("Check Product Name = " + JSON.stringify(VerInfo.ProductName || "N/A"));
  Log.Message("Check Product Company Name = " + JSON.stringify(VerInfo.CompanyName || "N/A"));
  
  Log.Message("Check Product Legal Copyright = " + String.valueOf(VerInfo.LegalCopyright));

}