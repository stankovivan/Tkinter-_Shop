from tkinter import *


def run_program():
    root = Tk()
    root.geometry('750x560')
    root.title("Animal Shop")
    root.iconbitmap("images/bone.ico")
    root.resizable(False, False)

    return root


def main_frame():
    frame_inner = Canvas(
        root,
        width=700,
        height=700,
    )
    frame_inner.grid(row=0, column=0)

    return frame_inner


root = run_program()
frame = main_frame()
