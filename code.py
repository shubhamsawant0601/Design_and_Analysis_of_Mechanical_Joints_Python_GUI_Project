from tkinter import *
from PIL import ImageTk, Image 
import os 
import math
from msilib.schema import ComboBox
from tkinter.ttk import Combobox

materials = {'Structural Steel (350 Mpa)':350,'Carbon Steel (400 Mpa)':400,'Aluminum alloy (270 Mpa)':270,'Cast iron 280 (Mpa)':280}
MainWindow = Tk()
MainWindow.geometry('1000x600')
MainWindow.title('Designs and Analysis of Mechanical Joints')
Labeltitle = Label(MainWindow,text='Design and Analysis of Mechanical Joints ',font=('Arial',25),bg='light grey').place(x=200,y=30)

def DesignKnuckleJoint():
    
    def DesignKnuckle():
        P = float(t1.get())*1000
        fos = int(tfos.get())
   
        St1= str(t2.get())
        St1= materials.get(St1)
        St1 = round(St1/fos,2)
        St2= str(t3.get())
        St2= materials.get(St2)
        St2 = round(St2/fos,2)
    
    
        D = pow(4*(P/St1)/3.14,(1/2))
        D = int(D+2)
        Dia = str(D)+" mm"
        t4.insert(0,Dia)
    
        D1 = int(1.1*D+2)
        D1str = str(D1)+" mm"
        t5.insert(0,D1str)
   
        a  = int(0.75*D+2)
        astr = str(a)+" mm"
        t6.insert(0,astr)
    
        b  = int(1.25*D+2)
        bstr = str(b)+" mm"
        t7.insert(0,bstr)
    
        d  = max((pow(2*P/(St2*0.5*3.14),(1/2))),(pow(32*P*(b/4+a/3)/(2*3.14*St2), (1/3))))
        d  = int(d+2)
        dstr = str(d)+" mm"
        t8.insert(0,dstr)
    
        d0 = int(2*d+1)
        d0str = str(d0)+" mm"
        t9.insert(0,d0str)
    
        d1 = int(1.5*d+1)
        d1str = str(d1)+" mm"
        t10.insert(0,d1str)
        Tstress1 = round(P/(b*(d0-d)),2)
        Cstress1 = round(P/(b*d),2)
        Sstress1 = round(P/(b*(d0-d)),2)
    
        Tstress2 = round(P/(2*a*(d0-d)),2)
        Cstress2 = round(P/(2*a*d),2)
        Sstress2 = round(P/(2*a*(d0-d)),2) 
    
        if Tstress1<St1:
            l11=Label(win,text="Safe against Tensile Stress in Eye",bg='light green')
            l11.place(x=0,y=320)
            l12=Label(win,text="Stress in Eye ({} Mpa) < ({} Mpa) Strength of the Material".format(Tstress1,St1))
            l12.place(x=0,y=350)
        else:
            l13=Label(win,text="Not Safe against Tensile Stress in Eye",bg='orange')
            l13.place(x=0,y=320)
            l13=Label(win,text="Stress in Eye ({} Mpa) > ({} Mpa) Strength of Material".format(Tstress1,St1))
            l13.place(x=0,y=350)
          
        if Cstress1<St1:
            l11=Label(win,text="Safe against Compressive Stress in Eye",bg='light green')
            l11.place(x=0,y=380)
            l12=Label(win,text="Stress in Eye ({} Mpa) < ({} Mpa) Strength of Material".format(Cstress1,St1))
            l12.place(x=0,y=410)
        else:
            l13=Label(win,text="Not Safe against Compressive Stress in Eye",bg='orange')
            l13.place(x=0,y=380)
            l13=Label(win,text="Stress in Eye ({} Mpa) > ({} Mpa) Strength of Material".format(Cstress1,St1))
            l13.place(x=0,y=410)
     
        if Sstress1<(0.5*St1):
            l11=Label(win,text="Safe against Shear Stress in Eye",bg='light green')
            l11.place(x=0,y=450)
            l12=Label(win,text="Stress in Eye ({} Mpa) < ({} Mpa) Strength of Material".format(Sstress1,0.5*St1))
            l12.place(x=0,y=480)
        else:
            l13=Label(win,text="Not Safe against Shear Stress in Eye",bg='orange')
            l13.place(x=0,y=450)
            l13=Label(win,text="Stress in Eye ({} Mpa) > ({} Mpa) Strength of Material".format(Sstress1,0.5*St1))
            l13.place(x=0,y=480)    

    # For Fork
       
        if Tstress2<St2:
            l14=Label(win,text="Safe against Tensile Stress in fork",bg='light green')
            l14.place(x=0,y=510)
            l14=Label(win,text="Stress in fork ({} Mpa) < ({} Mpa) Strength of Material".format(Tstress2,St2))
            l14.place(x=0,y=540)
        else:
            l15=Label(win,text="Not Safe against Tensile Stress in fork",bg='orange')
            l15.place(x=0,y=510)
            l15=Label(win,text="Stress in fork ({} Mpa) > ({} Mpa) Strength of Material".format(Tstress2,St2))
            l15.place(x=0,y=540)
    
        if Cstress2<St2:
            l16=Label(win,text="Safe against Compressive Stress in fork",bg='light green')
            l16.place(x=0,y=570)
            l16=Label(win,text="Stress in fork ({} Mpa) < ({} Mpa) Strength of Material".format(Cstress2,St2))
            l16.place(x=0,y=600)
        else:
            l17=Label(win,text="Not Safe against Compressive Stress in fork",bg='orange')
            l17.place(x=0,y=570)
            l17=Label(win,text="Stress in fork ({} Mpa) > ({} Mpa) Strength of Material".format(Cstress2,St2))
            l17.place(x=0,y=600)
     
        if Sstress2<(0.5*St2):
            l18=Label(win,text="Safe against Shear Stress in fork",bg='light green')
            l18.place(x=0,y=630)
            l18=Label(win,text="Stress in fork ({} Mpa) < ({} Mpa) Strength of Material".format(Sstress2,0.5*St2))
            l18.place(x=0,y=660)
        else:
            l19=Label(win,text="Not Safe against Shear Stress in fork",bg='orange')
            l19.place(x=0,y=630)
            l19=Label(win,text="Stress in fork ({} Mpa) > ({} Mpa) Strength of Material".format(Sstress2,0.5*St2))
            l19.place(x=0,y=660)
    
    win = Toplevel(MainWindow)
    win.geometry('1500x1750')
    win.title('Knuckle Joint Design Simulator')

    n = StringVar()
    n1 = StringVar()
 
    l0=Label(win,text="Enter the Parameters -",font=(7),bg='light grey')
    l0.grid(row=0,column=0)
    l1=Label(win,text="Maximun Load applied (in KN)    =")
    l1.grid(row=2,column=0)
    t1=Entry(win,width=30)
    t1.grid(row=2,column=1)

    l2=Label(win,text="Material used for Fork and Eye     =")
    l2.grid(row=3,column=0)
    t2 = Combobox(win,width=27,textvariable=n)
    t2 ['values']=('Structural Steel (350 Mpa)','Carbon Steel (400 Mpa)','Aluminum alloy (270 Mpa)','Cast iron 280 (Mpa)')
    t2.current(0)
    t2.grid(row=3,column=1)
 
    l3=Label(win,text="Material used for knuckle Pin       =")
    l3.grid(row=4,column=0)
    t3 = Combobox(win,width=27,textvariable=n1)
    t3 ['values']=('Structural Steel (350 Mpa)','Carbon Steel (400 Mpa)','Aluminum alloy (270 Mpa)','Cast iron 280 (Mpa)')
    t3.current(0)
    t3.grid(row=4,column=1)
 
    lfos=Label(win,text="Factor of Safety Required              =")
    lfos.grid(row=5,column=0)
    tfos=Entry(win,width=30)
    tfos.grid(row=5,column=1)

    b1=Button(win,text="Design Knuckle Joint",command=DesignKnuckle,bg='light grey',width=25)
    b1.grid(row=6,column=1) 

    l4=Label(win,text="Resultant Parameters -",font=(7),bg='light grey')
    l4.grid(row=8,column=0)

    l4=Label(win,text="                    D = diameter of each rod (mm)")
    l4.grid(row=10,column=0)
    t4=Entry(win)
    t4.grid(row=10,column=1)

    l5=Label(win,text="  D1 = enlarged diameter of each rod (mm)")
    l5.grid(row=11,column=0)
    t5=Entry(win)
    t5.grid(row=11,column=1)

    l6=Label(win,text="       a = thickness of each eye of fork (mm)")
    l6.grid(row=12,column=0)
    t6=Entry(win)
    t6.grid(row=12,column=1)

    l7=Label(win,text="         b = thickness of eye end of rod (mm)")
    l7.grid(row=13,column=0)
    t7=Entry(win)
    t7.grid(row=13,column=1)

    l8=Label(win,text="              d = diameter of knuckle pin (mm)")
    l8.grid(row=14,column=0)
    t8=Entry(win)
    t8.grid(row=14,column=1)

    l9=Label(win,text="d0 = outside diameter of eye or fork (mm)")
    l9.grid(row=15,column=0)
    t9=Entry(win)
    t9.grid(row=15,column=1)

    l10=Label(win,text="                 d1 = diameter of pin head (mm)")
    l10.grid(row=16,column=0)
    t10=Entry(win)
    t10.grid(row=16,column=1)

    ltitle = Label(win,text="Knuckle Joint Design Simulator",font=('Arial',27),bg='light grey')
    ltitle.place(x=600,y=0)
    
    img2 = Image.open("C:/Users/shubh/eclipse/KnuckleDesign.png") 
    img2 = img2.resize((800,600), resample=0)
    img2 = ImageTk.PhotoImage(img2)
    Lphoto2 = Label(win,image=img2)
    Lphoto2.place(x=520,y=60)

    win.mainloop()
 
def DesignCotterJoint():
    def DesignCotterJoint():
        P = float(EP.get())*1000
        fos = int(Efos.get())
   
        TensileSt= str(CMaterial.get())
        TensileSt= materials.get(TensileSt)
        TensileSt= round(TensileSt/fos,2)
        
        ShearSt=0.5*TensileSt
        CompressiveSt = TensileSt
    
    
        D = pow(4*P/(TensileSt*3.14),(1/2))
        D = int(D+2)
        Dia = str(D)+" mm"
        ED.insert(0,Dia)
        
        D2 = 1.21*D
        D2 = int(D2)
        
        t = round(0.31*D)
        
        # check Crushing 
        
        if (P/(D2*t))>TensileSt:
            D2 = pow(4*P/TensileSt,(1/2))
            t = round(D2/4,2)
            
        D2 = round(D2,2)    
        D2str = str(D2)+" mm"
        ED2.insert(0,D2str)
        
        tstr = str(t)+" mm"
        Et.insert(0,tstr) 
        
        D1 = 1.75*D
        D1 = round(D1+2)
        D1str = str(D1)+" mm"
        ED1.insert(0,D1str)
        
        b  = int((P/(2*t*(ShearSt)))+2)
        bstr = str(b)+" mm"
        Eb.insert(0,bstr)
    
        D4  = max((P/(CompressiveSt*t)+D2),2.4*D)
        D4  = int(D4+2)
        D4str = str(D4)+" mm"
        ED4.insert(0,D4str)
    
        c = int(P/((2*ShearSt*(D4-D2)))+1)
        cstr = str(c)+" mm"
        Ec.insert(0,cstr)
    
        a = int((P/(2*D2*ShearSt))+1)
        astr = str(a)+" mm"
        Ea.insert(0,astr)
        
        
        D3 = max(pow(int((4*P/(CompressiveSt*3.14))+pow(D2,2)),(1/2)),1.5*D)
        D3 = round(D3+2)
        D3str = str(D3)+" mm"
        ED3.insert(0,D3str)
        
        t1 = int((P/(3.14*D2*ShearSt))+2)
        t1str = str(t1)+" mm"
        Et1.insert(0,t1str)
        
        l = int(4*D)
        lstr = str(l)+" mm"
        El.insert(0,lstr)
        
        e = int(1.2*D)
        estr = str(e)+" mm"
        Ee.insert(0,estr)
        
        TensionRodSt = round(P/(3.14*pow(D,2)),2)
        TensionSpigotSt = round(P/((3.14/4)*pow(D2,2)-D2*t),2)
        CrushingCotterSt = round(P/(D2*t*CompressiveSt),2)
        TensionSocketSlotSt=round( P/( (3.14/4)*(pow(D1,2)-pow(D2,2) ) - (D1-D2)*t)  ,2)
        ShearingCotterSt = round(P/(2*b*t),2)
        ShearingSocketSt= round(P/(2*c*(D4-D2)),2)
        ShearingRodSt = round(P/(2*a*D2),2)
        CrushingSpigotCollarSt = round(4*P/(3.14*(pow(D3,2)-pow(D2,2))),2)
        ShearingSpigotCollarSt = round(P/(3.14*D2*t1),2)
        CrushingSocketCollarSt = round(P/(t*(D4-D2)),2)  
    
        if TensionRodSt<TensileSt:
            l11=Label(win2,text="Safe against Tensile Stress in Rod",bg='light green')
            l11.place(x=0,y=410)
            l12=Label(win2,text="Stress in Rod ({} Mpa) < ({} Mpa) Strength of the Material".format(TensionRodSt,TensileSt))
            l12.place(x=0,y=440)
        else:
            l13=Label(win2,text="Not Safe against Tensile Stress in Rod",bg='orange')
            l13.place(x=0,y=410)
            l13=Label(win2,text="Stress in Rod ({} Mpa) > ({} Mpa) Strength of Material".format(TensionRodSt,TensileSt))
            l13.place(x=0,y=440)
          
        if TensionSpigotSt<TensileSt:
            l11=Label(win2,text="Safe against Tensile Stress in Spigot",bg='light green')
            l11.place(x=0,y=470)
            l12=Label(win2,text="Stress in Spigot ({} Mpa) < ({} Mpa) Strength of Material".format(TensionSpigotSt,TensileSt))
            l12.place(x=0,y=500)
        else:
            l13=Label(win2,text="Not Safe against Tensile Stress in Spigot",bg='orange')
            l13.place(x=0,y=470)
            l13=Label(win2,text="Stress in Eye ({} Mpa) > ({} Mpa) Strength of Material".format(TensionSpigotSt,TensileSt))
            l13.place(x=0,y=500)
     
        if CrushingCotterSt<CompressiveSt:
            l11=Label(win2,text="Safe against Crushing in Cotter",bg='light green')
            l11.place(x=0,y=530)
            l12=Label(win2,text="Stress in Eye ({} Mpa) < ({} Mpa) Strength of Material".format(CrushingCotterSt,CompressiveSt))
            l12.place(x=0,y=560)
        else:
            l13=Label(win2,text="Not Safe against Crushing in Cotter",bg='orange')
            l13.place(x=0,y=530)
            l13=Label(win2,text="Stress in Cotter ({} Mpa) > ({} Mpa) Strength of Material".format(CrushingCotterSt,CompressiveSt))
            l13.place(x=0,y=560)    
       
        if TensionSocketSlotSt<TensileSt:
            l14=Label(win2,text="Safe against Tensile Stress in Socket Slot",bg='light green')
            l14.place(x=0,y=590)
            l14=Label(win2,text="Stress in Socket ({} Mpa) < ({} Mpa) Strength of Material".format(TensionSocketSlotSt,TensileSt))
            l14.place(x=0,y=620)
        else:
            l15=Label(win2,text="Not Safe against Tensile Stress in Socket",bg='orange')
            l15.place(x=0,y=590)
            l15=Label(win2,text="Stress in Socket ({} Mpa) > ({} Mpa) Strength of Material".format(TensionSocketSlotSt,TensileSt))
            l15.place(x=0,y=620)
    
        if ShearingCotterSt < ShearSt:
            l16=Label(win2,text="Safe against Shearing in Cotter",bg='light green')
            l16.place(x=0,y=650)
            l16=Label(win2,text="Stress in Cotter ({} Mpa) < ({} Mpa) Strength of Material".format(ShearingCotterSt ,ShearSt))
            l16.place(x=0,y=680)
        else:
            l17=Label(win2,text="Not Safe against Shearing in Cotter",bg='orange')
            l17.place(x=0,y=650)
            l17=Label(win2,text="Stress in Cotter ({} Mpa) > ({} Mpa) Strength of Material".format(ShearingCotterSt , ShearSt))
            l17.place(x=0,y=680)
    
        if ShearingSocketSt<ShearSt:
            l18=Label(win2,text="Safe against Shearing in Socket",bg='light green')
            l18.place(x=500,y=410)
            l18=Label(win2,text="Stress in Socket ({} Mpa) < ({} Mpa) Strength of Material".format(ShearingSocketSt,ShearSt))
            l18.place(x=500,y=440)
        else:
            l19=Label(win2,text="Not Safe against Shearing in Socket",bg='orange')
            l19.place(x=500,y=410)
            l19=Label(win2,text="Stress in Socket ({} Mpa) > ({} Mpa) Strength of Material".format(ShearingSocketSt,ShearSt))
            l19.place(x=500,y=440)
            
            
        if ShearingRodSt<ShearSt:
            l18=Label(win2,text="Safe against Shearing in Rod",bg='light green')
            l18.place(x=500,y=470)
            l18=Label(win2,text="Stress in Rod ({} Mpa) < ({} Mpa) Strength of Material".format(ShearingRodSt,ShearSt))
            l18.place(x=500,y=500)
        else:
            l19=Label(win2,text="Not Safe against Shearing in Rod",bg='orange')
            l19.place(x=500,y=470)
            l19=Label(win2,text="Stress in Rod ({} Mpa) > ({} Mpa) Strength of Material".format(CrushingSocketCollarSt,CompressiveSt))
            l19.place(x=500,y=500)    
        
        if CrushingSpigotCollarSt<CompressiveSt:
            l18=Label(win2,text="Safe against Crushing Spigot Collar",bg='light green')
            l18.place(x=500,y=530)
            l18=Label(win2,text="Stress in Collar ({} Mpa) < ({} Mpa) Strength of Material".format(CrushingSpigotCollarSt,CompressiveSt))
            l18.place(x=500,y=560)
        else:
            l19=Label(win2,text="Not Safe against Crushing in Spigot Collar",bg='orange')
            l19.place(x=500,y=530)
            l19=Label(win2,text="Stress in Collar ({} Mpa) > ({} Mpa) Strength of Material".format(CrushingSpigotCollarSt,CompressiveSt))
            l19.place(x=500,y=560)
                   
        if ShearingSpigotCollarSt<ShearSt:
            l18=Label(win2,text="Safe against Shearing in Spigot Collar",bg='light green')
            l18.place(x=500,y=590)
            l18=Label(win2,text="Stress in Spigot Collar({} Mpa) < ({} Mpa) Strength of Material".format(ShearingSpigotCollarSt,ShearSt))
            l18.place(x=500,y=620)
        else:
            l19=Label(win2,text="Not Safe against Shearing in Spigot Collar",bg='orange')
            l19.place(x=500,y=590)
            l19=Label(win2,text="Stress in Spigot Collar ({} Mpa) > ({} Mpa) Strength of Material".format(CrushingSocketCollarSt,ShearSt))
            l19.place(x=500,y=620)
       
        if CrushingSocketCollarSt<CompressiveSt:
            l18=Label(win2,text="Safe against Crushing in Socket Collar",bg='light green')
            l18.place(x=500,y=650)
            l18=Label(win2,text="Stress in Collar ({} Mpa) < ({} Mpa) Strength of Material".format(CrushingSocketCollarSt,CompressiveSt))
            l18.place(x=500,y=680)
        else:
            l19=Label(win2,text="Not Safe against Cruhing in Socket Collar",bg='orange')
            l19.place(x=500,y=650)
            l19=Label(win2,text="Stress in Collar ({} Mpa) > ({} Mpa) Strength of Material".format(CrushingSocketCollarSt,CompressiveSt))
            l19.place(x=500,y=670)  
            
    win2 = Toplevel(MainWindow)
    win2.geometry('1500x1750')
    win2.title('Knuckle Joint Design Simulator')
   
    n = StringVar()
    n1 = StringVar()
 
    Lpara=Label(win2,text="Enter the Parameters -",font=(7),bg='light grey')
    Lpara.grid(row=0,column=0)
    
    LP=Label(win2,text="Maximun Load applied (in KN)    =")
    LP.grid(row=2,column=0)
    EP=Entry(win2,width=30)
    EP.grid(row=2,column=1)

    Lmaterial=Label(win2,text="Material used for Cotter Joint       =")
    Lmaterial.grid(row=3,column=0)
    CMaterial = Combobox(win2,width=27,textvariable=n)
    CMaterial ['values']=('Structural Steel (350 Mpa)','Carbon Steel (400 Mpa)','Aluminum alloy (270 Mpa)','Cast iron 280 (Mpa)')
    CMaterial.current(0)
    CMaterial.grid(row=3,column=1)
 
    Lfos=Label(win2,text="Factor of Safety Required              =")
    Lfos.grid(row=5,column=0)
    Efos=Entry(win2,width=30)
    Efos.grid(row=5,column=1)

    Design=Button(win2,text="Design Cotter Joint",command=DesignCotterJoint,bg='light grey',width=25)
    Design.grid(row=6,column=1) 

    Lparameter=Label(win2,text="Resultant Parameters -",font=(7),bg='light grey')
    Lparameter.grid(row=8,column=0)

    LD=Label(win2,text="                d = Diameter of Rod (mm)")
    LD.grid(row=10,column=0)
    ED=Entry(win2)
    ED.grid(row=10,column=1)

    LD1=Label(win2,text="   d1 = Outside Diameter of Socket (mm)")
    LD1.grid(row=11,column=0)
    ED1=Entry(win2)
    ED1.grid(row=11,column=1)

    La=Label(win2,text="   a = length of Ends of Slot to Rod (mm)")
    La.grid(row=12,column=0)
    Ea=Entry(win2)
    Ea.grid(row=12,column=1)
 
    Lb=Label(win2,text="            b = Mean width of cotter (mm)")
    Lb.grid(row=13,column=0)
    Eb=Entry(win2)
    Eb.grid(row=13,column=1)

    ED2=Label(win2,text="            d2 = Diameter of Spigot (mm)")
    ED2.grid(row=14,column=0)
    ED2=Entry(win2)
    ED2.grid(row=14,column=1)

    LD3=Label(win2,text="         d3 = Outside Spigot Collar (mm)")
    LD3.grid(row=15,column=0)
    ED3=Entry(win2)
    ED3.grid(row=15,column=1)

    LD4=Label(win2,text="     d4 = Diameter of Socket Collar (mm)")
    LD4.grid(row=16,column=0)
    ED4=Entry(win2)
    ED4.grid(row=16,column=1)
    
    Lt=Label(win2,text="             t = Thickness of Cotter (mm)")
    Lt.grid(row=17,column=0)
    Et=Entry(win2)
    Et.grid(row=17,column=1)
    
    Lt1=Label(win2,text="   t1 = Thickness of Spigot Collar  (mm)")
    Lt1.grid(row=18,column=0)
    Et1=Entry(win2)
    Et1.grid(row=18,column=1)
    
    Lc=Label(win2,text="      c = Thickness of Socket Collar (mm)")
    Lc.grid(row=19,column=0)
    Ec=Entry(win2)
    Ec.grid(row=19,column=1)

    Ll=Label(win2,text="                l = Length of Cotter (mm)")
    Ll.grid(row=20,column=0)
    El=Entry(win2)
    El.grid(row=20,column=1)
    
    Le=Label(win2,text="                      e = Clearance  (mm)")
    Le.grid(row=21,column=0)
    Ee=Entry(win2)
    Ee.grid(row=21,column=1)
    
    ltitle = Label(win2,text="Cotter Joint Design Simulator",font=('Arial',27),bg='light grey')
    ltitle.place(x=600,y=0)
    
    img3 = Image.open("C:/Users/shubh/eclipse/CotterDesign.jpg")
    img3 = img3.resize((650,310), resample=0)
    img3 = ImageTk.PhotoImage(img3)
    Lphoto1 = Label(win2,image=img3)
    Lphoto1.place(x=520,y=60)
    
    win2.mainloop()
 
DesignKnuckleJoint=Button(MainWindow,text="Design Knuckle Joint",font=(5),command=DesignKnuckleJoint,bg='light grey',width = 31,height = 2)
DesignKnuckleJoint.place(x=100,y=510)   
    
DesignCotterJoint=Button(MainWindow,text="Design Cotter Joint",font=(5),command=DesignCotterJoint,bg='light grey',width =31, height = 2)
DesignCotterJoint.place(x=500,y=510)    
    
img = Image.open("C:/Users/shubh/eclipse/Knucklephoto.jpg")    
img= img.resize((350,350), resample=0)
img = ImageTk.PhotoImage(img) 
Lphoto = Label(MainWindow,image=img)
Lphoto.place(x=100,y=150)

img1 = Image.open("C:/Users/shubh/eclipse/Cotterphoto.jpg")    
img1= img1.resize((350,350), resample=0)
img1 = ImageTk.PhotoImage(img1) 
Lphoto1 = Label(MainWindow,image=img1)
Lphoto1.place(x=500,y=150)

MainWindow.mainloop()
