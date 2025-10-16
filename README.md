#  Hearlytics

**Hearlytics** is a web application built using **Streamlit** that predicts the risk of **heart disease** based on user-provided health parameters.


##  Features
- Predicts heart disease using a trained **Deep Learning model** (`heart_disease_model.joblib`).
- Uses the health and lifestyle parameters
- Interactive and user-friendly interface built with **Streamlit**  
- Takes multiple health and lifestyle parameters as input  
- Provides instant prediction results with clear and intuitive messages  

##  Features Used in Prediction

The model predicts heart disease based on the following health and lifestyle parameters:

- **Age** — The person’s age in years.  
- **Gender** — Biological sex of the individual (Male/Female).  
- **Diabetes** — Indicates whether the person has diabetes or not.  
- **Health-Insurance** — Availability of health insurance coverage.  
- **Blood-Rel-Stroke** — Family history of stroke among blood relatives.  
- **Vigorous-work** — Engagement in high-intensity physical activities.  
- **Annual-Family-Income** — Total yearly income of the family.  
- **UricAcid** — Level of uric acid in the blood (mg/dL).  
- **Blood-Rel-Diabetes** — Family history of diabetes among blood relatives.  
- **Glucose** — Blood glucose level (mg/dL), indicating sugar concentration.  
- **Creatinine** — Serum creatinine level reflecting kidney function.  
- **Total-Cholesterol** — Total cholesterol level in the blood (mg/dL).  
- **Glycohemoglobin** — HbA1c level representing long-term glucose control.  
- **Lymphocyte** — Percentage of lymphocytes in total white blood cells.  
- **Platelet-count** — Number of platelets in the blood (10⁹/L).  
- **Cholesterol** — LDL/HDL ratio or specific cholesterol measurement.  
- **Moderate-work** — Frequency of moderate-intensity physical activities.  
- **Red-Cell-Distribution-Width (RDW)** — Variation in size of red blood cells.  
- **X60-sec-pulse** — Pulse rate measured over 60 seconds (beats per minute).  
- **HDL** — High-Density Lipoprotein ("good cholesterol") level (mg/dL).  
- **Diastolic** — Diastolic blood pressure (mmHg), the lower value in BP readings.  
- **Systolic** — Systolic blood pressure (mmHg), the upper value in BP readings.  
- **Monocyte** — Percentage of monocytes in total white blood cells.  
- **Eosinophils** — Percentage of eosinophil cells, associated with immune response.

>  These parameters collectively help the model evaluate cardiovascular health and estimate the likelihood of heart disease.


##  Technologies Used
- **Streamlit**
- **Python**
- **Deep Learning Models**
- **Machine Learning Models**
- **Joblib**

##  Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/meenakshi3151/Heartlytics.git
cd Heartlytics

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate     # On macOS/Linux
# venv\Scripts\activate      # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
streamlit run app.py
```

##  Deployed Link
Access the deployed site here:  
🔗 [https://meenakshi3151-heartlytics-app-ykjm7s.streamlit.app/](https://meenakshi3151-heartlytics-app-ykjm7s.streamlit.app/)


##  Contributions
We warmly welcome contributions to **Hearlytics**!  
If you find any bugs, issues, or have ideas to enhance the project, please follow these steps:

1. **Fork** the repository  
2. **Create a new branch** for your feature or fix  
3. **Make your changes** and test thoroughly  
4. **Submit a pull request** with a clear explanation of your contribution  

>  Every contribution—big or small—helps improve Hearlytics and supports better heart health predictions!
