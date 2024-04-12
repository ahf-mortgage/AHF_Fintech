$(document).ready(function() {
    $('#id_password').after('<span class="password-toggle">Show</span>');
    $('.password-toggle').click(function() {
        var passwordField = $('#id_password');
        var passwordToggle = $(this);
        var fieldType = passwordField.attr('type');

        if (fieldType === 'password') {
            passwordField.attr('type', 'text');
            passwordToggle.text('Hide');
        } else {
            passwordField.attr('type', 'password');
            passwordToggle.text('Show');
        }
    });


    $('#id_password2').after('<span class="password-toggle">Show</span>');
    $('.password-toggle').click(function() {
        var passwordField = $('#id_password2');
        var passwordToggle = $(this);
        var fieldType = passwordField.attr('type');

        if (fieldType === 'password') {
            passwordField.attr('type', 'text');
            passwordToggle.text('Hide');
        } else {
            passwordField.attr('type', 'password');
            passwordToggle.text('Show');
        }
    });
});