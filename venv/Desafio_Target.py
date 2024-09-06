#1 FUNÇÃO SOMA

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(f"O valor da variável SOMA é: {SOMA}")

#2 FIBONACCI

def fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

# Número a ser verificado
numero = int(input("Informe um número: "))

# Verificação
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")


#3 FATURAMENTO DIARIO

import json

# Dados de faturamento diário
faturamento_diario = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]

# Filtra apenas os dias com faturamento maior que 0
faturamento_valido = [dia["valor"] for dia in faturamento_diario if dia["valor"] > 0]

# Menor faturamento
menor_faturamento = min(faturamento_valido)

# Maior faturamento
maior_faturamento = max(faturamento_valido)

# Média mensal
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Dias com faturamento acima da média
dias_acima_da_media = len([dia for dia in faturamento_valido if dia > media_mensal])

# Exibe os resultados
print(f"Menor faturamento: {menor_faturamento:.2f}")
print(f"Maior faturamento: {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")


#4 PERCENTUAL DE FATURAMENTO POR ESTADO

import xml.etree.ElementTree as ET

# Carregar os dados do XML
xml_data = '''<root>
<row>
  <dia>1</dia>
  <valor>31490.7866</valor>
</row>
<row>
  <dia>2</dia>
  <valor>37277.9400</valor>
</row>
<row>
  <dia>3</dia>
  <valor>37708.4303</valor>
</row>
<row>
  <dia>4</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>5</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>6</dia>
  <valor>17934.2269</valor>
</row>
<row>
  <dia>7</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>8</dia>
  <valor>6965.1262</valor>
</row>
<row>
  <dia>9</dia>
  <valor>24390.9374</valor>
</row>
<row>
  <dia>10</dia>
  <valor>14279.6481</valor>
</row>
<row>
  <dia>11</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>12</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>13</dia>
  <valor>39807.6622</valor>
</row>
<row>
  <dia>14</dia>
  <valor>27261.6304</valor>
</row>
<row>
  <dia>15</dia>
  <valor>39775.6434</valor>
</row>
<row>
  <dia>16</dia>
  <valor>29797.6232</valor>
</row>
<row>
  <dia>17</dia>
  <valor>17216.5017</valor>
</row>
<row>
  <dia>18</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>19</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>20</dia>
  <valor>12974.2000</valor>
</row>
<row>
  <dia>21</dia>
  <valor>28490.9861</valor>
</row>
<row>
  <dia>22</dia>
  <valor>8748.0937</valor>
</row>
<row>
  <dia>23</dia>
  <valor>8889.0023</valor>
</row>
<row>
  <dia>24</dia>
  <valor>17767.5583</valor>
</row>
<row>
  <dia>25</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>26</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>27</dia>
  <valor>3071.3283</valor>
</row>
<row>
  <dia>28</dia>
  <valor>48275.2994</valor>
</row>
<row>
  <dia>29</dia>
  <valor>10299.6761</valor>
</row>
<row>
  <dia>30</dia>
  <valor>39874.1073</valor>
</row>
</root>'''

# Parse do XML
root = ET.fromstring(xml_data)

# Extrair valores de faturamento
faturamento_diario = [float(row.find('valor').text) for row in root.findall('row') if float(row.find('valor').text) > 0]

# Menor e maior faturamento
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

# Média mensal
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Dias com faturamento acima da média
dias_acima_da_media = len([valor for valor in faturamento_diario if valor > media_mensal])

# Exibe os resultados
print(f"Menor faturamento: {menor_faturamento:.2f}")
print(f"Maior faturamento: {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

#5 INVERSÃO STRING

def inverter_string(texto):
    invertida = ''
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

# String a ser invertida
texto = input("Informe uma string: ")
print("String invertida:", inverter_string(texto))
