import pyttsx3
import PyPDF4

# Replace the pdf file with the path to your own PDF file
pdf_path = r'C:\Users\Oladapo\Documents\git (work)\text-to-speech\file.pdf'

# Use raw string to avoid escape sequence issues

# Initialize the PDF reader
try:
    pdf_reader = PyPDF4.PdfFileReader(open(pdf_path, 'rb'))
except FileNotFoundError:
    print(f"The file {pdf_path} was not found.")
    exit(1)

# Check if the PDF was read correctly
if pdf_reader.isEncrypted:
    try:
        pdf_reader.decrypt('')
    except:
        print("Failed to decrypt the PDF file.")
        exit(1)

# Initialize the text-to-speech engine
reader = pyttsx3.init()

# Set properties (optional, but helpful for debugging)
reader.setProperty('rate', 150)  # Speed of speech
reader.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Get the number of pages in the PDF
num_pages = pdf_reader.numPages

if num_pages == 0:
    print("The PDF file is empty or could not be read.")
    exit(1)

for page in range(num_pages):
    # Extract the text from the PDF page
    try:
        text = pdf_reader.getPage(page).extractText()
    except:
        print(f"Failed to extract text from page {page+1}.")
        continue
    
    if text:  # Check if text extraction was successful
        legible_text = text.strip().replace('\n', ' ')
        print(f"Page {page+1}: {legible_text}")  # Print the text for debugging
        
        # This part says the contents of the text
        reader.say(legible_text)
        reader.runAndWait()
    else:
        print(f"Warning: No text found on page {page+1}")

reader.stop()

