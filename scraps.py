import streamlit as st
import pandas as pd

# Load the clustered data
data = pd.read_csv('clustered_sport_articles.csv')

# Create a sidebar for selecting clusters
selected_cluster = st.sidebar.selectbox('Select Cluster', sorted(data['Cluster'].unique()))

# Filter the data based on the selected cluster
cluster_data = data[data['Cluster'] == selected_cluster]

# Display the articles in the selected cluster
st.header(f'Cluster {selected_cluster}')
for index, row in cluster_data.iterrows():
    st.subheader(row['Title'])
    st.write(f"URL: [{row['URL']}]({row['URL']})")
    st.write(row['Content'])
    st.markdown("---")
