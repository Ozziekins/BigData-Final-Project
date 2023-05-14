import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import time
from datetime import datetime
import plotly.express as px
import matplotlib
import sys, os
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from models.ModelService import ModelService

from models.SparkService import SparkService
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import plotly.figure_factory as ff

from models.DataService import DataService
spark = SparkService()
        
dataService = DataService()
service = ModelService()

beers = dataService.beer
brewers = dataService.brewer
reviews = dataService.review
persons = dataService.person

q1 = pd.read_csv("../clean_output/q1.csv")
q2 = pd.read_csv("../clean_output/q2.csv")
q3 = pd.read_csv("../clean_output/q3.csv")
q4 = pd.read_csv("../clean_output/q4.csv")
q5 = pd.read_csv("../clean_output/q5.csv")
q6 = pd.read_csv("../clean_output/q6.csv")
q7 = pd.read_csv("../clean_output/q7.csv")
q8 = pd.read_csv("../clean_output/q8.csv")
q9 = pd.read_csv("../clean_output/q9.csv")
q10 = pd.read_csv("../clean_output/q10.csv")
q11 = pd.read_csv("../clean_output/q11.csv")
q12 = pd.read_csv("../clean_output/q12.csv")
q13 = pd.read_csv("../clean_output/q13.csv")
q14 = pd.read_csv("../clean_output/q14.csv")
q15 = pd.read_csv("../clean_output/q15.csv")
q16 = pd.read_csv("../clean_output/q16.csv")
q17 = pd.read_csv("../clean_output/q17.csv")
q18 = pd.read_csv("../clean_output/q18.csv")
q19 = pd.read_csv("../clean_output/q19.csv")

# Rename the Count column in each dataframe to be unique
q7 = q7.rename(columns={' Count': 'Count appearance'})
q8 = q8.rename(columns={' Count': 'Count aroma'})
q9 = q9.rename(columns={' Count': 'Count total'})
q10 = q10.rename(columns={' Count': 'Count taste'})
q11 = q11.rename(columns={' Count': 'Count palate'})

session_state = {'toView': 'default'}

if 'toView' not in session_state:
    session_state['toView'] = ''

if 'headNum' not in session_state:
    session_state['headNum'] = 0

def displayRecommender():
    action = st.selectbox(
        'What action will you like to perform?',
        ('Predict Beers a user will like', 'Predict Users that will like a particular beer', 'Get Beers similar to a particular beer'))
    
    if action  == 'Predict Beers a user will like': 
        selected_users =  st.selectbox(
            'What users will you like to make predictions for',
            persons.collect())
        count = int(st.number_input('How many beers will you like to be recommended', step=1, min_value=1, max_value=10))
        if(st.button('Submit')):
            with st.spinner("Fetching Data"):
                user_ids = [[selected_users['id']]]
                result = service.predictItems(user_ids,count)
                st.title("Recommendation")
                st.table(pd.DataFrame(result[0]['recommendations'], columns=['Beer Id', 'Predicted Rating']))
    elif action  == 'Predict Users that will like a particular beer':
        selected_beers = st.selectbox(
            'What beers will you like to make predictions for',
            beers.collect())

        count = int(st.number_input('How many users will you like to be recommended', step=1, min_value=1, max_value=10))
        if(st.button('Submit')):
            with st.spinner("Fetching Data"):
                beer_ids = [[selected_beers['id']]]
                result = service.predictUsers(beer_ids,count)
                st.title("Recommendation")
                st.table(pd.DataFrame(result[0]['recommendations'], columns=['User Id', 'Predicted Rating']))

    elif action  == 'Get Beers similar to a particular beer':
        selected_beers =  st.selectbox(
            'What beers will you like to make predictions for',
            beers.na.drop().collect())    
        count = int(st.number_input('How many beers will you like to be recommended', step=1, min_value=1, max_value=10))
        if(st.button('Submit')):
            with st.spinner("Fetching Data"):
                beer_ids = [selected_beers['id']]
                result = service.similarItems(beer_ids, count)
                st.title("Recommendation")
                st.table(pd.DataFrame(result, columns=['id','name','abv','style','brewery_name']))
                # st.table(pd.DataFrame(result[0]['recommendations'], columns=['User Id', 'Predicted Rating']))

def showQuery(value):
    if value == "Persons":
        st.markdown('---')
        st.header('Some samples from the data')
        st.subheader('`persons` table')
        st.table(pd.DataFrame(persons.take(session_state['headNum']), columns=persons.columns))
    elif value == "Query 1":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q1')
        st.text('The number of beers for top 10 brewers') 
        st.bar_chart(data=q1.set_index(" Brewery name"), height=500)
        st.write(q1)
    elif value == "Query 2":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q2')
        st.text('The number of brewers that produced only 1 beer')
        st.table(q2)
        st.bar_chart(q2, use_container_width=True)
    elif value == "Query 3":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q3')
        st.text('The beers that have above average overall review')
        num_beers = int(st.number_input('How many samples will you like to show', step=1, min_value=1, max_value=25, value=10))
        st.line_chart(data=q3.set_index(" Beer name").sample(n=num_beers)[" Average review"], height=500)
        st.write(q3)
    elif value == "Query 4":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q4')
        st.text('The beers that have the least abv')
        st.bar_chart(data=q4.set_index(' Beer name')[" Beer abv"], height=500)
        st.write(q4)
    elif value == "Query 5":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q5')
        st.text('The beers that have the highest abv')
        st.bar_chart(data=q5.set_index(' Beer name')[" Beer abv"], height=500)
        st.write(q5)
    elif value == "Query 6":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q6')
        st.text('The styles of top 10 highest reviewed beers')
        st.bar_chart(data=q6.set_index(' Beer name')[" Average total review"], height=500)
        st.write(q6)
    elif value == "Query 7 - 11":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q7 - 11')
        
        st.text('The number of beers for each appearance score')
        st.bar_chart(data=q7.set_index('Beer appearance')["Count appearance"], height=500)
        st.write(q7)

        st.text('The number of beers for each aroma score')
        st.bar_chart(data=q8.set_index('Beer aroma')["Count aroma"], height=500)
        st.write(q8)

        st.text('The number of beers for each total score')
        st.bar_chart(data=q9.set_index('Beer total')["Count total"], height=500)
        st.write(q9)

        st.text('The number of beers for each taste score')
        st.bar_chart(data=q10.set_index('Beer taste')["Count taste"], height=500)
        st.write(q10)

        st.text('The number of beers for each palate score')
        st.bar_chart(data=q11.set_index('Beer palate')["Count palate"], height=500)
        st.write(q11)
    elif value == "Query 12":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q12')
        st.text('The users that reviewed a particular beer')
        beer_name = st.selectbox("What beer would you like to get reviewers for?", q12["Beer name"])
        if beer_name:
            data = q12[q12["Beer name"] == beer_name]
            st.table(data=data)
    elif value == "Query 13":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q13')

        st.text('The timestamp over overall time of users with most activity')
        opt = st.selectbox(
            'Choose the style of comparison',
            ('Randomly',
             'Show for particular reviewer'))
        
        if opt == "Randomly":
            num_reviewers = st.number_input("Enter the number of reviewers you want to compare", step=1, min_value=1, max_value=25, value=10)
            if num_reviewers:
                st.bar_chart(data=q13.set_index("Profile name").sample(n=num_reviewers)[" Number of reviews"], height=500)
        elif opt == "Show for particular reviewer":

            reviewer_name = st.selectbox("Select User", q13["Profile name"])
            data = q13[q13["Profile name"] == reviewer_name]
            reviews_edited = data[" Reviews"].apply(eval)
            timestamps_edited = data[" Timestamps"].apply(eval)
            df = pd.concat([data["Profile name"], reviews_edited, timestamps_edited], axis=1)

            # Convert timestamps to datetime format
            df[" Timestamps"] = df[" Timestamps"].apply(lambda x: [datetime.fromtimestamp(ts/1000) for ts in x])

            # Reverse the y-axis
            df[" Reviews"] = df[" Reviews"]

            # Flatten the lists of timestamps and reviews
            timestamps = [ts for sublist in df[" Timestamps"] for ts in sublist]
            q13_reviews = [r for sublist in df[" Reviews"] for r in sublist]

            # Create scatter plot
            fig, ax = plt.subplots()
            ax.scatter(timestamps, q13_reviews, marker="o")

            # Format x-axis as full timestamps
            date_fmt = mdates.DateFormatter("%Y-%m-%d %H:%M:%S")
            ax.xaxis.set_major_formatter(date_fmt)
            fig.autofmt_xdate()  # Adjusts the rotation and alignment of x-axis tick labels

            # Set plot labels and title
            plt.xlabel("Timestamps")
            plt.ylabel("Reviews")
            plt.title("Reviews vs. Timestamps")

            # Display the plot
            st.pyplot(fig)
    elif value == "Query 14":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q14')
        st.text('The number of reviews per year of active users')
        
        selected_users = st.multiselect("Select Users", q14["Profile name"])
        users_df = q14[q14["Profile name"].isin(selected_users)]
        pivot_df = users_df.pivot(index="Profile name", columns=" Year", values=" Number of reviews")
        chart_data = pivot_df.loc[selected_users].T
        chart_data.columns = selected_users
        st.line_chart(chart_data, height=500)

        st.markdown("**X-axis Label:** Year")
        st.markdown("**Y-axis Label:** Number of Reviews")
        st.markdown("**Title:** Number of Reviews per Year")
    elif value == "Query 15":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q15')
        st.text('The beer reviews over time for a particular beer')

        num_beers = st.number_input("Enter the number of beers you want to display", step=1, min_value=1, max_value=10, value=5)

        selected_beers = q15["Beer name"].sample(n=num_beers)
        users_df = q15[q15["Beer name"].isin(selected_beers)]
        pivot_df = users_df.pivot(index="Beer name", columns=" Date", values=" Number of reviews")
        

        chart_data = pivot_df.loc[selected_beers].T
        chart_data.columns = selected_beers.tolist()
        st.line_chart(chart_data, height=500, width=1000)

        st.markdown("**X-axis Label:** Date")
        st.markdown("**Y-axis Label:** Number of Reviews")
        st.markdown("**Title:** Number of Reviews per Date")
    elif value == "Query 16":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q16')
        st.text('The average rating of beers by abv')
        fig = px.scatter(
            q16,
            x="Beer abv",
            y=" Average rating",
            # size=1,
            color="Beer abv",
            # hover_name=" Average rating",
            log_x=True,
            # log_y=True,
            # size_max=60,
        )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        # st.table(data=q16)
    elif session_state['toView'] == "Query 17":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q17')
        st.text('The top-rated beers by style')

        st.table(data=q17)

        chart_data = q17.groupby('Beer style')[' Total rating'].sum()
        st.line_chart(chart_data, height=500)
    elif value == "Query 18":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q18')
        st.text('The breweries which are mentioned most often in positive reviews (aka >4)')

        opt = st.selectbox(
            'Choose the style of comparison',
            ('Top five',
             'Randomly',
             'Show for particular breweries'))
        
        if opt == "Top five":
             st.bar_chart(data=q18.set_index("Brewery name").head(5)[" Number of mentions"], height=500)
        elif opt == "Randomly":
            num_brewers = st.number_input("Enter the number of brewers you want to display", step=1, min_value=1, max_value=10, value=5)
            if num_brewers:
                st.bar_chart(data=q18.set_index("Brewery name").sample(n=num_brewers)[" Number of mentions"], height=500)
        elif opt == "Show for particular breweries":
            selected_breweries = st.multiselect("Select Users", q18["Brewery name"])
            breweries_df = q18[q18["Brewery name"].isin(selected_breweries)]
            # pivot_df = breweries_df.pivot(index="Brewery name", columns=" Brewery name", values=" Number of mentions")

            # chart_data = pivot_df.loc[selected_breweries].T
            st.bar_chart(breweries_df.set_index("Brewery name")[" Number of mentions"], height=500)

            st.markdown("**X-axis Label:** Breweries")
            st.markdown("**Y-axis Label:** Number of Mentions")
            st.markdown("**Title:** Number of Reviews per Brewery")
    elif value == "Query 19":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q19')
        st.text('How the popularity of different beer styles changed over years')

        selected_styles = st.multiselect("Select Styles", q19["Beer style"].unique())
        styles_df = q19[q19["Beer style"].isin(selected_styles)]
        pivot_df = styles_df.pivot(index="Beer style", columns=" Year", values=" Average rating")

        chart_data = pivot_df.loc[selected_styles].T
        chart_data.columns = selected_styles
        st.line_chart(chart_data, height=500)

        st.markdown("**X-axis Label:** Year")
        st.markdown("**Y-axis Label:** Average rating")
        st.markdown("**Title:** Average rating per Year")

def displayEDA():
    action = st.selectbox(
        'What action will you like to perform?',
        ('Checkout the descriptive data analysis', 'Show some snippets from the tables', 'View the results of queries'))
    
    if action == 'Checkout the descriptive data analysis':
        value = "dda"

        num_rows = 0
        if(st.button('Show')): 
            session_state['toView'] = value
    
    elif action  == 'Show some snippets from the tables':
        value = st.selectbox(
            'Which table will you like to see?',
            ('Beers', 'Brewers', 'Reviews', 'Persons'))
        
        
        session_state['headNum'] = int(st.number_input('How many rows will you like to be shown', step=1, min_value=1, max_value=10,value=1))

        if(st.button('Show')): 
            session_state['toView'] = value

    elif action  == 'View the results of queries':
        value =  st.selectbox(
            'View the results of queries',
            ('Query 1', 'Query 2', 'Query 3', 'Query 4', 'Query 5', 'Query 6', 
             'Query 7 - 11', 'Query 12', 'Query 13', 'Query 14', 'Query 15', 
             'Query 16', 'Query 17', 'Query 18', 'Query 19'))
        showQuery(value)

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

st.image("https://www.linkpicture.com/q/removal.ai-_tmp-6460ac9e64f7a.png", caption = "Beer Reviews", width=400)

st.header("Exploratory Data Analysis")
displayEDA()

st.header("Prediction Data Analysis")
displayRecommender()
    

def showMain():
    if session_state['toView'] == "dda":
        st.markdown('---')
        st.header('Descriptive Data Analysis')
        st.subheader('Data Characteristics')
        
        dda = pd.DataFrame(data = [["Beers", beers.count(), len(beers.columns)], ["Brewers", brewers.count(), len(brewers.columns)],  
                                         ["Reviews", reviews.count(), len(reviews.columns)],  ["Persons", persons.count(), len(persons.columns)]], 
                                         columns = ["Tables", "Instances", "Features"])
        st.write(dda)

        st.markdown('`beers` table')
        st.write(pd.DataFrame(beers.describe().collect(), columns=['summary']+beers.columns))
        st.markdown('`brewers` table')
        st.write(pd.DataFrame(brewers.describe().collect(), columns=['summary']+brewers.columns))
        st.markdown('`reviews` table')      
        st.write(pd.DataFrame(reviews.describe().collect(), columns=['summary']+[i for i in reviews.columns if i != "time"]))
        st.markdown('`persons` table')
        st.write(pd.DataFrame(persons.describe().collect(), columns=['summary']+persons.columns))
    elif session_state['toView'] == "Beers":
        st.markdown('---')
        st.header('Some samples from the data')
        st.subheader('`beers` table')
        st.table(pd.DataFrame(beers.take(session_state['headNum']), columns=beers.columns))
    elif session_state['toView'] == "Brewers":
        st.markdown('---')
        st.header('Some samples from the data')
        st.subheader('`brewers` table')
        st.table(pd.DataFrame(brewers.take(session_state['headNum']), columns=brewers.columns))
    elif session_state['toView'] == "Reviews":
        st.markdown('---')
        st.header('Some samples from the data')
        st.subheader('`reviews` table')
        st.table(pd.DataFrame(reviews.take(session_state['headNum']), columns=reviews.columns))
    elif session_state['toView'] == "Persons":
        st.markdown('---')
        st.header('Some samples from the data')
        st.subheader('`persons` table')
        st.table(pd.DataFrame(persons.take(session_state['headNum']), columns=persons.columns))
  
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q19')
        st.text('How the popularity of different beer styles changed over years')

        selected_styles = st.multiselect("Select Styles", q19["Beer style"].unique())
        styles_df = q19[q19["Beer style"].isin(selected_styles)]
        pivot_df = styles_df.pivot(index="Beer style", columns=" Year", values=" Average rating")

        chart_data = pivot_df.loc[selected_styles].T
        st.line_chart(chart_data, height=500)

        st.markdown("**X-axis Label:** Year")
        st.markdown("**Y-axis Label:** Average rating")
        st.markdown("**Title:** Average rating per Year")   

showMain()