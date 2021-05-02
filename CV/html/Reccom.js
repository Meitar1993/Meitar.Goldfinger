function copyElementText(id) {
    var text = document.getElementById(id).innerText;
    var elem = document.createElement("textarea");
    document.body.appendChild(elem);
    elem.value = text.replace('Copy Email','');
    elem.select();
    document.execCommand("copy");
    document.body.removeChild(elem);
    alert("Copied the email: " + elem.value);

}
