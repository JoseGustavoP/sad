$(document).ready(function() {
    $('.star').on('click', function() {
        const rating = $(this).data('rating');
        $('#id_avaliacao').val(rating);  // Atualize o campo de avaliação (não visível)
        $('.star').removeClass('active');  // Limpe todas as estrelas ativas
        $(this).addClass('active');  // Marque a estrela clicada como ativa
        $(this).prevAll('.star').addClass('active');  // Marque todas as estrelas anteriores como ativas
    });
});



// Função para alternar a exibição do menu suspenso
function toggleCustomDropdown() {
    var customDropdownMenu = document.getElementById("customDropdownMenu");
    if (customDropdownMenu.style.display === "none" || customDropdownMenu.style.display === "") {
      customDropdownMenu.style.display = "block";
    } else {
      customDropdownMenu.style.display = "none";
    }
  }
  