def Test():
  # Obtains the Table object
  doctable = Aliases.WINWORD.formADocxWord.panel.panelADocx.panelMicrosoftWordDocument.Page_1.Page_1_content
  # Obtains the control that displays data in the tabular form
  pdftable = Aliases.Acrobat.wndAcrobatSDIWindow.AVTabsContainerView.AVDocumentMainView.AVFlipContainerView.AVSplitterView.AVSplitationPageView.AVSplitterView.AVScrolledPageView.AVScrollView.AVPageView
  # Sets comparison properties
  ReportDifference = True
  MessageType = lmError
  # Compares data stored by the Table object with data displayed by the specified control
  doctable.CompareWithObject(pdftable, ReportDifference, MessageType)