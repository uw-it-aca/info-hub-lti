$(function(){

  // handle collapse click text toggling for links that have 'lti-more' class
  $('a.lti-more').click(function(){
    $(this).text(function(i,old){
        return old=='show resources' ? 'hide resources' : 'show resources';
    });
  });
  
});