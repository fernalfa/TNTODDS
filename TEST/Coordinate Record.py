from pynput import mouse

click_positions = []


def on_click(x, y, button, pressed):
    if pressed:
        click_positions.append((x, y))


def main():
    print("Click positions recorder started. Press Ctrl+C to stop.")
    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            pass
    print("Recording stopped.")

    with open("click_positions.txt", "w") as file:
        for position in click_positions:
            file.write(f"{position[0]}, {position[1]}\n")

    print("Click positions saved to 'click_positions.txt'.")


if __name__ == "__main__":
    main()
