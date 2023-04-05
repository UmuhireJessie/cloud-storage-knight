from typing import Any, Dict, Optional

from pydantic import BaseSettings, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    # The CONFIG_TYPE variable allows you to have different conditions for production, development and testing
    CONFIG_TYPE: str = "dev"

    # The application name is a unique identifier for the microservice
    APPLICATION_NAME: str = "cloud-storage-knight"

    # The API prefix is useful if we later have to have different versions of your microsevice
    API_PREFIX: str = "/api/v1"

    # CREDENIALS FOR UPLOADING FILE 
    ACCESS_KEY = 'AKIAUFHVNEVM7CH5RVN3'
    SECRET_KEY = 'CnIwfTa8550+z1bEZ4YqWYLOf090zp/WQdVe/WNY'

    # Temporary storage of uploaded files
    LOCAL_FILE_PATH: str="/home/jessie/Documents/Cloud/Assignments/cloud-storage-knight/"
    BUCKET_NAME: str = "knightsgroupbucket"

    # RELATION DTABASE POSTGRES CONFIGURATION
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "cloudstorage"
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):  # pragma: no cover
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True


settings = Settings()
