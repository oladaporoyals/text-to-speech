import pyttsx3
import PyPDF4

# Replace the pdf file with the path to your own PDF file
pdf_path = r'C:\Users\DAPO\Documents\python projects\file.pdf' 

# Use raw string to avoid escape sequence issues

#initialize the PDF reader
pdf_reader = PyPDF4.PdfFileReader(open(pdf_path, 'rb'))

#initialize the text to speech engine
reader = pyttsx3.init()

#get the page numbers in the PDF
num_pages = pdf_reader.numPages


for page in range(num_pages):
    #extract the texts from the pdf page
    text = pdf_reader.getPage(page).extractText()
    legible_text = text.strip().replace('\n', ' ')
    print(legible_text)
    
    # this part says the contents of the text
    reader.say(legible_text)
    reader.runAndWait()

    # Save the text to an MP3 file
    output_file = f'page_{page+1}.mp3'
    reader.save_to_file(legible_text, output_file)
    reader.runAndWait()

reader.stop()  
