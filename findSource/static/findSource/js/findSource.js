$("#search").click(function (){
    var input = $('#user-input').val();
    if (input){
        current_url = window.location.pathname;
        window.location.href = current_url  + input + '/result';
        /*sendAjax(input);
        $("#preLoaderDiv").show();     
        $("#content").hide();*/
    }
});

$('#user-input').keypress(function(e) {
    if(e.which == 13) {
        var input = $('#user-input').val();
        if (input){
          current_url = window.location.pathname;
          window.location.href = current_url  + input + '/result';
          /*sendAjax(input);
          $("#preLoaderDiv").show();     
          $("#content").hide();*/
        }
    }
});

function sendAjax(input){
  current_url = window.location.pathname;
  var token = $("input[name='csrfmiddlewaretoken']").val()
  $.removeCookie("URLsInfo", {path: '/'});
  $.post(current_url + input + '/urls', {
    csrfmiddlewaretoken: token
  }, function(response){
    if (response.success){
      $.cookie("URLsInfo", JSON.stringify(response));
      var res= $.cookie("URLsInfo");
      /*var resb = JSON.parse(res);
      console.log(resb);
      $.removeCookie("URLsInfo");*/
      window.location.href = current_url  + input + '/result';
    }
    else{
      alert('fail');
    }
  });
}


function checkLoad()
{
   if(document.getElementById("bottom"))
   {
    document.getElementById("preLoaderDiv").style.visibility = "hidden";
   }
}

