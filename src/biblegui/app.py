import wx

from biblegui.gui.MainWindow import MainWindow


class BibleLibraryGui(wx.App):
    def OnInit(self):
        self.frame = MainWindow(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


def main():
    BibleApp = BibleLibraryGui(0)
    BibleApp.MainLoop()