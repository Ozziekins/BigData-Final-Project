import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import time

beers = pd.read_csv("./data/beer.csv")
brewers = pd.read_csv("./data/brewer.csv")
reviews = pd.read_csv("./data/review.csv")
persons = pd.read_csv("./data/person.csv")
q1 = pd.read_csv("./output/q1.csv")
q2 = pd.read_csv("./output/q2.csv")
# q3 = pd.read_csv("./output/q3.csv")
q4 = pd.read_csv("./output/q4.csv")
q5 = pd.read_csv("./output/q5.csv")
q6 = pd.read_csv("./output/q6.csv")
q7 = pd.read_csv("./output/q7.csv")
q8 = pd.read_csv("./output/q8.csv")
q9 = pd.read_csv("./output/q9.csv")
q10 = pd.read_csv("./output/q10.csv")
q11 = pd.read_csv("./output/q11.csv")
# q12 = pd.read_csv("./o    utput/q12.csv")
# q13 = pd.read_csv("./output/q13.csv")
q14 = pd.read_csv("./output/q14.csv")
# q15 = pd.read_csv("./output/q15.csv")

if 'toView' not in st.session_state:
    st.session_state.toView = ''

if 'headNum' not in st.session_state:
    st.session_state.headNum = 0

def displayRecommender():
    action = st.selectbox(
        'What action will you like to perform?',
        ('Predict Beers a user will like', 'Predict Users that will like a particular beer', 'Get Beers similar to a particular beer'))
    
    if action  == 'Predict Beers a user will like':
        model = st.selectbox(
            'Which model will you like to use?',
            ('Best Model', 'ALS', 'Gradient Descent'))


        users =  st.multiselect(
            'What users will you like to make predictions for',
            ['User 1', 'User 2', 'User 3', 'User 4'],None)


        count = st.number_input('How many beers will you like to be recommended', step=1)

    elif action  == 'Predict Users that will like a particular beer':
        model = st.selectbox(
            'Which model will you like to use?',
            ('Best Model', 'ALS', 'Gradient Descent'))


        users =  st.multiselect(
            'What beers will you like to make predictions for',
            ['beer 1', 'beer 2', 'beer 3', 'beer 4'],None)


        count = st.number_input('How many beers will you like to be recommended', step=1)

    elif action  == 'Get Beers similar to a particular beer':
        beers =  st.multiselect(
            'What beers will you like to make predictions for',
            ['beer 1', 'beer 2', 'beer 3', 'beer 4'],None)    
        count = st.number_input('How many beers will you like to be recommended', step=1)

    if st.button('Submit'):
        runData()

def OnClick(key, num):
    st.session_state.toView = key
    st.session_state.headNum = num

def displayEDA():
    action = st.selectbox(
        'What action will you like to perform?',
        ('Checkout the descriptive data analysis', 'Show some snippets from the tables', 'View the results of queries'))
    
    if action == 'Checkout the descriptive data analysis':
        value = "dda"

        num_rows = 0
    
    elif action  == 'Show some snippets from the tables':
        value = st.selectbox(
            'Which table will you like to see?',
            ('Beers', 'Brewers', 'Reviews', 'Persons'))
        
        
        num_rows = st.number_input('How many rows will you like to be shown', step=1)


    elif action  == 'View the results of queries':
        value =  st.selectbox(
            'View the results of queries',
            ('Query 1', 'Query 2', 'Query 3', 'Query 4', 'Query 5', 'Query 6', 
             'Query 7', 'Query 8', 'Query 9', 'Query 10', 'Query 11', 'Query 12', 
             'Query 13', 'Query 14', 'Query 15'))
        
        num_rows = 0

    st.button('Show', on_click=lambda : OnClick(f'{value}', num=num_rows))


def runData():
    df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
    
    st.title("Recommendation")
    with st.spinner("Fetching Data"):
        time.sleep(5)
    st.dataframe(df.style.highlight_max(axis=0))

with st.sidebar:
    with st.expander("Exploratory data analysis"):
        st.write("Here, we list different exploratory data analysis actions")
        displayEDA()
    with st.expander("Recommendation System"):
        st.write("Different Recommendation tasks")
        displayRecommender()

def showMain():
    st.markdown('---')
    st.title("Big Data Project **2023**")
    st.markdown("""<style>body {
        background-color: #eee;
    }

    .fullScreenFrame > div {
        display: flex;
        justify-content: center;
    }
    </style>""", unsafe_allow_html=True)

    st.image("https://i2.wp.com/hr-gazette.com/wp-content/uploads/2018/10/bigstock-Recruitment-Concept-Idea-Of-C-250362193.jpg", caption = "Beer Reviews", width=400)

    # st.markdown("<p style='text-align: center; color: grey;'>Beer Reviews</p>", unsafe_allow_html=True)
    
    if st.session_state.toView == "dda":
        st.markdown('---')
        st.header('Descriptive Data Analysis')
        st.subheader('Data Characteristics')
        dda = pd.DataFrame(data = [["Beers", beers.shape[0]-1, beers.shape[1]], ["Brewers", brewers.shape[0], brewers.shape[1]],  
                                         ["Reviews", reviews.shape[0], reviews.shape[1]],  ["Persons", persons.shape[0], persons.shape[1]]], 
                                         columns = ["Tables", "Features", "Instances"])
        st.write(dda)

        st.markdown('`beers` table')
        st.write(beers.describe())
        st.markdown('`brewers` table')
        st.write(brewers.describe())
        st.markdown('`reviews` table')
        st.write(reviews.describe())
        st.markdown('`persons` table')
        st.write(persons.describe())

    elif st.session_state.toView == "Beers":
        st.markdown('---')
        st.header('Some samples from the data')
        st.subheader('`beers` table')
        st.write(beers.head(st.session_state.headNum))
    elif st.session_state.toView == "Brewers":
        st.markdown('---')
        st.header('Some samples from the data')
        st.subheader('`brewers` table')
        st.write(brewers.head(st.session_state.headNum))
    elif st.session_state.toView == "Reviews":
        st.markdown('---')
        st.header('Some samples from the data')
        st.subheader('`reviews` table')
        st.write(reviews.head(st.session_state.headNum))
    elif st.session_state.toView == "Persons":
        st.markdown('---')
        st.header('Some samples from the data')
        st.subheader('`persons` table')
        st.write(persons.head(st.session_state.headNum))

    elif st.session_state.toView == "Query 1":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q1')
        st.text('The number of beers for top 10 brewers')
        st.bar_chart(data=q1, x=' Brewery name')
        st.write(q1)
    elif st.session_state.toView == "Query 2":
        st.subheader('Q2')
        st.text('The number of brewers that produced only 1 beer')
        st.table(q2)
        st.bar_chart(q2)
    elif st.session_state.toView == "Query 4":
        st.subheader('Q4')
        st.text('The beers that have the least abv')
        st.bar_chart(data=q4, x=' Beer name', y=' Beer abv')
        st.write(q4)
    elif st.session_state.toView == "Query 5":
        st.subheader('Q4')
        st.text('The beers that have the highest abv')
        st.bar_chart(data=q5, x=' Beer name', y=' Beer abv')
        st.write(q5)

showMain()