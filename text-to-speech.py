import pyttsx3
import PyPDF2

# Replace the pdf file with the path to your own PDF file
pdf_path = r'C:\Users\DAPO\Documents\python projects\file.pdf'  # Use raw string to avoid escape sequence issues
pdf_reader = PyPDF2.PdfFileReader(open(pdf_path, 'rb'))
reader = pyttsx3.init()

for page in range(pdf_reader.numPages):
    text = pdf_reader.getPage(page).extractText()
    legible_text = text.strip().replace('\n', ' ')
    print(legible_text)
    reader.say(legible_text)

    # Save the text to an MP3 file
    output_file = f'page_{page+1}.mp3'
    reader.save_to_file(legible_text, output_file)
    reader.runAndWait()

reader.stop()  