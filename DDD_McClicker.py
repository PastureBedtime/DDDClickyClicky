import pyautogui
from PIL import ImageGrab
import time

# Target color in RGB
TARGET_COLOR = (228, 242, 114)  # RGB value of #E4F272

def find_color_on_screen(color):
    """ Function to find if a specific color is on the screen. """
    screen = ImageGrab.grab()
    width, height = screen.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            pixel_color = screen.getpixel((x, y))
            if pixel_color == color:
                return x, y
    return None

def auto_click_on_color(color):
    """ Function to continuously check for color and click when found. """
    while True:
        pos = find_color_on_screen(color)
        if pos:
            pyautogui.click(pos)
            print(f"Clicked at {pos}")
        time.sleep(0.01)  # Adjust sleep time as needed

if __name__ == "__main__":
    auto_click_on_color(TARGET_COLOR)
