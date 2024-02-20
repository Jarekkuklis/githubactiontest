def Test1():
    Project.Variables.Var11.Reset()
    while not Project.Variables.Var11.IsEOF():
        #Posts an information message to the test log.
        Log.Message(Project.Variables.Var11.Value["F1"], "")
        if Project.Variables.Var11.Value["F1"] == 4:
            #Posts an error to the test log.
            Log.Error("", "")
        Project.Variables.Var11.Next()

def EventControl1_OnLogError(Sender, LogParams):
    Log.Message("the event work")
    pass
