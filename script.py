import PyPDF2

def preencher_campos_pdf(input_pdf, output_pdf, campo_valores):
    # Abre o arquivo PDF de entrada
    with open(input_pdf, 'rb') as file:
        # Cria um objeto PDF para o arquivo de entrada
        pdf_reader = PyPDF2.PdfReader(file)

        # Cria um objeto PDF para o arquivo de saída
        pdf_writer = PyPDF2.PdfWriter()

        # Loop através de todas as páginas do PDF
        #for page_num in range(pdf_reader.getNumPages()):
        for page_num in range(len(pdf_reader.pages)):
            # Obtém a página atual
            page = pdf_reader.pages[page_num]

            # Verifica se a página possui formulários interativos
            if '/Annots' in page:
                # Obtém os campos de formulário da página
                annotations = page['/Annots']

                # Converte os objetos IndirectObject para objetos PdfDict
                #annotations = annotations.resolve() if annotations else None

                # Converte o ArrayObject para uma lista
                #annotations = annotations.get_object() if annotations else None
                annotations_list = annotations.get_object() if isinstance(annotations, PyPDF2.generic.IndirectObject) else annotations


                for annotation in annotations:
                    # Verifica se é um campo de formulário
                    #if '/T' in annotation and '/V' in annotation:
                    # Verifica se é um campo de formulário
                    if isinstance(annotation, PyPDF2.generic.DictionaryObject) and '/T' in annotation and '/V' in annotation:
                        # Obtém o nome do campo
                        campo_nome = annotation['/T']

                        # Verifica se o campo está na lista de campos a serem preenchidos
                        if campo_nome in campo_valores:
                            # Preenche o valor do campo
                            annotation.update({
                                PyPDF2.generic.NameObject("/V"): PyPDF2.generic.createStringObject(campo_valores[campo_nome])
                            })

            # Adiciona a página ao arquivo de saída
            pdf_writer.add_page(page)

        # Salva o arquivo de saída com os campos preenchidos
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

# Exemplo de uso
#campos_para_preencher = {'(unnamed2)': '(unnamed2)', '(unnamed2_3)': '(unnamed2_3)', '(unnamed0)': '(unnamed0)'}
campos_para_preencher = {
    #'(Caixa de sele#C3#A7#C3#A3o 1_9)': '/Yes',
    'Nome do Usuário': 'oie',
    'Caixa de seleção 1_9': '/Yes',
    'Caixa de seleção 1_10': '/Yes',
    'Caixa de seleção 1_11': '/Yes',
    'Caixa de seleção 1_12': '/Yes',
    'Caixa de seleção 1_13': '/Yes',
    'Caixa de seleção 1_14': '/Yes',
    'Caixa de seleção 1_15': '/Yes',
    'CHAMADO': 'chamado',
    'Campo de data 1': '06/12/2023',
    'unnamed0': 'login',
    'unnamed11': 'colaborador',
    'unnamed2_2': 'telefone',
    'unnamed2': 'email',
    'unnamed2_3': 'localidade',
    'Notebook': '/Yes',
    'D': '/Yes',
    'M': '/Yes',
    'O': '/Yes',
    'unnamed1': 'outro_tipo',
    'Caixa de combinação 2': 'þÿ\x00N\x00E\x00T',
    'unnamed18_2': 'serial_atual',
    'unnamed7': 'ae_atual',
    'unnamed8': 'fabricante_atual',
    'unnamed14': 'modelo_atual',
    'unnamed4': 'processador_atual',
    'unnamed16': 'hd_atual',
    'unnamed5': 'hostname_atual',
    'Caixa de texto 2': 'memoria_atual',
    'unnamed18': 'serial_novo',
    'unnamed7_2': 'ae_novo',
    'unnamed8_2': 'fabricante_novo',
    'unnamed14_2': 'modelo_novo',
    'unnamed4_2': 'processador_novo',
    'unnamed16_2': 'hd_novo',
    'unnamed5_2': 'hostname_novo',
    'unnamed15': 'memoria_novo',
    'past': 'pasta_perfil_pst',
    'sw': 'software',
    'sw_2': 'analista field service',
    'Caixa de seleção 8_2': '/Yes',
    'Caixa de seleção 8_3': '/Yes',
    'Caixa de seleção 4': '/Yes',
    'Caixa de seleção 5': '/Yes',
    'Caixa de seleção 6': '/Yes',
    'Caixa de seleção 7': '/Yes',
    'Caixa de seleção 8': '/Yes',
    'out': 'memoria_frequencia',
    'Caixa de seleção 9': '/Yes',
    'Caixa de seleção 10': '/Yes',
    'Caixa de seleção 11': '/Yes',
    'Caixa de seleção 12': '/Yes',
    'out_4': 'part_number',
    'Caixa de seleção 14': '/Yes',
    'out_2': 'outros_itens_afetados',
    'out_3': 'centro_custo',
    'Caixa de seleção 1': '/Yes',
    'Caixa de seleção 1_2': '/Yes',
    'Caixa de seleção 1_7': '/Yes',
    'Caixa de seleção 1_3': '/Yes',
    'Caixa de seleção 1_4': '/Yes',
    'Caixa de seleção 1_8': '/Yes',
    'Caixa de seleção 1_5': '/Yes',
    'Caixa de seleção 1_16': '/Yes',
    'Caixa de seleção 1_6': '/Yes',
    'Caixa de seleção 2': '/Yes',
    'unnamed13': 'outros_diagnostico',
    'unnamed28': 'descricao_opcional',
    'Caixa de seleção 2_6': '/Yes',
    # Adicione aqui os outros campos e valores conforme necessário
}
preencher_campos_pdf('formulario.pdf', 'formulario_preenchido.pdf', campos_para_preencher)
