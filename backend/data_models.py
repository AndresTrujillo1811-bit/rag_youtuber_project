from pydantic import Field
from lancedb.embeddings import get_registry
from lancedb.pydantic import Vector, LanceModel
from dotenv import load_dotenv


load_dotenv()
embedding_model = get_registry().get("gemini-text").create(name="gemini-embedding-001")

class TranscriptYT(LanceModel): 
    id: str
    content: str = embedding_model.SourceField()
    