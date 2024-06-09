import streamlit as st
import pandas as pd

def search():
    st.set_page_config(
        page_title='Gods Eye - Dashboard',
        page_icon='assets/favicon.png',
        layout='wide',
        initial_sidebar_state='collapsed'
    )
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
            st.text_input('Share Price', value='Unavailable')

    with col4:
        if 'company_origin' in st.session_state:
            st.text_input('Company Origin', value=st.session_state.company_origin)
        else:
            st.text_input('Company Origin', value='Unavailable')

    if 'article_summary' in st.session_state:
        st.text_area('Document Summary', value=st.session_state.article_summary, height=400, help='Powered by Gemini')
    else:
        st.text_area('Document Summary', value='Unavailable', height=400, help='Powered by Gemini')
    
    st.button('Download Summary', use_container_width=True)

    st.divider()

    row = st.columns([4, 4])
    grid = [col.container(height=200) for col in row]

    with grid[0]:
        st.subheader('Key Points')
        if 'article_highlight' in st.session_state:
            st.write("1.")
        else:
            st.write("1. ")

    with grid[1]:
        st.subheader('Company Background')
        if 'trending_highlight' in st.session_state:
            st.write(f'CEO: {st.session_state.trending_highlight}')
        else:
            st.write('CEO: Unavailable')

        if 'article_keyword' in st.session_state:
            st.write(f'CTO: {st.session_state.article_keyword}')
        else:
            st.write('CTO: Unavailable')
        
        if 'article_keyword' in st.session_state:
            st.write(f'CFO: {st.session_state.article_keyword}')
        else:
            st.write('CFO: Unavailable')


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
    st.write("Box Plot for 'Restated Earnings Per Share'")
    st.pyplot(financial_df.loc["Restated Earnings Per Share (Basic) (Fiscal 2023)"]["value"].plot.box())
    st.title('Financial Performance Metrics (Box Plot)')

    # 5. Histogram
    st.write("Histogram for 'Restated Earnings Per Share'")
    st.pyplot(financial_df.loc["Restated Earnings Per Share (Basic) (Fiscal 2023)"]["value"].plot.hist())
    st.title('Financial Performance Metrics (Histogram)')


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

search()
