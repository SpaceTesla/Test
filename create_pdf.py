from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(text_file, pdf_file):
    # Create a canvas
    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Read text from the input file with the appropriate encoding
    with open(text_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Set the font and size
    c.setFont("Helvetica", 12)

    # Set starting y position
    y = 750

    # Set the left margin
    x = 50

    # Define the line height
    line_height = 15

    # Set bottom margin
    bottom_margin = 50

    # Write text to the PDF
    for line in lines:
        words = line.split()  # Split line into words
        for word in words:
            # Calculate the width of the word
            word_width = c.stringWidth(word, "Helvetica", 12)

            # Check if the word goes beyond the right margin
            if x + word_width > 550:
                # Move to the next line
                y -= line_height

                # Check if the y position goes beyond the bottom margin
                if y < bottom_margin:
                    # Add a new page
                    c.showPage()
                    # Reset y position to the top margin
                    y = 750

                # Reset x position to the left margin
                x = 50

            # Draw the word
            c.drawString(x, y, word)

            # Move to the next word position
            x += word_width + c.stringWidth(' ', "Helvetica", 12)

        # Move to the next line
        y -= line_height
        # Check if the y position goes beyond the bottom margin
        if y < bottom_margin:
            # Add a new page
            c.showPage()
            # Reset y position to the top margin
            y = 750
        # Reset x position to the left margin
        x = 50

    # Save the PDF
    c.save()

if __name__ == "__main__":
    text_file = "output.txt"  # Change this to your input file
    pdf_file = "output.pdf"  # Change this to your output file

    create_pdf(text_file, pdf_file)
