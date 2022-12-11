from mouse.mouse_se import MouseSE
import mouse.mouse_client as mse
import wordhuntsolver
import time


def goto_spot(val, debug=False):
    x, y = val
    my_mouse.goto(130 + x * 100, 480 + y * 100)


if __name__ == "__main__":
    global my_mouse
    my_mouse = MouseSE()
    file = open("letters10.txt", "r")
    words = sorted(file.readlines(), key=len, reverse=True)
    iterator = wordhuntsolver.WordHuntIterator(words, input("Give me letters: "), True)
    num = 0
    my_mouse.goto(130, 480)
    for i in iterator:
        num += 1
        my_mouse.press(False)
        print(i[1])
        for spot in i[0]:
            # time.sleep(0.2)
            goto_spot(spot)
            my_mouse.press(True)
        my_mouse.press(False)
    print(f"done with {num} words")
