import fitz  # PyMuPDF

# Correct path to your PDF file
pdf_file = "/Users/avirajahalawat/Desktop/rasa_project/rasa_project/NCRTC-Premises-Hiring-Policy-for-Events.pdf"



# Open the PDF file
try:
    document = fitz.open(pdf_file)
    print("PDF opened successfully.")
except Exception as e:
    print(f"Failed to open PDF: {e}")
    exit()

# Extract text from each page
text = ""
for page in document:
    text += page.get_text() + "\n"  # Adding a newline for better formatting
    print(f"Extracted text from page {page.number + 1}")

# Save the extracted text to a text file
output_file = "ncrtc_hiring_policy.txt"
try:
    with open(output_file, "w") as text_file:
        text_file.write(text)
    print(f"Text extraction complete! Check {output_file} for the output.")
except Exception as e:
    print(f"Failed to write to file: {e}")

document.close()
