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

fetch('https://reqres.in/api/users?page=2').then(
    response => response.json()
).then(
    responseobject => createUserList(responseobject.data)
).catch(
    err =>console.log(err)
);

function createUserList(users){
    console.log(users);
    const curr_main = document.querySelector("main");
    for(let user of users){
        const section = document.createElement("section");
        section.innerHTML = `
        <img src="${user.avatar}" alt="profile Picture">
        <div>
           <span>${user.first_name} ${user.last_name} </span>
           <br>
           <a href="mailto:${user.email}">Send Email</a>
        </div>
        `;
        curr_main.appendChild(section);
    }
}
