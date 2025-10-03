# train_clusters.py
import os
import logging
import pandas as pd
import pickle

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from pipeline import load_vaers_data, generate_ade_clusters

if __name__ == "__main__":
    try:
        data_dir = "data"
        if not os.path.isdir(data_dir):
            raise FileNotFoundError(f"Data directory '{data_dir}' not found")
        
        logger.info("Loading VAERS data (2020–2025)...")
        df = load_vaers_data(data_dir)
        
        logger.info(f"Loaded {len(df):,} reports. Generating ADE clusters...")
        cluster_df = generate_ade_clusters(df, batch_size=64, max_phrases=15000)
        
        if cluster_df.empty:
            logger.error("No clusters generated - check data quality")
            exit(1)
        
        # Save results
        with open("models/precomputed_clusters.pkl", "wb") as f:
            pickle.dump(cluster_df, f)
        
        cluster_df.to_csv("models/ade_clusters.csv", index=False)
        
        logger.info(f"✅ Saved {len(cluster_df):,} ADE clusters")
        logger.info("Cluster distribution:")
        print(cluster_df['cluster'].value_counts())
        
    except Exception as e:
        logger.error(f"Training failed: {e}")
        print("Check logs for details")