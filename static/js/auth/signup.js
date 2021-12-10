const username = document.getElementById("id_username");
const password1 = document.getElementById("id_password1");
const password2 = document.getElementById("id_password2");
const email = document.getElementById("id_email");
const first_name = document.getElementById("id_first_name")
const last_name = document.getElementById("id_last_name");

const fields = [username, password1, password2, email, first_name, last_name];

function styleElements(fields) {
    fields.forEach((field) => {
         field.classList.add("form-control");
    })
}

styleElements(fields)