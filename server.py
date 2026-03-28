from datetime import datetime, UTC
from scripts.run_pipeline import run_pipeline

print("\n[GitHub Action] Pipeline started at:", datetime.now(UTC))

try:
    run_pipeline()
    print("[GitHub Action] Pipeline finished successfully")
except Exception as e:
    print("[GitHub Action] Pipeline error:", e)
    raise e