//Fails
async function LoginManager(){
    let url = "http://127.0.0.1:5000/manager/login"
    const user = document.getElementById("user");
    const passcode = document.getElementById("passcode");

    sessionStorage.setItem("user", user.value);
    sessionStorage.setItem("passcode", passcode.value);
    console.log(user.value);
    console.log(passcode.value);
    managerJSON = JSON.stringify({"user": user.value.toLowerCase(), "passcode": passcode.value});
    console.log(managerJSON);

    let response = await fetch(url, {
        method: "POST",
        headers:{"Content-Type": 'application/json'},
        body:managerJSON}).then(response => {return response.json()});

    if (response.user == user.value.toLowerCase() && response.passcode == passcode.value){
        window.location.href = "../html/manager_page.html";
    }
    else{
        alert("Invalid user or passcode")
        console.log(response.user, response.passcode);
        }

}
//Fail
async function Login(){
    let url = "http://127.0.0.1:5000/employee/login"
    const user = document.getElementById("user");
    const passcode = document.getElementById("passcode");

    sessionStorage.setItem("user", user.value);
    sessionStorage.setItem("passcode", passcode.value);
    console.log(user.value);
    console.log(passcode.value);
    employeeJSON = JSON.stringify({"user": user.value.toLowerCase(), "passcode": passcode.value});
    console.log(employeeJSON);

    let response = await fetch(url, {
        method: "POST",
        headers:{"Content-Type": 'application/json'},
        body:employeeJSON}).then(response => {return response.json()});

    if (response.user == user.value.toLowerCase() && response.passcode == passcode.value){
        window.location.href = "../html/employee_page.html";
    }
    else{
        LoginManager()
        }

}