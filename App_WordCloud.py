import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Title and Markdown
st.markdown("This app performs Word Cloud \
             Python Libraries: streamlit, pandas, BeautifulSoup, wordcloud")

# Options for links
st.sidebar.header("Select Link")
links = ["https://www.forrester.com/blogs/the-seventh-wave-how-ai-will-change-the-technology-industry/", "https://www.forrester.com/blogs/master-tech-mayhem-technology-innovation-summit-comes-to-london/", "https://www.forrester.com/blogs/a-peek-at-bank-of-americas-ai-playbook/", "https://www.forrester.com/blogs/cx-summit-north-america-lessons-to-deliver-the-total-experience/", "https://www.forrester.com/blogs/pause-innovation-now-and-pay-the-price-later-why-ai-readiness-cant-wait/"]

# Select link
URL = st.sidebar.selectbox('Link', links)

# Select no. of words to display
st.sidebar.header("Select number of words you want to display")
words = st.sidebar.selectbox('Number of words', range(10, 1000, 10))

# Create wordcloud
if URL is not None:
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('div', class_='blog-post-content') or soup.find('article')
    if table is not None:
        text = table.text
        cleaned_text = re.sub('\t', "", text)
        cleaned_texts = re.split('\n', cleaned_text)
        cleaned_textss = "".join(cleaned_texts)
        st.write("Word Cloud Plot")
        stopwords = set(STOPWORDS)
        wordcloud = WordCloud(background_color="white", max_words=words, stopwords=stopwords).generate(cleaned_textss)

        # Display Word Cloud
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.error("Main content not found in the selected URL.")
