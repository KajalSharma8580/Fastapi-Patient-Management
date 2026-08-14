# FastAPI Patient Management System 🏥

A simple **Patient Management REST API** built using **FastAPI, Python, Pydantic, and JSON**.

This project provides APIs to create, view, update, sort, and delete patient records. It also uses Pydantic models for data validation and automatically calculates **BMI** and **BMI-based health verdicts**.

## 🚀 Features

* Create new patient records
* View all patients
* View a specific patient by ID
* Update existing patient information
* Delete patient records
* Sort patients by:

  * Height
  * Weight
  * BMI
* Automatic BMI calculation
* Automatic BMI health verdict
* Request validation using Pydantic
* HTTP exception handling
* Interactive API documentation using Swagger UI
* JSON-based data storage

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Pydantic**
* **Uvicorn**
* **JSON**
* **Git & GitHub**

## 📁 Project Structure

```text
Fastapi-Patient-Management/
│
├── main.py
├── patients.json
├── README.md
├── .gitignore
└── myenv/
```

> `myenv/` should not be uploaded to GitHub. Add it to `.gitignore`.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/KajalSharma8580/Fastapi-Patient-Management.git
```

### 2. Navigate to the project

```bash
cd Fastapi-Patient-Management
```

### 3. Create a virtual environment

```bash
python -m venv myenv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\myenv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

## ▶️ Run the Application

Start the FastAPI server using:

```bash
python -m uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

You can directly test all API endpoints from the browser.

### ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

FastAPI generates these interactive documentation interfaces automatically from the API definition.

## 🔗 API Endpoints

| Method | Endpoint                | Description                |
| ------ | ----------------------- | -------------------------- |
| GET    | `/`                     | Check API status           |
| GET    | `/about`                | Get API information        |
| GET    | `/view`                 | View all patients          |
| GET    | `/patient/{patient_id}` | Get a patient by ID        |
| GET    | `/sort`                 | Sort patients              |
| POST   | `/create`               | Create a new patient       |
| PUT    | `/edit/{patient_id}`    | Update patient information |
| DELETE | `/delete/{patient_id}`  | Delete a patient           |

## 🧑‍⚕️ Patient Data Model

A patient contains:

```text
id
name
city
age
gender
height
weight
```

The API automatically calculates:

```text
BMI = weight / (height²)
```

The BMI result is then used to generate a health verdict:

* **Underweight** → BMI < 18.5
* **Normal** → BMI 18.5–24.9
* **Overweight** → BMI 25–29.9
* **Obese** → BMI ≥ 30

## 📝 Example: Create Patient

### Request

```http
POST /create
```

### JSON Body

```json
{
    "id": "P001",
    "name": "Aarav Sharma",
    "city": "Delhi",
    "age": 28,
    "gender": "male",
    "height": 1.75,
    "weight": 70
}
```

The API validates the request using Pydantic before storing the patient data.

## 📊 Example Response

```json
{
    "message": "patient created successfully"
}
```

## 🔍 Example: Get Patient

```http
GET /patient/P001
```

Example response:

```json
{
    "name": "Aarav Sharma",
    "city": "Delhi",
    "age": 28,
    "gender": "male",
    "height": 1.75,
    "weight": 70,
    "bmi": 22.86,
    "verdict": "Normal"
}
```

## 🎯 Learning Outcomes

Through this project, I practiced:

* Building REST APIs with FastAPI
* Creating Pydantic data models
* Request validation
* Path parameters
* Query parameters
* CRUD operations
* HTTP status codes
* Exception handling
* JSON file handling
* Computed fields
* API documentation with Swagger UI
* Git and GitHub

## 🔮 Future Improvements

* Connect the application to MySQL/PostgreSQL
* Add user authentication and authorization
* Add JWT-based security
* Add database models using SQLAlchemy
* Add automated testing with Pytest
* Deploy the API using a cloud platform
* Add frontend interface for patient management

## 👩‍💻 Author

**Kajal Sharma**

GitHub: [KajalSharma8580](https://github.com/KajalSharma8580)

## 📄 License

This project is created for educational and learning purposes.
