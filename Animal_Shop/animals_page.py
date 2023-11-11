from json import load, dump
from tkinter import Button
from PIL import ImageTk, Image

from buy_animal_form import buy_animal_final
from main import frame, root
from cleaner import screen_clean


def display_animals():
    screen_clean()
    display_stocks()
    card_buy()


def display_stocks():
    global info

    with open("test_db/animals_in_stock.json", "r") as stock:
        info = load(stock)

        x = 150
        y = 50
    for item_name, item_stock in info.items():
        item_image = ImageTk.PhotoImage(Image.open(item_stock["image"]))

        # Трябва да се запази референция за да се визуализира снимката.

        images.append(item_image)

        frame.create_text(
            x,
            y,
            text=item_name,
            font=("Comic Sans MS", 15)
        )
        frame.create_image(
            x,
            y + 100,
            image=item_image
        )
        if item_stock["quantity"] > 0:
            message = f"In stock: {item_stock['quantity']}"
            color = "green"

            item_button = Button(
                root,
                text="Adopt",
                font=("Comic Sans MS", 12),
                bg="green",
                fg="white",
                width=5,
                command=lambda item_name=item_name: buy_product(item_name)
            )
            frame.create_window(x, y + 230, window=item_button)
        else:
            color = "red"
            message = "Out of stock"

        frame.create_text(
            x,
            y + 180,
            font=("Comic Sans MS", 12),
            fill=color,
            text=message
        )
        x += 200
        if x > 550:
            x = 150
            y += 230


def buy_product(product):
    info[product]["quantity"] -= 1
    with open("test_db/animals_in_stock.json", "w") as stock:
        dump(info, stock)

    display_animals()


images = []


def card_buy():
    current_image = ImageTk.PhotoImage(Image.open("images/cat_cart.png").resize((40, 40)))
    cart_buy.append(current_image)
    button = Button(
        root,
        image=current_image,
        # borderwidth=0,
        command=buy_animal_final,
    )

    frame.create_window(600, 480, window=button)


cart_buy = []
