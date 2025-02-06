import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Netflix Data Analysis")

# File uploader
df = None
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file, lineterminator='\n')
    st.write("### Data Preview")
    st.dataframe(df.head())
    
    # Display basic info
    st.write("### Dataset Info")
    st.write(df.info())
    
    # Convert Release_Date to datetime if it exists
    if 'Release_Date' in df.columns:
        df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce').dt.year
        st.write("Converted 'Release_Date' to year format.")
    
    # Drop unnecessary columns
    drop_cols = ['Overview', 'Original_Language', 'Poster_Url']
    df.drop(columns=[col for col in drop_cols if col in df.columns], inplace=True)
    
    # Show summary statistics
    st.write("### Data Summary")
    st.write(df.describe())
    
    # Visualization: Genre Count
    if 'Genre' in df.columns:
        st.write("### Genre Distribution")
        plt.figure(figsize=(10,5))
        sns.countplot(y=df['Genre'], order=df['Genre'].value_counts().index)
        plt.xlabel("Count")
        plt.ylabel("Genre")
        st.pyplot(plt)
    
    # Visualization: Release Year Distribution
    if 'Release_Date' in df.columns:
        st.write("### Release Year Distribution")
        plt.figure(figsize=(10,5))
        sns.histplot(df['Release_Date'].dropna(), bins=20, kde=True)
        plt.xlabel("Year")
        st.pyplot(plt)

st.write("Upload a Netflix dataset to analyze!")
