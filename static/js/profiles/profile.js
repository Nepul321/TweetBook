const container = document.querySelector(".container")

function UpdateOnChange() {

}

function followUnFollow() {

}

function InsertToRoot(item) {
    container.innerHTML = `
    <div class="card mb-3">
         <div class="row g-0">
        <div class="col-md-4">
        <img src="https://www.w3schools.com/howto/img_avatar.png" class="img-fluid rounded-start" alt="" />
        </div>
        <div class="col-md-8">
        <div class="card-body">
            <h5 class="card-title">${item.name} (@${item.username})</h5>
            <p class="card-text">${item.bio}</p>
            <p class="card-text">${item.location}</p>
            <p class="card-text">Followers ${item.followers}, Following ${item.following}</p>
            ${item.is_following === false ? `<button class="btn btn-primary">Follow</button>` : `<button class="btn btn-primary">Unfollow</button>`}
            <p class="card-text my-3"><small class="text-muted">Joined on ${item.joined}</small></p>
        </div>
        </div>
    </div>
    </div>
    `
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


