// Espera o html carregar completamente antes de executar o codigo
document.addEventListener("DOMContentLoaded", function () { //capturar apenas elementos (botao e campos)

    //botao logar
    const botaoLogar = document.getElementById("btn-logar");


    // verifica se o botao foi encontrado 
    if (botaoLogar) {
        // adiciona um ouvinte para o evento clique
        botaoLogar.addEventListener("click", function () {
            event.preventDefault(); // previne submissao do formulario
            const campoEmail = document.getElementById("email").value.trim();
            const campoSenha = document.getElementById("senha").value.trim();

            if (campoEmail === "" || campoSenha === "") {
                alert("Por favor, preencha os campos obrigatórios")
                return;
            }
            // redireciona para a pagina do formulario
            window.location.href = "../cadastro/formulario.html";
        }
        )
    }
}

)