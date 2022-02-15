
//##### Elements IDs are made here ########################################

const currentManager = document.getElementById("currentManager");
const currentManagerBody = document.getElementById("managerBody");
const currentReimbursement = document.getElementById("currentReimbursement");
const currentReimbursementBody = document.getElementById("currentReimbursementBody");
const currentReimbursementPending = document.getElementById("currentReimbursementPendingBody");
const userid = sessionStorage.getItem("userid");
const reimbursementId = 0

//#####

const reimbursementRequestsTotal = document.getElementById("reimbursementRequestsTotal");
const reimbursementRequestsPending = document.getElementById("reimbursementRequestsPending");
const reimbursementRequestsApproved = document.getElementById("reimbursementRequestsApproved");
const reimbursementRequestsDenied = document.getElementById("reimbursementRequestsDenied");
const reimbursementRequestsNull = document.getElementById("reimbursementRequestsNull");

//##### Log out button to get back to sign in screen ########################################

function logout(){
    sessionStorage.clear();
    window.location.href = "../html/login.html"
}
//###### This gets the data from the manager table using userid ########################################

async function getAllManagerData(){
    let url = "http://127.0.0.1:5000/manager/" + userid.toLowerCase();
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateManagerData(body);
        getAllPastReimbursementData();
        getAllPendingReimbursementData();
    }
    else{
        alert("Error attempting to get manager information.");
    }

}
//##### Gets all "pending" reimbursements from the reimbursement table ########################################

async function getAllPendingReimbursementData(){
    let managerID = sessionStorage.getItem("managerId");
    let url = "http://127.0.0.1:5000/manager/pending/reimbursement/" + managerID;
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        populatePendingReimbursementData(body);
    }
    else{
        alert("Error attempting to get pending reimbursement information.");
    }
}

//##### This adds the pending reimbursement data to the table ########################################

function populatePendingReimbursementData(responseBody){
    for( let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.reimbursement}</td><td>${reimbursement.reasonwhy}</td><td>${reimbursement.acceptance}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        currentReimbursementPending.appendChild(tableRow);
        console.log(currentReimbursementPending);
    }
}

//##### This gets the pending data from the pending table and add its to the past table ########################################

async function getAllPastReimbursementData(){
    let managerID = sessionStorage.getItem("managerId");
    let url = "http://127.0.0.1:5000/past/reimbursements/" + managerID;
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        populatePastReimbursementData(body);
    }
    else{
        alert("Error Attempting to get past reimbursement information.");
    }
}

//###### This adds the past reimbursement data to the table ########################################

function populatePastReimbursementData(responseBody){
    for (let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.reimbursement}</td><td>${reimbursement.reasonwhy}</td><td>${reimbursement.acceptance}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        currentReimbursementBody.appendChild(tableRow);
        console.log(currentReimbursementBody);
    }
}
//constant variable that will reference elements 100-112 rid of leave, change let into conts, get rid of dots
//120 employee. employee. 
//pass in variable .value added to them
//##### This function updates the pending reimbursement to be approved ########################################

async function updateApproveReimbursementInfo(){
    let reimbursementId = document.getElementById("ReimbursementIdInput").value;
    console.log(reimbursementId);
    let employeeId = document.getElementById("employeeIdInput").value;
    console.log(employeeId);
    let managerId = document.getElementById("managerIdInput").value;
    console.log(managerId);
    let reimbursement = document.getElementById("requestReimbursementInput").value;
    console.log(reimbursement);
    let reasonwhy = document.getElementById("reasonwhyinput").value;
    console.log(reasonwhy);
    let acceptance = document.getElementById("acceptanceinput").value;
    console.log(acceptance);
    let managerComment = document.getElementById("managerCommentinput").value;
    console.log(managerComment);


    let url = "http://127.0.0.1:5000/reimbursement/approve/" + reimbursementId;
    let response = await fetch(url, {
    method: "PATCH",
    headers:{"Content-Type": 'application/json'},
    body: JSON.stringify({"employeeId":employeeId, "managerId":managerId, "reimbursement":reimbursement, "reasonwhy":reasonwhy, "acceptance":acceptance, "managerComment":managerComment})
    });


    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        //populateApproveReimbursementData(body);
    }
    else{
        alert("Error Attempting to update pending reimbursement.");
    }
}

//##### This function updates the pending reimbursement to be denied ########################################

async function updateDenyReimbursementInfo(){
    let reimbursementId = document.getElementById("ReimbursementIdInput").value;
    console.log(reimbursementId);
    let employeeId = document.getElementById("employeeIdInput").value;
    console.log(employeeId);
    let managerId = document.getElementById("managerIdInput").value;
    console.log(managerId);
    let reimbursement = document.getElementById("requestReimbursementInput").value;
    console.log(reimbursement);
    let reasonwhy = document.getElementById("reasonwhyinput").value;
    console.log(reasonwhy);
    let acceptance = document.getElementById("acceptanceinput").value;
    console.log(acceptance);
    let managerComment = document.getElementById("managerCommentinput").value;
    console.log(managerComment);


    let url = "http://127.0.0.1:5000/reimbursement/deny/" + reimbursementId;
    let response = await fetch(url, {
    method: "PATCH",
    headers:{"Content-Type": 'application/json'},
    body: JSON.stringify({"employeeId":employeeId, "managerId":managerId, "reimbursement":reimbursement, "reasonwhy":reasonwhy, "acceptance":acceptance, "managerComment":managerComment})
    });


    if (response.status === 200){
        let body = await response.json();
        //populateDenyReimbursementdata(body)
    }
    else{
        alert("Error attempting to update pending reimbursement.");
    }
}

//##### this adds the denied reimbursement to the new table ########################################

function populateDenyReimbursementData(responseBody){
    for(let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.reimbursementId}</td><td>${reimbursement.reasonwhy}</td><td>${reimbursement.acceptance}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        currentReimbursementPending.appendChild(tableRow);
        console.log(currentReimbursementPending);
    }
}

//##### This  adds the approved reimbursement to the new table ########################################

function populateApproveReimbursementData(responseBody){
    for (let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.reimbursementId}</td><td>${reimbursement.reasonwhy}</td><td>${reimbursement.acceptance}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        currentReimbursementPending.appendChild(tableRow);
        console.log(currentReimbursementPending);
    }
}

//##### this adds the reimbursement data to the table ########################################

function populateManagerData(manager){
    let tableRow = document.createElement("tr");
    //tableRow.innerHTML = ''
    tableRow.innerHTML = `<td>${manager.managerId}</td><td>${manager.firstName}</td><td>${manager.lastName}</td><td>${manager.userid}</td>`;
    currentManagerBody.appendChild(tableRow);
    sessionStorage.setItem("managerId", manager.managerId);
}

//####

// async function getReimbursementRequestsTotal(){
//     const response = await fetch(`http://127.0.0.1:5000/manager/total`)
//     const totalRequests = await response.json()
//     const total = totalRequests.totalRequests
//     reimbursementRequestsTotal.innerHTML = total
// }

// async function getReimbursementRequestsPending(){
//     const response = await fetch(`http://127.0.0.1:5000/manager`)
//     const pendingRequests = await response.json()
//     const pending = pendingRequests.PendingRequests
//     reimbursementRequestsPending.innerHTML = pending
// }

// async function getReimbursementRequestsApproved(){
//     const response = await fetch(`http://127.0.0.1:5000/manager/approved`)
//     const approvedRequests = await response.json()
//     const approved = approvedRequests.ApprovedRequests
//     reimbursementRequestsApproved.innerHTML = approved
// }
// async function getReimbursementRequestsDenied(){
//     const response = await fetch(`http://127.0.0.1:5000/manager/denied`)
//     const deniedRequests = await response.json()
//     const denied = deniedRequests.DeniedRequests
//     reimbursementRequestsDenied.innerHTML = denied
// }

// async function getReimbursementRequestsNull(){
//     const response = await fetch(`http://127.0.0.1:5000/manager/null/`)
//     const nullRequests = await response.json()
//     const nulll = nullRequests.NullRequests
//     reimbursementRequestsNull.innerHTML = nulll

// }

//##### Adds all data to tables ########################################

getAllManagerData();
// getReimbursementRequestsTotal();
// getReimbursementRequestsPending();
// getReimbursementRequestsApproved();
// getReimbursementRequestsDenied();
// getReimbursementRequestsNull();
