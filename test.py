# debug_import.py
try:
    import pipeline
    print("✅ pipeline imported successfully!")
    print("Functions available:", [name for name in dir(pipeline) if not name.startswith('_')])
except Exception as e:
    print("❌ FAILED to import pipeline")
    print("Error:", e)
    import traceback
    traceback.print_exc()