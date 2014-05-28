$(document).ready(function(){
  $(function(){
    var urlsList = JSON.parse($.cookie("URLsInfo"));
    $.removeCookie("URLsList");
    var url = urlsList.urls.split(';');
    url.pop()

    /*var delay = (function(){
      var timer = 0;
      return function(callback, ms){
        clearTimeout(timer);
        timer = setTimeout(callback, ms);
      };
    })();*/
    for (var i = 0; i != 12; i++){
      setTimeout(function(){
        $.post('/Sourcerous/getInfo', {
          url: url[i]
        }, function(response){
          if (response.success){
            var append_content = '<p>'
            + response['title'] + '<br>'
            + response['url'] + '<br>'
            + response['author'] + '<br>';

            append_content += '</p>';
            $('#results').append(append_content);
          } else {
            alert("fail");
          }
        });
      }, 10000 * i);
    }

  });
});



