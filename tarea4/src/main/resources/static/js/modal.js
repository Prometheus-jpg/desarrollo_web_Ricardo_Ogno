// Get the modal
let modal = document.getElementById("modal");
let calificacion = document.getElementById("calificacion");

// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[0];

let btn = document.getElementById("calificar");

const openModal =  (id) => {
  modal.style.display = "block";
  btn.addEventListener("click", async () => {
    const nota = document.getElementById('nota').value;
    await validate(id, nota);
  });
}

// When the user clicks on <span> (x), close the modal
span.onclick = () => {
  modal.style.display = "none";
  document.getElementById('form').reset();
  checkInput();
}

// When the user clicks anywhere outside of the modal, close it
modal.onclick = (event) => {
  if (event.target == modal) {
    modal.style.display = "none";
    document.getElementById('form').reset();
    checkInput();
  }
}

const checkInput = () => {
  let nota = document.getElementById("nota").value;
  const notaNum = +nota;
  if (nota != "" && nota > 0 && nota <= 7 && Number.isInteger(notaNum)) {
    btn.disabled = false;
  }
  else {
    btn.disabled = true;
  }
}

document.getElementById("nota").addEventListener("change", checkInput);


