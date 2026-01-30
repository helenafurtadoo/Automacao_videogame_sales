// criando as variaveis que pegam os elementos do DOM
const formJogos = document.getElementById("formJogos"); // formulario
const corpoTabela = document.getElementById("corpoTabela"); // corpo da tabela 
const limparTabelaBtn = document.getElementById("limparTabela"); // botao de limpar tabela

// funcao para adicionar jogo à tabela quando o formulario é enviado 
formJogos.addEventListener('submit', function (event) {
    event.preventDefault(); // impede o envio padrao (recarregar a pagina)

    // coletar valores dos campos do formulário
    const ranking = document.getElementById('ranking').value;
    const nome = document.getElementById('nome').value;
    const plataforma = document.getElementById('plataforma').value;
    const ano = document.getElementById('ano').value;
    const genero = document.getElementById('genero').value;
    const editora = document.getElementById('editora').value;
    const vendaTotal = document.getElementById('vendaTotal').value;

    // criar uma nova linha na tabela com os dados coletados do formulario
    const novaLinha = document.createElement('tr'); //cria um elemento <tr> (uma linha)
    novaLinha.innerHTML = `
        <td>${ranking}</td>
        <td>${nome}</td>
        <td>${plataforma}</td>
        <td>${ano}</td>
        <td>${genero}</td>
        <td>${editora}</td>
        <td>${vendaTotal}</td>
 `; // preenche a linha com celulas <td> contendo os vlaores adicionados

    //adicionar a nova linha ao CORPO DA TABELA
    corpoTabela.appendChild(novaLinha);

    // limpar o formulario para permitir novos cadastros
    formJogos.reset();

});

// evento para limpar a tabela quando apertar o botao "limpar"
limparTabelaBtn.addEventListener('click', function(event) {
    event.preventDefault(); // evita qlqr comportamento padrao (como submit)
    corpoTabela.innerHTML= ''; // deixa a tabela vazia
});
