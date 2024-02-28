from qdrant_client import QdrantClient, models
from src.config.qdrant_cfg import QdrantDBInfo
from loguru import logger


class QdrantConnection:
    def __init__(self) -> None:
        self.client = self.connect_qdrant()
        self.distance = (
            models.Distance.COSINE
            if QdrantDBInfo.metric_type == "COSINE"
            else models.Distance.EUCLID
        )

    def connect_qdrant(self):
        try: 
            return QdrantClient(QdrantDBInfo.path_qdrant_db)
        except Exception:
            logger.exception("Connect to Qdrant fail!")

    def create_collection(self, collection_name):
        try:
            self.client.recreate_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=QdrantDBInfo.embed_size, distance=self.distance
                ),
            )
        except Exception:
            logger.exception("Create collection failed!")

    def upsert_data(self, collection_name, data):
        self.client.upsert(
            collection_name=collection_name,
            points=models.Batch(
                **data
            ),
        )

    def get_collection(self, collection_name):
        try: 
            return self.client.get_collection(collection_name=collection_name)
        except Exception:
            logger.exception(f"Get collection {collection_name} failed!")


if __name__=="__main__":
    qdrant_connection = QdrantConnection()
    qdrant_connection.create_collection("test")
