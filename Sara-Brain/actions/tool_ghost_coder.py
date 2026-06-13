import os

def scaffold_workspace(root_path: str, structure: dict) -> str:
    """
    Accepts a root path and a dictionary mapping filenames to content strings. 
    It programmatically structures complete directories and populates complex boilerplates.
    """
    try:
        if not os.path.exists(root_path):
            os.makedirs(root_path)
            
        summary = []
        for filename, content in structure.items():
            full_path = os.path.join(root_path, filename)
            
            # Ensure subdirectories exist inside the workspace mapping
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            with open(full_path, "w", encoding="utf-8") as file:
                file.write(content)
            summary.append(f"Generated: {filename}")
            
        return "Workspace created successfully.\n" + "\n".join(summary)
    except Exception as e:
        return f"Error executing Ghost Coder workspace mapping: {str(e)}"
