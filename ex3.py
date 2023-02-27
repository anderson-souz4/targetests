import json

with open('dados.json') as file:
    dados = json.load(file)

# Filtrando os dados para remover os dias sem faturamento
dados_faturamento = [dia['valor'] for dia in dados if dia['valor'] != 0]

# Calculando as informações requeridas
menor_faturamento = min(dados_faturamento)
maior_faturamento = max(dados_faturamento)
media_faturamento = sum(dados_faturamento) / len(dados_faturamento)
dias_acima_media = len([dia for dia in dados_faturamento if dia > media_faturamento])

# Exibindo os resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
