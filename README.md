
 💼 Employee Salary Prediction App

This web application predicts an employee's salary based on their **education level**, **age**, and **occupation** using a pre-trained machine learning model. Built with Streamlit, it's simple, interactive, and user-friendly.

 🔍 Overview

- 📚 Input: Education Level, Age, and Occupation
- 🧠 Model: Trained using Scikit-learn
- 📈 Output: Predicted annual salary in Indian Rupees (₹)
- 💻 Interface: Built using Streamlit

 🧰 Technologies Used

- Python 3.x  
- Streamlit  
- scikit-learn  
- NumPy  
- joblib  

 📁 Project Files



Employee Salary Prediction/
│
├── app.py               # Streamlit application script
├── best\_model.pkl       # Trained machine learning model
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies (optional)



 ⚙️ How to Run the App

1. Install dependencies:

pip install streamlit scikit-learn joblib numpy


2. Run the application:

streamlit run app.py

3. Access the app in your browser:

http://localhost:8501


🧪 Example

 👤 Input:

* Education Level: Master
* Age: 28
* Occupation: Data Scientist

 💰 Output:

✅ Predicted Salary: ₹ 7,85,432.50




 📝 Notes

* Ensure the model file `best_model.pkl` exists in the project directory.
* The `app.py` uses label encoding for categorical inputs — update the mappings if your model uses different encoding.
* You can customize the UI further using Streamlit widgets and styling.






