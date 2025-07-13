from fastapi import APIRouter
from models import FormData, FormDataResponse

router = APIRouter()

# Fake database (list)
form_db = []
next_id = 1

@router.post("/save", response_model=FormDataResponse)
def save_form_data(data: FormData):
    global next_id
    form_entry = FormDataResponse(id=next_id, **data.dict())
    form_db.append(form_entry)
    next_id += 1
    return form_entry

@router.get("/getAll", response_model=list[FormDataResponse])
def get_all_form_data():
    return form_db
