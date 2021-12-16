const container = document.querySelector(".container")

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
}

function UpdateOnChange(item) {
    container.innerHTML = `
    <div class="card mb-3">
         <div class="row g-0">
        <div class="col-md-4">
        ${item.image ? `<img src="${item.image}" class="img-fluid rounded-start" alt="" />` : `        <img src="https://www.w3schools.com/howto/img_avatar.png" class="img-fluid rounded-start" alt="" />`}
        </div>
        <div class="col-md-8">
        <div class="card-body">
            <h5 class="card-title">${item.name} (@${item.username})</h5>
            <p class="card-text">${item.bio}</p>
            <p class="card-text">${item.location}</p>
            <p class="card-text">Followers ${item.followers}, Following ${item.following}</p>
            ${item.is_following === false ? `<button class="btn btn-primary" onclick="followUnFollow('follow')">Follow</button>` : `<button class="btn btn-primary"onclick="followUnFollow('unfollow')">Unfollow</button>`}
            <p class="card-text my-3"><small class="text-muted">Joined on ${item.joined}</small></p>
            <a href="" class="btn btn-outline-success">View posts &#8594;</a>
        </div>
        </div>
    </div>
    </div>
    `
}

function followUnFollow(action) {
    const endpoint = `/api/profiles/${container.id}/`
    const data = {action : action}
    const method = "POST"
    const xhr = new XMLHttpRequest();
    const csrftoken = getCookie("csrftoken");
    xhr.open(method, endpoint)
    xhr.setRequestHeader("Content-Type", "application/json");
    if (csrftoken) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
    xhr.onload = () => {
      if (xhr.status === 200) {
        const responseData = JSON.parse(xhr.response)
        UpdateOnChange(responseData)
      } else if(xhr.status === 404) {
        alert("Profile does not exist")
      } else if (xhr.status === 401 || xhr.status === 403) {
        alert("Authentication error");
        console.log(xhr.response)
        // window.location.href = "/accounts/login/?next=/";
      } else if (xhr.status === 500) {
        alert("Please try again");
      }    
    }
  
    xhr.onerror = () => {
      alert("An error occured. Please try again");
    };
  
    xhr.send(JSON.stringify(data))
}

function InsertToRoot(item) {
    container.innerHTML = `
    <div class="card mb-3">
         <div class="row g-0">
        <div class="col-md-4">
        ${item.image ? `<img src="${item.image}" class="img-fluid rounded-start" alt="" />` : `        <img src="https://www.w3schools.com/howto/img_avatar.png" class="img-fluid rounded-start" alt="" />`}
        </div>
        <div class="col-md-8">
        <div class="card-body">
            <h5 class="card-title">${item.name} (@${item.username})</h5>
            <p class="card-text">${item.bio}</p>
            <p class="card-text">${item.location}</p>
            <p class="card-text">Followers ${item.followers}, Following ${item.following}</p>
            ${item.is_following === false ? `<button class="btn btn-primary" onclick="followUnFollow('follow')">Follow</button>` : `<button class="btn btn-primary"onclick="followUnFollow('unfollow')">Unfollow</button>`}
            <p class="card-text my-3"><small class="text-muted">Joined on ${item.joined}</small></p>
            <a href="" class="btn btn-outline-success">View posts &#8594;</a>
        </div>
        </div>
    </div>
    </div>
    `
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


