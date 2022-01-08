from tkinter import *
from time import sleep
import random
import os


def start_button_command():
    # animate the text of start button
    countdown_list = (3, 2, 1, "Go!")
    start_button.config(state="disabled")  # disable the button after its pressed
    for count in countdown_list:
        # sleep 1 second after every iteration but don't sleep after Go!. start the timer immediately
        if count != "Go!":
            start_button.config(text=count)
            root.update()
            sleep(1)
        elif count == "Go!":
            start_button.config(text=count)
            root.update()
    # after Go!, make typing area writable which was unwritable on default
    typing_area.config(state=NORMAL)

    # start timer after start button says Go!
    t = 12
    while t != (-1):
        # change timer color to red when less than 10 seconds are remaining
        if t <= 10:
            timer_label.config(fg="red")
            # change the text area to unwritable after time over
            if t == (-1):
                typing_area.config(state=DISABLED)
                break
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        # print(timer, end="\r")
        timer_label.config(text=f"Time: {timer}")
        sleep(1)
        root.update()
        t -= 1
    timer_label.config(text=f"Time: Over")


root = Tk()
root.title("Typing Test")  # change main window title

# tried creating frame but was not able to place the text widget on it center aligned
# main_frame = Frame(root, relief='solid', width=800, height=500, bg='red')
# main_frame.pack()

###### text to be typed ######
refernce_text = Text(root, wrap=WORD, width=130, height=15)

txt_path = os.path.abspath("most_used_dictionary_words.txt")  # get path of txt file
with open(txt_path, "r") as file:
    f = file.read().split()
    text_to_type = ""
    # take random 150 words from the txt file and put in the referece text field
    for i in range(150):
        text_to_type += f"{random.choice(f)} "

refernce_text.insert(INSERT, text_to_type)
refernce_text.config(state=DISABLED)
refernce_text.grid(row=0, column=0, columnspan=3)

###### score handling ######
score_label = Label(root, text="Score: ")
score_label.grid(row=1, column=0)

###### start button ######
start_button = Button(
    root, text="Start", font=(10), width=10, height=2, command=start_button_command
)
start_button.grid(row=1, column=1)

###### timer label ######
timer_label = Label(root, text="Time: 01:00")
timer_label.grid(row=1, column=2)

###### text to be typed ######
# typing area will be disable by default until the start button is pressed and and timer is started
typing_area = Text(root, width=150, height=15, state=DISABLED)
typing_area.grid(row=2, column=0, columnspan=3)

###### highlight the word that is being typed ######
# get_typed_text = typing_area.get('1.0', 'end')
# print(get_typed_text)

root.mainloop()  # keep window opened
