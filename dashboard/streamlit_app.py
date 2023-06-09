import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import time
from datetime import datetime
import plotly.express as px
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import plotly.figure_factory as ff

beers = pd.read_csv("./data/beer.csv")
brewers = pd.read_csv("./data/brewer.csv")
reviews = pd.read_csv("./data/review.csv")
persons = pd.read_csv("./data/person.csv")

q1 = pd.read_csv("./output/q1.csv")
q2 = pd.read_csv("./output/q2.csv")
q3 = pd.read_csv("./output/q3.csv")
q4 = pd.read_csv("./output/q4.csv")
q5 = pd.read_csv("./output/q5.csv")
q6 = pd.read_csv("./output/q6.csv")
q7 = pd.read_csv("./output/q7.csv")
q8 = pd.read_csv("./output/q8.csv")
q9 = pd.read_csv("./output/q9.csv")
q10 = pd.read_csv("./output/q10.csv")
q11 = pd.read_csv("./output/q11.csv")
q12 = pd.read_csv("./output/q12.csv")
q13 = pd.read_csv("./output/q13.csv")
q14 = pd.read_csv("./output/q14.csv")
q15 = pd.read_csv("./output/q15.csv")
q16 = pd.read_csv("./output/q16.csv")
q17 = pd.read_csv("./output/q17.csv")
q18 = pd.read_csv("./output/q18.csv")
q19 = pd.read_csv("./output/q19.csv")

# Rename the Count column in each dataframe to be unique
q7 = q7.rename(columns={' Count': 'Count appearance'})
q8 = q8.rename(columns={' Count': 'Count aroma'})
q9 = q9.rename(columns={' Count': 'Count total'})
q10 = q10.rename(columns={' Count': 'Count taste'})
q11 = q11.rename(columns={' Count': 'Count palate'})

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

    st.button('Submit', on_click=lambda : OnClick(f'Submit', num=0))

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
        # value =  st.selectbox(
        #     'View the results of queries',
        #     ('Query 1', 'Query 2', 'Query 3', 'Query 4', 'Query 5', 'Query 6', 
        #      'Query 7', 'Query 8', 'Query 9', 'Query 10', 'Query 11', 'Query 12', 
        #      'Query 13', 'Query 14', 'Query 15', 'Query 16', 'Query 17', 'Query 18',
        #      'Query 19'))
        value =  st.selectbox(
            'View the results of queries',
            ('Query 1', 'Query 2', 'Query 3', 'Query 4', 'Query 5', 'Query 6', 
             'Query 7 - 11', 'Query 12', 'Query 13', 'Query 14', 'Query 15', 
             'Query 16', 'Query 17', 'Query 18', 'Query 19'))
        
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

    st.image("https://img.freepik.com/premium-vector/craft-beer-illustration_132292-126.jpg?w=2000", caption = "Beer Reviews", width=600)
    # https://img.freepik.com/premium-vector/craft-beer-illustration_132292-126.jpg?w=2000
    # st.markdown("<p style='text-align: center; color: grey;'>Beer Reviews</p>", unsafe_allow_html=True)
    
    if st.session_state.toView == "dda":
        st.markdown('---')
        st.header('Descriptive Data Analysis')
        st.subheader('Data Characteristics')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        dda = pd.DataFrame(data = [["Beers", beers.shape[0], beers.shape[1]], ["Brewers", brewers.shape[0], brewers.shape[1]],  
                                         ["Reviews", reviews.shape[0], reviews.shape[1]],  ["Persons", persons.shape[0], persons.shape[1]]], 
                                         columns = ["Tables", "Features", "Instances"])
        st.write(dda)

        st.markdown('`beers` table')
        st.write(beers.describe())
        beer_box = beers.boxplot(meanline=True, showmeans=True)
        st.pyplot(beer_box.figure)

        st.markdown('`brewers` table')
        st.write(brewers.describe())
        brewer_box = brewers.boxplot(meanline=True, showmeans=True)
        st.pyplot(brewer_box.figure)

        st.markdown('`reviews` table')
        st.write(reviews.describe())
        review_box = reviews[["review.id"]].boxplot(meanline=True, showmeans=True)
        st.pyplot(review_box.figure)

        st.markdown('`persons` table')
        st.write(persons.describe())
        person_box = persons.boxplot(meanline=True, showmeans=True)
        st.pyplot(person_box.figure)

    elif st.session_state.toView == "Beers":
        st.markdown('---')
        st.header('Some samples from the data')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.subheader('`beers` table')
        st.write(beers.head(st.session_state.headNum))
    elif st.session_state.toView == "Brewers":
        st.markdown('---')
        st.header('Some samples from the data')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.subheader('`brewers` table')
        st.write(brewers.head(st.session_state.headNum))
    elif st.session_state.toView == "Reviews":
        st.markdown('---')
        st.header('Some samples from the data')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.subheader('`reviews` table')
        st.write(reviews.head(st.session_state.headNum))
    elif st.session_state.toView == "Persons":
        st.markdown('---')
        st.header('Some samples from the data')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.subheader('`persons` table')
        st.write(persons.head(st.session_state.headNum))

    elif st.session_state.toView == "Query 1":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q1')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The number of beers for top 10 brewers')
        st.bar_chart(data=q1, x=' Brewery name')
        st.write(q1)
    elif st.session_state.toView == "Query 2":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q2')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The number of brewers that produced only 1 beer')
        st.table(q2)
        st.bar_chart(q2)
    elif st.session_state.toView == "Query 3":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q3')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The beers that have above average overall review')
        
        num_beers = st.number_input("Enter the number of beers you want to show", step=1)
        if num_beers:
            st.line_chart(data=q3.sample(n=num_beers), x=' Beer name', y=' Average review')
        st.write(q3)
    elif st.session_state.toView == "Query 4":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q4')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The beers that have the least abv')
        st.bar_chart(data=q4, x=' Beer name', y=' Beer abv')
        st.write(q4)
    elif st.session_state.toView == "Query 5":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q5')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The beers that have the highest abv')
        st.bar_chart(data=q5, x=' Beer name', y=' Beer abv')
        st.write(q5)
    elif st.session_state.toView == "Query 6":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q6')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The styles of top 10 highest reviewed beers')
        st.bar_chart(data=q6, x=' Beer name', y=' Average total review')
        st.write(q6)
    elif st.session_state.toView == "Query 7 - 11":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q7 - 11')
        with st.spinner("Fetching Data"):
            time.sleep(5)

        tab1, tab2 = st.tabs(['Bars', 'Pies'])

        with tab1:

            st.text('The number of beers for each appearance score')
            st.bar_chart(data=q7, x='Beer appearance', y='Count appearance')
            # st.write(q7)

            st.text('The number of beers for each aroma score')
            st.bar_chart(data=q8, x='Beer aroma', y='Count aroma')
            # st.write(q8)

            st.text('The number of beers for each total score')
            st.bar_chart(data=q9, x='Beer total', y='Count total')
            # st.write(q9)

            st.text('The number of beers for each taste score')
            st.bar_chart(data=q10, x='Beer taste', y='Count taste')
            # st.write(q10)

            st.text('The number of beers for each palate score')
            st.bar_chart(data=q11, x='Beer palate', y='Count palate')
            # st.write(q11)

        with tab2:
            font_size = 6

            st.text('The number of beers for each appearance score')
            fig, ax = plt.subplots()
            ax.pie(q7['Count appearance'], labels=q7['Beer appearance'], autopct='%1.1f%%', textprops={'fontsize': font_size})
            st.pyplot(fig)

            st.text('The number of beers for each aroma score')
            fig, ax = plt.subplots()
            ax.pie(q8['Count aroma'], labels=q8['Beer aroma'], autopct='%1.1f%%', textprops={'fontsize': font_size})
            st.pyplot(fig)

            st.text('The number of beers for each total score')
            fig, ax = plt.subplots()
            ax.pie(q9['Count total'], labels=q9['Beer total'], autopct='%1.1f%%', textprops={'fontsize': font_size})
            st.pyplot(fig)

            st.text('The number of beers for each taste score')
            fig, ax = plt.subplots()
            ax.pie(q10['Count taste'], labels=q10['Beer taste'], autopct='%1.1f%%', textprops={'fontsize': font_size})
            st.pyplot(fig)

            st.text('The number of beers for each palate score')
            fig, ax = plt.subplots()
            ax.pie(q11['Count palate'], labels=q11['Beer palate'], autopct='%1.1f%%', textprops={'fontsize': font_size})
            st.pyplot(fig)

    # elif st.session_state.toView == "Query 8":
    #     st.markdown('---')
    #     st.header("Exploratory Data Analysis")
    #     st.subheader('Q8')
    #     with st.spinner("Fetching Data"):
    #         time.sleep(5)
    #     st.text('The number of beers for each aroma score')
    #     st.bar_chart(data=q8, x='Beer aroma', y=' Count')
    #     st.write(q8)
    # elif st.session_state.toView == "Query 9":
    #     st.markdown('---')
    #     st.header("Exploratory Data Analysis")
    #     st.subheader('Q9')
    #     with st.spinner("Fetching Data"):
    #         time.sleep(5)
    #     st.text('The number of beers for each total score')
    #     st.bar_chart(data=q9, x='Beer total', y=' Count')
    #     st.write(q9)
    # elif st.session_state.toView == "Query 10":
    #     st.markdown('---')
    #     st.header("Exploratory Data Analysis")
    #     st.subheader('Q10')
    #     with st.spinner("Fetching Data"):
    #         time.sleep(5)
    #     st.text('The number of beers for each taste score')
    #     st.bar_chart(data=q10, x='Beer taste', y=' Count')
    #     st.write(q10)
    # elif st.session_state.toView == "Query 11":
    #     st.markdown('---')
    #     st.header("Exploratory Data Analysis")
    #     st.subheader('Q11')
    #     with st.spinner("Fetching Data"):
    #         time.sleep(5)
    #     st.text('The number of beers for each palate score')
    #     st.bar_chart(data=q11, x='Beer palate', y=' Count')
    #     st.write(q11)
    elif st.session_state.toView == "Query 12":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q12')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The users that reviewed a particular beer')
        beer_name = st.selectbox("What beer would you like to get reviewers for?", q12["Beer name"])
        if beer_name:
            data = q12[q12["Beer name"] == beer_name]
            st.table(data=data)
    elif st.session_state.toView == "Query 13":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q13')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The timestamp over overall time of users with most activity')
        opt = st.selectbox(
            'Choose the style of comparison',
            ('Randomly',
             'Show for particular reviewer'))
        
        if opt == "Randomly":
            num_reviewers = st.number_input("Enter the number of reviewers you want to compare", step=1)
            if num_reviewers:
                st.bar_chart(data=q13.sample(n=num_reviewers), x="Profile name", y=" Number of reviews")
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

    elif st.session_state.toView == "Query 14":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q14')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The number of reviews per year of active users')
        
        selected_users = st.multiselect("Select Users", q14["Profile name"])
        users_df = q14[q14["Profile name"].isin(selected_users)]
        pivot_df = users_df.pivot(index="Profile name", columns=" Year", values=" Number of reviews")

        chart_data = pivot_df.loc[selected_users].T
        st.line_chart(chart_data)

        st.markdown(f"**X-axis Label:** Year")
        st.markdown(f"**Y-axis Label:** Number of Reviews")
        st.markdown(f"**Title:** Number of Reviews per Year")
    elif st.session_state.toView == "Query 15":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q15')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The beer reviews over time for a particular beer')

        num_beers = st.number_input("Enter the number of beers you want to display", step=1)

        selected_beers = q15["Beer name"].sample(n=num_beers)
        users_df = q15[q15["Beer name"].isin(selected_beers)]
        pivot_df = users_df.pivot(index="Beer name", columns=" Date", values=" Number of reviews")

        chart_data = pivot_df.loc[selected_beers].T
        st.line_chart(chart_data)

        st.markdown(f"**X-axis Label:** Date")
        st.markdown(f"**Y-axis Label:** Number of Reviews")
        st.markdown(f"**Title:** Number of Reviews per Date")
    elif st.session_state.toView == "Query 16":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q16')
        with st.spinner("Fetching Data"):
            time.sleep(5)
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
    elif st.session_state.toView == "Query 17":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q17')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The top-rated beers by style')

        st.table(data=q17)

        chart_data = q17.groupby('Beer style')[' Total rating'].sum()
        st.line_chart(chart_data)
    elif st.session_state.toView == "Query 18":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q18')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('The breweries which are mentioned most often in positive reviews (aka >4)')

        opt = st.selectbox(
            'Choose the style of comparison',
            ('Top five',
             'Randomly',
             'Show for particular breweries'))
        
        if opt == "Top five":
             st.bar_chart(data=q18.head(5), x="Brewery name", y=" Number of mentions")
        elif opt == "Randomly":
            num_brewers = st.number_input("Enter the number of brewers you want to display", step=1)
            if num_brewers:
                st.bar_chart(data=q18.sample(n=num_brewers), x="Brewery name", y=" Number of mentions")
        elif opt == "Show for particular breweries":
            selected_breweries = st.multiselect("Select Users", q18["Brewery name"])
            breweries_df = q18[q18["Brewery name"].isin(selected_breweries)]
            # pivot_df = breweries_df.pivot(index="Brewery name", columns=" Brewery name", values=" Number of mentions")

            # chart_data = pivot_df.loc[selected_breweries].T
            st.bar_chart(breweries_df, x="Brewery name", y=" Number of mentions")

            st.markdown(f"**X-axis Label:** Breweries")
            st.markdown(f"**Y-axis Label:** Number of Mentions")
            st.markdown(f"**Title:** Number of Reviews per Brewery")
    elif st.session_state.toView == "Query 19":
        st.markdown('---')
        st.header("Exploratory Data Analysis")
        st.subheader('Q19')
        with st.spinner("Fetching Data"):
            time.sleep(5)
        st.text('How the popularity of different beer styles changed over years')

        selected_styles = st.multiselect("Select Styles", q19["Beer style"].unique())
        styles_df = q19[q19["Beer style"].isin(selected_styles)]
        pivot_df = styles_df.pivot(index="Beer style", columns=" Year", values=" Average rating")

        chart_data = pivot_df.loc[selected_styles].T
        st.line_chart(chart_data)

        st.markdown(f"**X-axis Label:** Year")
        st.markdown(f"**Y-axis Label:** Average rating")
        st.markdown(f"**Title:** Average rating per Year")
    elif st.session_state.toView == "Submit":
        runData()

showMain()