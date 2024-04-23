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
        except Exception as e:
            logger.exception(f"Connect to Qdrant fail: {e}")

    def create_collection(self, collection_name):
        try:
            self.client.recreate_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=QdrantDBInfo.embed_size, distance=self.distance
                ),
            )
            logger.info(f"Collection {collection_name} created successfully!")
            return True
        except Exception as e:
            logger.exception(f"Create collection failed: {e}")
        return False
    
    def upsert_data(self, collection_name, data):
        try:
            response = self.client.upsert(
                collection_name=collection_name,
                points=models.Batch(**data),
            )
            if response.status == "completed":
                logger.info("Upsert data successfully!")
                return True
        except Exception as e:
            logger.exception("Error while upserting data: %s", e)
        logger.info("Upsert data failed!")
        return False

    def get_collection(self, collection_name):
        try: 
            return self.client.get_collection(collection_name=collection_name)
        except Exception:
            logger.exception(f"Get collection {collection_name} failed!")
        return None


if __name__=="__main__":
    qdrant_connection = QdrantConnection()
    qdrant_connection.create_collection("test")
    batch_data = {
        "ids": [1, 2, 3],
        "vectors": [[0.1, 0.2, 0.4], [0.3, 0.4, 0.5], [0.5, 0.6, 0.7]],
        "payloads": [
            {
                "text": "a",
                "title": "b",
                "url": "c",
            }
            for _ in range(0,3)
        ],
    }
    qdrant_connection.upsert_data("test", batch_data)
