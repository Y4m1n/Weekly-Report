(function downloadChatMessage(nd) {
  if(nd < 160)
    setTimeout(function(){
      filtergroupchanged1(nd);
      $(".btn").click();
      downloadChatMessage(++nd);
    }, 3000);
}(154));
