import gradio as gr
import pandas as pd
import numpy as np
import pickle

#load the model
with open('student_rf_pipeline.pkl', "rb") as file:
    model = pickle.load(file)

#main logic will be here
def predict_gpa(gender, age, address, famsize, 
                Pstatus, M_Edu, F_Edu, M_Job, F_Job, 
                relationship, smoker, tuition_fee, time_friends,
                  ssc_result):
    
    input_df = pd.DataFrame([[
        gender, age, address, famsize, Pstatus, 
        M_Edu, F_Edu, M_Job, F_Job, relationship, 
        smoker, tuition_fee, time_friends, ssc_result

    ]], columns=[
        'gender', 'age', 'address', 'famsize', 'Pstatus', 'M_Edu', 'F_Edu', 'M_Job', 'F_Job', 'relationship', 'smoker', 'tuition_fee', 'time_friends', 'ssc_result'
    ])

    prediction = model.predict(input_df)[0]

    return f"Predicted HSC Result: {np.clip(prediction, 0, 5):.2f}"

with gr.Blocks() as app:
    with gr.Row():
        with gr.Column():
            gender = gr.Radio(["M", "F"], label="Gender")
            age = gr.Number(label="Age", value=18)
            address = gr.Radio(["Urban", "Rural"], label="Address")
            famsize = gr.Radio(["LE3", "GT3"], label="Family Size")
            Pstatus = gr.Radio(["Together", "Apart"], label="Parental Status")
            M_Edu = gr.Slider(0, 4, step=1, label="Mother's Education")
            F_Edu = gr.Slider(0, 4, step=1, label="Father's Education")

        with gr.Column():
            M_Job = gr.Dropdown(["At_home", "Health", "Other", "Services", "Teacher"], label="Mother's Job")
            F_Job = gr.Dropdown(["Teacher", "Other", "Services", "Health", "Business", "Farmer"], label="Father's Job")
            relationship = gr.Radio(["Yes", "No"], label="Relationship")
            smoker = gr.Radio(["Yes", "No"], label="Smoker")
            tuition_fee = gr.Number(label="Tuition Fee")
            time_friends = gr.Slider(1, 5, step=1, label="Time with Friends")
            ssc_result = gr.Number(label="SSC Result (GPA)")
    
    predict_btn = gr.Button("Predict HSC GPA")
    output = gr.Textbox(label="Prediction Result")

    predict_btn.click(
        fn=predict_gpa,
        inputs=[gender, age, address, famsize, Pstatus,
                M_Edu, F_Edu, M_Job, F_Job, relationship,
                smoker, tuition_fee, time_friends, ssc_result],
        outputs=output
    )



#lauch code will be here
app.launch(share=True)