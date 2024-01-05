//selectors
const usernameField = document.getElementById('inputContainer');
//event listeners
//variables
function showdropdown(){
  if (document.getElementById('master-dropdown-menu')){
  }
  let master_dropdown = document.getElementById('master-dropdown-menu');
  console.log(master_dropdown);
  if (master_dropdown.classlist.contains("hidden")){
      master_dropdown.classList.remove("hidden")
      master_dropdown.classList.add("visible")
  } else {
      master_dropdown.classList.remove("visible")
      master_dropdown.classList.add("hidden")
       }
}