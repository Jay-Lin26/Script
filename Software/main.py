import wx
import demo


class CalcFrame(demo.MyFrame1):
    def __init__(self, parent):
        demo.MyFrame1.__init__(self, parent)

    def FindSquare(self, event):
        num = int(self.m_textCtrl1.GetValue())
        self.m_textCtrl2.SetValue(str(num*num))
        event.Skip()


# app = wx.App()
# frame = wx.Frame(None, title="wxpython", size=(1000, 800))
# panel = wx.Panel(frame)
# label = wx.StaticText(panel, label="Hello World", pos=(100, 50))
# frame.Show(True)
# app.MainLoop()
app = wx.App()
frame = CalcFrame(None)
frame.Show(True)
app.MainLoop()