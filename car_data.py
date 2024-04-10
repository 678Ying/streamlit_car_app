import streamlit as st
import pandas as pd

df = pd.read_csv('car_data.csv') # Ensure the CSV file is in your project folder

# Sidebar filters
st.sidebar.header('Filters')
car_name = st.sidebar.text_input('Car Name', '')
transmission = st.sidebar.multiselect('Transmission', df['Transmission'].unique(), default=df['Transmission'].unique())
selling_price_range = st.sidebar.slider('Selling Price Range', int(df['Selling_Price'].min()), int(df['Selling_Price'].max()), (0, 20))
year_range = st.sidebar.slider('Year Range', int(df['Year'].min()), int(df['Year'].max()), (2000, 2024))

# Main app
if st.sidebar.button('Submit'):
    # Filter data
    filtered_df = df
    if car_name:
        filtered_df = filtered_df[filtered_df['Car_Name'].str.contains(car_name, case=False)]
    filtered_df = filtered_df[filtered_df['Transmission'].isin(transmission)]
    filtered_df = filtered_df[(filtered_df['Selling_Price'] >= selling_price_range[0]) & (filtered_df['Selling_Price'] <= selling_price_range[1])]
    filtered_df = filtered_df[(filtered_df['Year'] >= year_range[0]) & (filtered_df['Year'] <= year_range[1])]
    
    # Display filtered data
    st.dataframe(filtered_df)
else:
    # Display original data
    st.dataframe(df)
