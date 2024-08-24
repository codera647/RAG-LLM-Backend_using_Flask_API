import PyPDF2




# Function to read text
def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to read PDF file
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    all_text = ""
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        all_text += page.extract_text()
    return all_text

# Document loader
def doc_load(uploaded_file):


    if uploaded_file['file_type'] == "text":
            content = read_text(uploaded_file["absolute_path"])
    elif uploaded_file['file_type'] == "PDF":
       try:
             content = read_pdf(uploaded_file["absolute_path"])
       except Exception as e:
           return None

    return content