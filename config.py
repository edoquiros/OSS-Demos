# config.py  — single source of truth for paths
UC_SERVER    = "http://localhost:8080/api/2.1/unity-catalog"
UC_CATALOG   = "demo_catalog"
DELTA_BASE   = "file:///tmp/uc_storage"   # swap for s3:// or abfs:// in prod

VOLUMES_PATH = f"{DELTA_BASE}/ingestion/raw_docs"
CHUNKS_PATH  = f"{DELTA_BASE}/ingestion/parsed_chunks"
EMBEDDINGS_PATH = f"{DELTA_BASE}/ingestion/embedded_chunks"

MLFLOW_URI   = "http://localhost:5000"
OS_HOST      = "localhost"
OS_PORT      = 9200
OS_INDEX     = "doc_chunks"