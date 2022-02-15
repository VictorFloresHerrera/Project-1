async function LoginManager(){
    let url = "http://127.0.0.1:5000/manager/login"
    const userid = document.getElementById("userid");
    const passcode = document.getElementById("passcode");

    sessionStorage.setItem("userid", userid.value);
    sessionStorage.setItem("passcode", passcode.value);
    console.log(userid.value);
    console.log(passcode.value);
    managerJSON = JSON.stringify({"userid": userid.value.toLowerCase(), "passcode": passcode.value});
    console.log(managerJSON);

    let response = await fetch(url, {
        method: "POST",
        headers:{"Content-Type": 'application/json'},
        body:managerJSON}).then(response => {return response.json()});

    if (response.userid == userid.value.toLowerCase() && response.passcode == passcode.value){
        window.location.href = "../html/manager_page.html";
    }
    else{
        alert("Invalid userid or passcode")
        console.log(response.userid, response.passcode);
        }

}

async function Login(){
    let url = "http://127.0.0.1:5000/employee/login"
    const userid = document.getElementById("userid");
    const passcode = document.getElementById("passcode");

    sessionStorage.setItem("userid", userid.value);
    sessionStorage.setItem("passcode", passcode.value);
    console.log(userid.value);
    console.log(passcode.value);
    employeeJSON = JSON.stringify({"userid": userid.value.toLowerCase(), "passcode": passcode.value});
    console.log(employeeJSON);

    let response = await fetch(url, {
        method: "POST",
        headers:{"Content-Type": 'application/json'},
        body:employeeJSON}).then(response => {return response.json()});

    if (response.userid == userid.value.toLowerCase() && response.passcode == passcode.value){
        window.location.href = "../html/employee_page.html";
    }
    else{
        LoginManager()
        }

}