## wx_alumnos_BD_2020_search_menu.py + creación de base de datos vacía

from wx import *
from wx.dataview import * 
import sqlite3
from sqlite3 import Error
from wx.dataview import DataViewListCtrl
from wx.adv import *


class MyApp(App):
    
    def OnInit(self):
        f1 = Frame(None, -1, "Listado de Fallecidos", size=(700, 500))
        p1 = self.p1 = Panel(f1)
        self.dvlc = dvlc = DataViewListCtrl(p1)
        dvlc.Bind(EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.modif)
        dvlc.AppendTextColumn('#', width=30)
        dvlc.AppendTextColumn('Apellido y Nombre', width=200)
        dvlc.AppendTextColumn('Fecha', width=75)
        dvlc.AppendTextColumn('Localidad', width=100)
        dvlc.AppendTextColumn('Autorizado', width=200)
        dvlc.AppendTextColumn('Destino', width=50, mode=DATAVIEW_CELL_EDITABLE)

        for c in self.dvlc.Columns:
            c.Sortable = True
            c.Reorderable = True

        self.nombreBD = nombreBD = TextCtrl(p1, style = TE_PROCESS_ENTER)
        self.search = search = SearchCtrl(p1, size=(-1, 33))
        search.Hide()
        search.ShowCancelButton(True)
       
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        sizer.Add(nombreBD, 0, EXPAND)
        sizer.Add(search, 0, EXPAND)
        search.Bind(EVT_TEXT, self.buscar)
        p1.SetSizer(sizer)



        menuBar = MenuBar()

        menu1 = Menu()
        menu1.Append(101, "&Carga", "Traer todos los datos")
        menu1.Append(102, "&Alta", "Insertar un dato nuevo")
        
        menu1.AppendSeparator()
        menu1.Append(103, "&Eliminar", "Borrar fila")
        menu1.AppendSeparator()
        menu1.Append(104, "&Buscar", "Buscar por nombre")
        menu1.Append(105, "&Salir", "Cerrar el programa")
        menuBar.Append(menu1, "&Archivo")



        f1.SetMenuBar(menuBar)

        idList = [101, 102, 103, 104, 105, 106]
        for e in idList:
            f1.Bind(EVT_MENU, self.accion, id=e)        

        f1.Show()
        return True

    def accion(self, event):
        id = event.GetId()
        if id == 101:
            self.cargaDatos()
        if id == 102:
            self.alta()
        if id == 103:
            self.borrar()
        if id == 104:
            self.search.Show()
            self.p1.Layout()
            self.search.SetFocus()





    def buscar(self, event):
        busco = self.search.GetValue()
        num = self.search.GetLastPosition()
        tot = self.dvlc.GetItemCount()
        for i in range(tot):
            self.dvlc.DeleteItem(0)

        for i in range(len(self.busqueda)):
            if busco == self.busqueda[i][1][:num]:
                self.dvlc.AppendItem(self.busqueda[i])
                

    def cargaDatos(self):
        def recupBD():
            con = sqlite3.connect("muertos.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM datos ORDER BY Nombre")
            tuplas = cur.fetchall()
            print(tuplas)
            listaA = [list(e) for e in tuplas]
            for e in listaA:
                e[0] = str(e[0])
            con.close()
            return listaA

        lista = recupBD()
        print(lista)
        for e in lista:
            self.dvlc.AppendItem(e)
        self.busqueda = lista

    def modif(self, evt):
        def grabaBD(id, ApeyNom, fecha, localidad, Autorizado, destino):
            con = sqlite3.connect("muertos.db")
            cur = con.cursor()
            actu = f"UPDATE datos SET destino='{destino}' WHERE id={id}"
            cur.execute(actu)
            con.commit()
            con.close()

        row = self.dvlc.GetSelectedRow()
        id = self.dvlc.GetTextValue(row, 0)
        ApeyNom = self.dvlc.GetTextValue(row, 1)
        fecha = self.dvlc.GetTextValue(row, 2)
        localidad = self.dvlc.GetTextValue(row, 3)
        Autorizado = self.dvlc.GetTextValue(row, 4)
        destino = self.dvlc.GetTextValue(row, 5)
        grabaBD(id, ApeyNom, fecha, localidad, Autorizado, destino)

    def alta(self):
        f2 = Frame(None, title="Agregar fallecido", size=(500, 350))
        p2 = self.p2 = Panel(f2)
        col1 = GridBagSizer(5,5)
        # Apellido - Caja de Texto
        flagsTex = TOP|ALIGN_CENTER
        flagsInp = EXPAND
        l_ape = StaticText(p2, -1, "Apellido y Nombre")
        col1.Add(l_ape, pos=(0,0), flag=flagsTex, border=5)
        ape = self.ape = TextCtrl(p2, -1, "Apellido")
        col1.Add(ape, pos=(0,1), span = (1, 2), flag=flagsInp)
        #fecha
        l_fna = StaticText(p2, -1, "Fecha")
        col1.Add(l_fna, pos = (2,0), flag=flagsTex, border=5)
        fna =self.fna = DatePickerCtrl(p2, size=(120,-1), style = DP_DROPDOWN | DP_SHOWCENTURY)
        fna.Bind(EVT_DATE_CHANGED, self.OnDateChanged, fna)
        col1.Add(self.fna, pos = (2,1), span = (1, 2), flag=flagsInp)
        # Profesión - Combo
        l_pro = StaticText(p2, -1, "Localidad")
        col1.Add(l_pro, pos = (3,0), flag=flagsTex, border=5)
        proList = ["Local", "Reinscripcion"]
        self.pro = cb = ComboBox(p2, 500, "Localidad", (0, 0), (-1, -1), proList, CB_DROPDOWN | TE_PROCESS_ENTER )
        cb.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
        col1.Add(self.pro, pos = (3,1), span = (1, 2), flag=flagsInp)
        # Adicionales - CheckBoxes
        l_adi = StaticText(p2, -1, "Se autoriza: ")
        col1.Add(l_adi, pos = (4,0), flag=flagsTex, border=5)
        adi1 = self.adi1 = CheckBox(p2, -1, "sepultura")
        adi2 = self.adi2 = CheckBox(p2, -1, "cremacion")
        adi3 = self.adi3 = CheckBox(p2, -1, "libre traslado")
        col1.Add(adi1, pos = (4, 1), span = (1, 1))
        col1.Add(adi2, pos = (4, 2), span = (1, 1))
        col1.Add(adi3, pos = (4, 3), span = (1, 1))
        
        s = BoxSizer(HORIZONTAL)
        s.Add(col1)
        b = Button(p2, -1, "&Alta")

        b.Bind(EVT_BUTTON, self.altaBD)
        s.Add(b, 1, ALL|EXPAND, 20)
        p2.SetSizer(s)
        f2.Show()

 


    def altaBD(self, event):
        ApeyNom = self.ape.GetValue()
        fecha = self.fna.GetValue()
        localidad = self.pro.GetValue()
        Autorizado = ""
        if self.adi1.GetValue():
            Autorizado += "Sepultura"
        if self.adi2.GetValue():
            Autorizado += " Cremacion"
        if self.adi3.GetValue():
            Autorizado += "Traslado"
        destino = " "
    
        self.dvlc.AppendItem(["0", ApeyNom, fecha, localidad, Autorizado, destino])
        con = sqlite3.connect("muertos.db")
        cur = con.cursor()
        alta = f"INSERT INTO datos (ApeyNom, nombre, comision, Autorizado, fnac) VALUES ('{ApeyNom}', '{fecha}', '{localidad}', '{Autorizado}', '{destino}')"
        cur.execute(alta)
        con.commit()
        con.close()

    def borrar(self):
        def borraBD(id):
            con = sqlite3.connect("muertos.db")
            cur = con.cursor()
            dele = f"DELETE from datos WHERE id={id}"
            cur.execute(dele)
            con.commit()
            con.close()
        row = self.dvlc.GetSelectedRow()
        id = self.dvlc.GetTextValue(row, 0)
        self.dvlc.DeleteItem(row)
        borraBD(id)
    def OnKillFocus(self, evt):
        self.pr = self.pro.GetValue()
        evt.Skip()
    def OnDateChanged(self, evt):
        print(evt.GetDate())
        d = evt.GetDate()
        print(d.FormatISODate())
        self.fe = d.FormatISODate()
    

prog = MyApp()
prog.MainLoop()
