
document.getElementById("mySidenav").style.width = "0";

function menuOpen() {
  if (document.getElementById("mySidenav").style.width == "180px") {
    document.getElementById("mySidenav").style.width = "0";
  } else {
    document.getElementById("mySidenav").style.width = "180px";
  }
}
