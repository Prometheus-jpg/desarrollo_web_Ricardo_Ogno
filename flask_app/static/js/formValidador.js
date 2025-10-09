const validadorSelect = (select) => {
    if (!select) return false;
    return true;
};

const validadorNombre = (nombre) => {
    let valido = false;
    if (nombre && nombre.length>=3 && nombre.length<=200) {
        valido = true;
    }
    return valido;
};

const validadorEmail = (email) => {
    if (!email) return false;
    let largoEmail = email.length<=100;
    let regxEmail = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
    return regxEmail.test(email) && largoEmail;
};

const validadorNumero = (numero) => {
    let regxTel = /^\+569\d{8}$/;
    return regxTel.test(numero);
};

const validadorEdad = (edad) => {
    if (!edad || edad.length<1) return false;
    return true;
};

const validarForm = () => {
    let form = document.forms["formAviso"];
    let email = form["email"].value;
    let nombre = form["nombre"].value;
    let num = form["tel"].value;
    let edad = form["edad"].value;
    let region = form["select_region"].value;
    let comuna = form["select_comuna"].value;
    let tipo = form["tipo"].value;
    let foto = form["foto0"].value;
    let unidad = form["unidad_edad"].value;

    let msg = "";

    if (!validadorSelect(region)) {
        msg += "Seleccione una Region\n";
    }
    if (!validadorSelect(comuna)) {
        msg += "Seleccione una Comuna\n";
    }
    if (!validadorNombre(nombre)) {
        msg += "Nombre incorrecto\n";
    }
    if (!validadorEmail(email)) {
        msg += "Email incorrecto\n";
    }
    if (!validadorNumero(num)) {
        msg += "Numero incorrecto, sigua el patron +56912345678\n";
    }
    if (!validadorSelect(tipo)) {
        msg += "Seleccione que tipo es la Mascota\n";
    }
    if (!validadorEdad(edad)) {
        msg += "Edad incorrecta, minimo es 1\n";
    }
    if (!validadorSelect(unidad)) {
        msg += "Seleccione que unidad de edad\n";
    }
    if (!validadorSelect(foto)) {
        msg += "Suba al menos una foto\n"
    }

    if (msg === "") {
        let enviarBox = document.getElementById("enviar-box");
        let enviarMsg = document.getElementById("enviar-msg");
        let enviarLista = document.getElementById("enviar-list");
        form.style.display = "none";

        enviarMsg.innerText = "¿Está seguro que desea agregar este aviso de adopción?";
        enviarLista.textContent = ""

        let btnVolver = document.createElement("button");
        btnVolver.innerText = "No, volver";
        btnVolver.addEventListener("click", () => {
            form.style.display = "block";
            enviarBox.hidden = true;
        });

        let btnEnviar = document.createElement("button");
        btnEnviar.innerText = "Si, Enviar";
        btnEnviar.addEventListener("click", () => {
            let formAviso = document.getElementById("formAviso")
            formAviso.submit()
            enviarMsg.innerText = "Muchas gracias, hemos recibido la informacion de adopcion";
            btnVolver.remove()
            btnEnviar.remove()
            let lastBtn = document.createElement("button");
            lastBtn.innerText = "Volver a la portada";
            lastBtn.addEventListener("click", () => {
                window.location.href = "portada.html";
            });
            enviarLista.appendChild(lastBtn);
        });

        enviarLista.appendChild(btnVolver);
        enviarLista.appendChild(btnEnviar);

        enviarBox.hidden = false;
    } else {
        alert(msg);
    }
};

let validarBtn = document.getElementById("validar");
validarBtn.addEventListener("click", validarForm);


