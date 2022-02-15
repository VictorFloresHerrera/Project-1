//##### this creates the element ids that will be used through employee table ########################################

const currentemployee = document.getElementById("currentemployee");
const currentEmployeeBody = document.getElementById("employeeBody");
const currentReimbursement = document.getElementById("currentReimbursement");
const currentReimbursementBody = document.getElementById("currentReimbursementBody");
const userid = sessionStorage.getItem("userid");

//##### this adds the reimbursement ########################################

const reimbursementId = 0
const employeeId = document.getElementById("employeeIdInput");
const managerId = document.getElementById("managerIdInput");
const requestReimbursement = document.getElementById("requestReimbursementInput");
const reasonwhy = document.getElementById("reasonwhy");
const acceptance = "Pending";
const managerComment = "";

//##### this logout will send the user back to the sign in page ########################################

function logout(){
    sessionStorage.clear();
    window.location.href = "../html/login.html"
}

//##### we will be able to create our reimbursement here ########################################

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
        alert("Error Attempting to request reimbursement form.");
    }
}

//##### this will let us to obtain the employee info by userid ########################################

async function getAllEmployeeData(){
    let url = "http://127.0.0.1:5000/employee/" + userid.toLowerCase();
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateEmployeeData(body);
        getAllReimbursementInfo();
    }
    else{
        alert("Error attempting to get employee information.");
    }

}

//##### this will allow us to grab the reimbursement by employeeID ########################################

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
        alert("Error attempting to receive the reimbursement information.");
    }
}

//##### we will grab and add the employee ########################################

function populateEmployeeData(employee){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = ''
    tableRow.innerHTML = `<td>${employee.employeeId}</td><td>${employee.firstName}</td><td>${employee.lastName}</td><td>${employee.userid}</td>`;
    currentEmployeeBody.appendChild(tableRow);
    sessionStorage.setItem("employeeId", employee.employeeId);

}
//##### we will grab and add reimbursement for the employee ########################################

function populateReimbursementsData(responseBody){
    for(let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.managerId}</td><td>${reimbursement.reimbursement}</td><td>${reimbursement.reasonwhy}</td><td>${reimbursement.acceptance}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        currentReimbursementBody.appendChild(tableRow);
        console.log(currentReimbursementBody);
    }
}

//##### add data to the table ########################################
getAllEmployeeData();