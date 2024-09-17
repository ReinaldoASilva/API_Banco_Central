import pandas as pd
import matplotlib.pyplot as plt
import ssl

def extração_bcb(codigo, data_inicio, data_final):
    import ssl
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json&dataInicial={}&dataFinal={}'.format(codigo, data_inicio,data_final)
    df = pd.read_json(url)
    df.set_index('data', inplace=True)
    df.index = pd.to_datetime(df.index, dayfirst=True)
    return df

selic = pd.DataFrame(extração_bcb(433, '01/01/2010', '01/06/2024')).plot();

inflacao = pd.DataFrame(extração_bcb(10841, '01/01/2010', '01/06/2024')).plot();

indice_confi_consumidor = pd.DataFrame(extração_bcb(4393, '01/01/2010', '01/06/2024')).plot();

dolar = pd.DataFrame(extração_bcb(10813, '01/01/2010', '01/06/2024')).plot();




