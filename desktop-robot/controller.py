def pressed_keys_handler(pressed_keys):
    if 'H' in pressed_keys:
        print("PRESSED H")
    if 'L' in pressed_keys:
        print("PRESSED L")

    if 'Up' in pressed_keys:
        print("PRESSED UP")
    elif 'Down' in pressed_keys:
        print("PRESSED DOWN")

    if 'W' in pressed_keys and 'A' in pressed_keys:
        print("PRESSED W and A")

    elif 'W' in pressed_keys and 'D' in pressed_keys:
        print("PRESSED W and D")

    elif 'S' in pressed_keys and 'A' in pressed_keys:
        print("PRESSED S and A")

    elif 'S' in pressed_keys and 'D' in pressed_keys:
        print("PRESSED S and D")

    elif 'W' in pressed_keys and 'S' in pressed_keys:
        print("PRESSED W and S")

    elif 'W' in pressed_keys:
        print("PRESSED W")

    elif 'A' in pressed_keys:
        print("PRESSED A")

    elif 'S' in pressed_keys:
        print("PRESSED S")

    elif 'D' in pressed_keys:
        print("PRESSED D")

    elif 'Left' in pressed_keys and 'Right' in pressed_keys:
        print("PRESSED LEFT and RIGHT")

    elif 'Left' in pressed_keys:
        print("PRESSED LEFT")

    elif 'Right' in pressed_keys:
        print("PRESSED RIGHT")

