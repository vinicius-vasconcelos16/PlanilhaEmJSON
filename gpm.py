from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import json
import pandas as pd


data = """
[
	DICT
]
"""

data_json = json.loads(data)

success = True
datafinal = []
for dt in data_json:
    dados = {}
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://localizeip.com.br/")
    xpath_arc = '//*[@id="baixo-mapa"]/form/input'
    input = driver.find_element('xpath', xpath_arc)
    input.clear()
    input.send_keys(dt["cod_ip_hsl"])

    xpath_btn = '//*[@id="baixo-mapa"]/form/button'
    btn = driver.find_element('xpath', xpath_btn).click()

#     dados['cod_his_log_hsl'] = dt["cod_his_log_hsl"]
#     dados['cod_stat_hsl'] = dt["cod_stat_hsl"]
#     dados['cod_imei_hsl'] = dt["cod_imei_hsl"]
#     dados['cod_placa_hsl'] = dt["cod_placa_hsl"]
#     dados['cod_ip_hsl'] = dt["cod_ip_hsl"]
#     dados['obs_hsl'] = dt["obs_hsl"]
#     dados['cod_versao_hsl'] = dt["cod_versao_hsl"]
#     dados['usr_ins_hsl'] = dt["usr_ins_hsl"]
#     dados['dta_ins_hsl'] = dt["dta_ins_hsl"]

    pais = '//*[@id="left"]/div[2]'
    pais1 = driver.find_element('xpath', pais).text
    dados['pais'] = (pais1).split(': ')[1]

    estado = '//*[@id="left"]/div[3]'
    estado1 = driver.find_element('xpath', estado).text
    dados['estado'] = (estado1).split(': ')[1]

    cidade = '//*[@id="left"]/div[4]'
    cidade1 = driver.find_element('xpath', cidade).text
    dados['cidade'] = (cidade1).split(': ')[1]

    lat = '//*[@id="right"]/div[3]'
    lat1 = driver.find_element('xpath', lat).text
    dados['lat'] = (lat1).split(': ')[1]

    long = '//*[@id="right"]/div[4]'
    long1 = driver.find_element('xpath', long).text
    dados['long'] = (long1).split(': ')[1]
    datafinal.append(dados)
    time.sleep(1)
driver.quit()
df = pd.DataFrame(datafinal)
nova_planilha = pd.ExcelWriter('DadosIP.xlsx', engine='xlsxwriter')
df.to_excel(nova_planilha, sheet_name='DadosIP', index=False)
nova_planilha.close()
