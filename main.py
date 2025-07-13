from fastapi import FastAPI
from routes import form_data

app = FastAPI(title="KPA Form Data API")

app.include_router(form_data.router, prefix="/formData", tags=["Form Data"])

