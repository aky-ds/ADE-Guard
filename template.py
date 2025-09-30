import os
from pathlib import Path
list_of_files=[
    'data/',
    'requirements.txt',
    'setup.py',
    'pipeline.py',
    'models/'
    'app.py'
]

for file in list_of_files:
    file_path=Path(file)
    file_dir,file_name=os.path.split(file_path)
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
    
    if not os.path.exists(file_path):
        with open(file_path,'w') as f:
            pass