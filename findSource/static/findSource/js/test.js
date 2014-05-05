$(document).ready(function(){
    $('#test').click(function(){
        var articles = document.forms[0].articles;

        var output = [];
        var txt = '';
        var i;
        for (i=0;i<articles.length;i++)
          {
          if (articles[i].checked)
            {
              txt = txt + articles[i].value + ';'
            }
          }

        //alert(txt);

        var token = $("input[name='csrfmiddlewaretoken']").val()
        $.post('/Sourcerous/comcast/result', {
            url: txt,
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
