// once the document is ready...
$(document).ready(function() {

    // CROSS-SITE REQUEST FORGERY PROTECTION ===========================================================================

    // Use a function from django documentation to create a cookie for CSRF safety
    // https://docs.djangoproject.com/en/dev/ref/csrf/#django.views.decorators.csrf.csrf_exempt
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Create a csrf cookie and store it in a variable
    var csrftoken = getCookie('csrftoken');

    // Define a function for methods that don't require a csrf token
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    // CUSTOM ACTION ==========================================================================================

    // Switch a user's status
    $('.switch_status').click(function(event) {
        this_user = $(this).parent().parent().find("td:first").text();

        // THIS SHOULD BE DONE IN THE SUCCESS FUNCTION
        // switch the status visible in html
        if ($(this).parent().parent().find(".active_status").text() == "True") {
            $(this).parent().parent().find(".active_status").html("False")
        } else {
            $(this).parent().parent().find(".active_status").html("True")
        }

        // Send the request to our deactivate user view (Django)
        $.ajax({
            url: "switch/status/",
            type: "POST",
            dataType: "json",
            data: {
                name_of_user: this_user,
            },
            beforeSend: function(xhr, settings) {
                // CSRF protection
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
        });
    });
})
