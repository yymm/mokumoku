$("#banner").after("<div class='about-me'>Click Me</div>")
$(".no-thank-yu > .container").after("<div class='more-info'>More Blog Info</div>")

$(".about-me").click(function(){
  $(".about-me").fadeOut(1000, function() {
    $(".no-thank-yu > .container").slideDown(1500, function(){
        $(".more-info").fadeIn(1000);
    });
    $("#contentinfo .container").fadeIn(1000);
    $("#title-logo").fadeIn(1000);
  });
});
$(".more-info").click(function() {
    $("#extras").fadeIn(1000);
    $(".more-info").fadeOut(1000);
});
window.onload=function() {
}
