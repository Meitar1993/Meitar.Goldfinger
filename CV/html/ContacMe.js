function Form(EmailAddress,Name,PhoneNumber,Message){
    if(Check(EmailAddress) || Check(Name) || Check(Message)){
        alert("Please fill all");
    }
    else{
        alert("Thank You!");
        location.href='../html/cv.html';
    }
}

function Check(str) {
    return (!str || str.length === 0 );
}