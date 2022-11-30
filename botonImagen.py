from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, size=(770, 516))
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        ib1 = Image("em01.jpg", BITMAP_TYPE_ANY).ConvertToBitmap()
        b1 = BitmapButton(p, -1, ib1)
        b1.Bind(EVT_BUTTON, self.accion)
        s.Add(b1, 0, ALL|ALIGN_LEFT, 30)
        p.SetSizer(s)
        f.Show()
        return True

    def accion(self, event):
        print("hola")

app = MyApp()
app.MainLoop()
