async function get_Notas(idAviso) {
  const res = await fetch(`${window.origin}/nota/${idAviso}`);
  const data = await res.json();

  const cuadroNota = document.getElementById(`notaAviso${idAviso}`);
  cuadroNota.innerText = data.nota;
  
}

async function changeNota(idAviso, nota) {

  try {
    const res = await fetch(`${window.origin}/notas/${idAviso}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ "aviso": {"id": idAviso}, "nota": nota })
    });

    if (!res.ok) {
      const error = await res.json();
      alert("Error: " + error.error);
      return;
    }

    document.getElementById('form').reset();
    document.getElementById("modal").style.display = "none";
    checkInput();
    await get_Notas(idAviso);

  } catch (err) {
    console.error("Error al enviar comentario:", err);
  }
}

const validate = async (id, nota) => {
    const notaNum = +nota;
    if (nota>=1 && nota<=7 && Number.isInteger(notaNum)) {
        await changeNota(id, nota);
    }
    else {
        alert("calificar con nota entre 1 y 7, debe ser un numero entero");
    }
}