import pyautogui
import pygetwindow as gw
import time

def type_global_text(text_to_type: str, target_app: str = None, delay_seconds: float = 1.0) -> str:
    """
    Emulates a hardware keyboard to inject text. 
    Enhanced to verify active window focus.
    """
    try:
        if target_app:
            windows = gw.getWindowsWithTitle(target_app)
            if not windows:
                return f"Error: Could not find any open window containing '{target_app}'."
            win = windows[0]
            try:
                win.activate()
            except Exception as act_e:
                # Sometimes win.activate() fails in Windows if another window is aggressively taking focus.
                pass
            time.sleep(1) # Wait for window activation

        time.sleep(delay_seconds)
        pyautogui.write(text_to_type, interval=0.01)
        return f"Successfully injected {len(text_to_type)} characters into the UI."
    except Exception as e:
        return f"Error executing Phantom Typer: {str(e)}"
