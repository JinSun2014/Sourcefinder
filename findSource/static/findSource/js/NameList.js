$(document).ready(function(){
  $(function(){
    var urlsList = JSON.parse($.cookie("URLsInfo"));
    $.removeCookie("URLsList");
    var urlL = urlsList.urls.split(';');
    urlL.pop();
    var original_source = urlsList.original_sources.split(';');
    original_source.pop();    


    (function myloop(i){
      setTimeout(function (){
        $.post('/Sourcerous/getInfo', {
          url: urlL[i],
          osource:original_source[i]
        }, function(response){
          if (response.success){
            var end ='<div id='+'bottom'+'></div>';              
            $('#results').append(end); 
            if (response['people']){

              var append_content = '';              
              // append_content +='<dl class='+'dl-horizontal'+'>'
              // +'<dt>Article Title</dt>'
              // +'<dd> '            
              // + '<a href='+response['url'] + '>'+response['title']+'</a>'
              // +'</dd>'
              // +'</dl>'
              // +'<dl class='+'dl-horizontal'+'>'
              // +'<dt>Author Name</dt>'
              // +'<dd> '            
              // + response['author']
              // +'</dd>'            
              // +'</dl>';

              append_content +='<dl class='+'dl-horizontal'+'>'
              +'<dt>People Info</dt>'
              +'<dd>';
                           
              $.each(response['people'] , function(key, value) {
                append_content += '<div class ='+'business'+'>'; 

                if (response['people'][key]['quotation'].length<10){
                  append_content += '<br>'; 
                }  

                append_content += '<h4 id=\'peopleName\' onclick="Name(\'' + key + '\')">'+key+'</h4>'; 
                append_content += '<p><h5><b>Company: </b>'+response['people'][key]['company'] +'</h5></p>';
                append_content += '<p><h5><b>Job Title: </b>'+response['people'][key]['job_title'] +'</h5></p>';
                append_content += '<p><h5><b>LinkedIn: </b><a href='+response['people'][key]['linkedInLink']+'>'+'Click Me'+'</a></h5></p>';
                append_content += '<p><h6><b>Quotation: </b>'+response['people'][key]['quotation'] +'</h6></p>';
                append_content +='</div><br>';                 
              });  
 
              append_content +='</dd>'
              +'</dl>';             
              append_content +='<dl class='+'dl-horizontal'+'>'
              +'<dt>Article Title</dt>'
              +'<dd> '            
              + '<a href='+response['url'] + '>'+response['title']+'</a>'
              +'</dd>'
              +'</dl>'
              +'<dl class='+'dl-horizontal'+'>'
              +'<dt>Author Name</dt>'
              +'<dd> '            
              + response['author']
              +'</dd>'            
              +'</dl>'
              +'<dl class='+'dl-horizontal'+'>'
              +'<dt>Source</dt>'
              +'<dd> '            
              + response['original_source']
              +'</dd>'            
              +'</dl>'
              +'<br>';  

              $('#results').append(append_content);  
                                        
            }           

          } else {
            alert("fail");
            var fail = '<dl class='+'dl-horizontal'+'>'
            +'<dt>Source Info</dt>'
            +'<dd>No source found</dd>'
            +'</dl>';  
            $('#results').append(fail);  
          }

        })
        if (--i) myloop(i);
      }, 5)
    })(12);

  });


});

function Name(key){
  SendAjax(key);
  $("#preLoaderDiv").show();
  $("#content").hide();

}

function SendAjax(input){
  current_url = window.location.pathname;
  var token = $("input[name='csrfmiddlewaretoken']").val()
  $.removeCookie("URLsInfo", {path: '/'});
  $.post('/Sourcerous/' + input + '/urls', {
    csrfmiddlewaretoken: token
  }, function(response){
    if (response.success){
      $.cookie("URLsInfo", JSON.stringify(response));
      var res= $.cookie("URLsInfo");
      /*var resb = JSON.parse(res);
      console.log(resb);
      $.removeCookie("URLsInfo");*/
      window.location.href = '/Sourcerous/'  + input + '/result';
    }
    else{
      alert('fail');
    }
  });
}
