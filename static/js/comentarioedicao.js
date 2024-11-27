// Adiciona um evento de clique aos botões de edição
function editar_comentario_js(commentId){
        $.ajax({
            type: "GET",
            url: `/editar_comentario_js/${commentId}/`,
            success: function (data) {
                $('#edicaoComentario .modal-body').first().html(data);
                console.log(data)
                $('#edicaoComentario').modal('show');
            },
            error: function () {
                alert("Falha na requisição");
            }
        });  
}

function toggleCustomDropdowncomentarios(comentarioID) {
    // Lógica para alternar a visibilidade do dropdown do comentário específico
    const dropdown = document.getElementById(`customDropdownMenu-${comentarioID}`);

    // Verifica se o dropdown está visível e altera seu estado
    if (dropdown.style.display === 'none' || dropdown.style.display === '') {
        dropdown.style.display = 'block'; // ou outra propriedade para exibir
    } else {
        dropdown.style.display = 'none'; // ou outra propriedade para ocultar
    }
}

// Fechar dropdowns ao clicar fora
document.addEventListener('click', function(event) {
    const dropdowns = document.querySelectorAll('.custom-dropdown-menu');
    if (!event.target.matches('.custom-dropdown-toggle')) {
        dropdowns.forEach(dropdown => {
            if (dropdown.style.display !== 'none') {
                dropdown.style.display = 'none';
            }
        });
    }
});



// Script para abrir o modal de confirmação ao clicar no botão de exclusão
$('.btn-excluir').on('click', function (e) {
    e.preventDefault();
    var comentarioID = $(this).data('comentario-id');
    
    // Ao clicar em "Excluir", definimos o ID do comentário a ser excluído
    $('#confirmacaoExclusao').modal('show').find('.btn-danger').on('click', function() {
        var csrftoken = getCookie('csrftoken');

        fetch('/excluir_comentario/' + comentarioID + '/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            }
        })
        .then(response => {
            if (response.ok) {
                location.reload(); // Recarrega a página após a exclusão bem-sucedida
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    });
});

$(document).ready(function () {
    // Fecha o modal ao clicar no botão "Cancelar" ou no botão "X"
    $('#confirmacaoExclusao button[data-dismiss="modal"]').on('click', function () {
        $('#confirmacaoExclusao').modal('hide');
    });
});

// Função para obter o token CSRF do cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


