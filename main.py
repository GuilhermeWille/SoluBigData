import pandas as pd

data = pd.read_csv(
    'data/exercicios.csv', 
    sep=';',
    engine='python',
    encoding='utf-8'
)

print("=== INFORMACOES DOS DADOS ORIGINAIS ===")
print(data.info())

print("\n=== PRIMEIRAS 10 LINHAS ===")
print(data.head(10))

data_tratado = data.copy()

data_tratado['Calories'] = data_tratado['Calories'].fillna(0)

print("\n=== APOS CORRIGIR CALORIES ===")
print(data_tratado.to_string(index=False))

data_tratado['Date'] = data_tratado['Date'].str.strip("'")

data_tratado['Date'] = data_tratado['Date'].fillna('1900/01/01')

print("\n=== APOS PREENCHER DATAS NULAS ===")
print(data_tratado.to_string(index=False))

data_tratado['Date'] = data_tratado['Date'].replace(
    '1900/01/01', float('nan')
)

data_tratado['Date'] = data_tratado['Date'].replace(
    '20201226', '2020/12/26'
)

data_tratado['Date'] = pd.to_datetime(
    data_tratado['Date'],
    format='%Y/%m/%d'
)

print("\n=== DADOS APOS CONVERSAO DAS DATAS ===")
print(data_tratado.to_string(index=False))

data_tratado = data_tratado.dropna(subset=['Date'])

print("\n=== DATAFRAME FINAL ===")
print(data_tratado.to_string(index=False))

print("\n=== INFORMACOES FINAIS ===")
data_tratado.info()