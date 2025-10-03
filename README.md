# ADEGuard – Real-Time Adverse Drug Event (ADE) Severity Triage

ADEGuard is an end-to-end AI pipeline designed to:

✅ Predict **severity of adverse drug events (mild / moderate / severe)** in **real time**  
✅ Provide **token-level NER highlighting** (ADE spans, drugs, modifiers)  
✅ Offer **explainability (rule-based + SHAP)** for clinical auditability  
✅ Automatically **cluster symptom narratives** to reveal safety signals  
✅ Support **human annotation + weak supervision + model training**

---

## 🚀 System Overview

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Data Loader** | `utils/load_vaers.py` | Merges VAERSDATA + SYMPTOMS + VAX across years |
| **Annotation Module** | Label Studio-compatible | Create gold ADE / DRUG labeled samples |
| **Weak Supervision** | `weak_supervision.py` | Auto-label severity from structured VAERS fields |
| **NER Training** | BioBERT / SciBERT Token Classification | Extract ADE & Drug mentions |
| **Severity Classifier** | Transformer Fine-Tuning | Predict likelihood of hospitalization / severe outcomes |
| **Clustering (Signal Detection)** | SBERT + HDBSCAN + UMAP | Group recurring ADE patterns |
| **Explainability** | Rule-Based & SHAP | Justify every prediction |
| **Frontend UI** | Streamlit (`app.py`) | Real-Time Clinical Triage Tool |

---

## 🛠️ Quickstart

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Scaffold all directories (optional)
python template.py

# 3. Merge VAERS data into unified dataset
python -c "from utils.load_vaers import load_vaers_dataset; df = load_vaers_dataset('data'); df.to_csv('data/vaers_full.csv', index=False)"

# 4. Train models (optional stages)
python ner/train_ner.py
python classifier/train_classifier.py
python clusters/train_clusters.py

# 5. Launch App
streamlit run app.py
