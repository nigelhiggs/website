window.onscroll = function() {scroll_Func()};

var header = document.getElementById("myHeader");
var sticky = header.offsetTop;

function scroll_Func() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

