
function iterationShellFunc(){
  dragIntegral();
}

var iterationButton = document.getElementById("iteration_button");
iterationButton.onclick = iterationShellFunc;


//I'm not sure why I have to do this, but doing it like above doesn't work for some reason.
function function2(){
	resetAllFields();
}

var resetButton = document.getElementById("reset_button");
resetButton.onclick = function2;

function getGravForce() {
  var g = parseFloat(document.getElementById("g").value);
  var m = parseFloat(document.getElementById("mass").value);

  return g * m;
}

//you need to give the function the name of the velocity variable to use for flexibility
function getDragForce(vel_var_id) {
  var dc = parseFloat(document.getElementById("d_coefficient").value);
  var vel = parseFloat(document.getElementById(vel_var_id).innerText);

  return dc * vel * vel * -1;
}

function getTotalForce(vel_var_id) {
  var df = getDragForce(vel_var_id)
  var gf = getGravForce();
  return (df + gf);
}

function dragIntegral() {
  //console.log("running dragIntegral");

  var m = parseFloat(document.getElementById("mass").value);
  var dc = parseFloat(document.getElementById("d_coefficient").value);
  var gc = parseFloat(document.getElementById("g").value);
  var t = parseFloat(document.getElementById("i_time").value);
  var v_id = "";

  //sets current_vel to starting velocity if it hasn't been set already
  var valueTest = document.getElementById("current_vel").innerText;
  if (valueTest == "n/a") {
    document.getElementById("current_vel").innerText = parseFloat(document.getElementById("start_vel").value);
  }

  if (t < 0.01) {
    t = 0.01;
  } else {
    t = Math.round(t * 100) / 100;
  }

  for (i = 0; i < t; i += 0.01) {
    document.getElementById("current_vel").innerText = parseFloat(document.getElementById("current_vel").innerText) + (parseFloat(getTotalForce("current_vel")) * 0.01 / m);
  }
}

function resetAllFields() {
  document.getElementById("mass").value = "";
  document.getElementById("d_coefficient").value = "";
  document.getElementById("g").value = "";
  document.getElementById("start_vel").value = "";
  document.getElementById("i_time").value = "";
  document.getElementById("current_vel").innerText = "n/a";
}
