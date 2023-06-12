def CreatingAndWritingToTextFile():
    aqFile.WriteToTextFile("C:\\Users\\jaroslaw.kuklis\\Downloads\\mlb_players.tsv", "Hello!", aqFile.ctUTF8)
    Log.Message("The file is created and the specified text is written to it successfully.")