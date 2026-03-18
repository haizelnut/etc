import os
import shutil
from pathlib import Path

def organize_downloads():
    downloads = Path.home() / "Downloads"
    
    categories = {
        'Images': ['.jpg', '.png', '.gif', '.jpeg'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Archives': ['.zip', '.rar', '.7z']
    }
    
    for file in downloads.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            
            for category, extensions in categories.items():
                if ext in extensions:
                    dest = downloads / category
                    dest.mkdir(exist_ok=True)
                    shutil.move(str(file), str(dest / file.name))
                    print(f"✅ {file.name} → {category}/")
                    break

if __name__ == "__main__":
    organize_downloads()
    print("🎉 Done!")
