const modal = document.getElementById("myModal");

const span = document.getElementsByClassName("close")[0];

for (let i=0;i<5;i++) {
    let fila = document.getElementById(`fila${i}`);
    fila.addEventListener("click", () => {
        modal.style.display = "block";
    });
}

for (let i=0;i<2;i++) {
    const imagen = document.getElementById(`img-modal${i}`);
    imagen.addEventListener("mouseover", () => {
        imagen.width = "800";
        imagen.height = "600";
    });
    imagen.addEventListener("mouseout" ,() => {
        imagen.width = "320";
        imagen.height = "240";
    });
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}