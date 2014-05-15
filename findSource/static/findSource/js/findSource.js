$("#search").click(function (){
    var input = $('#user-input').val();
    if (input){
        current_url = window.location.pathname;
        window.location.href = current_url  + input + '/result';
    }
});

$('#user-input').keypress(function(e) {
    if(e.which == 13) {
        var input = $('#user-input').val();
        if (input){
            current_url = window.location.pathname;
            window.location.href = current_url + input + '/result';
        }
    }
});
