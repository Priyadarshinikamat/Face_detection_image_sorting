# Import the required libraries
from tkinter import *
import shutil
from PIL  import ImageTk, Image

from os import listdir, mkdir, rename
from os.path import isfile, join
mypath= 'Path where the images are stored'
onlyfiles= [f for f in listdir(mypath) if isfile(join(mypath,f)) & f.endswith('.jpg')]

pathFood= mypath+ '\\Food'
pathSelected= mypath+ '\\Selected'
pathDelete= mypath+ '\\Delete'
pathPersonal= mypath+ '\\Personal'
pathGeneral= mypath+ '\\General'

def CreateFood():
    mkdir(pathFood)
    print("Created Food")
def CreateSelected():
    mkdir(pathSelected)
    print("Created Selected")
def CreateDelete():
    mkdir(pathDelete)
    print("Created Delete")
def CreatePersonal():
    mkdir(pathPersonal)
    print("Created Personal")
def CreateGeneral():
    mkdir(pathGeneral)
    print("Created General")

def MoveToFood(url):
    url1= mypath+'\\'+url
    url2= mypath+'\\Food'+'\\'+url
    shutil.move(url1,url2)
    print("Photo moved to Food")
    a.set(a.get()+1)
    start()

def MoveToSelected(url):
    url1= mypath+'\\'+url
    url2= mypath+'\\Selected'+'\\'+url
    shutil.move(url1,url2)
    print("Photo moved to Selected")
    a.set(a.get()+1)
    start()

def MoveToDelete(url):
    url1= mypath+'\\'+url
    url2= mypath+'\\Delete'+'\\'+url
    shutil.move(url1,url2)
    print("Photo moved to Delete")
    a.set(a.get()+1)
    start()

def MoveToPersonal(url):
    url1= mypath+'\\'+url
    url2= mypath+'\\Personal'+'\\'+url
    shutil.move(url1,url2)
    print("Photo moved to Personal")
    a.set(a.get()+1)
    start()

def MoveToGeneral(url):
    url1= mypath+'\\'+url
    url2= mypath+'\\General'+'\\'+url
    shutil.move(url1,url2)
    print("Photo moved to General")
    a.set(a.get()+1)
    start()

def printInput(urltemp2):
    urltemp3=urltemp2
    inp = inputtxt.get(1.0, "end-1c")
    rename_file(urltemp3,inp)

def printInput2(urltemp2):
    urltemp3=urltemp2
    inp = inputtxt.get(1.0, "end-1c")
    rename_file2(urltemp3,inp)

def rename_file(url,inp):
    m= mypath+'\\'+url
    n= mypath+'\\'+inp
    rename(m,n)
    l.config(text=inp)
    global urltemp
    urltemp= inp
    print("Photo renamed")

url=""

def rename_file2(urlnew,inp):
    m= mypath+'\\'+urlnew
    n= mypath+'\\'+inp
    rename(m,n)
    l.config(text=inp)
    global url
    url= inp
    print("Photo renamed")

# Create an instance of Tkinter Frame
win = Tk()
width= 700
height= 700

a=IntVar()
a.set(0)

# Set the geometry of Tkinter Frame
win.geometry("1000x1000")
def start():
    b= a.get()
    global url
    url = onlyfiles[b]
    l.config(text=url)
    b1.configure(command=lambda: MoveToDelete(url))
    b2.configure(command=lambda: MoveToSelected(url))
    b3.configure(command=lambda: MoveToFood(url))
    b4.configure(command=lambda: MoveToPersonal(url))
    b5.configure(command=lambda: MoveToGeneral(url))
    printButton.configure(command=lambda: printInput2(url))

    newurl= mypath + temp+  url
    # Open the Image File
    image = Image.open(newurl)
    
    # Resize the image using resize() method
    resize_image = image.resize((width, height))
    img = ImageTk.PhotoImage(resize_image)
    label1.configure(image=img)
    label1.image=img   
    
    #win.after(5000)

b = Button(win, text = "Start", background = "red", fg = "white", command= start)
#b.pack(side = LEFT, expand = True)



temp= "\\"
urltemp= onlyfiles[0]

l = Label(win, text = urltemp)
l.pack(fill=BOTH, expand=True)

newurl2= mypath + temp+  urltemp
image2 = Image.open(newurl2)
resize_image2 = image2.resize((width, height))
img2 = ImageTk.PhotoImage(resize_image2)
# create label and add resize image
label1 = Label(image=img2)
label1.image = img2
label1.pack(fill=BOTH, expand=True)

d = Button(win, text = "Create", background = "red", fg = "white", command= lambda: [CreateFood(),CreateDelete(),CreatePersonal(),CreateSelected(),CreateGeneral()])
d.pack(side = LEFT, expand = True)

print("waiting....")
# Button 1
b1 = Button(win, text = "Delete", background = "red", fg = "white",command= lambda: MoveToDelete(urltemp))
b1.pack(side = LEFT, expand = True, fill = "x")

# Button 2
b2 = Button(win, text = "Selected", background = "blue", fg = "white",command=lambda: MoveToSelected(urltemp))
b2.pack(side = LEFT, expand = True, fill = "x")

# Button 3
b3 = Button(win, text = "Food", background = "green", fg = "white",command=lambda: MoveToFood(urltemp))
b3.pack(side = LEFT, expand = True, fill = "x")

b4 = Button(win, text = "Personal", background = "blue", fg = "white",command=lambda: MoveToPersonal(urltemp))
b4.pack(side = LEFT, expand = True, fill = "x")

b5 = Button(win, text = "General", background = "red", fg = "white",command=lambda: MoveToGeneral(urltemp))
b5.pack(side = LEFT, expand = True, fill = "x")


  
# TextBox Creation
inputtxt = Text(win, height = 5, width = 20)
inputtxt.pack(side = BOTTOM, expand = True, fill = BOTH)
  
# Button Creation
printButton = Button(win, text = "Rename", command =lambda: printInput(urltemp))
printButton.pack()

win.mainloop()


