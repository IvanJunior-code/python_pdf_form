import pdfrw

def obter_campos_e_valores(input_pdf):
    campos_e_valores = {}

    template = pdfrw.PdfReader(input_pdf)
    for page in template.pages:
        if '/Annots' in page:
            annotations = page['/Annots']
            for annotation in annotations:
                if '/T' in annotation and '/V' in annotation:
                    campo_id = annotation.id
                    campo_nome = annotation['/T']
                    campo_valor = annotation['/V']
                    campos_e_valores[campo_nome] = (campo_id, campo_valor)

    return campos_e_valores

# Exemplo de uso
campos_e_valores = obter_campos_e_valores('formulario_preenchido.pdf')
print("Campos e valores do formulário:", campos_e_valores)
