const managerTable = document.getElementById("managerTable");
const managerTableBody = document.getElementById("managerBody");
const reimbursementTable = document.getElementById("reimbursementTable");
const reimbursementTableBody = document.getElementById("reimbursementBody");
const reimbursementTablePending = document.getElementById("reimbursementPendingBody");
const user = sessionStorage.getItem("user");

//WORKS
async function getAllManagerData(){
    let url = "http://127.0.0.1:5000/manager/" + user.toLowerCase();
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateManagerData(body);
        getAllPastReimbursementData();
        getAllPendingReimbursementData();
    }
    else{
        alert("There was a problem trying to get the manager information: apologies!");
    }

}

//WORKS
async function getAllPendingReimbursementData(){
    let managerID = sessionStorage.getItem("managerId");
    let url = "http://127.0.0.1:5000/manager/pending/reimbursement/" + managerID;
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        populatePendingReimbursementData(body);
    }
    else{
        alert("There was a problem trying to get the pending reimbursement information: apologies!");
    }
}
function populatePendingReimbursementData(responseBody){
    for( let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.reimbursement}</td><td>${reimbursement.reasonwhy}</td><td>${reimbursement.acceptance}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        reimbursementTablePending.appendChild(tableRow);
        console.log(reimbursementTablePending);
    }
}
//WORKS
async function getAllPastReimbursementData(){
    let managerID = sessionStorage.getItem("managerId");
    let url = "http://127.0.0.1:5000/past/reimbursements/" + managerID;
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        populatePastReimbursementData(body);
    }
    else{
        alert("There was a problem trying to get the past reimbursement information: apologies!");
    }
}

function populatePastReimbursementData(responseBody){
    for (let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.reimbursement}</td><td>${reimbursement.reasonwhy}</td><td>${reimbursement.acceptance}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        reimbursementTableBody.appendChild(tableRow);
        console.log(reimbursementTableBody);
    }
}

//WORKS
async function updateApproveReimbursementInfo(){
    let reimbursementId = sessionStorage.getItem("reimbursementId");
    console.log(reimbursementId);
    let url = "http://127.0.0.1:5000/reimbursement/approve/" + reimbursementId;
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        populateApproveReimbursementData(body);
    }
    else{
        alert("There was a problem trying to update the pending reimbursement informaton: apologies!");
    }
}

function populateApproveReimbursementData(responseBody){
    for (let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.reimbursementId}</td><td>${reimbursement.reasonwhy}</td><td>${reimbursement.acceptance}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        reimbursementTablePending.appendChild(tableRow);
        console.log(reimbursementTablePending);
    }
}



function populateManagerData(manager){
    let tableRow = document.createElement("tr");
    // tableRow.innerHTML = ''
    tableRow.innerHTML = `<td>${manager.managerId}</td><td>${manager.firstName}</td><td>${manager.lastName}</td><td>${manager.user}</td>`;
    managerTableBody.appendChild(tableRow);
    sessionStorage.setItem("managerId", manager.managerId);
}

getAllManagerData();