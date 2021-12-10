const old_password = document.getElementById("id_old_password")
const new_password1 = document.getElementById("id_new_password1")
const new_password2 = document.getElementById("id_new_password2")

const elements = [old_password, new_password1, new_password2]

function styleElements(elements) {
    elements.forEach((element) => {
        element.classList.add("form-control")
    })
}

styleElements(elements);