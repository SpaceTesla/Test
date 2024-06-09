import streamlit as st

def technology():
    st.set_page_config(
        page_title='Gods Eye - Overview',
        page_icon='assets/favicon.png',
        layout='wide',
        initial_sidebar_state='collapsed'
    )
    st.markdown(
        "<h1 style='text-align: center;'>Technology Overview</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    st.markdown(
        """
# Technology Stack and Project Flow of StockDragon Gen 1

## Technology Stack

To implement StockDragon Gen 1, we have meticulously chosen a robust technology stack to ensure seamless operation, effective data processing, and an intuitive user experience. Here’s an overview of the technologies used:

### Front End and Data Visualization

- Streamlit: We use Streamlit for building the front end and data visualization. Streamlit's simplicity and interactivity make it an ideal choice for creating dynamic web applications, allowing us to present summaries, key facts, and data visualizations in an intuitive manner.

### Document Processing

- PyPDF2: For converting PDF documents to text, we utilize PyPDF2. This library allows us to extract text data from the legal affidavits (DRHP, RHP, Prospectuses) efficiently, forming the basis for further text analysis and summarization.

### Web Scraping

- Puppeteer: Puppeteer is employed for web scraping to collect legal affidavits from various sources. It helps automate the extraction of these documents, ensuring we have the latest and most accurate data for analysis.

### Summarization and Text Analysis

- Gemini API: The Gemini API is the core of our text analysis and summarization. It processes the extracted text, transforming extensive 500+ page documents into concise 10-page summaries. Additionally, it highlights key facts and generates summaries that are easy to understand.

### Chatbot Integration

- Gemini API: We also use the Gemini API to power our chatbot feature. This chatbot assists users by answering queries and providing explanations, ensuring that users can interactively engage with the information provided.

## Project Flow

The following steps outline the complete flow of the StockDragon Gen 1 project:

### 1. User Input

The user starts by inputting the name of the company and selecting the specific legal affidavit (DRHP, RHP, or Prospectus) they wish to analyze.

### 2. Document Retrieval

Using Puppeteer, StockDragon Gen 1 scrapes the required legal affidavit from relevant sources. This ensures that the user has access to the most current and comprehensive documents.

### 3. PDF to Text Conversion

Once the document is retrieved, PyPDF2 is employed to convert the PDF content into text format. This text data serves as the raw material for further processing.

### 4. Text Analysis and Summarization

The Gemini API processes the extracted text, summarizing the 500+ page document into a 10-page document. This summary focuses on key facts, providing an accessible overview of the IPO details.

### 5. Data Visualization and Presentation

Using Streamlit, the summarized content is presented to the user. This includes:
- A concise paragraph summary of the document.
- Highlighted key facts and essential information.
- Interactive graphs and visualizations to aid in data interpretation.

### 6. Interactive User Support

The Gemini API-powered chatbot is available for user queries. It helps clarify any doubts, providing explanations and additional information as needed.

## Conclusion

By integrating these technologies, StockDragon Gen 1 delivers a powerful tool for small and medium investors. It simplifies complex IPO documents, making the stock market more accessible and understandable. The seamless flow from document retrieval to interactive user support ensures that investors can make informed decisions with ease and confidence.

---
""",
        unsafe_allow_html=True
    )
    st.image('design.drawio.png', caption='System Design', use_column_width=True)
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

technology()
