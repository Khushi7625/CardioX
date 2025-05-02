
from django.shortcuts import render
import pickle
import numpy as np
import pandas as pd
from .forms import HeartDiseaseForm
from .forms import HeartDiseasePredictorForm
import os
import sys

# Create your views here.
def homepage(request):
    return render(request, 'home.html')
def predictor(request):
    return render(request, 'predict.html')
def about(request):
    return render(request, 'about.html')
def predict_1(request):
    return render(request,'predict_1.html')
def predict_2(request):
    return render(request,'predict_2.html')

# Load the trained model


def predictor_view_2(request):
    model_path=r"C:\Users\khush\OneDrive\Documents\Desktop\heart prediction\heart_disease\predictor\model\heart_model_2.pkl"
    if not os.path.exists(model_path):
          raise FileNotFoundError(f"🚨 Model file not found at: {model_path}.\nPlease check if 'heart_model_2.pkl' exists!")

    with open(model_path, "rb") as file:
          model = pickle.load(file)
    prediction = None

    if request.method == 'POST':
        print(request.POST)  # To check if data is being received
        print(prediction) 
        form = HeartDiseaseForm(request.POST)


        if form.is_valid():
            print("✅ Form is valid")
            data = np.array([
                form.cleaned_data['age'],
                int(form.cleaned_data['sex']),  # Convert ChoiceField to int
                form.cleaned_data['cp'],
                form.cleaned_data['trestbps'],
                form.cleaned_data['chol'],
                int(form.cleaned_data['fbs']),  # Convert ChoiceField to int
                form.cleaned_data['restecg'],
                form.cleaned_data['thalach'],
                int(form.cleaned_data['exang']),  # Convert ChoiceField to int
                form.cleaned_data['oldpeak'],
                form.cleaned_data['slope'],
                form.cleaned_data['ca'],
                form.cleaned_data['thal']
            ]).reshape(1, -1)


            # Predict using the ML model
            prediction = model.predict(data)[0]  # Output: 1 (High Risk) or 0 (Low Risk)


        else:
            print("❌ Form Validation Failed:", form.errors)  # Debugging

    else:
        print("📩 Received GET request")
        form = HeartDiseaseForm()
    print(f"🎯 Sending Prediction to Template: {prediction}")
    return render(request, "predict_2.html", {"form": HeartDiseaseForm(), "prediction": prediction})





# Paths to model files



def predictor_view_1(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    MODEL_PATH = os.path.join(BASE_DIR, "predictor", "model", "heart_model.pkl")
    ENCODER_PATH = os.path.join(BASE_DIR, "predictor", "model", "onehot_encoder.pkl")
    COLUMNS_PATH = os.path.join(BASE_DIR, "predictor", "model", "column_order.pkl")
    # Load model, encoder, and columns  
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    
    with open(ENCODER_PATH, "rb") as f:
        encoder = pickle.load(f)

    with open(COLUMNS_PATH, "rb") as f:
        column_order = pickle.load(f)

    prediction = None
    result = ""
    if request.method == 'POST':
        form = HeartDiseasePredictorForm(request.POST)
        if form.is_valid():
            #cd = form.cleaned_data
            data = {
            'bmi': float(request.POST.get('bmi')),
            'smoking': int(request.POST.get('smoking')),
            'AlcoholDrinking': int(request.POST.get('AlcoholDrinking')),
            'stroke': int(request.POST.get('stroke')),
            'physical_health': float(request.POST.get('physical_health')),
            'mental_health': float(request.POST.get('mental_health')),
            'diff_walking': int(request.POST.get('diff_walking')),
            'sex': int(request.POST.get('sex')),
            'age_category': int(request.POST.get('age_category')),
            'race': request.POST.get('race'),
            'diabetic': int(request.POST.get('diabetic')),
            'physical_activity': int(request.POST.get('physical_activity')),
            'gen_health': int(request.POST.get('gen_health')),
            'sleep_time': float(request.POST.get('sleep_time')),
            'asthma': int(request.POST.get('asthma')),
            'kidney_disease': int(request.POST.get('kidney_disease')),
            'skin_cancer': int(request.POST.get('skin_cancer'))
        }
            input_data = pd.DataFrame([data])
            
            # 🔍 Check raw form input
            print("Raw Input Data:\n", input_data)

            # Encoding categorical columns
            cat_cols = input_data.select_dtypes(include='object').columns
            encoded_data = encoder.transform(input_data[cat_cols])
            encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(cat_cols))
            
            # Combine numerical + encoded
            final_input = pd.concat([input_data.drop(columns=cat_cols).reset_index(drop=True), encoded_df], axis=1)
            final_input = final_input.reindex(columns=column_order, fill_value=0)

            # 🔍 Check final input to model
            print("Final Input to Model:\n", final_input)

            # 🔍 Check predicted probabilities
            print("Model Probabilities:\n", model.predict_proba(final_input))

            prediction = model.predict(final_input)[0]
            print("Model Prediction (0 = low, 1 = high):", prediction)

            result = "HAS heart disease" if prediction == 1 else "does NOT have heart disease"
    else:
        form = HeartDiseasePredictorForm()
    
    return render(request, "predict_1.html", {"form": form, "prediction": prediction})













