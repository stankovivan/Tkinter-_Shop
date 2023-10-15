from cleaner import screen_clean
from main import frame


def buy_animal_final():
    screen_clean()
    text = "You have a new puppy!"
    frame.create_text(
        340,
        150,
        text=text,
        font=('Comic Sans MS', 15, 'bold'),
        fill="green",
    )

    frame.create_text(
        330,
        350,
        text="Thank you!",
        font=('Comic Sans MS', 15, 'bold'),
        fill="green",
    )
