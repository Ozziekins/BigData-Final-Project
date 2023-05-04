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
# q3 = pd.read_csv("../output/q3.csv")
# q4 = pd.read_csv("../output/q4.csv")
# q5 = pd.read_csv("../output/q5.csv")
# q6 = pd.read_csv("../output/q6.csv")
# q7 = pd.read_csv("../output/q7.csv")
# q8 = pd.read_csv("../output/q8.csv")
# q9 = pd.read_csv("../output/q9.csv")
# q10 = pd.read_csv("../output/q10.csv")
# q11 = pd.read_csv("../output/q11.csv")
# q12 = pd.read_csv("../output/q12.csv")
# q13 = pd.read_csv("../output/q13.csv")
# q14 = pd.read_csv("../output/q14.csv")
# q15 = pd.read_csv("../output/q15.csv")

if 'toView' not in st.session_state:
    st.session_state.toView = ''

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

def OnClick(key):
    print(key)
    st.session_state.toView = key
    print(st.session_state.toView)

def displayEDA():
    if st.button('Snippets'):
        st.button('Snippet of beers', on_click=lambda : OnClick('beerSnippet'))
        st.button('Snippet of brewers', on_click=lambda : OnClick('brewerSnippet'))
        st.button('Snippet of reviews')
        st.button('Snippet of reviewers')

    if st.button('Queries'):
        st.button('Q1')
        st.button('Q2')
    
    # print(st.session_state.beerSnippet)
    # st.subheader('Some samples from the data')
    # st.markdown('`beers` table')
    # st.write(beers.head(5))
    # st.markdown("`brewers` table")
    # st.write(brewers.head(5))
    # st.markdown("`reviews` table")
    # st.write(reviews.head(5))
    # st.markdown("`persons` table")
    # st.write(persons.head(5))

    st.markdown('---')
    st.header("Exploratory Data Analysis")
    st.subheader('Q1')
    st.text('The number of beers for top 10 brewers')
    st.bar_chart(q1['Number beers'])

    st.subheader('Q2')
    st.text('The number of brewers that produced only 1 beer')
    st.table(q2)
    st.line_chart(q2, width=400)


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

    st.markdown("<p style='text-align: center; color: grey;'>Beer Reviews</p>", unsafe_allow_html=True)

    st.markdown('---')
    st.header('Descriptive Data Analysis')
    st.subheader('Data Characteristics')
    beers_dda = pd.DataFrame(data = [["Beers", beers.shape[0]-1, beers.shape[1]], ["Reviews", reviews.shape[0], reviews.shape[1]]], columns = ["Tables", "Features", "Instances"])
    st.write(beers_dda)
    # st.markdown('`beers` table')
    # st.write(beers.describe())
    # st.markdown('`brewers` table')
    # st.write(brewers.describe())
    # st.markdown('`reviews` table')
    # st.write(reviews.describe())
    # st.markdown('`persons` table')
    # st.write(persons.describe())
    
    if st.session_state.toView == "beerSnippet":
        st.subheader('Some samples from the data')
        st.markdown('`beers` table')
        st.write(beers.head(5))
    elif st.session_state.toView == "brewerSnippet":
        st.subheader('Some samples from the data')
        st.markdown('`brewers` table')
        st.write(brewers.head(5))

showMain()