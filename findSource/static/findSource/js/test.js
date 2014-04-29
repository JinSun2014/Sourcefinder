$(document).ready(function(){
    $('#test').click(function(){
        var token = $("input[name='csrfmiddlewaretoken']").val()
        $.post('/Sourcerous/comcast/result', {
            url: "http://www.cnbc.com/id/101614448",
            csrfmiddlewaretoken: token
        }, function(data){
            if (data.success){
                //alert("success");
                window.location.href = "/Sourcerous/comcast/result"
            }
            else{
                alert('fail');
            }
        });
    });
});
