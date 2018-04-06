import wx

WIDTH = 240
HEIGHT = 240
class Drop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.constrain = window.constrain

    def OnDropFiles(self, x, y, filenames):        
       	if self.constrain(x,y):
       		return True
        pos = (x//240*240, y//240*240)

        png = wx.Image(filenames[0], wx.BITMAP_TYPE_ANY)

        leftTop = (png.GetWidth() - WIDTH, png.GetHeight() - HEIGHT)
        png = png.GetSubImage(wx.Rect(leftTop, (WIDTH, HEIGHT)))
        png = wx.Bitmap(png)

        wx.StaticBitmap(self.window, -1, png, pos)
        return True

#daiichibutai
class First(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        drop = Drop(self)
        self.SetDropTarget(drop)

    def constrain(self, x, y):
        if x//240 >= 3 or y//240 >= 2:
            return True
        return False

#yugekibutai
class Third(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetSize(0,0,840,660)
        drop = Drop(self)
        self.SetDropTarget(drop)

    def constrain(self, x, y):
        if x//240 >= 4 or y//240 >= 2:
            return True
        elif x//240 == 3 and y//240 == 1:
        	return True
        return False

#rengoukantai 
class Union(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
 
class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, style=wx.MINIMIZE_BOX 
            | wx.SYSTEM_MENU | wx.CAPTION 
            | wx.CLOSE_BOX, size = (740, 550))#proper size = 740 550
 
        p = wx.Panel(self)
        nb = wx.Notebook(p)
 
        first = First(nb)
        third = Third(nb)
        union = Union(nb)
 
        nb.AddPage(first, "單一艦隊")
        nb.AddPage(third, "遊擊部隊")
        nb.AddPage(union, "連合艦隊")
        
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)
        self.Show(True)

app = wx.App()
MainFrame(None, -1, 'Window')
app.MainLoop()