##  <img src="https://media.tenor.com/Wq-8a2yGCSkAAAAi/stethoscope-stethoscope-images.gif" width="48" height="48"> Doctor Fee Prediction
This project aims to create a web interface that allows users to predict doctor consultation fees based on their input. The machine learning model was trained on a dataset obtained by scraping data from the Practo website using Selenium. With the use of Python Pandas, the scraped data was thoroughly cleaned & preprocessed for accurate predictions.
##  <img src="https://user-images.githubusercontent.com/106439762/181935629-b3c47bd3-77fb-4431-a11c-ff8ba0942b63.gif" width="48" height="48"> **User's Manual**

| Files/Folder| Description |
| ------------- | ------------- |
| **Dataset Folder** | This folder provides data state wise and district wise data in csv format |
| **Python File** | This contains the .ipynb file of the analysis for Data Extract, Data cleaning, EDA and ML Models.  |

<br>

<p align="center"><img src="https://i.pinimg.com/originals/13/66/c9/1366c95f8c249b8422d2caaae287cb63.gif" width="400" ></p>

   
## Findings from the Doctor Fee Prediction Project 🧪

- According to the Practo dataset, Bangalore has the highest number of doctors.

  ![Screenshot 2023-08-09 233443](https://github.com/ankitpal154/Doctor_fees_prediction_ML_project/assets/139064260/4eba4a20-39cc-4798-98f7-c4b8c8b64c09)

  
- The most common degrees among doctors are MBBS, MD, and BDS, with the highest representation in the dataset.


  ![Screenshot 2023-08-09 233626](https://github.com/ankitpal154/Doctor_fees_prediction_ML_project/assets/139064260/5949c211-4fd8-4e0f-b9e5-eff349eace32)

- The dataset indicates that the three most prominent specialties among doctors are:
  - Dentist
  - Gynecologist
  - Pediatrician
 


   ![Screenshot 2023-08-09 233739](https://github.com/ankitpal154/Doctor_fees_prediction_ML_project/assets/139064260/26f61e31-0e63-4120-a245-5a8f15a4f75f)

 <br>


## 🏥 Doctor Fee Prediction ML Model Creation Steps 🧠


![Screenshot 2023-08-09 233938](https://github.com/ankitpal154/Doctor_fees_prediction_ML_project/assets/139064260/1580c2f7-4a16-497e-a620-bca0f9a9d749)

**1. Data Collection:** Gathered doctor-related information from Practo using web scraping techniques with Selenium.

**2. Data Preprocessing:** Conducted thorough data cleaning, handling missing values, and transforming categorical variables into numerical representations.

**3. Feature Engineering:** Derived additional relevant features from the existing dataset, such as extracting qualifications.

**4. Model Selection:** Explored various regression algorithms and selected potential candidates based on initial performance evaluation.

**5. Hyperparameter Tuning:** Utilized GridSearchCV to fine-tune hyperparameters for each selected model, optimizing their performance.

**6. Model Training:** Trained multiple models on the dataset with the tuned hyperparameters to improve predictive accuracy.

**7. Weighted Voting:** Implemented a Weighted Voting technique, combining predictions from multiple models, each with a specific weight.

**8. Model Evaluation:** Evaluated the ensemble model using appropriate metrics such as Mean Absolute Error (MAE) or Root Mean Squared Error (RMSE) to measure prediction accuracy.


![Screenshot 2023-08-09 234117](https://github.com/ankitpal154/Doctor_fees_prediction_ML_project/assets/139064260/0f0c70f0-fe2b-45fd-b63e-481f91cf0311)


![Screenshot 2023-08-09 234154](https://github.com/ankitpal154/Doctor_fees_prediction_ML_project/assets/139064260/799feea6-a700-480b-b23c-5d07a9ed91ce)


**9. Web App Development:** Developed a user-friendly web application using Flask, HTML, and CSS to offer an intuitive interface for users to input parameters.

## 🏥 Doctor Fee Prediction Web application

 <p align="center"><img src="https://github.com/Sannidhi-Shetty2/Doctor-Fee-Prediction/assets/62684303/92d53380-68d4-4289-8d43-4e386d3b2025" width="500" ></p>
 
