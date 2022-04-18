class Form(Frame):
    def __init__(self, master,name1,name2,combo=0, dir=""):
        Frame.__init__(self, master)
        if combo == "1":
            self.rows = 0
            self.name1 = name1
            self.name2 = name2
            print ("name1 is %s name2 in %s"% (name1,name2))
            self.initialize()  
        if combo == "0":
            self.rows = 0
            self.dir = dir
            self.initialize()
    def initialize(self):
        self.grid()
#top of root window
        self.label_fname = Label(self, anchor="w",fg="black", font=("Times New Roman",24))
        self.label_fname["text"] = " NAME:"
        self.label_fname.grid(row=1, column=0, columnspan=3,padx =(20,20),pady =(20,0),sticky =E)
#score frame with separated columns and same number of rows
#canvas width makes the layout of the body of window
        self.label_cname = Label(self,fg="white" , font=("Times New Roman",24),bg="gray") 
        self.label_cname["text"] = "   YOUR COMPANION: "
        self.label_cname.grid(row=1, column=4, columnspan=4,padx =(20,20),pady =(20,0),sticky =W)
#canvas web body

        self.create_widgets()

    def create_widgets(self):
        '''Create view widgets'''
        self.body()

    def body(self):
        #data class
        self.width =Canvas(self,height=466,width=466,bg="white",
        relief=RIDGE)
        self.width.grid(row=3, rowspan=1, column=3,columnspan=3,
        sticky=EW)
        self.scrollbar = Scrollbar(self.width)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        if self.rows&gt != 10:
            self.width.config(scrollregion = (0,0 ,200,self.rows*20 ))
        self.scrollbar.config(command = self.width.yview)
        self.column =0
        self.row1 =3
        self.st_font = "Times New Roman",24
        for i in range(self.rows):
            self.label_score = Label(self.width,anchor="w",name= i ,font= self.st_font) 
            self.label_score["text"] =  self.name1[i]
            self.label_score.grid(row=self.row1 , column=1, columnspan=1,padx =(1,1),pady =(0,0),sticky =EW)
            self.column =self.column +1
            self.row1 = self.row1+1
        self.row2 =3
        for i in range(self.rows):
            self.label_score = Label(self.width,anchor="w" ,font= self.st_font ,bg="white") 
            self.label_score["text"] = " "+self.name2[i]+"\n"
            self.label_score.grid(row=self.row2 , column=4, columnspan=1,padx =(1,1),pady =(0,0),sticky =EW)
            self.column =self.column +1
            self.row2 = self.row2+1
        self.width.config(scrollregion =self.width.bbox("all"))

    def insertItem(self,item):
        '''Add item to list'''
        self.widgets[self.row][1].config(text=item[0])
        self.widgets[self.row][2].config(text=item[1])
        self.widgets[self.row][3].config(text=item[2])
        self.row += 1 

    def NewFile(self):
        '''New file chosen in toolbar'''
        initialdir = self.dir
        self.Text.delete('1.0', END)
        self.Text.insert('1.0', '')
        self.dir = fd.askopenfilename(initialdir=initialdir)
        if (self.dir):
            self.Text.insert(END, "&gt;&gt;"+_translate("ProblemsMainWindow",
            "You have choosen this directory: \n", None)+self.dir)
            # now read file ...
            self.ReadFile()

    def ReadFile(self):
        print ("Open file %s."% self.dir)
        ''' Read content from file in Widget'''
        self.Text.insert(END, "\n&gt;&gt;"+_translate("ProblemsMainWindow",
        "Reading file contents and parsing information...\n", None))
        f = open(self.dir, 'rb')
        file_content = f.read()
        f.close()
        # Load pickle file
        chapter, prob_list, max_fct_len, problems, \
        problem_figs,problem_sols,mets, converters = \
        cPickle.loads(str(file_content))
        #Print chapter 
        self.Text.insert(END, "\n\nChapter: \n"+ chapter+"\n\n")
        self.numTests = len(prob_list)
        #Add problems to the list
        for i in range(self.numTests):
            item = prob_list[i]
            self.insertItem(item)
class Application(Frame):
    def __init__(self, master=None,dir="", rows=0,name1=0,name2=0):
        Frame.__init__(self, master)
        self.dir =dir
        self.name1=name1
        self.name2=name2
        self.rows=rows
        self.pack()
        self.createWidgets(self.dir,self.rows,self.name1,self.name2)

    def createWidgets(self,dir,rows,name1,name2):
        self.form=Form(self,name1,name2, combo="1")

main = Tk()
#initialization utf-16
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
inpath = os.path.join(PROJECT_ROOT, 'test.txt')
#test functions that return the neccessary data to table,
#before retrieving this data from database
##name1,name2 = Hello()
##rows =x =open(inpath,"r").readlines()
##print rows[0],"kheeeeeeeeem"


#main.geometry('1000x800+100+100')
#main.geometry('1000x800+100+100')
##main.minsize(300,600)
##main.state('zoomed')

main.geometry('550x505+50+50')
main.state('normal')
inmin = Application(master=main, name1 ,name2 ,rows)
#Main program loop
main.mainloop()

