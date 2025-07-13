#  KPA Form Data API – Backend Assignment

This project is a backend assignment that implements two APIs using **FastAPI** and **PostgreSQL**, based on the provided Postman collection and Swagger documentation.

---

##  Tech Stack

- **Backend:** Python + FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **API Docs:** Swagger UI (`/docs`)
- **Testing:** Swagger + Postman

---

##  Implemented Endpoints

| Method | Endpoint              | Description              |
|--------|------------------------|--------------------------|
| POST   | `/formData/save`       | Save form submission     |
| GET    | `/formData/getAll`     | Retrieve all submissions |

---

##  Project Structure

kpa_api_project/
├── main.py # FastAPI app entry point
├── database.py # DB connection setup
├── models.py # SQLAlchemy + Pydantic models
├── routes/
│ └── form_data.py # Form-related endpoints
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── KPA_form_data_tested.postman_collection.json # Postman test file

##  How to Run This Project

1. Clone the Project


git clone https://github.com/saiprasadgijja45/kpa-form-data-api.git
cd kpa-form-data-api

2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate     # Windows

3. Install Dependencies
   pip install -r requirements.txt
4. Setup PostgreSQL Database
   Create a PostgreSQL DB: kpa_db
   Update your DB URL inside database.py:
   SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@localhost/kpa_db"
5. Run the API Server
   uvicorn main:app --reload
Visit: http://127.0.0.1:8000/docs to explore the APIs

Testing the APIs
  Swagger UI: Visit http://127.0.0.1:8000/docs
  Postman: Import KPA_form_data_tested.postman_collection.json

Author
Sai Prasad Gijja
Python Developer | Hyderabad
GitHub: @saiprasadgijja45




