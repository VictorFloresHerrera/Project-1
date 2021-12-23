//Info added to page
const employeeTable = document.getElementById("employeeTable");
const employeeTableBody = document.getElementById("employeeBody");
const reimbursementTable = document.getElementById("reimbursementTable");
const reimbursementTableBody = document.getElementById("reimbursementBody");
const user = sessionStorage.getItem("user");
// Below is Create Employee Reimbursement
const reimbursementId = 0
const employeeId = document.getElementById("employeeIdInput");
const managerId = document.getElementById("managerIdInput");
const requestReimbursement = document.getElementById("requestReimbursementInput");
const reasonwhy = document.getElementById("reasonwhy");
const acceptance = "Pending";
const managerComment = "";

function logout(){
    sessionStorage.clear();
    window.location.href = "../html/login.html"
}
//WORKS
async function employeeCreateReimbursement(){
    let response = await fetch(
        "http://127.0.0.1:5000/reimbursement", {
            method: "POST", headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"reimbursementId":reimbursementId, "employeeId":employeeId.value, "managerId":managerId.value, "reimbursement":requestReimbursement.value, "reasonwhy":reasonwhy.value, "acceptance":acceptance, "managerComment":managerComment})

        }
    )
    if(response.status === 200){
        let body = await response.json();
    }
    else{
        alert("There was a problem requesting.");
    }
}
//Works
async function getAllEmployeeData(){
    let url = "http://127.0.0.1:5000/employee/" + user.toLowerCase();
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateEmployeeData(body);
        getAllReimbursementInfo();
    }
    else{
        alert("problem trying to get the employee ");
    }

}
//WORKS
//this function to grab all the reimbursement data.
async function getAllReimbursementInfo(){
    let employeeID = sessionStorage.getItem("employeeId");
    let url = "http://127.0.0.1:5000/employee/reimbursement/" + employeeID;
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateReimbursementsData(body);
    }
    else{
        alert("problem trying to receive the reimbursement");
    }
}


//function to grab the employee...
function populateEmployeeData(employee){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = ''
    tableRow.innerHTML = `<td>${employee.employeeId}</td><td>${employee.firstName}</td><td>${employee.lastName}</td><td>${employee.user}</td>`;
    employeeTableBody.appendChild(tableRow);
    sessionStorage.setItem("employeeId", employee.employeeId);

}

//function to grab the reimbursement for the employee...
function populateReimbursementsData(responseBody){
    for(let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.managerId}</td><td>${reimbursement.reimbursement}</td><td>${reimbursement.reasonwhy}</td><td>${reimbursement.acceptance}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        reimbursementTableBody.appendChild(tableRow);
        console.log(reimbursementTableBody);
    }
}
getAllEmployeeData();