// document.getElementById('add_network').onclick = duplicate;
var i = 0;
var original = document.getElementById('network_add');
function duplicate() {
  var clone = original.cloneNode(true); // "deep" clone
  clone.id = "network_add" + ++i; // there can only be one element with an ID
  console.log(original.parentNode)
  original.parentNode.appendChild(clone);
  document.getElementById(clone.id).focus();
}