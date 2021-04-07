from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x400+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=10,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",25,"bold"),pady=2).pack(fill=X)

        #======================Variables===========================
        #=================== Cosmetics================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()

        #=========================== Grocery =======================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.salt=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.tea=IntVar()

        #================================= Cold Drink=====================
        self.maza=IntVar()
        self.cocacola=IntVar()
        self.sprite=IntVar()
        self.frooti=IntVar()
        self.limca=IntVar()
        self.thumbs_up=IntVar()

        #=========================== total product price & Tax variables=================
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #========================== Customer=============================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        #============Customer Details Frame==========================
        F1=LabelFrame(self.root,bd=8,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=60,relwidth=1)

        customer_name_label=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",13,"bold")).grid(row=0,column=0,padx=20,pady=5)
        customer_name_text=Entry(F1,width=12,textvariable=self.c_name,font="arial 13",bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        customer_phone_label = Label(F1, text=" Phone No", bg=bg_color, fg="white",font=("times new roman", 13, "bold")).grid(row=0, column=2, padx=20, pady=5)
        customer_phone_text = Entry(F1, width=12,textvariable=self.c_phone, font="arial 13", bd=5, relief=SUNKEN).grid(row=0, column=3, pady=5,padx=10)

        bill_no_label = Label(F1, text=" Bill Number", bg=bg_color, fg="white",font=("times new roman", 13, "bold")).grid(row=0, column=4, padx=20, pady=5)
        bill_no_text = Entry(F1, width=12,textvariable=self.bill_no, font="arial 13", bd=5, relief=SUNKEN).grid(row=0, column=5, pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=5,font="arial 15 bold").grid(row=0,column=6,pady=10,padx=15)

        # ============================Cosmetics Frame==================
        F2 = LabelFrame(self.root, bd=10, text="Cosmetics ", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=2, y=165, width=340, height=380)

        bath_label = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_text = Entry(F2, width=10,textvariable=self.soap ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10,pady=10)

        Face_cream_label = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_text = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10,pady=10)

        Face_wash_label = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_wash_text = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10,pady=10)

        Hair_gell_label = Label(F2, text="Hair Gell ", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_gell_text = Entry(F2, width=10,textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_spray_label = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_spray_text = Entry(F2, width=10,textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10,pady=10)

        Body_loshan_label = Label(F2, text="Body Loshan", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_loshan_text = Entry(F2, width=10,textvariable=self.loshan, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=11,pady=10)

                         # ============================Grocery Frame==================
        F3 = LabelFrame(self.root, bd=10, text="Grocery ", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F3.place(x=320, y=165, width=340, height=380)

        g1_label = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_text = Entry(F3, width=10, textvariable=self.rice,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        g2_label = Label(F3, text="Food oil", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_text = Entry(F3, width=10,textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        g3_label = Label(F3, text="Salt", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_text = Entry(F3, width=10, textvariable=self.salt,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10,pady=10)

        g4_label = Label(F3, text="Daal ", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_text = Entry(F3, width=10, textvariable=self.daal,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1, padx=10,pady=10)

        g5_label = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_text = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_label = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6__text = Entry(F3, width=10, textvariable=self.tea,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1, padx=11,pady=10)

                # ============================Cold Drinks Frame==================
        F4 = LabelFrame(self.root, bd=10, text="Cold Drink", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F4.place(x=655, width=340, y=165, height=380)

        g1_label = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_text = Entry(F4, width=10, textvariable=self.maza,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        g2_label = Label(F4, text="Cocacola", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_text = Entry(F4, width=10,textvariable=self.cocacola, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        g3_label = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_text = Entry(F4, width=10,textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10,pady=10)

        g4_label = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_text = Entry(F4, width=10, textvariable=self.frooti,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1, padx=10,pady=10)

        g5_label = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_text = Entry(F4, width=10,textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_label = Label(F4, text="Thumbs up", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6__text = Entry(F4, width=10,textvariable=self.thumbs_up, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1, padx=11,pady=10)

             #=================================== Bill Area ================================================
        F5 =Frame(self.root, bd=10,relief=GROOVE)
        F5.place(x=980, y=165, width=300, height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=5,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5, orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fil=BOTH,expand=1)

            #======================================= Button Frame ============================================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=530,relwidth=1,height=140)

        m1_label=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_label = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_label=Label(F6,text="Total Cold Drinks",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_label=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_label = Label(F6,text="Grocery Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_label=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=725,width=530,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=13,width=9,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        gen_bill_btn=Button(btn_F,text="Genreate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=13,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=13,width=9,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=2,pady=13,width=9,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=(self.soap.get() * 40)
        self.c_fc_p=(self.face_cream.get() * 120)
        self.c_fw_p=(self.face_wash.get() * 60)
        self.c_hs_p=(self.spray.get() * 180)
        self.c_g_p=(self.gell.get() * 140)
        self.c_l_p=(self.loshan.get() * 180)

        self.total_cosmetic_price=float(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_hs_p+
            self.c_g_p+
            self.c_l_p
            )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=(self.rice.get() * 40)
        self.g_fo_p=(self.food_oil.get() * 120)
        self.g_sa_p=(self.salt.get() * 20)
        self.g_d_p=(self.daal.get() * 100)
        self.g_w_p=(self.wheat.get() * 40)
        self.g_t_p=(self.tea.get() * 80)

        self.total_grocery_price=float(
            self.g_r_p+
            self.g_fo_p+
            self.g_sa_p+
            self.g_d_p+
            self.g_w_p+
            self.g_t_p
             )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.01),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.cd_m_p=(self.maza.get() * 40)
        self.cd_c_p=(self.cocacola.get() * 90)
        self.cd_f_p=(self.frooti.get() * 20)
        self.cd_s_p=(self.sprite.get() * 50)
        self.cd_l_p=(self.limca.get() * 40)
        self.cd_t_p=(self.thumbs_up.get() * 50)
        self.total_cold_drink_price=float(
            self.cd_m_p+
            self.cd_c_p+
            self.cd_f_p+
            self.cd_s_p+
            self.cd_l_p+
            self.cd_t_p
             )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))

        self.Total_bill=float(  self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_cold_drink_price+
                                self.c_tax + self.g_tax + self.cd_tax
                            )


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Webcode Retail")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n ===============================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\tPrice")
        self.txtarea.insert(END,f"\n ===============================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No  Product Purchased")

        else:
            self.welcome_bill()
        #====================Cosmetics==============================
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t{self.c_s_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t{self.c_fw_p}")
            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\n Spray\t\t{self.spray.get()}\t{self.c_hs_p}")
            if self.gell.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gell\t\t{self.gell.get()}\t{self.c_g_p}")
            if self.loshan.get() != 0:
                self.txtarea.insert(END, f"\n Loshan\t\t{self.loshan.get()}\t{self.c_l_p}")

         # ==================== Grocery ==============================
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t{self.g_r_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t{self.g_d_p}")
            if self.salt.get() != 0:
                self.txtarea.insert(END, f"\n Salt\t\t{self.salt.get()}\t{self.g_sa_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t{self.g_w_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t{self.g_fo_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t{self.g_t_p}")

            # ==================== Cold Drink ==============================
            if self.maza.get() != 0:
                 self.txtarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t{self.cd_m_p}")
            if self.cocacola.get() != 0:
                self.txtarea.insert(END, f"\n Cocacola\t\t{self.cocacola.get()}\t{self.cd_c_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sptite\t\t{self.sprite.get()}\t{self.cd_s_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t{self.cd_l_p}")
            if self.thumbs_up.get() != 0:
                self.txtarea.insert(END, f"\n Thumbs Up \t\t{self.thumbs_up.get()}\t{self.cd_t_p}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t{self.cd_f_p}")

            self.txtarea.insert(END,f"\n -------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t{self.grocery_tax.get()}")

            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill\t\tRs. {self.Total_bill}")
            self.txtarea.insert(END,f"\n -------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill"," Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+" .txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved Successful")
        else:
            retuen

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
             messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear Data?")
        if op > 0:
            self.root.destroy()
        # =================== Cosmetics================
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.loshan.set(0)

        # =========================== Grocery =======================
        self.rice.set(0)
        self.food_oil.set(0)
        self.salt.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.tea.set(0)
        # ================================= Cold Drink=====================
        self.maza.set(0)
        self.cocacola.set(0)
        self.sprite.set(0)
        self.frooti.set(0)
        self.limca.set(0)
        self.thumbs_up.set(0)

        # =========================== total product price & Tax variables=================
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")
        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")

        # ========================== Customer=============================
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()

























