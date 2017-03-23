$(document).ready(function () {
    $('#up').on('click', function (event) {
        event.preventDefault();
        var element = $(this);
        $.ajax({
            url: '/like_questionPost',
            type: 'GET',
            data: { questionPost: element.attr("data")},

            success: function (response) {
                    element.html(''+response);

            }
        })

    })
});