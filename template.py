import os
from pathlib import Path

# ✅ Fixed: added missing commas + converted directories to explicit handling
list_of_paths = [
    'data/',
    'models/',
    'app.py',
    'pipeline.py',
    'requirements.txt',
    'setup.py',
    'utils/__init__.py',          # example nested directory & file
    'utils/load_vaers.py',
    'annotation/',
    'clusters/',
    'classifier/',
    'ner/',
    'explain/',
    'configs/model_config.yaml',
    'README.md'
]

for path in list_of_paths:
    path = Path(path)

    if path.suffix == "":  # ✅ No file extension → treat as directory
        os.makedirs(path, exist_ok=True)
        print(f"📁 Created directory: {path}")
    else:
        # Ensure parent directory exists before creating file
        path.parent.mkdir(parents=True, exist_ok=True)

        # Create file only if it doesn't already exist
        if not path.exists():
            with open(path, 'w') as f:
                pass
            print(f"📄 Created file: {path}")
        else:
            print(f"✅ Skipped (already exists): {path}")
