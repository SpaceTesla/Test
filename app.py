from gemini import bot

from pdf_to_text import extract_sections
from create_pdf import create_pdf

sections = ["Risk Factors", "About Our Company", "Financial Information", 
                "Legal and Other Information", "Offer Related Information", 
                "Other Information"]

extract_sections('1707994184221.pdf', sections, 'output.txt');

create_pdf('output.txt', 'output.pdf');

