const root = document.getElementById("root")
const form = document.getElementById("reply-create-form")

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

function getReplies() {
const comment_id = root.dataset.id
const xhr = new XMLHttpRequest();
const method = "GET";
const url = `/api/replies/comment/${comment_id}/`
const responseType = "json"
xhr.response = responseType
xhr.open(method, url)
xhr.onload = () => {
   const serverResponse = xhr.response;
   var listedItems = serverResponse;
   if (xhr.status === 200) {
       listedItems = JSON.parse(listedItems)
       insertToRoot(listedItems);
   } else {
       alert("An error occured")
   }
}

xhr.send();
}

function DeleteReply(id) {
    const method = "DELETE";
    const endpoint = `/api/replies/${id}/`;
    const xhr = new XMLHttpRequest();
    const csrftoken = getCookie("csrftoken");
    xhr.open(method, endpoint);
    xhr.setRequestHeader("Content-Type", "application/json");
    if (csrftoken) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
    xhr.onload = () => {
      if (xhr.status === 200) {
        const response = JSON.parse(xhr.response);
        alert(response.message);
        window.location.reload();
      } else if (xhr.status === 404) {
        alert("Reply does not exist");
      } else if (xhr.status === 401 || xhr.status === 403) {
        alert(
          "An authentication error, you are not logged in or this is not your post"
        );
        window.location.href = "/accounts/login/?next=/" + info_div.id + "/";
      } else if (xhr.status === 500) {
        alert("Please try again");
      }
    };
    xhr.onerror = () => {
      alert("An error occured. Please try again");
    };
  
    xhr.send();
}

function UpdateonLike(item) {
    const element = document.getElementById(`${item.id}`)
    element.innerHTML = `
    <p>${item.user.first_name} ${item.user.last_name} (<a href="/profile/${item.user.username}/">@${item.user.username}</a>)</p>
    <p style="font-size : 20px;">${item.content}</p>
    <p class="text-muted small">On ${item.date}</p>
    <div class="btn-group">
    ${
      item.is_owner === true
      ? 
      `
      <button class="btn btn-danger" onclick="DeleteReply(${item.id})">Delete</button>
      <button class="btn btn-primary" onclick="likeUnlikeReply(${item.id}, 'like')"> ${item.likes} Likes</button>
      <button class="btn btn-primary" onclick="likeUnlikeReply(${item.id}, 'unlike')">Unlike</button>
      <a href="/reply/${item.id}/sub-replies/" class="btn btn-outline-primary">Replies</a>
      `
      :
      `
      <button class="btn btn-primary" onclick="likeUnlikeReply(${item.id}, 'like')">${item.likes} Likes</button>
      <button class="btn btn-primary" onclick="likeUnlikeReply(${item.id}, 'unlike')">Unlike</button>
      <a href="/reply/${item.id}/sub-replies/" class="btn btn-outline-primary">Replies</a>
      `
    }
    </div>
    `
}

function likeUnlikeReply(id, action) {
    const endpoint = "/api/replies/like-unlike/";
    const data = { id: id, action: action };
    const method = "POST";
    const xhr = new XMLHttpRequest();
    const csrftoken = getCookie("csrftoken");
    xhr.open(method, endpoint);
    xhr.setRequestHeader("Content-Type", "application/json");
    if (csrftoken) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
    xhr.onload = () => {
      if (xhr.status === 200) {
        const responseData = JSON.parse(xhr.response);
        UpdateonLike(responseData);
      } else if (xhr.status === 404) {
        alert("Reply does not exist");
      } else if (xhr.status === 401 || xhr.status === 403) {
        alert("You must login");
        window.location.href = "/accounts/login/?next=/";
      } else if (xhr.status === 500) {
        alert("Please try again");
      }
    };
  
    xhr.onerror = () => {
      alert("An error occured. Please try again");
    };
  
    xhr.send(JSON.stringify(data));
} 

function addNewReply(item) {
    const card = document.createElement("div")
    const card_correct = document.createElement("div")
    const card_body = document.createElement("div")
    card_correct.className += "card mb-3"
    card_body.id  = `${item.id}`
    card_body.className += "card-body"
    card_body.innerHTML = `
    <p>${item.user.first_name} ${item.user.last_name} (<a href="/profile/${item.user.username}">@${item.user.username}</a>)</p>
    <p style="font-size : 20px;">${item.content}</p>
    <p class="text-muted small">On ${item.date}</p>
    <div class="btn-group">
    ${
      item.is_owner === true
      ? 
      `
      <button class="btn btn-danger"  onclick="DeleteReply(${item.id})">Delete</button>
      <button class="btn btn-primary" onclick="likeUnlikeReply(${item.id}, 'like')"> ${item.likes} Likes</button>
      <button class="btn btn-primary" onclick="likeUnlikeReply(${item.id}, 'unlike')">Unlike</button>
      <a href="/reply/${item.id}/sub-replies/" class="btn btn-outline-primary">Replies</a>
      `
      :
      `
      <button class="btn btn-primary"  onclick="likeUnlikeReply(${item.id}, 'like')">${item.likes} Likes</button>
      <button class="btn btn-primary"  onclick="likeUnlikeReply(${item.id}, 'unlike')">Unlike</button>
      <a href="/reply/${item.id}/sub-replies/" class="btn btn-outline-primary">Replies</a>
      `
    }
    </div>
    `
    card_correct.appendChild(card_body)
    card.appendChild(card_correct)
    return card.innerHTML
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const myForm = e.target
    const myformdata = new FormData(myForm)
    const endpoint = "/api/replies/create/"
    const method = "POST"
    const xhr = new XMLHttpRequest();
    xhr.open(method, endpoint)
    xhr.onload = () => {
      if (xhr.status === 201) {
        const responseData = JSON.parse(xhr.response)
        root.innerHTML = addNewReply(responseData) + root.innerHTML
      } else if(xhr.status === 400) {
        alert("Input empty or Post too long")
      } else if (xhr.status === 401 || xhr.status === 403) {
        alert("Authentication error");
        window.location.href = "/accounts/login/?next=/";
      } else if (xhr.status === 500) {
        alert("Please try again");
      } else if(xhr.status === 404) {
        alert("Comment not found")
      }
      myForm.reset();
    }
    xhr.onerror = () => {
      alert("An error occured. Please try again");
    };
    xhr.send(myformdata)
})

function insertToRoot(data) {
  data.forEach((item) => {
      const card = document.createElement("div")
      const card_body = document.createElement("div")
      card.className = "card mb-3"
      card_body.className = "card-body"
      card_body.id = `${item.id}`
      card_body.innerHTML = `
      
      <p>${item.user.first_name} ${item.user.last_name} (<a href="/profile/${item.user.username}/">@${item.user.username}</a>)</p>
      <p style="font-size : 20px;">${item.content}</p>
      <p class="text-muted small">On ${item.date}</p>
      <div class="btn-group">
      ${
        item.is_owner === true
        ? 
        `
        <button class="btn btn-danger" onclick="DeleteReply(${item.id})">Delete</button>
        <button class="btn btn-primary" onclick="likeUnlikeReply(${item.id}, 'like')"> ${item.likes} Likes</button>
        <button class="btn btn-primary" onclick="likeUnlikeReply(${item.id}, 'unlike')">Unlike</button>
        <a href="/reply/${item.id}/sub-replies/" class="btn btn-outline-primary">Replies</a>
        `
        :
        `
        <button class="btn btn-primary" onclick="likeUnlikeReply(${item.id}, 'like')">${item.likes} Likes</button>
        <button class="btn btn-primary" onclick="likeUnlikeReply(${item.id}, 'unlike')">Unlike</button>
        <a href="/reply/${item.id}/sub-replies/" class="btn btn-outline-primary">Replies</a>
        `
      }
      </div>
      
      `
      card.appendChild(card_body)
      root.appendChild(card)
  })
}

getReplies();