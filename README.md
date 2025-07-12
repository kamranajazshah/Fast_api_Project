# 🛡️ Insurance Premium Category Predictor

This project is an end-to-end machine learning application built with **FastAPI** for the backend and **Streamlit** for the frontend. It predicts a user’s **insurance premium category** based on personal and lifestyle information such as age, weight, height, income, smoking habits, city, and occupation.

---

## 🚀 Features

- 🔍 FastAPI REST API for predictions
- 🧠 Machine Learning model trained using `scikit-learn`
- ⚙️ Pydantic-based schema validation with computed fields (BMI, age group, lifestyle risk)
- 🖼️ Streamlit frontend for easy interaction
- 📦 Docker-ready for deployment
- 📈 Swagger UI auto-generated at `/docs`

---

---

## 🔢 Input Parameters

| Parameter     | Type     | Description                                                                 |
|---------------|----------|-----------------------------------------------------------------------------|
| `age`         | `int`    | Age of the user (1–120)                                                     |
| `weight`      | `float`  | Weight in kilograms                                                         |
| `height`      | `float`  | Height in meters (e.g., 1.75)                                               |
| `income_lpa`  | `float`  | Annual income in LPA (Lakhs Per Annum)                                      |
| `smoker`      | `bool`   | Whether the user is a smoker                                                |
| `city`        | `str`    | City of residence                                                           |
| `occupation`  | `str`    | Must be one of: `retired`, `freelancer`, `student`, `government_job`, `business_owner`, `unemployed`, `private_job` |

---

## 🧪 Example Input

```json
{
  "age": 30,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 10,
  "smoker": false,
  "city": "Delhi",
  "occupation": "private_job"
}
## Example output
{
  "predicted_category": "Medium"
}

