import PyPDF2
from gemini import bot
def extract_sections(pdf_path, sections, output_txt):
    # Initialize an empty string to store the text
    text = ''

    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Iterate through each page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()

            # Check if the page contains any of the specified sections
            for section in sections:
                section_index = page_text.lower().find(section.lower())
                if section_index != -1:
                    # Add text starting from the section title to the next section title
                    next_section_index = page_text.lower().find(section.lower(), section_index + len(section))
                    if next_section_index != -1:
                        text += page_text[section_index:next_section_index]
                    else:
                        text += page_text[section_index:]
                    break

    # Write the extracted text to a text file
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
        bot(text)

if __name__ == "__main__":
    pdf_path = r"1707994184221.pdf"
    output_txt = "output.txt"
    
    # Define the necessary sections
    sections = ["Risk Factors", "About Our Company", "Financial Information", 
                "Legal and Other Information", "Offer Related Information", 
                "Other Information"]

    extract_sections(pdf_path, sections, output_txt)
