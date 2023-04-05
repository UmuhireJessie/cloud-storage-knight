from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
import uuid
from app.utils.helper import upload_to_aws, get_db


router = APIRouter()

@router.post("/")
async def upload_file(
        upload_document: UploadFile = File(...),
        db: Session = Depends(get_db),
):
    """
    Upload a document on AWS
    """

    minio_path = upload_to_aws(upload_document, upload_document.filename)

    # db_obj = self.model(**obj_in_data)  # type: ignore
    # db.add(db_obj)
    # db.commit()
    # db.refresh(db_obj)

    # return db_obj

    return {
        "status": "success",
        "data": minio_path
    }