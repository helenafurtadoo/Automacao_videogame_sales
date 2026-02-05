import pandas
import pandas as pd
from pathlib import Path

# procurando o caminho dos dados
# base_dir = Path(__file__).parent
# csv_path = base_dir.parent / "dados" / "data_sales.csv"


# excluindo as colunas irrelevantes, para deixar o codigo mais limpo
# sales = sales.drop(columns=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"])

# salvar mudanças no arquivo original (sobrescreve)
# sales.to_csv("dados/data_sales.csv", index=False)

# mostrando a tabela depois das mudancas
# print(sales.info)

# bilbiotecas a usar: pyautogui (para a pausa entre passos)| time (para a pausa maior entre paginas) | pandas (para a base de dados)
import time
import pyautogui
pyautogui.PAUSE = 2

link_sistema = 'https://helenafurtadoo.github.io/Automacao_videogame_sales/'
# PASSOS PARA A AUTOMAÇÃO:

# 1°- entrar no sistema (site)
# apertar tecla Windows
pyautogui.press('win')

# pesquisar o navegador
pyautogui.write('google')

# apertar tecla enter
pyautogui.press('enter')


# clicar para tela cheia, caso o google abra pequeno
pyautogui.click(x=1300, y=115)

# 2°- fazer login no sistema (site)
# pesquisar o link do siste (https://helenafurtadoo.github.io/Automacao_videogame_sales/)  --> criar variavel para o link
pyautogui.write(link_sistema)
# apertar tecla enter
pyautogui.press('enter')

# PAUSA MAIOR --> usar toda vez que entrar/mudar de pagina web, para evitar erro de internet
# time.sleep(segundos)
time.sleep(3)
# scroll a tela um pouco para baixo
pyautogui.scroll(-500)
# clicar no campo email (+ achar as coordenadas do campo --> time.sleep(5) | print(pyautogui.position())  )
pyautogui.click(x=870, y=646)

# digitar o email de login
pyautogui.write('emailDeTeste@gmail.com')

# apertar tecla Tab
pyautogui.press('tab')

# digitar a senha de login
pyautogui.write('senhaimaginariasitema')

# apertar a tecla Tab (para passar para o botao "logar")
pyautogui.press('tab')

# apertar a tecla enter (para entrar)
pyautogui.press('enter')

# PAUSA MAIOR --> (trocando de pagina web)
time.sleep(3)

# 3°- abrir base de dadosailDeTeste@gmail.com
sales = pd.read_csv("dados/data_sales.csv")

# excluindo as colunas irrelevantes, para deixar o codigo mais limpo
base_final = sales.drop(columns=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"])

# scroll a tela para baixosenhaimaginariasitema 
pyautogui.scroll(-500)
# 4°- cadastrar produtos
for linha in base_final.index:
    # clicar no campo RANKING DE VENDAS (pegar a coordenada)
    pyautogui.click(x=884, y=246)

    # escrever o numero do RANKING
    ranking = str(base_final.loc[linha, "Rank"])
    pyautogui.write(ranking)

    # proximo campo ('tab')
    pyautogui.press('tab')

    # escrever o NOME DO JOGO
    nome = str(base_final.loc[linha, "Name"])
    pyautogui.write(nome)
    # proximo campo
    pyautogui.press('tab')

    # escrever a PLATAFORMA DE LANÇAMENTO
    plataforma = str(base_final.loc[linha, "Platform"])
    pyautogui.write(plataforma)

    # proximo campo
    pyautogui.press('tab')

    # escrever o ANO DE LANÇAMENTO
    ano_lancamento = str(base_final.loc[linha, "Year"])
    pyautogui.write(ano_lancamento)



    # proximo campo
    pyautogui.press('tab')

    # escrever o GENERO DO JOGO
    genero = str(base_final.loc[linha, "Genre"])
    pyautogui.write(genero)


    # proximo campo
    pyautogui.press('tab')

    # escrever a EDITORA DE PUBLICACAO
    editora = str(base_final.loc[linha, "Publisher"])
    pyautogui.write(editora)


    # proximo campo
    pyautogui.press('tab')

    # escrever o TOTAL DE VENDAS
    total_vendas = str(base_final.loc[linha, "Global_Sales"])
    pyautogui.write(total_vendas)


    # proximo campo ('tab' -> botao enviar)
    pyautogui.press('tab')
    pyautogui.press('enter')

    

    # 5°- repetir o passo 4 ate acabar a base de dados
