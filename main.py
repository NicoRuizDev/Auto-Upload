# Import the required libraries
import pyautogui
import keyboard

# Define the function to be called when "ctrl + prtscn" is pressed
def on_press_func():
    # Import the necessary libraries for requests and handling response data
    import requests
    import pyperclip
    import json
    
    # Take a screenshot using pyautogui and save it as a PNG file
    im = pyautogui.screenshot()
    im.save("screenshot.png")
    
    # Notify that "ctrl + prtscn" has been pressed
    print("Ctrl + PrintScrn Pressed!")
    
    # Define the API endpoint for uploading the screenshot
    url = "https://cdn.nicoruiz.dev/api/upload"
    file_path = "screenshot.png"

    # Open the screenshot file in binary mode and send a POST request to the API
    with open(file_path, 'rb') as f:
        files = {'myFile': f}
        response = requests.post(url, files=files)
    
    # Extract the relevant information from the API response
    data = response.json()
    file_link = data['data']['fileLink']
    file_size = data['data']['fileSize']
    file_name = data['data']['fileName']
    
    # Print the extracted information
    print("File link:", file_link)
    print("File size:", file_size)
    print("File name:", file_name)
    
    # Copy the file link to the clipboard
    pyperclip.copy(file_link)

# Register the function to be called when the key combination is pressed
keyboard.add_hotkey("ctrl+prtscn", on_press_func)

# Start listening for key presses
keyboard.wait()
