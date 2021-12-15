const container = document.querySelector(".container")

function UpdateOnChange() {

}

function followUnFollow() {

}

function InsertToRoot(item) {
    console.log(item)
}

function loadProfile() {
    const xhr = new XMLHttpRequest();
    const method = "GET";
    const url = '/api/profiles/' + container.id + "/"
    const responseType = "json"
    xhr.response = responseType
    xhr.open(method, url)
    xhr.onload = () => {
    const serverResponse = xhr.response;
    var listedItem = serverResponse;
    item = listedItem
    if (xhr.status === 200) {
        listedItem = JSON.parse(listedItem)
        InsertToRoot(listedItem);
    } else if (xhr.status === 404) {
        alert("Profile does not exist")
        window.location.href = "/"
    } else {
        alert("An error occured")
    }
    }
       
    xhr.send();
}

loadProfile();


