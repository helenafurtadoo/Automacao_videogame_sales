// Espera o html carregar completamente antes de executar o codigo
document.addEventListener("DOMContentLoaded", function () {

    //botao logar
    const botaoLogar = document.getElementById("btn-logar");


    // verifica se o botao foi encontrado 
    if (botaoLogar) {
        // adiciona um ouvinte para o evento clique
        event.preventDefault(); 
        botaoLogar.addEventListener("click", function () {

            // redireciona para a pagina do formulario
            window.location.href = "../cadastro/formulario.html";
        }
        )
    }
}

)