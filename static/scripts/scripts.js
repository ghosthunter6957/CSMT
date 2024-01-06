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