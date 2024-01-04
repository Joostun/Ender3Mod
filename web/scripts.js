const start = document.getElementById("start").addEventListener("click", () =>{
  request("http://127.0.0.1:5000/api/printer/start")
});
const stop = document.getElementById("stop").addEventListener("click", () =>{
  request("http://127.0.0.1:5000/api/printer/stop")
});
const autohome = document.getElementById("autohome").addEventListener("click", () =>{
  request("http://127.0.0.1:5000/api/printer/autohome")
});



// upload code
document.getElementById("uploadButton").addEventListener("click", () => {
  const Input = document.getElementById("Input");
  const statusMessage = document.getElementById("statusMessage");

  const gcode_file = Input.files[0];

  if (!gcode_file) {
      statusMessage.textContent = "No file selected.";
      return;
  }

  const formData = new FormData();
  formData.append("gcode_file", gcode_file);

  //send request
  fetch("http://127.0.0.1:5000/api/printer", {
      method: "POST",
      body: formData,
  })
});