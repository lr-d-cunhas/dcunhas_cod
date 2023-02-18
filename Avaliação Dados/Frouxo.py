import MaquinaSuporte as ms
from datetime import datetime
import pandas as pd

def AmostraDinamica(periodo: int) -> tuple:  
    """Cria data inicio e fim de um range x"""
    lista_anos: list = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
                  2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

    lista_meses: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    dia_hoje = datetime.today().strftime('%d')

    lista_data_start = []
    lista_data_end = []

    ano_limite: int = lista_anos[-1] - periodo
    mes_limite = datetime.today().strftime('%m')
    for ano in lista_anos:
        for mes in lista_meses:

            data_start = str(ano) + '-' + str(mes) + '-' +str(dia_hoje)
            if ano > ano_limite:
                pass

            else:
                if ano == ano_limite:
                    if mes > int(mes_limite):
                        pass
                    else:
                        end_ano = ano + periodo
                        data_end = str(end_ano) + '-' + str(mes) + '-' + str(dia_hoje)
                        lista_data_start.append(data_start)
                        lista_data_end.append(data_end)
                else:
                    end_ano = ano + periodo
                    data_end = str(end_ano) + '-' + str(mes) + '-' +str(dia_hoje)
                    lista_data_start.append(data_start)
                    lista_data_end.append(data_end)

    return (lista_data_start, lista_data_end)

def FolgadoTeste(ativo):
    """Varia o periodo. Avaliar se variável muda o resultado em diferentes periodos,
    se mudar então não é uma bão variável"""
    
    amostra_dinamica = AmostraDinamica(periodo=10)
    ad_start = amostra_dinamica[0]
    ad_end = amostra_dinamica[1]

    lista_indice, lista_ac_teste, lista_ac_treino, lista_perc_posi, lista_perc_posi_teste = [], [], [], [], []

    for ind in range(len(ad_start)):
        print(ind)
        modelo = ms.CaixaPreta(ativo=ativo,
                                inicio_amostra=ad_start[ind], fim_amostra=ad_end[ind])
        
        ano_indice_start = str(ad_start[ind][:4])
        mes_indice_start = str(ad_start[ind][5:7]).replace('-', '')
        
        ano_indice_end = str(ad_end[ind][:4])
        mes_indice_end = str(ad_end[ind][5:7]).replace('-', '')

        indice = ano_indice_start + '-' + mes_indice_start + '_' + ano_indice_end + '-' + mes_indice_end
        
        lista_indice.append(indice)
        lista_ac_teste.append(modelo[0])
        lista_ac_treino.append(modelo[1])
        lista_perc_posi.append(modelo[2])
        lista_perc_posi_teste.append(modelo[3])
    
    tabela1 = pd.DataFrame(data=[lista_indice, lista_ac_teste, lista_ac_treino, lista_perc_posi, lista_perc_posi_teste]
                           ).T.rename(columns={0: 'indice', 1: 'ac_teste', 2: 'ac_treino', 3: 'perc_posi', 4: 'perc_posi_teste'})
    
    tabela1.to_csv('tabela1.csv')
    
FolgadoTeste(ativo='GOAU4.SA')

