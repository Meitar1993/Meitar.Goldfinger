function updateDate(){
    var d = new Date();
    var a = d.getMonth();
    var months = []
    var m = ["January", "February", "March", "April","May","June","July","August","September","October","November","December"]
    document.getElementById("img").innerHTML=m[d.getMonth()] +" "+ d.getFullYear();
        }