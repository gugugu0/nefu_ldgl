function submit(action_url) {
    var f = $('<form method="post"></form>');
    var xsrf = $("<input type='hidden' name='csrfmiddlewaretoken' value='DiumdgzQ8uSem6ubxjtwiocVYF3CWp2cnNjGVWwZW03HoW0VeaFttl62fmZLytti' />");
    f.append(xsrf);
    f.prop('action', action_url);
    f.appendTo('body').submit();
}
window.onload = function () {
    $(".confirm-alert").on('click', function (e) {
        if(!confirm('确认要执行这个操作？')) {
            return e.preventDefault();
        }
    });
    $("form.form-confirm").on("submit", function (e) {
        if(!confirm('确认要执行这个操作？')) {
            return e.preventDefault();
        }
    });
    $("div.has-captcha img.captcha").css('cursor', 'pointer').on('click', function() {
        var $form = $(this).parents('.has-captcha');

        // Make the AJAX-call
        $.getJSON("/captcha/refresh/", {}, function(json) {

            $form.find('input[name="captcha_0"]').val(json.key);
            $form.find('img.captcha').attr('src', json.image_url);
        });

        return false;
    });
};