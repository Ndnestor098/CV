from tkinter import *
import os
import webbrowser
from PIL import ImageTk, Image
import pyperclip as cp

class Ventana():
    def __init__(self) -> None:
#======================================================Ventana======================================================
        self.root = Tk()
        self.root.title('Nestor Daniel Salom')
        self.root.iconbitmap(f'{os.getcwd()}/image/gato.ico')
        self.root.resizable(0,0)
        
        #Centrado de imagen
        w_total = self.root.winfo_screenwidth()
        h_total = self.root.winfo_screenheight()
        
        w_ventana = 1100
        h_ventana = 900

        pwidth = round(w_total/2 - w_ventana/2)
        pheight = round(h_total/2 - 490)

        self.root.geometry(str(w_ventana)+'x'+str(h_ventana)+'+'+str(pwidth)+'+'+str(pheight))

#======================================================Imagenes======================================================
        self.mail = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}/Image/mail.png").resize((20,18)))
        self.cel = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}/Image/cell.png").resize((20,18)))
        self.ubi = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}/Image/ubicacion.png").resize((20,18)))
        self.Aciz = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}/Image/Muestra.png").resize((90,60)))
        self.WhatsApp = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}/Image/w.png").resize((35,35)))
        self.Twitter = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}/Image/t.png").resize((35,35)))
        self.Instagram = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}/Image/i.png").resize((39,39)))
        self.Facebook = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}/Image/f.png").resize((35,35)))
        self.linkedin = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}/Image/linkedin.png").resize((35,35)))
        self.github = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}/Image/github.png").resize((35,35)))
        self.yo = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}/Image/yo.png").resize((170,170)))
    

#======================================================Funciones======================================================
        self.Head()
        self.Aside()
        self.Aside_2()
        self.Main()
        self.Footer()

        self.root.mainloop()
#======================================================Cabecera de Pagina=============================================
    def Head(self):
        self.Frame_C = Frame(self.root, bg='#303846')
        self.Frame_C.place(x=0, y=0, height=200, width=1100)

        #Imagen
        Label(self.Frame_C, image=self.yo, bg='#303846', foreground='white').place(x=50, y=15)

        #Nombre
        Label(self.Frame_C, text='Nestor Daniel Salom Nuñez', font=('Arial', 25, 'bold'), bg='#303846', foreground='white').place(x=286, y=40)

        #Email
        Button(self.Frame_C, text='trabajo.nestor.098@gmail.com', font=('Arial', 11, 'bold'), bg='#303846', foreground='#979ba2', bd=0, relief=FLAT, activebackground='#303846', activeforeground='#FFFFFF', command=lambda:cp.copy('trabajo.nestor.098@gmail.com')).place(x=310, y=118)
        Button(self.Frame_C, image=self.mail, bg='#303846', relief=FLAT, bd=0, activebackground='#303846', command=lambda:cp.copy('trabajo.nestor.098@gmail.com')).place(x=290, y=122)

        #Numero Telefonico
        Button(self.Frame_C, text='+584144412054', font=('Arial', 11, 'bold'), bg='#303846', foreground='#979ba2', bd=0, relief=FLAT, activebackground='#303846', activeforeground='#FFFFFF', command=lambda:self.Browser(1)).place(x=610, y=119)
        Button(self.Frame_C, image=self.cel, bg='#303846', relief=FLAT, bd=0, activebackground='#303846', command=lambda:self.Browser(1)).place(x=588, y=122)

        #Ubicacion
        Button(self.Frame_C, text='Montemarano, Avellino, Italia', font=('Arial', 11, 'bold'), bg='#303846', foreground='#979ba2', bd=0, relief=FLAT, activebackground='#303846', activeforeground='#FFFFFF', command=lambda:self.Browser(10)).place(x=800, y=119)
        Button(self.Frame_C, image=self.ubi, bg='#303846', bd=0, relief=FLAT, activebackground='#303846', command=lambda:self.Browser(10)).place(x=780, y=122)

#======================================================Menu Lateral 1=================================================
    def Aside(self):
        self.Frame_A = Frame(self.root, bg='#ECECEC')
        self.Frame_A.place(x=600, y=200, height=650, width=250)

        #Competencias
        Label(self.Frame_A, text='Competencias', font=('Arial', 16, 'bold'), bg='#ECECEC').place(x=46, y=20)

        #Primera competencia
        Label(self.Frame_A, text='Python', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=75)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=105, width=212, height=8)
        
        #Segunda Competencia
        Label(self.Frame_A, text='Git', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=140)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=170, width=212, height=8)

        #Tercera Competencia
        Label(self.Frame_A, text='Django', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=205)
        Label(self.Frame_A,  bg='#BDBDBD').place(x=20, y=235, width=212, height=8)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=235, width=150, height=8)
        
        #Cuarta Competencia
        Label(self.Frame_A, text='SQL', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=270)
        Label(self.Frame_A,  bg='#BDBDBD').place(x=20, y=300, width=212, height=8)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=300, width=180, height=8)
                
        #Quinta Competencia
        Label(self.Frame_A, text='HTML', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=335)
        Label(self.Frame_A,  bg='#BDBDBD').place(x=20, y=365, width=212, height=8)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=365, width=200, height=8)

        
        #Sexta Competencia
        Label(self.Frame_A, text='CSS', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=400)
        Label(self.Frame_A,  bg='#BDBDBD').place(x=20, y=430, width=212, height=8)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=430, width=70, height=8)


        #=====================================Separacion===============================
        Label(self.Frame_A,  bg='#C2C2C2').place(x=40, y=470, width=210, height=1)

        #Idiomas
        Label(self.Frame_A, text='Idiomas', font=('Arial', 16, 'bold'), bg='#ECECEC').place(x=84, y=480)

        #Español
        Label(self.Frame_A, text='Español', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=520)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=551, width=212, height=8)

        #Italiano
        Label(self.Frame_A, text='Italiano', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=580)
        Label(self.Frame_A,  bg='#BDBDBD').place(x=20, y=610, width=212, height=8)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=610, width=130, height=8)

#======================================================Menu Lateral 2=================================================
    def Aside_2(self):
        self.Frame_A = Frame(self.root, bg='#ECECEC')
        self.Frame_A.place(x=850, y=200, height=650, width=250)

        #Septima competencia
        Label(self.Frame_A, text='JavaScripts', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=75)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=105, width=212, height=8)
        
        #Octava Competencia
        Label(self.Frame_A, text='Tecnico Computo', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=140)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=170, width=212, height=8)

        #Novena Competencia
        Label(self.Frame_A, text='Diseño Grafico', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=205)
        Label(self.Frame_A,  bg='#BDBDBD').place(x=20, y=235, width=212, height=8)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=235, width=150, height=8)
        
        #Decima Competencia
        Label(self.Frame_A, text='WordPress', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=270)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=300, width=212, height=8)
                
        #Onceava Competencia
        Label(self.Frame_A, text='WordPress | Elementor', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=335)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=365, width=212, height=8)

        
        #Doceava Competencia
        Label(self.Frame_A, text='WordPress | Astra', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=400)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=430, width=212, height=8)


        #=====================================Separacion===============================
        Label(self.Frame_A,  bg='#C2C2C2').place(x=0, y=470, width=215, height=1)

        #Italiano
        Label(self.Frame_A, text='Ingles', font=('Arial', 10, 'bold'), bg='#ECECEC').place(x=16, y=520)
        Label(self.Frame_A,  bg='#BDBDBD').place(x=20, y=551, width=212, height=8)
        Label(self.Frame_A,  bg='#303846').place(x=20, y=551, width=40, height=8)

#======================================================Contenido Principal============================================
    def Main(self):
        self.Frame_M = Frame(self.root, bg='#ECECEC')
        self.Frame_M.place(x=0, y=200, height=650, width=600)

        #Linea de separacion
        Label(self.Frame_M, bg='#C2C2C2').place(x=599, y=20, height=660, width=1)

        #Experiencias
        Label(self.Frame_M, text='Experiencias', font=('Arial', 16, 'bold'), bg='#ECECEC').place(x=40, y=20)


        #Primera Experiencia
        Label(self.Frame_M, text='Tecnico en computos', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=39, y=75)
        Label(self.Frame_M, text='Mzo. 2018 - Presente', font=('Arial', 9), bg='#ECECEC').place(x=470, y=77)

        Label(self.Frame_M, text='Servicio Tecnico, Mexico', font=('Arial', 9), foreground='#767676', bg='#ECECEC').place(x=41, y=95)

        
        Label(self.Frame_M, text='Atencion al clientes', font=('Arial', 9), bg='#ECECEC').place(x=55, y=115)
        Label(self.Frame_M, text='•', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=45, y=113)
        
        Label(self.Frame_M, text='Reparacion en equipos computos', font=('Arial', 9), bg='#ECECEC').place(x=55, y=135)
        Label(self.Frame_M, text='•', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=45, y=133)

        Label(self.Frame_M, text='Optamizacion y analisis de sistemas computos', font=('Arial', 9), bg='#ECECEC').place(x=55, y=155)
        Label(self.Frame_M, text='•', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=45, y=153)

        Label(self.Frame_M, text='Soporte tecnico al cliente', font=('Arial', 9), bg='#ECECEC').place(x=55, y=175)
        Label(self.Frame_M, text='•', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=45, y=173)


        #Segunda Experiencia
        Label(self.Frame_M, text='Desarrollador de Aplicaciones de Escritorio', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=39, y=220)
        Label(self.Frame_M, text='Dic. 2021 - Presente', font=('Arial', 9), bg='#ECECEC').place(x=470, y=222)

        Label(self.Frame_M, text='Programador Full-Stack, Venezuela', font=('Arial', 9), foreground='#767676', bg='#ECECEC').place(x=40, y=240)

        
        Label(self.Frame_M, text='Analisis y Desarrollo de algoritmos', font=('Arial', 9), bg='#ECECEC').place(x=55, y=260)
        Label(self.Frame_M, text='•', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=45, y=258)
        
        Label(self.Frame_M, text='Desarrollo en Python, SQLite, PostgreSQL', font=('Arial', 9), bg='#ECECEC').place(x=55, y=280)
        Label(self.Frame_M, text='•', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=45, y=278)

        Label(self.Frame_M, text='Diseñador Grafico', font=('Arial', 9), bg='#ECECEC').place(x=55, y=300)
        Label(self.Frame_M, text='•', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=45, y=298)


        #Tercera Experiencia
        Label(self.Frame_M, text='Desarrollador de Paginas Webs', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=39, y=345)
        Label(self.Frame_M, text='Sep. 2023 - Presente', font=('Arial', 9), bg='#ECECEC').place(x=470, y=347)

        Label(self.Frame_M, text='Desarrollador Web Full-Stack, España', font=('Arial', 9), foreground='#767676', bg='#ECECEC').place(x=40, y=365)

        
        Label(self.Frame_M, text='Diseño Web', font=('Arial', 9), bg='#ECECEC').place(x=55, y=385)
        Label(self.Frame_M, text='•', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=45, y=383)
        
        Label(self.Frame_M, text='Desarrollo en JavaScript, HTML, CSS', font=('Arial', 9), bg='#ECECEC').place(x=55, y=405)
        Label(self.Frame_M, text='•', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=45, y=403)

        Label(self.Frame_M, text='Creacion de algoritmos', font=('Arial', 9), bg='#ECECEC').place(x=55, y=425)
        Label(self.Frame_M, text='•', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=45, y=423)

        Label(self.Frame_M, text='Creacion de paginas webs en WordPress | Elementor y Astra', font=('Arial', 9), bg='#ECECEC').place(x=55, y=445)
        Label(self.Frame_M, text='•', font=('Arial', 12, 'bold'), bg='#ECECEC').place(x=45, y=443)
        
        #Aplicaciones
        Label(self.Frame_M, text='Proyectos', font=('Arial', 16, 'bold'), bg='#ECECEC').place(x=40, y=485)

        Button(self.Frame_M, image=self.Aciz, bg='#ECECEC', bd=0, relief=FLAT, activebackground='#ECECEC', command=lambda:self.Browser(7)).place(x=100, y=530)
        Button(self.Frame_M, text='Programa de Gestion y Administracion', font=('Arial', 9), foreground='#767676', bg='#ECECEC', bd=0, relief=FLAT, activebackground='#ECECEC', command=lambda:self.Browser(7)).place(x=40, y=590)
        Button(self.Frame_M, text='de negocios y comercios', font=('Arial', 9), foreground='#767676', bg='#ECECEC', bd=0, relief=FLAT, activebackground='#ECECEC', command=lambda:self.Browser(7)).place(x=75, y=610)

#======================================================Pies de Pagina=================================================
    def Footer(self):
        self.Frame_F = Frame(self.root, bg='#303846')
        self.Frame_F.place(x=0, y=850, height=50, width=1100)

        Button(self.Frame_F, image=self.WhatsApp, bg='#303846', bd=0, relief=FLAT, activebackground='#303846', command=lambda:self.Browser(1)).place(x=150, y=9)

        Button(self.Frame_F, image=self.Instagram, bg='#303846', bd=0, relief=FLAT, activebackground='#303846', command=lambda:self.Browser(2)).place(x=301, y=9)

        Button(self.Frame_F, image=self.Twitter, bg='#303846', bd=0, relief=FLAT, activebackground='#303846', command=lambda:self.Browser(3)).place(x=452, y=9)

        Button(self.Frame_F, image=self.Facebook, bg='#303846', bd=0, relief=FLAT, activebackground='#303846', command=lambda:self.Browser(4)).place(x=605, y=9)

        Button(self.Frame_F, image=self.linkedin, bg='#303846', bd=0, relief=FLAT, activebackground='#303846', command=lambda:self.Browser(5)).place(x=755, y=9)

        Button(self.Frame_F, image=self.github, bg='#303846', bd=0, relief=FLAT, activebackground='#303846', command=lambda:self.Browser(6)).place(x=910, y=9)

#======================================================Links==========================================================
    def Browser(self, control):
        if control == 1:
            url = ['https://wa.me/584144412054']

        elif control == 2:
            url = ['https://www.instagram.com/nd_nestor_d/']

        elif control == 3:
            url = ['https://twitter.com/Ndnestor_098']

        elif control == 4:
            url = ['https://www.facebook.com/Ndnestor098']

        elif control == 5:
            url = ['https://www.linkedin.com/in/nestor-daniel-salom-nunez/']
        
        elif control == 6:
            url = ['https://github.com/Ndnestor098']

        elif control == 7:
            url = ['https://github.com/Ndnestor098/Software_ACIZ']

        else:
            url =['https://www.google.com/maps?sca_esv=592257846&output=search&q=montemarano+avellino&source=lnms&entry=mc']





        
        webbrowser.open_new(url[0])

        
if __name__ == '__main__':
    Ventana()