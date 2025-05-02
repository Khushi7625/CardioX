from django import forms

class HeartDiseaseForm(forms.Form):
    age = forms.IntegerField(label="Age", min_value=0, required=True)
    sex = forms.ChoiceField(label="Sex", choices=[(1, "Male"), (0, "Female")], required=True)
    cp = forms.IntegerField(label="Chest Pain Type", min_value=0, required=True)
    trestbps = forms.IntegerField(label="Resting Blood Pressure", min_value=0, required=True)
    chol = forms.IntegerField(label="Cholesterol", min_value=0, required=True)
    fbs = forms.ChoiceField(label="Fasting Blood Sugar", choices=[(1, "Yes"), (0, "No")], required=True)
    restecg = forms.IntegerField(label="Resting ECG", min_value=0, required=True)
    thalach = forms.IntegerField(label="Maximum Heart Rate", min_value=0, required=True)
    exang = forms.ChoiceField(label="Exercise Induced Angina", choices=[(1, "Yes"), (0, "No")], required=True)
    oldpeak = forms.FloatField(label="Oldpeak", required=True)
    slope = forms.IntegerField(label="Slope", min_value=0, required=True)
    ca = forms.IntegerField(label="Number of Major Vessels", min_value=0, required=True)
    thal = forms.IntegerField(label="Thal", min_value=0, required=True)


class HeartDiseasePredictorForm(forms.Form):
    BMI = forms.FloatField(label="BMI", required=True)
    Smoking = forms.ChoiceField(label="Smoking", choices=[("Yes", "Yes"), ("No", "No")], required=True)
    AlcoholDrinking = forms.ChoiceField(label="Alcohol Drinking", choices=[("Yes", "Yes"), ("No", "No")], required=True)
    Stroke = forms.ChoiceField(label="Stroke", choices=[("Yes", "Yes"), ("No", "No")], required=True)
    PhysicalHealth = forms.IntegerField(
        label="Physical Health (days of poor health in last 30 days)", min_value=0, max_value=30, required=True
    )
    MentalHealth = forms.IntegerField(
        label="Mental Health (days of poor mental health in last 30 days)", min_value=0, max_value=30, required=True
    )
    DiffWalking = forms.ChoiceField(label="Difficulty Walking", choices=[("Yes", "Yes"), ("No", "No")], required=True)
    Sex = forms.ChoiceField(label="Sex", choices=[("Male", "Male"), ("Female", "Female")], required=True)
    AgeCategory = forms.ChoiceField(
        label="Age Category",
        choices=[
            ("18-24", "18-24"), ("25-29", "25-29"), ("30-34", "30-34"),
            ("35-39", "35-39"), ("40-44", "40-44"), ("45-49", "45-49"),
            ("50-54", "50-54"), ("55-59", "55-59"), ("60-64", "60-64"),
            ("65-69", "65-69"), ("70-74", "70-74"), ("75-79", "75-79"),
            ("80 or older", "80 or older")
        ],
        required=True
    )
    Race = forms.ChoiceField(
        label="Race",
        choices=[
            ("White", "White"), ("Black", "Black"), ("Asian", "Asian"),
            ("American Indian/Alaskan Native", "American Indian/Alaskan Native"),
            ("Other", "Other")
        ],
        required=True
    )
    Diabetic = forms.ChoiceField(label="Diabetic", choices=[("Yes", "Yes"), ("No", "No")], required=True)
    
    PhysicalActivity = forms.ChoiceField(label="Physical Activity", choices=[("Yes", "Yes"), ("No", "No")], required=True)
    GenHealth = forms.ChoiceField(
        label="General Health",
        choices=[
            ("Excellent", "Excellent"), ("Very good", "Very good"), 
            ("Good", "Good"), ("Fair", "Fair"), ("Poor", "Poor")
        ],
        required=True
    )
    SleepTime = forms.IntegerField(label="Sleep Time (hours per night)", min_value=0, max_value=24, required=True)
    Asthma = forms.ChoiceField(label="Asthma", choices=[("Yes", "Yes"), ("No", "No")], required=True)
    KidneyDisease = forms.ChoiceField(label="Kidney Disease", choices=[("Yes", "Yes"), ("No", "No")], required=True)
    SkinCancer = forms.ChoiceField(label="Skin Cancer", choices=[("Yes", "Yes"), ("No", "No")], required=True)
