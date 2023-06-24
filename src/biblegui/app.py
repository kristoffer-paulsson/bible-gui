import wx


def main():
    app = wx.App()

    window = wx.Frame(None, title="Bible Analyzer", size=(300, 200))
    panel = wx.Panel(window)
    label = wx.StaticText(panel, label="For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life. - John 3:16 (KJV)", pos=(100, 50))
    window.Show(True)
    app.MainLoop()