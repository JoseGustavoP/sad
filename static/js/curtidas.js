$(document).ready(function () {
    $(".like-button, .dislike-button").on("click", function () {
        const commentId = $(this).data("comment-id");
        const liked = $(this).data("liked");
        const action = liked ? "dislike" : "like";
        const button = $(this);
        const otherButton = liked ? button.siblings(".like-button") : button.siblings(".dislike-button");

        // Obter o token CSRF do cookie de sessão
        const csrftoken = getCookie('csrftoken');

        $.ajax({
            type: "POST",
            url: `/like-comment/${commentId}/`,
            data: {
                action: action
            },
            headers: {
                "X-CSRFToken": csrftoken
            },
            success: function (data) {
                if (action === "like") {
                    button.html("<img src='/static/img/descurtir.png' alt='' id='curtircoracao'>");
                } else {
                    button.html("<img src='/static/img/curtir.png' alt='' id='curtircoracao'>");
                }
                // Update the like count
                const likesCount = data.num_likes;
                $(`#likes-count-${commentId}`).text(likesCount);

                // Toggle the liked state
                button.data("liked", !liked);
            },
            error: function () {
                console.log("Erro ao curtir/descurtir o comentário.");
            }
        });
    });
});

// Função para obter o token CSRF do cookie de sessão
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
