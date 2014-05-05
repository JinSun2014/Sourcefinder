$(document).ready(function(){
    $('#test').click(function(){
        var articles = document.forms[0].articles;
        var txt = [];
        var index = 0;
        var i;
        for (i=0;i<articles.length;i++)
          {
          if (articles[i].checked)
            {
              txt = txt + articles[index].value + " ";
              index += 1;
            }
          }

        alert(txt);

        var token = $("input[name='csrfmiddlewaretoken']").val()
        $.post('/Sourcerous/comcast/result', {
            url: "http://www.cnbc.com/id/101614448;http://www.prnewswire.com/news-releases/comcast-announces-new-600-seat-customer-support-center-set-to-open-this-summer-in-hudson-nh-257951051.html",
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
