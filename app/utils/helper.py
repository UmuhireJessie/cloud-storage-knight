from app.core.config import settings  # noqa
import boto3
from botocore.exceptions import NoCredentialsError
from typing import Generator
from app.db.session import SessionLocal

def upload_to_aws(file, filename):
    s3 = boto3.client('s3', aws_access_key_id=settings.ACCESS_KEY,
                      aws_secret_access_key=settings.SECRET_KEY)

    local_file_path = settings.LOCAL_FILE_PATH + filename
    print(local_file_path)
    print(file.file.name)
    destination = Path(local_file_path)

    with destination.open("wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        res = s3.upload_file(destination, settings.BUCKET_NAME, filename)
        os.remove(destination)
        print("Upload Successful")
        return (f"{filename} Upload Successful", res)
    except FileNotFoundError:
        print("The file was not found")
        return ("The file was not found")
    except NoCredentialsError:
        print("Credentials not available")
        return ("Credentials not available")
        

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



# uploaded = upload_to_aws('local_file', 'bucket_name', 's3_file_name')