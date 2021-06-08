import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
import plotly.express as px
import plotly.graph_objects as go







def get_data(file):
    df = pd.read_csv(file)
    return df

def show_data(df):
    st.write('**Viewing History:** ')
    df =df.dropna()
    st.write(df)
    
    

    df['Date'] = pd.to_datetime(pd.Series(df['Date']))
    df['Year'], df['Month'] = df['Date'].dt.year, df['Date'].dt.month_name()
    df['Day'] = df['Date'].dt.day
    df['Day_of_week'] = df['Date'].dt.day_name()
    category = []
    for value in df['Title']:
        if ': ' in value:
            category.append('TV')
        else:
            category.append('Movie')
    df['Category'] = category
    


    tv_titles= df[df['Category'] == 'TV']
    tv_titles[['Show','Episode']] = tv_titles['Title'].str.split(": ", n=1,expand=True)

    n = 10
    top10= tv_titles['Show'].value_counts()[:n].rename_axis('Show').reset_index(name='EpisodeCount')
    
    top10shows = tv_titles[tv_titles['Show'].isin(top10['Show'])]


    
    
    
    

    

    

####Data Vis############
    
    plot_month = alt.Chart(df).mark_bar(
        cornerRadiusTopLeft=4,
        cornerRadiusTopRight=4,
    ).encode(
        x= alt.X('Month',sort='-y'),
        y= 'count()',
        color= 'Category',
        tooltip=['Category', 'count()']
    ).properties(
        title='Month'
    ).interactive()  
    
    plot_weekday = alt.Chart(df).mark_bar(
        cornerRadiusTopLeft=4,
        cornerRadiusTopRight=4
    ).encode(
        x= alt.X('Day_of_week', title=None, sort='-y'),
        y= 'count()',
        color= 'Category',
        tooltip=['Category', 'count()']
    ).properties(
        title='Day of The Week'
    ).interactive()

    plot_titles = alt.Chart(df).mark_circle().encode(
        x='yearmonth(Date)',
        y='Category',
        color='Category',
        tooltip=['Title', 'Date']
    ).interactive()

    plot_top10 = alt.Chart(top10).mark_bar(
        cornerRadiusTopLeft=3,
        cornerRadiusTopRight=3,
        opacity=1
    ).encode(
        x= alt.X('Show', sort='-y'),
        y= 'EpisodeCount',
        tooltip= ['Show', 'EpisodeCount']
    ).properties(
        title='Top 10 Shows'
    ).interactive()

    fig = px.strip(df, x="Date",color="Category",hover_name='Title')
    
    fig3= px.strip(top10shows, x='Date', y='Show', color='Show', hover_name='Episode')
    fig3 =fig3.update_layout(showlegend=False)
    config = {
        'displaylogo': False
        
    }


    
 

###show charts
    #st.altair_chart(plot_top10, use_container_width=True)
    #top10 charts
    #weekly and monthly charts
    left_column, right_column= st.beta_columns(2)
    with left_column:
        st.altair_chart(plot_weekday, use_container_width=True)
    with right_column:
        st.altair_chart(plot_month, use_container_width=True)


    col1, col2 = st.beta_columns([1,2])
    col1.subheader('Top 10 Shows')
    col1.write(top10)
    col2.plotly_chart(fig3, use_container_width=True, config=config)

    st.subheader('Viewing History Across Time')
    st.plotly_chart(fig, use_container_width=True, config=config)
    
    
    
    

    
    

    
    
    
    




def main():

    st.title('Analyize Your Netflix Viewing History')
    st.subheader('**A breakdown of your netflix history**')

    st.write('[**click here to download your netlfix viewing history**](https://www.netflix.com/viewingactivity)')

    file = st.file_uploader('Upload file', type=['csv'])
    
    
    if file == None:
        pass
    else:
        df = get_data(file)
        show_data(df)
    
    



main()
    
