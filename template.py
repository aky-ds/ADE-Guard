"""
Template scaffolding script for ADEGuard project.

This script generates a clean directory + file structure for the full ADEGuard pipeline:
- Real-time severity triage UI (Streamlit)
- Annotation / Weak Supervision / NER / Classifier / Clustering Modules
- Configs & Utilities

Run:
    python template.py

It will safely create missing folders and files without overwriting existing ones.
"""

import os
from pathlib import Path

# ✅ Project scaffold definition
list_of_paths = [
    # Core data folders
    'data/',
    'models/',
    'logs/',

    # Core app components
    'app.py',
    'pipeline.py',
    'requirements.txt',
    'setup.py',
    'README.md',

    # Supporting modules
    'utils/__init__.py',
    'utils/load_vaers.py',
    'utils/text_utils.py',

    # Annotation & labeling
    'annotation/',
    'annotation/guidelines.md',
    'annotation/make_gold.py',

    # Weak supervision and labeling
    'weak_supervision.py',

    # Model training modules
    'ner/train_ner.py',
    'classifier/train_classifier.py',
    'clusters/train_clusters.py',

    # Explainability
    'explain/shap_explainer.py',

    # Configs
    'configs/model_config.yaml'
]

for path in list_of_paths:
    path = Path(path)

    if path.suffix == "":  # Directory (no file extension)
        os.makedirs(path, exist_ok=True)
        print(f"📁 Created directory: {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            with open(path, 'w') as f:
                pass
            print(f"📄 Created file: {path}")
        else:
            print(f"✅ Skipped (already exists): {path}")
