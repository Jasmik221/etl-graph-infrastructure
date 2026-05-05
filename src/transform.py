import pandas as pd
from pathlib import Path

# Define input and output directories
RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

# Create processed directory if it does not exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load raw datasets
nodes = pd.read_csv(RAW_DIR / "nodes.csv")
edges = pd.read_csv(RAW_DIR / "edges.csv")

# ---------------------------------------------------
# STEP 1: Remove duplicated nodes
# ---------------------------------------------------
# Duplicate node IDs may cause issues during graph import
nodes = nodes.drop_duplicates(subset=["id"])

# ---------------------------------------------------
# STEP 2: Validate edge references
# ---------------------------------------------------
# Keep only edges where both source and target nodes exist

valid_node_ids = set(nodes["id"])

edges = edges[
    edges["source"].isin(valid_node_ids)
    & edges["target"].isin(valid_node_ids)
].copy()

# ---------------------------------------------------
# STEP 3: Standardize column names
# ---------------------------------------------------
# Rename columns to make them compatible with Neo4j import

nodes = nodes.rename(columns={
    "id": "node_id"
})

# ---------------------------------------------------
# STEP 4: Save processed datasets
# ---------------------------------------------------
# Export cleaned and validated data for graph import

nodes.to_csv(
    PROCESSED_DIR / "processed_nodes.csv",
    index=False
)

edges.to_csv(
    PROCESSED_DIR / "processed_edges.csv",
    index=False
)

# ---------------------------------------------------
# Final summary
# ---------------------------------------------------

print("Transformation completed successfully.")
print(f"Total processed nodes: {len(nodes)}")
print(f"Total processed edges: {len(edges)}")