from tkinter import *
from random import randint
from tkinter import ttk
from tkinter import messagebox

def login():
    window=Tk()
    window.title("welcome to rps")
    window.geometry=("500x800")
    window.config(width=600, height =500)
    
    img = PhotoImage(file="final.png")
    my_label=Label(window ,image =img)
    my_label.place(x=0, y=0 ,relwidth=1,relheight =1)
    
    #adding text on the image
    my_text = Label(window,text="WELCOME!",font=("algerian" , 50),fg="black",bd=0)
    my_text.pack(pady=40)
    lb = Label(window,text="Login here:",font=("algerian" , 30),fg="black",bd=0)
    lb.pack()
    lb=Label(window,text="Username:",font=("Bradley Hand ITC",24)).pack() 
    
    def ok():
        usn=e1.get()
        passw=e2.get()
        
        if (usn == "" and passw == ""):
            messagebox.showinfo("","blank not allowed")
            
        elif (usn== "smriti" and passw == "1234"):
            messagebox.showinfo("","login success")
            window.destroy()
            
        elif (usn== "sree nidhi" and passw == "5678"):
            messagebox.showinfo("","login success ")
            window.destroy()   
            
        else :
            messagebox.showinfo("","incorrect credentials")
        
    e1=Entry(window,width=25)
    e1.pack()
    lb1=Label(window,text="Password:",font=("Bradley Hand ITC",24)).pack()
    e2=Entry(window,width=25)
    e2.config(show="*")
    e2.pack()
    bt=Button(window,text = "login",padx=10,pady=10,command=ok)
    bt.pack(pady=40)
    
    window.mainloop()

login()  


#actual play window:
root= Tk()
root.title('ROCK PAPER SCISSORS')
root.geometry("300x300")


root.config(bg="white")


lb3=Label(root,text="Computer choice:",font=("Bradley Hand ITC",24)).pack(pady =10)

rock = PhotoImage(file='rock.png')
paper = PhotoImage(file='paper.png')
scissors = PhotoImage(file='scissors.png')

#adding images to list so as to pick randomly in list using indexing
ilist=[rock , paper, scissors]

#to pick random  choice from the list of ilist
picknumber = randint(0,2)

#to display an image when the program executes:
i_label = Label(root, image=ilist[picknumber], bd=0)
i_label.pack(pady=30)

user_score = 0
comp_score = 0
def spin_it() :
    picknumber = randint(0,2)
    #show image
    i_label.config(image=ilist[picknumber])
    # 0 = rock
    # 1 = paper
    # 2 = scissors
    global user_score
    global comp_score
    
    #convert dropdown choice to a number
    if user_choice.get() == "Rock" :
        user_choice_value = 0
    elif user_choice.get() == "Paper" :
        user_choice_value = 1
    elif user_choice.get() == "Scissors" :
        user_choice_value = 2
    

    #determine if we won or lost :
    if user_choice_value ==2 and picknumber ==0 or user_choice_value==1 and picknumber==2 or user_choice_value==0 and  picknumber == 1:  # paper
        win_lose_label.config(text="You lose!! spin again...")
        comp_score += 1
        print('computer score:', comp_score, 'your score:', user_score)


    elif user_choice_value == picknumber:
        win_lose_label.config(text="its a tie!! spin again..")
        print('computer score:', comp_score, 'your score:', user_score)

    elif user_choice_value ==0 and picknumber == 2 or user_choice_value==2 and picknumber==1 or user_choice_value==1 and picknumber==0:  # scissors
        win_lose_label.config(text="u win!! spin again...")
        user_score+=1
        print('computer score:', comp_score, 'your score:', user_score)
    pass
    return comp_score,user_score 
        
lb4=Label(root,text="your choice:",font=("Bradley Hand ITC",24)).pack()


#creating a combobox by giving user a choice
values = ("Rock" ,"Paper" ,"Scissors")
user_choice = ttk.Combobox(root ,value = values )
user_choice.current(0)
user_choice.pack() 

# to create a spin button
spin_button = Button(root , text = 'Play!' , command =spin_it)
spin_button.pack()

#label if we won or lost:
win_lose_label = Label(root , text ="" , font=("algerian",20),bg="white")
win_lose_label.pack(pady=50)


#button to exit!
bt5=Button(root,text= "quit",command=root.destroy)
bt5.pack()

root.mainloop()

def scorecard():
    r=Tk()
    r.config(bg = "black")
    
    img3 = PhotoImage(file="opening.png")
    my_label=Label(r ,image =img3,bg="black")
    my_label.pack(pady=40)
    
    p = Label(r, text='',font=("Bradley Hand ITC", 20), bg='black', fg='white')
    
    y=Label(r,text=('your score',user_score),font=("Bradley Hand ITC", 20),bg='black',fg='white')
    y.pack(pady=5)
    f=Label(r,text=('computer score',comp_score),font=("Bradley Hand ITC", 20),bg='black',fg='white')
    f.pack(pady=10)
    p.pack(pady=15)
    
    if user_score>comp_score:
        p.config(text='Congartulations,you won!!')
    elif user_score<comp_score:
         p.config(text='You lost!better luck next time')
    else:
        p.config(text='its a tie!!')

    r.mainloop()

scorecard()