from pydantic import BaseModel
from typing import List, Optional


class Response(BaseModel):
    id: str
    file_name: str
    file_link: str
    updated_at: date
    created_at: date

    class Config:
        schema_extra = {
            "example": {
                "id": "a4ae83e2-1618-46b1-9111-57f84da99e07",
                "file_name": "file.txt",
                "file_link": "https://www.aws.com/example-link",
                "updated_at": "2023-04-07",
                "created_at": "2023-04-07",
            }
        }
        orm_mode = True



class FileResponseModel(BaseModel):
    status: str
    data: Response

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "data": {
                    "id": "a4ae83e2-1618-46b1-9111-57f84da99e07",
                    "file_name": "file.txt",
                    "file_link": "https://www.aws.com/example-link",
                    "updated_at": "2023-04-07",
                    "created_at": "2023-04-07",
                },
            }
        }


class FileCreate(BaseModel):
    pass
    # id: str
    # name: str

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "id": "AIRTEL-RW",
    #             "name": "Airtel Rwanda",
    #         }
    #     }

class AllFileModel(BaseModel):
    status: str
    data: Optional[List[Response]]

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "data": [
                    {
                        "id": "a4ae83e2-1618-46b1-9111-57f84da99e07",
                        "file_name": "file.txt",
                        "file_link": "https://www.aws.com/example-link",
                        "updated_at": "2023-04-07",
                        "created_at": "2023-04-07",
                    }
                ],
            }
        }

class ErrorModel(BaseModel):
    status: str
    data: dict

    class Config:
        schema_extra = {
            "example": {
                "status": "error",
                "data": {"message": "<REASON FOR THE ERROR>"},
            }
        }


class MNOFailModel(BaseModel):
    status: str
    data: dict

    class Config:
        schema_extra = {
            "example": {"status": "fail", "data": {"message": "<REASON FOR FAILING>"}}
        }
