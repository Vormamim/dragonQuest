import time

def typing_animation(text, speed=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)

typing_animation("This is a typing animation.")
