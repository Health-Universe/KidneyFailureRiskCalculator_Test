import streamlit as st
import time

def calculate_kidney_failure_risk_score(eGFR, sex, urine_albumin_to_creatinine_ratio, age, serum_albumin, serum_phosphorus, serum_bicarbonate, serum_calcium):
    # Define point values
    eGFR_points = {
        (10, 14): -35, (15, 19): -30, (20, 24): -25, (25, 29): -20,
        (30, 34): -15, (35, 39): -10, (40, 44): -5, (45, 49): 0,
        (50, 54): 5, (55, 59): 10
    }

    sex_points = {'Female': 0, 'Male': -2}

    urine_albumin_points = {'<30': 0, '30-300': -14, '>300': -22}

    age_points = {'<30': -4, '30-39': -2, '40-49': 0, '50-59': 2, '60-69': 4, '70-79': 6, '80-89': 8, '≥90': 10}

    serum_albumin_points = {'≤2.5 (≤25)': -5, '2.6-3.0 (26-30)': 0, '3.1-3.5 (31-36)': 2, '≥3.6 (≥36)': 4}

    serum_phosphorus_points = {'<3.5 (<1.13)': 3, '3.5-4.5 (1.13-1.45)': 0, '4.6-5.5 (1.49-1.78)': -3, '>5.5 (>1.78)': -5}

    serum_bicarbonate_points = {'<18': -7, '18-22': -4, '23-25': -1, '>25': 0}

    serum_calcium_points = {'≤8.5 (≤2.12)': -3, '8.6-9.5 (2.12-2.37)': 0, '≥9.6 (≥2.4)': 2}

    # Calculate points for each variable
    eGFR_score = next(value for key, value in eGFR_points.items() if key[0] <= eGFR <= key[1])
    sex_score = sex_points[sex]
    urine_albumin_score = urine_albumin_points[urine_albumin_to_creatinine_ratio]
    age_score = age_points[age]
    serum_albumin_score = serum_albumin_points[serum_albumin]
    serum_phosphorus_score = serum_phosphorus_points[serum_phosphorus]
    serum_bicarbonate_score = serum_bicarbonate_points[serum_bicarbonate]
    serum_calcium_score = serum_calcium_points[serum_calcium]

    # Calculate total points
    total_points = (eGFR_score + sex_score + urine_albumin_score + age_score +
                    serum_albumin_score + serum_phosphorus_score + serum_bicarbonate_score +
                    serum_calcium_score)

    # Determine kidney failure risk
    if total_points <= -41:
        risk_category = '>90.0%'
    elif total_points == -40:
        risk_category = '89.0%'
    elif total_points == -39:
        risk_category = '86.9%'
    elif total_points == -38:
        risk_category = '84.1%'
    elif total_points == -37:
        risk_category = '81.0%'
    elif total_points == -36:
        risk_category = '78.0%'
    elif total_points == -35:
        risk_category = '74.4%'
    elif total_points == -34:
        risk_category = '70.9%'
    elif total_points == -33:
        risk_category = '67.3%'
    elif total_points == -32:
        risk_category = '63.6%'
    elif total_points == -31:
        risk_category = '59.9%'
    elif total_points == -30:
        risk_category = '56.3%'
    elif total_points == -29:
        risk_category = '52.8%'
    elif total_points == -28:
        risk_category = '49.3%'
    elif total_points == -27:
        risk_category = '45.9%'
    elif total_points == -26:
        risk_category = '42.7%'
    elif total_points == -25:
        risk_category = '39.6%'
    elif total_points == -24:
        risk_category = '36.6%'
    elif total_points == -23:
        risk_category = '33.8%'
    elif total_points == -22:
        risk_category = '31.2%'
    elif total_points == -21:
        risk_category = '28.7%'
    elif total_points == -20:
        risk_category = '26.4%'
    elif total_points == -19:
        risk_category = '24.2%'
    elif total_points == -18:
        risk_category = '22.2%'
    elif total_points == -17:
        risk_category = '20.3%'
    elif total_points == -16:
        risk_category = '18.6%'
    elif total_points == -15:
        risk_category = '17.0%'
    elif total_points == -14:
        risk_category = '15.5%'
    elif total_points == -13:
        risk_category = '14.1%'
    elif total_points == -12:
        risk_category = '12.9%'
    elif total_points == -11:
        risk_category = '11.7%'
    elif total_points == -10:
        risk_category = '10.7%'
    elif total_points == -9:
        risk_category = '9.7%'
    elif total_points == -8:
        risk_category = '8.8%'
    elif total_points == -7:
        risk_category = '8.0%'
    elif total_points == -6:
        risk_category = '7.3%'
    elif total_points == -5:
        risk_category = '6.6%'
    elif total_points == -4:
        risk_category = '6.0%'
    elif total_points >= -3:
        risk_category = '<5.0%'


    return total_points, risk_category

# Streamlit UI
st.title('Kidney Failure Risk Calculator 💊')
st.divider()

# Collect user inputs
eGFR_options = ['10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59']
eGFR_selected_range = st.selectbox('GFR, mL/min/1.73m^2', eGFR_options,help="The Glomerular Filtration Rate (GFR) is a crucial test for assessing kidney function and determining the stage of kidney disease. It is calculated based on your blood creatinine levels, age, and sex. A lower GFR indicates poorer kidney function. If your GFR drops below 30, consulting a nephrologist is advised, and if it falls below 15, discussions about treatments for kidney failure will begin.")
# Convert the selected range into a numerical value (midpoint)
eGFR = sum(map(int, eGFR_selected_range.split('-'))) / 2 if eGFR_selected_range != 'Select' else None
sex = st.radio('Sex', ['Female', 'Male'])
urine_albumin_to_creatinine_ratio = st.selectbox('Urine Albumin-to-Creatinine Ratio mg/g', ['<30', '30-300', '>300'], help="Healthy kidneys filter waste, retaining large cells like red blood cells and proteins. Kidney failure causes these large cells to leak into urine, leading to damage and scarring. Doctors assess the ratio of albumin to creatinine in urine (normal level: <30 mg/g) to gauge kidney function.")
age = st.selectbox('Age', ['<30', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '≥90'])
serum_albumin = st.selectbox('Serum Albumin, g/dL(g/L)', ['≤2.5 (≤25)', '2.6-3.0 (26-30)', '3.1-3.5 (31-35)', '≥3.6 (≥36)'], help="Albumin, a protein from the diet, is produced in the body. Kidney dysfunction leads to its leakage into urine. Testing albumin levels in kidney disease patients' blood indicates nutritional status. Low albumin levels may compromise the body's ability to fend off infections.")
serum_phosphorus = st.selectbox('Serum Phosphorus, mg/dL (mmol/L)', ['<3.5 (<1.13)', '3.5-4.5 (1.13-1.45)', '4.6-5.5 (1.49-1.78)', '>5.5 (>1.78)'], help="Phosphorus, essential for bone health alongside calcium, is normally regulated by healthy kidneys. In advanced kidney disease, phosphorus buildup can cause serious issues like organ damage, poor circulation, bone pain, and skin sores. Managing diet and medications, with guidance from a dietitian, is key to maintaining normal phosphorus levels. Doctors may also prescribe phosphate-binding medication to control blood levels.")
serum_bicarbonate = st.selectbox('Serum Bicarbonate, mEq/L', ['<18', '18-22', '23-25', '>25'], help="Impaired kidney function can disrupt the balance of acidity in the blood, causing Metabolic Acidosis. This condition poses risks to bones, muscles, and kidney health. Monitoring bicarbonate levels, the substance that counteracts high acidity, is crucial. If bicarbonate levels drop too low, your doctor may prescribe medications to raise them.")
serum_calcium = st.selectbox('Serum Calcium, mg/dL (mmol/L)', ['≤8.5 (≤2.12)', '8.6-9.5 (2.12-2.37)', '≥9.6 (≥2.4)'], help="Corrected calcium, a crucial mineral, partners with phosphate to strengthen bones and regulate muscle, heart, and blood functions. Kidneys play a key role in maintaining balanced corrected calcium levels. In Chronic Kidney Disease, imbalances can lead to heart issues. Elevated corrected calcium levels may cause various symptoms, while low levels may necessitate a prescribed supplement. Dietary adjustments and medications may be recommended to manage corrected calcium levels.")

# Calculate and display results
if st.button('Calculate Risk'):
    # Show a spinner while calculating
    with st.spinner('Calculating...'):
        time.sleep(2)
        total_points, risk_category = calculate_kidney_failure_risk_score(eGFR, sex, urine_albumin_to_creatinine_ratio,
                                                                          age, serum_albumin, serum_phosphorus,
                                                                          serum_bicarbonate, serum_calcium)
        st.divider()
        st.subheader("Results")
        st.markdown(f'Kidney Failure Risk Score: {total_points}')
        st.markdown(f'Probability of kidney failure at 5 years: {risk_category}')

#Reference
#Tangri N, Stevens LA, Griffith J, et al.
#A predictive model for progression of chronic kidney disease to kidney failure.
#JAMA. 2011;305(15). DOI:10.001/jama.2011.451
