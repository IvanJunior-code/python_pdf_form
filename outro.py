import pdfrw

def preencher_campos(input_pdf, output_pdf, campos_para_preencher):
    template = pdfrw.PdfReader(input_pdf)

    for page in template.pages:
        if '/Annots' in page:
            annotations = page['/Annots']
            for annotation in annotations:
                if '/T' in annotation and '/V' in annotation:
                    campo_nome = annotation['/T']
                    campo_valor = annotation['/V']

                    if campo_nome in campos_para_preencher:
                        # Modifique o valor do campo
                        annotation.update(pdfrw.PdfDict(V=campos_para_preencher[campo_nome]))

    # Salve o PDF preenchido
    pdfrw.PdfWriter().write(output_pdf, template)

# Exemplo de uso
campos_para_preencher = {
    '(Caixa de sele#C3#A7#C3#A3o 1_9)': '/No',
    '(Caixa de sele#C3#A7#C3#A3o 1_10)': '/Off',
    '(Caixa de sele#C3#A7#C3#A3o 1_11)': '/On',
    '(Caixa de sele#C3#A7#C3#A3o 1_12)': '/Yes',
    '(Caixa de sele#C3#A7#C3#A3o 1_13)': '/Yes',
    '(Caixa de sele#C3#A7#C3#A3o 1_14)': '/Yes',
    '(Caixa de sele#C3#A7#C3#A3o 1_15)': '/Yes',
    '(CHAMADO)': 'VAIIIIIIIII',  # Substitua '/Yes' pelo valor desejado
    '(unnamed2_2)': 'EEEEEEEEE',
    '(Campo de data 1)': '06/12/2023',
    '(unnamed0)': 'login',
    '(unnamed11)': 'colaborador',
    '(unnamed2_2)': 'telefone',
    '(unnamed2)': 'email',
    '(unnamed2_3)': 'localidade',
    '(Notebook)': '/Yes',
    '(D)': '/Y',
    '(M)': '/Y',
    '(O)': '/Y',
    '(unnamed1)': 'outro_tipo',
    '(Caixa de combinação 2)': 'þÿ\x00N\x00E\x00T',
    '(unnamed18_2)': 'serial_atual',
    '(unnamed7)': 'ae_atual',
    '(unnamed8)': 'fabricante_atual',
    '(unnamed14)': 'modelo_atual',
    '(unnamed4)': 'processador_atual',
    '(unnamed16)': 'hd_atual',
    '(unnamed5)': 'hostname_atual',
    '(Caixa de texto 2)': 'memoria_atual',
    '(unnamed18)': 'serial_novo',
    '(unnamed7_2)': 'ae_novo',
    '(unnamed8_2)': 'fabricante_novo',
    '(unnamed14_2)': 'modelo_novo',
    '(unnamed4_2)': 'processador_novo',
    '(unnamed16_2)': 'hd_novo',
    '(unnamed5_2)': 'hostname_novo',
    '(unnamed15)': 'memoria_novo',
    '(past)': 'pasta_perfil_pst',
    '(sw)': 'software',
    '(sw_2)': 'analista field service',
    '(Caixa de seleção 8_2)': '/Yes',
    '(Caixa de seleção 8_3)': '/Yes',
    '(Caixa de seleção 4)': '/Yes',
    '(Caixa de seleção 5)': '/Yes',
    '(Caixa de seleção 6)': '/Yes',
    '(Caixa de seleção 7)': '/Yes',
    '(Caixa de seleção 8)': '/Yes',
    '(out)': 'memoria_frequencia',
    '(Caixa de seleção 9)': '/Yes',
    '(Caixa de seleção 10)': '/Yes',
    '(Caixa de seleção 11)': '/Yes',
    '(Caixa de seleção 12)': '/Yes',
    '(out_4)': 'part_number',
    '(Caixa de seleção 14)': '/Yes',
    '(out_2)': 'outros_itens_afetados',
    '(out_3)': 'centro_custo',
    '(Caixa de seleção 1)': '/Yes',
    '(Caixa de seleção 1_2)': '/Yes',
    '(Caixa de seleção 1_7)': '/Yes',
    '(Caixa de seleção 1_3)': '/Yes',
    '(Caixa de seleção 1_4)': '/Yes',
    '(Caixa de seleção 1_8)': '/Yes',
    '(Caixa de seleção 1_5)': '/Yes',
    '(Caixa de seleção 1_16)': '/Yes',
    '(Caixa de seleção 1_6)': '/Yes',
    '(Caixa de seleção 2)': '/Yes',
    '(unnamed13)': 'outros_diagnostico',
    '(unnamed28)': 'descricao_opcional',
    '(Caixa de sele#C3#A7#C3#A3o 2_6)': ('/Yes')
}

preencher_campos('formulario.pdf', 'formulario_preenchido.pdf', campos_para_preencher)
