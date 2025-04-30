import streamlit as st
import pickle
import pandas as pd
team = ['Royal Challengers Bangalore',
 'Punjab Kings',
 'Chennai Super Kings',
 'Gujarat Titans',
 'Delhi Capitals',
 'Lucknow Super Giants',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Sunrisers Hyderabad',
 'Mumbai Indians']

city = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
       'Lucknow', 'Guwahati', 'Mohali']

pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("IPL WIN PREDICTOR")

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox("Choose Batting Team", sorted(team))

with col2:
     bowling_team = st.selectbox("Choose Bowling Team", sorted(team))

selected_city = st.selectbox("Choose City", sorted(city))

target = st.number_input("Target")

col3, col4, col5 = st.columns(3)
with col3:
    Score= st.number_input("Enter Score")

with col4:
     overs = st.number_input("Overs")

with col5:
     wicket = st.number_input("Wicket")


if st.button("Predict Win Probablity"):
    runleft = target - Score
    ball_left = 120 - (6 * overs)
    wicket = 10 - wicket
    crr = Score / overs if overs > 0 else 0
    rrr = (runleft * 6) / ball_left if ball_left > 0 else 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runleft': [runleft],
        'ball_left': [ball_left],
        'wicket': [wicket],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)
    win = result[0][1]
    loss = result[0][0]

    st.text(batting_team + " Win Probability: " + str(round(win * 100)) + "%")
    st.text(bowling_team + " Win Probability: " + str(round(loss * 100)) + "%")






# if st.button("Predict Win Probablity"):
#   runleft = target - Score
#   ball_left = 120-(6*overs)
#   wicket = 10-wicket
#   crr= Score/overs
#   rrr= (runleft*6)/ball_left

# input_df = pd.DataFrame({
#         'batting_team': [batting_team],
#         'bowling_team': [bowling_team],
#         'city': [selected_city],
#         'run_left': [runleft],
#         'ball_left': [ball_left],
#         'wicket': [wicket],
#         'total_runs_x': [target],
#         'crr': [crr],
#         'rrr': [rrr]
#     })

# result = pipe.predict_proba(input_df)