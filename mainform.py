from tkinter import *
from tkinter import messagebox
import product_db as pdb
import tkinter.font as setFont
import sys
import os


def transferlist(window=None):
    window.destroy()
    window = Tk()
    window.title('transfer information')
    window.geometry('450x450')
    window.minsize(450, 450)
    window.maxsize(450, 450)
    window['padx'] = 50
    window['pady'] = 20
    window.grid()

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0)
    window.rowconfigure(1, weight=2)
    window.rowconfigure(2)

    # Radiobutton
    var = IntVar()
    radioA = Radiobutton(window, text='stock A to stock B', variable=var, value=1, command=lambda: get_transfer_list())
    radioB = Radiobutton(window, text='stock B to stock A', variable=var, value=2, command= lambda: get_transfer_list())
    radioA.grid(column=0, row=0)
    radioB.grid(column=1, row=0)
    
    # Listbox
    lstbox = Listbox(window, height=15, width=50)
    lstbox.grid(column=0, row=1, columnspan=2)

    #button
    button = Button(window, text='Back', width=10, command=lambda: exit())
    button.grid(column=1, row=2)
    
    # gettransferlist
    def get_transfer_list():
        result = ""
        if var.get() == 1:
            result, name_fields = pdb.select_transfer_table(1)
        elif var.get() == 2:
            result, name_fields = pdb.select_transfer_table(2)
        
        lstbox.delete(0, END)
        lstbox.insert(0, ':'.join(name_fields._fields))

        for item in result:
            format_item = f"{item.code}:{item.name}:{item.quantity}"
            lstbox.insert(END, format_item)

        lstbox.focus_set()

    def exit():
        window.destroy()
        maindata()


    window.mainloop()


def transferdata(window=None):

    def exit():
        window.destroy()
        maindata()

    def get_product_list():
        column_name = ':'.join(['code', 'name', 'stockA', 'stockB', 'price'])
        data_in_database = pdb.select_product_table()
        if data_in_database:
            lb1.insert(0, column_name)
            for idx, datas in enumerate(data_in_database):
                str_id, *data = (str(data) for data in datas )
                if len(str_id) == 1:
                    str_id = f'P00{str_id}'            
                elif len(str_id) == 2:
                    str_id = f'P0{str_id}'
                elif len(str_id) == 3:
                    str_id = f'P{str_id}'
                data.insert(0, str_id)
                lb1.insert(idx+1, ':'.join(data))

    def display_data(values):
            data = lb1.get(values)
            print(data)
            if data != 'code:name:stockA:stockB:price':
                data = data.split(':', 4)
                label_code_show['text'] = data[0]
                label_product_show.config(text=data[1])
                label_quan_a_show.config(text=data[2])
                label_quan_b_show.config(text=data[3])
            else:
                messagebox.showerror(window, message='Please select other')


    window.destroy()
    window = Tk()

    # Create Font object
    font_paragraph = setFont.Font(family='tahoma', size=11)

    window.title('Make transfer information')
    window.geometry('450x400')
    window.minsize(450, 400)
    window.maxsize(450, 400)
    window['padx'] = 50
    window['pady'] = 20
    window.grid()

    # configure the grid
    window.columnconfigure(0, weight=2)
    window.columnconfigure(1, weight=2)
    window.columnconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)
    window.rowconfigure(0)
    window.rowconfigure(1)
    window.rowconfigure(2)
    window.rowconfigure(3)
    window.rowconfigure(4)
    window.rowconfigure(5)
    window.rowconfigure(6)
    window.rowconfigure(7, weight=1)
    window.rowconfigure(8)
    window.rowconfigure(9, weight=1)
    window.rowconfigure(10)

    # Frame for labels
    label_code = Label(window, text='Product code', font=font_paragraph, width=20, anchor='w')
    label_name = Label(window, text='Product name', font=font_paragraph, width=20, anchor='w')
    label_inv1 = Label(window, text='Quantity stock A', font=font_paragraph, width=20, anchor='w')
    label_inv2 = Label(window, text='Quantity stock B', font=font_paragraph, width=20, anchor='w')

    label_code.grid(column=0, row=0, sticky='w')
    label_name.grid(column=0, row=1, sticky='w')
    label_inv1.grid(column=0, row=2, sticky='w')
    label_inv2.grid(column=0, row=3, sticky='w')

    # Tarnsfer number labels
    transfer_number = Label(window, text='Transfer number', font=font_paragraph, width=20, anchor='w')
    quantity = Label(window, text='Quantity', font=font_paragraph, width=20, anchor='w')
    transfer_number.grid(column=0, row=5, sticky='w')
    quantity.grid(column=0, row=6, sticky='w')

    label_code_show = Label(window, font=font_paragraph, bg='#C0DDF0', width=16, justify='left')
    label_product_show = Label(window, font=font_paragraph, bg='#A1B9C8', width=16, justify='left')
    label_quan_a_show = Label(window, font=font_paragraph, bg='#C0DDF0', width=16, justify='left')
    label_quan_b_show = Label(window, font=font_paragraph,bg='#A1B9C8', width=16, justify='left')
    label_code_show.grid(column=1, row=0, sticky='w', columnspan=2)
    label_product_show.grid(column=1, row=1, sticky='w', columnspan=2)
    label_quan_a_show.grid(column=1, row=2, sticky='w', columnspan=2)
    label_quan_b_show.grid(column=1, row=3, sticky='w', columnspan=2)

    # Tarnsfer number entrys
    tid_text = StringVar()
    entry_number = Entry(window, textvariable=tid_text, font=font_paragraph, width=16, justify='left')
    str_quant = StringVar()
    entry_squnt = Entry(window, textvariable=str_quant, font=font_paragraph, width=16, justify='left')

    entry_number.grid(column=1, row=5, sticky='w', columnspan=2)
    entry_squnt.grid(column=1, row=6, sticky='w', columnspan=2)

    # Frame for button
    button_save = Button(window, text='Save', font=font_paragraph, width=5, command=lambda: insert_transfer(ACTIVE))
    button_save.grid(column=3, row=6)

    button_exit = Button(window, text='Back', font=font_paragraph, width=10, command=lambda: exit())
    button_exit.grid(column=1, row=10)

    # Frame for Radiobutton
    var = IntVar()
    r1 = Radiobutton(window, text='A -> B', font=font_paragraph, variable=var, value=1, justify='center', command=lambda: get_transfer_id())
    r2 = Radiobutton(window, text='B -> A', font=font_paragraph, variable=var, value=2, justify='center', command=lambda: get_transfer_id())
    r1.grid(column=0, row=4)
    r2.grid(column=1, row=4)

    # Button select
    button_select = Button(window, width=5, text='select', command=lambda: display_data(ACTIVE))
    button_select.grid(column=3,row=8)

    # Frame for List box
    lb1 = Listbox(window, height=5, width=50)
    lb1.grid(column=0, row=8, columnspan=3)


    def get_transfer_id():
        transfer_id = pdb.select_transfer_id()
        if not transfer_id:
            tid = 'T001'
        else:
            tid = transfer_id[1:4]
            tid = str(int(tid) + 1)

            if len(tid) == 1:
                tid = f'T00{tid}'            
            elif len(tid) == 2:
                tid = f'T0{tid}'
            elif len(tid) == 3:
                tid = f'T{tid}'

        tid_text.set(tid)
        

    def insert_transfer(values):

        def Insert_To_Database_And_Update(type_stock):
            # Insert data to database, tansfer table
            pdb.insert_transfer_table(tid, pid, pqty, type_stock)
            pdb.update_product_table(pid, pname, stock_a, stock_b)
            messagebox.showinfo('Warning', message='successfully')
            label_code_show.config(text='')
            label_product_show.config(text='')
            label_quan_a_show.config(text='')
            label_quan_b_show.config(text='')
            tid_text.set('')
            str_quant.set('')
            var.set(None)
            get_product_list()

        data = lb1.get(values)
        if not str_quant.get().isnumeric():
            messagebox.showinfo('Warning', message='Please enter quantity')
        else:
            if data != 'code:name:stockA:stockB:price':
                data = data.split(':', 4)
                pid = data[0]
                pname = data[1]
                stock_a = int(data[2])
                stock_b = int(data[3])
                tid = entry_number.get()
                pqty = int(entry_squnt.get())

                # edit pid
                pid = int(pid[1:])
                type_stock = var.get()

                if type_stock == 1:
                    # stock A --> stock B
                    if pqty > stock_a:
                        messagebox.showinfo('Warning', message='not correct')
                        entry_squnt.focus_set()
                    else:
                        stock_a -= pqty 
                        stock_b += pqty
                        Insert_To_Database_And_Update(type_stock)
                else:
                    if pqty > stock_b:
                        messagebox.showinfo('Warning', message='not correct')
                        entry_squnt.focus_set()
                    else:
                        stock_a += pqty 
                        stock_b -= pqty
                        Insert_To_Database_And_Update(type_stock)
                        
            else:
                messagebox.showinfo('Warning', message='Please select other')

    get_product_list()
    window.mainloop()


def productdata(window=None):

    def get_product_label_id():
        product_id = pdb.select_product_id()
        str_id = str(product_id + 1)
        if not product_id:
            pid_text = 'P001'
        else:
            if len(str_id) == 1:
                pid_text = f'P00{str_id}'            
            elif len(str_id) == 2:
                pid_text = f'P0{str_id}'
            elif len(str_id) == 3:
                pid_text = f'P{str_id}'

        label_id.config(text = pid_text)
        
    def insert_product():
        Label_Id = label_id.cget('text')
        pname = name_product.get()
        stock_a = quantity_a.get()
        stock_b = quantity_b.get()
        product_price = price.get()

        if not (Label_Id and pname and stock_a and stock_b and product_price):
            messagebox.showerror(title='Warning!', message='Please enter complete')
        else:
            Name_Product = pdb.select_product_name(pname)
            if Name_Product:
                messagebox.showinfo('Warning!', message='Product already exists')
            else:
                result = pdb.insert_product_table(pname, stock_a, stock_b, product_price)
                if result:
                    messagebox.showinfo('Warning', message='Save completed')

                    get_product_label_id()
                    name_product.set("")
                    quantity_a.set(0)
                    quantity_b.set(0)
                    price.set(0)

            label_name.focus_set()

    def exit():
        window.destroy()
        maindata()

    window.destroy()
    window = Tk()
    window.title('Information')
    window.geometry('350x250')
    window.minsize(350, 250)
    window.maxsize(350, 250)
    window['padx'] = 50
    window['pady'] = 20
    window.grid()

    # Create Font object
    font_paragraph = setFont.Font(family='tahoma', size=11)

    # configure the grid
    window.columnconfigure(0, weight=3)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=3)
    window.rowconfigure(0)
    window.rowconfigure(1)
    window.rowconfigure(2)
    window.rowconfigure(3)
    window.rowconfigure(4)
    window.rowconfigure(5)
    window.rowconfigure(6)
    # blank label
    blank_label = Label(window)
    blank_label.grid(column=1, ipadx=10)

    # frame for  Labels
    label_id = Label(window, fg='#fff', bg='blue', font=font_paragraph, width=10, justify='left')
    label_code = Label(window, text='Product code', font=font_paragraph, width=20, anchor='w')
    label_name = Label(window, text='Product name', font=font_paragraph, width=20, anchor='w')
    label_inv1 = Label(window, text='Quantity stock A', font=font_paragraph, width=20, anchor='w')
    label_inv2 = Label(window, text='Quantity stock B', font=font_paragraph, width=20, anchor='w')
    label_price = Label(window, text='unit price', font=font_paragraph, width=20, anchor='w')

    label_id.grid(column=2, row=0)
    label_code.grid(column=0, row=0)
    label_name.grid(column=0, row=1)
    label_inv1.grid(column=0, row=2)
    label_inv2.grid(column=0, row=3)
    label_price.grid(column=0, row=4)

    # Frame for  entrys
    name_product = StringVar()
    entry_product = Entry(window, textvariable=name_product, font=font_paragraph, width=10, justify='left')
    quantity_a = IntVar()
    entry_quan_a = Entry(window, textvariable=quantity_a, font=font_paragraph, width=10, justify='left')
    quantity_b = IntVar()
    entry_quan_b = Entry(window, textvariable=quantity_b, font=font_paragraph, width=10, justify='left')
    price = IntVar()
    entry_price = Entry(window, textvariable=price, font=font_paragraph, width=10, justify='left')

    entry_product.grid(column=2, row=1)
    entry_quan_a.grid(column=2, row=2)
    entry_quan_b.grid(column=2, row=3)
    entry_price.grid(column=2, row=4)

    # Frame for  buttons
    button_save = Button(window, text='Save', font=font_paragraph, width=10, command=lambda: insert_product())
    button_back = Button(window, text='Back', font=font_paragraph, width=10, command=lambda: exit())
    button_save.grid(column=0, row=5, pady=30, sticky='w')
    button_back.grid(column=2, row=5, pady=30, sticky='w')

    get_product_label_id()
    window.mainloop()

    
def maindata():
    # Set GUI
    window = Tk()
    window.title('First Page')
    window.geometry('275x250')
    window.grid()   

    # Create Font object
    font_paragraph = setFont.Font(family='tahoma', size=11)

    app_main = Frame(window)
    app_main.pack()
    
    # blank label
    blanklabel1 = Label(app_main, height=1)
    blanklabel2 = Label(app_main, height=1)
    blanklabel1.pack()
    blanklabel2.pack()

    # Crate option button
    width_button = 25
    cursor = 'arrow'

    # Label Seclect Menu
    label_menu = Label(app_main, text='Select Menu', font=('Helvetica', '16'))
    label_menu.pack()

    # Create button
    button_product = Button(app_main, text="Add products", font=font_paragraph, width=width_button, cursor=cursor, command=lambda: productdata(window))
    button_make_transfer = Button(app_main, text='Make transfer information', font=font_paragraph, width=width_button, cursor=cursor, command=lambda: transferdata(window))
    button_transfer_list = Button(app_main, text='Transfer list information', font=font_paragraph, width=width_button, cursor=cursor, command=lambda:transferlist(window))
    button_exit = Button(app_main, text='Exit', font=font_paragraph, width=width_button, cursor=cursor, command=sys.exit)
    button_product.pack()
    button_make_transfer.pack()
    button_transfer_list.pack()
    button_exit.pack()

    if not os.path.exists('productDB.db'):
        pdb.create_table()

    window.mainloop()
    

if __name__ == '__main__':
    maindata()
