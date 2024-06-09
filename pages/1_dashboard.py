import streamlit as st
import pandas as pd
import json
import random
from create_pdf import create_pdf

st.set_page_config(
        page_title='Gods Eye - Dashboard',
        page_icon='assets/favicon.png',
        layout='wide',
        initial_sidebar_state='collapsed'
)

def get_share_price():
    return random.randint(10, 100)

with open('summary.json') as file:
    summary_data = json.load(file)

def search():
    st.markdown(
        "<h1 style='text-align: center;'>Dashboard</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    col1, col2, col3, col4 = st.columns([4, 4, 2, 2])

    with col1:
        if 'news_source' in st.session_state:
            st.text_input('Company Name', value=st.session_state.news_source)
        else:
            st.text_input('Company Name', value='Unavailable')

    with col2:
        if 'news_topic' in st.session_state:
            st.text_input('Document Type', value=st.session_state.news_topic)
        else:
            st.text_input('Document Type', value='Unavailable')

    with col3:
        if 'share_price' in st.session_state:
            st.text_input('Share Price', value=st.session_state.share_price)
        else:
            st.text_input('Share Price', value=f'₹ {get_share_price()}')

    with col4:
        if 'company_origin' in st.session_state:
            st.text_input('Company Origin', value=st.session_state.company_origin)
        else:
            st.text_input('Company Origin', value='India')

    if 'summary' in summary_data['summary']:
        text_area = ""
        for key, value in summary_data['summary'].items(): 
            text_area+= f"{key}: {value}\n\n"
        # st.text_area('Document Summary', value=summary_data['summary'], height=400, help='Powered by Gemini')
        st.text_area('Document Summary', value=text_area, height=400, help='Powered by Gemini')
    else:
        text_area = ""
        for key, value in summary_data['summary'].items(): 
            text_area+= f"{key}: {value}\n\n"
        st.text_area('Document Summary', value=text_area, height=400, help='Powered by Gemini')
    
    # Assuming 'summary.pdf' exists in your current directory or specify the path
        file_path = 'summary.json'

        # Check if the button is clicked
        with open(file_path, "r") as pdf_file:
    # Create a download button and use the content of the pdf file directly
            st.download_button(label="Download Summary PDF",
                            data=pdf_file,
                            file_name="summary.pdf",
                            mime="application/octet-stream",
                            use_container_width=True)

    st.divider()

    row = st.columns([4, 4])
    grid = [col.container(height=200) for col in row]

    with grid[0]:
        st.subheader('Key Points')

        for key, value in summary_data['key_points'].items(): 
            st.write(f"{key}. {value}\n\n")


    with grid[1]:
        st.subheader('Company Background')
        if 'trending_highlight' in st.session_state:
            st.write(f'CEO: {st.session_state.trending_highlight}')
        else:
            st.write('CEO: Mr. Aloke Bajpai')

        if 'article_keyword' in st.session_state:
            st.write(f'CTO: {st.session_state.article_keyword}')
        else:
            st.write('CTO: Rajnish Kumar')
        
        if 'article_keyword' in st.session_state:
            st.write(f'CFO: {st.session_state.article_keyword}')
        else:
            st.write('CFO:  Mr. Shailesh Lakhani')
        
        st.write('Founded: 2005')
        st.write('Headquarters: Gurugram, Haryana, India')
        st.write('Industry: Travel and Tourism')
        st.markdown(
            "Website: https://www.ecorentacar.com/about-us/"
        )
        st.write('Stock Exchange: BSE, NSE')
        st.write('Stock Symbol: [:green[ECOS]]')
        st.write('Market Cap: [:orange[₹ 1,000 Cr]]')
        st.write('Revenue: [:red[₹ 500 Cr]]')
        st.write('Employees: [:violet[500+]]')
        st.write('Company Type: [:gray[Public]]')
        st.write('Company Size: [:rainbow[501-1000 employees]]')



# Financial performance data
    financial_performance = {
        "Year-on-Year Revenue Growth (Fiscal 2023 vs. Fiscal 2022)": {
            "value": "33.61",
            "unit": "%"
        },
        "EBITDA Margin (Fiscal 2023)": {
            "value": "8.70",
            "unit": "%"
        },
        "Adjusted EBITDA Margin (Fiscal 2023)": {
            "value": "8.85",
            "unit": "%"
        },
        "Restated Earnings Per Share (Basic) (Fiscal 2023)": {
            "value": "0.58",
            "unit": "\u20b9"
        },
        "Restated Earnings Per Share (Diluted) (Fiscal 2023)": {
            "value": "0.57",
            "unit": "\u20b9"
        }
    }

# Convert data to DataFrame
    financial_df = pd.DataFrame(financial_performance).T
    financial_df["value"] = financial_df["value"].astype(float)

    # 1. Bar Plot
    st.bar_chart(financial_df["value"])
    # st.xlabel('Metrics')
    # st.ylabel('Value')
    st.title('Financial Performance Metrics (Bar Plot)')

    # 2. Line Chart
    st.line_chart(financial_df["value"])
    # st.xlabel('Metrics')
    # st.ylabel('Value')
    st.title('Financial Performance Metrics (Line Chart)')

    # 3. Pie Chart
    st.write("Pie Chart for 'EBITDA Margin' and 'Adjusted EBITDA Margin'")
    st.write(financial_df.loc[["EBITDA Margin (Fiscal 2023)", "Adjusted EBITDA Margin (Fiscal 2023)"]]["value"].plot.pie())
    st.title('Financial Performance Metrics (Pie Chart)')

    # 4. Box Plot
    try:
        st.write("Box Plot for 'Restated Earnings Per Share'")
        st.pyplot(financial_df.loc["Restated Earnings Per Share (Basic) (Fiscal 2023)"]["value"].plot.box())
        st.title('Financial Performance Metrics (Box Plot)')
    except Exception as e:  
        st.write("unable to get box plot")  

    # 5. Histogram
    try:
        st.write("Histogram for 'Restated Earnings Per Share'")
        st.pyplot(financial_df.loc["Restated Earnings Per Share (Basic) (Fiscal 2023)"]["value"].plot.hist())
        st.title('Financial Performance Metrics (Histogram)')
    except Exception as e:
        st.write("unable to get histogram")

    # with grid[1]:
    #     st.subheader('Sentiment Analysis')
    #     if 'average_positivity' in st.session_state:
    #         st.write(f'Average :green[Positivity]: {st.session_state.average_positivity}')
    #     else:
    #         st.write('Average :green[Positivity]: Unavailable')

    #     if 'average_neutrality' in st.session_state:
    #         st.write(f'Average :grey[Neutrality]: {st.session_state.average_neutrality}')
    #     else:
    #         st.write('Average :grey[Neutrality]: Unavailable')

    #     if 'average_negativity' in st.session_state:
    #         st.write(f'Average :red[Negativity]: {st.session_state.average_negativity}')
    #     else:
    #         st.write('Average :red[Negativity]: Unavailable')

    # with grid[2]:
    #     st.subheader('Media Analysis')
    #     if 'total_article' in st.session_state:
    #         st.write(f':orange[Total] Articles: {st.session_state.total_article}')
    #     else:
    #         st.write(':orange[Total] Articles: Unavailable')

    #     if 'flagged_article' in st.session_state:
    #         st.write(f':red[Flagged] Articles: {st.session_state.flagged_article}')
    #     else:
    #         st.write(':red[Flagged] Articles: Unavailable')

    #     if 'ai_content' in st.session_state:
    #         st.write(f':green[AI Generated] Content: {st.session_state.ai_content}')
    #     else:
    #         st.write(':green[AI Generated] Content: Unavailable')

    st.divider()
    st.markdown(
        """
        <footer style='text-align: center; margin-top: 40px;'>
            <p>Made with ♥️ Powered by Gemini</p>
            <a href="https://github.com/areebahmeddd/GodsEye/blob/main/LICENSE">License</a> •
            <a href="https://github.com/areebahmeddd/GodsEye/blob/main/README.md">Documentation</a>
        </footer>
        """,
        unsafe_allow_html=True
    )

search()
