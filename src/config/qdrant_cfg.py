import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class QdrantDBInfo:
    path_qdrant_db: str = os.getenv("QDRANT_URL")
    embed_size = 786
    # The most typical metric used in similarity learning models is the cosine metric
    metric_type = "COSINE"
