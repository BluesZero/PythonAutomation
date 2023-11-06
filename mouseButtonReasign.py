from pynput.mouse import Listener, Button
from pynput.keyboard import Key, Controller

# Initialize the keyboard controller
keyboard = Controller()

# Define the key combination (Ctrl+Z) for the "Undo" action
keyCombination = [Key.ctrl, 'z']

# Function to be called when a mouse button is clicked
def onMouseClick(x, y, button, pressed):
    if pressed:
        # Check if the middle mouse button was clicked
        if button == Button.x1:
            # Simulate pressing Ctrl+Z (Undo) when the middle mouse button is clicked
            for key in keyCombination:
                keyboard.press(key)
            for key in reversed(keyCombination):
                keyboard.release(key)

# Set up the mouse listener to listen for clicks on the middle mouse button
def assignMouseButtons():
    with Listener(on_click=onMouseClick) as listener:
        listener.join()

if __name__ == "__main__":
    assignMouseButtons()
