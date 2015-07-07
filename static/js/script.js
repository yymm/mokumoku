$("#look").hover(
    function () {  // hover
        var num = Math.floor(Math.random()*7)+1;
        var url = "/theme/img/" + num.toString() + ".svg";
        $(this).attr("src", url)
    },
    function () {  // out
        var url = "/theme/img/2.svg";
        $(this).attr("src", url)
    }
);
