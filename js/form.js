const changeDate = () => {
    const date = new Date();
    const year = date.getFullYear();
    let month = date.getMonth()+1;
    let day = date.getDate();
    let hour = date.getHours();
    let min = date.getMinutes();
    if (hour<21) {
        hour+=3;
    } else { 
        hour = 8;
        min = 0;
        day += 1;
    }
    if (day<10) {day=`0${day}`}
    if (hour<10) {hour=`0${hour}`}
    if (min<10) {min=`0${min}`}
    if (month<10) {month=`0${month}`}
    const fechaActual = `${year}-${month}-${day}T${hour}:${min}`;
    document.getElementById("fecha_entrega").value = fechaActual;
    document.getElementById("fecha_entrega").min = fechaActual;
};

const poblarRegiones = () => {
  let regionSelect = document.getElementById("select_region");
  for (let i=0;i<15;i++) {
    const region = region_comuna["regiones"][i];
    let option = document.createElement("option");
    option.value = region["numero"];
    option.text = region["nombre"];
    regionSelect.appendChild(option);
  }
};

const updateComuna = () => {
    let regionSelect = document.getElementById("select_region");
    let comunaSelect = document.getElementById("select_comuna");
    let regionSelected = regionSelect.value;

    comunaSelect.innerHTML = '<option value="">Seleccione una comuna</option>';

    if (regionSelected!="") {
        let p = parseInt(regionSelected)-1;
        region_comuna["regiones"][p]["comunas"].forEach(comuna => {
          let option = document.createElement("option");
          option.value = comuna["id"];
          option.text = comuna["nombre"];
          comunaSelect.appendChild(option);
      });
    }
};

const addContacto = (idSelect) => {
    const redesSociales = ["Whatsapp","Telegram","X","Instagram","Tiktok","Snapchat"];
    let contactoSelect = document.getElementById(idSelect);
    for (let i=0;i<6;i++) {
        let option = document.createElement("option");
        option.value = redesSociales[i];
        option.text = redesSociales[i];
        contactoSelect.appendChild(option);
    }
};

const changeContact = (numIdSelect) => {
    let selectSig = document.getElementById(`contacto${numIdSelect+1}`);
    selectSig.style.display = "inline";
    addContacto(`contacto${numIdSelect+1}`);
    if (numIdSelect<3) {
        let btnSig = document.getElementById(`buttonSelect${numIdSelect+1}`);
        btnSig.style.display = "inline";    
    }
    let btnActual = document.getElementById(`buttonSelect${numIdSelect}`);
    btnActual.style.display = "none";
    let textSig = document.getElementById(`textContacto${numIdSelect+1}`);
    textSig.style.display = "inline";
};

document.getElementById("select_region").addEventListener("change", updateComuna);
for (let i=0;i<4;i++) {
    let btnSelect = `buttonSelect${i}`;
    document.getElementById(btnSelect).addEventListener("click",() => {
        changeContact(i);
    });
    document.getElementById(`foto${i}`).addEventListener("change",() => {
        document.getElementById(`foto${i+1}`).style.display = "inline";
    });
}
document.getElementById("contacto0").addEventListener("change",() => {
    if (document.getElementById("contacto0").value != ""){
        document.getElementById("textContacto0").style.display = "inline";
        document.getElementById("buttonSelect0").style.display = "inline";
    } else {
        document.getElementById("textContacto0").style.display = "none";
        document.getElementById("buttonSelect0").style.display = "none";
    }
});


window.onload = () => {
    poblarRegiones();
    changeDate();
    addContacto("contacto0");
};