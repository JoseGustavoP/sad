$(document).ready(function() {
    // Função para carregar mais comentários
    function carregarComentarios(url) {
        $.ajax({
            url: url,
            type: 'GET',
            success: function(data) {
                $('#comentarios').html(data);
            }
        });
    }

    // Lidar com a navegação entre as páginas de comentários
    $('#comentarios .pagination a').click(function(e) {
        e.preventDefault();
        var url = $(this).attr('href');
        carregarComentarios(url);
    });
});