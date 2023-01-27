window.onload=function () {
  document.onclick=hideDetails;
}

function hideDetails() {
  var details = document.querySelector('details');
  details.open = false;
}
