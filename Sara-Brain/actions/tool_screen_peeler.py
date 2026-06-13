import pyautogui
import google.generativeai as genai
import os
from PIL import Image

def extract_text_from_screen() -> str:
    """
    Captures a full screenshot and uses Gemini Vision to parse and explain it.
    Replaces basic local OCR with advanced multimodal context.
    """
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
             return "Error: GEMINI_API_KEY is not set in environment variables. Please add it to your .env file."
        genai.configure(api_key=api_key)

        screenshot_path = "temp_ocr_capture.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        
        # Use gemini flash for fast vision processing
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        img = Image.open(screenshot_path)
        response = model.generate_content(["Extract all structural text and describe the layout and context from this UI screenshot.", img])
        
        return f"--- Extracted Screen Data via Gemini Vision ---\n{response.text}"
    except Exception as e:
        return f"Error executing Multimodal Screen Peeler: {str(e)}"
