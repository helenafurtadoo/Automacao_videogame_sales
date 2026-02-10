import pandas as pd
from pathlib import Path
import time
import pyautogui
# bilbiotecas: pyautogui (para a pausa entre passos)| time (para a pausa maior entre paginas) | pandas (para a base de dados)


BASE = Path(__file__).resolve().parent.parent  # se app.py está em automacao/
csv_path = BASE / "dados" / "data_sales.csv"
sales = pd.read_csv(csv_path)

pyautogui.PAUSE = 3


def main():

    link_sistema = 'https://helenafurtadoo.github.io/Automacao_videogame_sales/'
    # PASSOS PARA A AUTOMAÇÃO:

    # 1° - entrar no sistema
    pyautogui.press('win')
    pyautogui.write('google')
    pyautogui.press('enter')

    # clicar para tela cheia, caso o google abra pequeno
    pyautogui.click(x=1300, y=115)

    # 2°- fazer login no sistema (site)
    pyautogui.write(link_sistema)
    pyautogui.press('enter')
    # PAUSA MAIOR --> usar toda vez que entrar/mudar de pagina web, para evitar erro de internet
    time.sleep(3)

    pyautogui.scroll(-500)
    pyautogui.click(x=870, y=646)
    pyautogui.write('emailDeTeste@gmail.com')
    pyautogui.press('tab')
    pyautogui.write('senhaimaginariasitema')
    pyautogui.press('tab')
    pyautogui.press('enter')

    # PAUSA MAIOR --> (trocando de pagina web)
    time.sleep(3)

    # 3°- abrir base de dados
    sales = pd.read_csv(csv_path)
    base_final = sales.drop(
        columns=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"])
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


if __name__ == "__main__":
    main()
