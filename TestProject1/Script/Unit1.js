
function CloseAllTabs() {
    while (TestComplete.Tabs.Count > 0) {
        TestComplete.Tabs.Close(0); // Close the first tab repeatedly
    }
}