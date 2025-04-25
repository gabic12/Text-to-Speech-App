import requests
import pypdf

API_KEY = "8a024506cfa948edab518d0d7c93581d"
FILE_PATH = "duck.pdf"

#Read the contents of the PDF file
file_content = ''
file_reader = pypdf.PdfReader(FILE_PATH)

for page in range(len(file_reader.pages)):
    file_content += file_reader.pages[page].extract_text(extraction_mode="plain")

file_content = ' '.join(line.strip() for line in file_content.splitlines()) #compress everything into one block (no newlines)

api_parameters = {
    "key": API_KEY,
    "hl": "en-us",
    "src": file_content,
    "v": "Mary",
    "c": "MP3",
    "f": "ulaw_44khz_stereo"
}

#Requesting the API to convert the text to audio
response = requests.get(url="http://api.voicerss.org/", params=api_parameters)
response.raise_for_status()

#Creating the audio file
try:
    with open("audio_file.mp3", "wb") as audio_file:
        audio_file.write(response.content)
    print("Audio file created successfully!")
except Exception:
    print("Failed to create audio file!")