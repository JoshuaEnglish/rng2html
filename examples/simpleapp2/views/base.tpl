<!DOCTYPE html>
<html>
<title>{{title or 'No title'}}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="/static/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><style>
body {font-family: "Raleway", sans-serif;
      line-hight: 1.618 em;}
.w3-sidenav a {padding:16px;font-weight:bold}

</style>
<body>

<nav class="w3-sidenav w3-collapse w3-white w3-animate-left w3-card-2" style="z-index:3;width:250px;" id="mySidenav">
  <%
  navstuff=[('/index', 'index', 'Home'),
            ('/hardcoded', 'hardcoded', 'Hard Coded'),
           ]
  active_page = setdefault('active_page', 'index')
  %>
  <a href="javascript:void(0)" onclick="w3_close()" 
  class="w3-text-red w3-hide-large w3-closenav w3-large"><i class="fa fa-remove"></i></a>
  % for href, id, caption in navstuff:
  <a href="{{ tools.get_url(href)}}" class="{{"w3-light-grey" if active_page == id else ""}} w3-medium">{{caption}}</a>
  % end
</nav>

<div class="w3-overlay w3-hide-large w3-animate-opacity" onclick="w3_close()" style="cursor:pointer" id="myOverlay"></div>

<div class="w3-main" style="margin-left:250px;">


<div id="myTop" class="w3-top w3-container w3-padding-16 w3-theme w3-dark-gray w3-text-white w3-large">
  <i class="fa fa-bars w3-opennav w3-hide-large w3-xlarge w3-margin-left w3-margin-right" onclick="w3_open()"></i>
  <span id="myIntro" class="w3-hide">{{'Sample App'}}</span>
</div>

<div class="w3-container w3-padding-32" style="padding-left:32px">
{{!base}}

</div>

<footer class="w3-container w3-theme w3-padding-32 w3-dark-gray w3-text-white" style="padding-left:32px">
  <p>&copy; 2017 Josh English</p>
</footer>
     
</div>

<script>
// Open and close the sidenav on medium and small screens
function w3_open() {
    document.getElementById("mySidenav").style.display = "block";
    document.getElementById("myOverlay").style.display = "block";
}
function w3_close() {
    document.getElementById("mySidenav").style.display = "none";
    document.getElementById("myOverlay").style.display = "none";
}

// Change style of top container on scroll
window.onscroll = function() {myFunction()};
function myFunction() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        document.getElementById("myTop").classList.add("w3-card-4", "w3-animate-opacity");
        document.getElementById("myIntro").classList.add("w3-show-inline-block");
    } else {
        document.getElementById("myIntro").classList.remove("w3-show-inline-block");
        document.getElementById("myTop").classList.remove("w3-card-4", "w3-animate-opacity");
    }
}

// Accordions
function myAccordion(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
        x.previousElementSibling.className += " w3-theme";
    } else { 
        x.className = x.className.replace("w3-show", "");
        x.previousElementSibling.className = 
        x.previousElementSibling.className.replace(" w3-theme", "");
    }
}
</script>
     
</body>
</html> 
