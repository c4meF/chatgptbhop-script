import time
import threading
import keyboard

# Global flag to indicate if auto-press is active
active = False

def auto_press_space():
    # Keep sending the space key every 50ms while active is True
    while active:
        keyboard.send('space')
        time.sleep(0.05)

def on_space_down(event):
    global active
    # If not already active, start auto pressing
    if not active:
        active = True
        # Start the auto press in a separate thread
        threading.Thread(target=auto_press_space, daemon=True).start()

def on_space_up(event):
    global active
    # Stop the auto press when space is released
    active = False

# Set up event handlers for pressing and releasing the space bar
keyboard.on_press_key('space', on_space_down)
keyboard.on_release_key('space', on_space_up)

print("Hold down the space bar to auto-press space every 50ms. Release to stop.")
print("Press ESC to exit the program.")

# Wait for the ESC key to exit the program
keyboard.wait('esc')
