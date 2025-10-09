
for (let i=0;i<5;i++) {
    let fila = document.getElementById(`fila${i}`);
    let modal = document.getElementById(`myModal${i}`);
    let span = document.getElementById(`close${i}`);
    fila.addEventListener("click", () => {
        modal.style.display = "block";
    });
    span.addEventListener("click", () => {
        modal.style.display = "none";
    });
    for (let j=0;j<5;j++) {
      let imagen = document.getElementById(`img-modal${i}${j}`);
      if (imagen) {
        imagen.addEventListener("mouseover", () => {
            imagen.width = "800";
            imagen.height = "600";
        });
        imagen.addEventListener("mouseout" ,() => {
            imagen.width = "320";
            imagen.height = "240";
        });
      }
    }
}
