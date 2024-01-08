//selectors
const usernameField = document.getElementById('inputContainer');
//event listeners
//variables
function showdropdown(){
  let master_dropdown = document.getElementById('master-dropdown-menu');
  var classes = master_dropdown.className
  if (classes.indexOf('hidden') > -1) {
    master_dropdown.classList.remove("hidden")
    master_dropdown.classList.add("visible")}
  else {master_dropdown.classList.remove("visible")
    master_dropdown.classList.add("hidden")}      
}

function confirm_answers_password(){
   var confirm = window.confirm("Do you want to submit your answers?");
  if (confirm){
  var PassQ1 = document.querySelector('input[name="StrongPass_Comp"]:checked')
  var PassQ2 = document.querySelector('input[name="MinLength_Pass"]:checked')
  var PassQ3 = document.querySelector('input[name="Strongest_Pass"]:checked')
  var PassQ4 = document.querySelector('input[name="Reuse_Pass"]:checked')
  var total = 0
  if (!PassQ1 || !PassQ2 || !PassQ3 || !PassQ4){
    alert("Please answer all questions!")
  }else{
    if (PassQ1.value == "7"){total += 5}
    if (PassQ2.value == "12"){total += 5}
    if (PassQ3.value == "C"){total += 5}
    if (PassQ4.value == "False"){total += 5}
    const dataToSend = {passTotal: total}
    console.log(total)
    fetch('/Send_Data',{
         method:'POST',
      headers:{
      'Content-Type':'application/json'
      },
      body: JSON.stringify(dataToSend)
  }).then(response => response.text())
    .then(result => {
      window.location.href = result;
})}}}

function confirm_answers_phish(){
  var confirm = window.confirm("Do you want to submit your answers?");
  if (confirm){
  var Q1 = document.querySelector('input[name="Phish_Hours"]:checked')
  var Q2 = document.querySelector('input[name="Phish_Header"]:checked')
  var Q3 = document.querySelector('input[name="Phish_Parcel"]:checked')
  var Q4 = document.querySelector('input[name="Phish_Info"]:checked')
  var total = 0
  if (!Q1 || !Q2 || !Q3 || !Q4){
    alert("Please answer all questions!")
  }else{
    if (Q1.value == "True"){total += 5}
    if (Q2.value == "True"){total += 5}
    if (Q3.value == "True"){total += 5}
    if (Q4.value == "True"){total += 5}
    const dataToSend = {phishTotal: total}
    console.log(total)
    fetch('/Send_Data',{
       method:'POST',
    headers:{
    'Content-Type':'application/json'
    },
    body: JSON.stringify(dataToSend)
    }).then(response => response.text())
    .then(result => {
      window.location.href = result;
    })}}}

function confirm_answers_social(){
  var confirm = window.confirm("Do you want to submit your answers?");
  if (confirm){
  var Q1 = document.querySelector('input[name="Stage_Social"]:checked')
  var Q2 = document.querySelector('input[name="Goal_Social"]:checked')
  var Q3 = document.querySelector('input[name="Prevent_Target"]:checked')
  var Q4 = document.querySelector('input[name="Social_Tech"]:checked')
  var total = 0
  if (!Q1 || !Q2 || !Q3 || !Q4){
    alert("Please answer all questions!")
  }else{
    if (Q1.value == "4"){total += 5}
    if (Q2.value == "Man"){total += 5}
    if (Q3.value == "Care"){total += 5}
    if (Q4.value == "ALL"){total += 5}
    const dataToSend = {socialTotal: total}
    console.log(total)
    fetch('/Send_Data',{
       method:'POST',
    headers:{
    'Content-Type':'application/json'
    },
    body: JSON.stringify(dataToSend)
    }).then(response => response.text())
    .then(result => {
      window.location.href = result;
    })}}}

function confirm_answers_usb(){
  var confirm = window.confirm("Do you want to submit your answers?");
  if (confirm){
  var Q1 = document.querySelector('input[name="q1"]:checked')
  var Q2 = document.querySelector('input[name="q2"]:checked')
  var Q3 = document.querySelector('input[name="q3"]:checked')
  var Q4 = document.querySelector('input[name="q4"]:checked')
  var total = 0
  if (!Q1 || !Q2 || !Q3 || !Q4){
    alert("Please answer all questions!")
  }else{
    if (Q1.value == "3"){total += 5}
    if (Q2.value == "3"){total += 5}
    if (Q3.value == "3"){total += 5}
    if (Q4.value == "3"){total += 5}
    const dataToSend = {usbTotal: total}
    console.log(total)
    fetch('/Send_Data',{
       method:'POST',
    headers:{
    'Content-Type':'application/json'
    },
    body: JSON.stringify(dataToSend)
    }).then(response => response.text())
    .then(result => {
      window.location.href = result;
    })}}}

function confirm_answers_insider(){
  var confirm = window.confirm("Do you want to submit your answers?");
  if (confirm){
  var Q1 = document.querySelector('input[name="InsiderThreats"]:checked')
  var Q2 = document.querySelector('input[name="InsiderWeapon"]:checked')
  var Q3 = document.querySelector('input[name="Compromised_Insider"]:checked')
  var Q4 = document.querySelector('input[name="Decommission"]:checked')
  var total = 0
  if (!Q1 || !Q2 || !Q3 || !Q4){
    alert("Please answer all questions!")
  }else{
    if (Q1.value == "D"){total += 5}
    if (Q2.value == "A"){total += 5}
    if (Q3.value == "True"){total += 5}
    if (Q4.value == "A"){total += 5}
    const dataToSend = {insiderTotal: total}
    console.log(total)
    fetch('/Send_Data',{
       method:'POST',
    headers:{
    'Content-Type':'application/json'
    },
    body: JSON.stringify(dataToSend)
    }).then(response => response.text())
    .then(result => {
      window.location.href = result;
    })}}}