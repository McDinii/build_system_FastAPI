from pydantic import BaseModel


class BuildName(BaseModel):
    """BuildName model used to validate the POST request data"""
    build: str
