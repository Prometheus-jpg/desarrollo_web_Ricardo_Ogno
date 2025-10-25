
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

async function get_comentarios(comentario_id, idAviso) {
  const res = await fetch(`${window.origin}/get-comentarios?idAviso=${idAviso}`);
  const data = await res.json();
  console.log("Comentarios cargados:", data);
  const divComentarios = document.getElementById(`comentarios${comentario_id}`);
  divComentarios.innerHTML = "";

  for (let i=0; i<data.length; i++) {
    const newDiv = document.createElement("div");
    newDiv.classList.add("comentario");
    newDiv.innerHTML = `<p>${data[i].nombre} - ${data[i].fecha}</p><p>${data[i].comentario}</p>`;
    divComentarios.appendChild(newDiv);
  }
}

async function addComentario(event, idAviso, num) {
  event.preventDefault();

  const nombre = document.getElementById(`nombre${num}`).value;
  const comentario = document.getElementById(`comentario${num}`).value;
  try {
    const res = await fetch(`${window.origin}/add-comentario`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nombre, comentario, idAviso: idAviso })
    });

    if (!res.ok) {
      const error = await res.json();
      alert("Error: " + error.error);
      return;
    }

    document.getElementById(`formComentario${num}`).reset();
    await get_comentarios({num}, idAviso);

  } catch (err) {
    console.error("Error al enviar comentario:", err);
  }
}
