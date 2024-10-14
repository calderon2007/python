from tkinter import Tk, Menu, messagebox, simpledialog
import pandas as pd

class MenuApp:
    def __init__(self, master):
        self.master = master
        self.create_menu()
        self.nombreArchivo = ""
        self.estudiantes = pd.read_exel(self.nombreArchivo)
        
        self.text_area = Text(master, wrap='word' , height=20, width=60)
        self.text_area.pack(side='left', fill='both', expand=True)

    def create_menu(self):
        barra_menus = Menu(self.master)

        menu_excel = Menu(barra_menus, tearoff=0)
        barra_menus.add_cascade(label="Excel", menu=menu_excel)

        menu_calculos = Menu(barra_menus, tearoff=0)
        barra_menus.add_cascade(label="Calculos", menu=menu_calculos)

        menu_excel.add_command(label="Todos", command=self.show_all)
        menu_excel.add_command(label="Nombre", command=self.show_name)
        menu_excel.add_command(label="Mayores de 18", command=self.show_over_18)

        menu_calculos.add_command(label="Promedio", command=self.show_average)
        menu_calculos.add_command(label="Mediana", command=self.show_median)
        menu_calculos.add_command(label="Moda", command=self.show_mode)
        
        barra_menus.add_command(label="Salir", command=self.master.quit)

        self.master.config(menu=barra_menus)

    def show_all(self):
        messagebox.showinfo("Opción seleccionada", "Mostrar todos los datos.")

    def show_name(self):
        name = simpledialog.askstring("Nombre", "Introduce tu nombre:")
        if name:
            messagebox.showinfo("Nombre ingresado", f"Tu nombre es: {name}")

    def show_over_18(self):
        age = simpledialog.askinteger("Edad", "Introduce tu edad:")
        if age is not None:
            if age >= 18:
                messagebox.showinfo("Acceso permitido", "Eres mayor de 18 años.")
            else:
                messagebox.showwarning("Acceso denegado", "Eres menor de 18 años.")

    def show_average(self):
        messagebox.showinfo("Promedio", "10.")

    def show_median(self):
        messagebox.showinfo("Mediana", "5.")

    def show_mode(self):
        messagebox.showinfo("Moda", "2.")

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Aplicación con Menú Excel")
        
        # Create the menu
        self.menu_app = MenuApp(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
