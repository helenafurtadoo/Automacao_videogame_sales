import pandas as pd
from pathlib import Path

# procurando o caminho dos dados
base_dir = Path(__file__).parent
csv_path = base_dir.parent / "dados" / "data_sales.csv"

sales = pd.read_csv(csv_path)

# excluindo as colunas irrelevantes, para deixar o codigo mais limpo
sales = sales.drop(columns=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"])

# salvar mudanças no arquivo original (sobrescreve)
sales.to_csv("data_sales.csv", index=False)

# mostrando a tabela depois das mudancas
print(sales.info)

