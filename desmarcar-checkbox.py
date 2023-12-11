from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject

def desmarcar_checkboxes(input_pdf, output_pdf):
    with open(input_pdf, "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        pdf_writer = PdfFileWriter()

        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            if '/Annots' in page:
                annotations = page['/Annots']
                for annotation_ref in annotations:
                    annotation = annotation_ref.getObject()
                    if "/FT" in annotation and annotation["/FT"] == "/Btn" and "/V" in annotation:
                        # Desmarca o checkbox (define o valor como "/Off")
                        annotation.update({
                            NameObject("/V"): createStringObject("/Off")
                        })

            pdf_writer.addPage(page)

        with open(output_pdf, "wb") as output_file:
            pdf_writer.write(output_file)

# Exemplo de uso
desmarcar_checkboxes("formulario.pdf", "formulario_sem_selecao.pdf")
