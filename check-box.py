from PyPDF2 import PdfFileReader

def getcheckboxes(filename):
    with open(filename, "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        fields = pdf_reader.getFields()

        for field_name, field in fields.items():
            if "/FT" in field and field["/FT"] == "/Btn" and "/V" in field:
                print(f"Checkbox {field_name} value is {field['/V']}")

getcheckboxes("formulario.pdf")