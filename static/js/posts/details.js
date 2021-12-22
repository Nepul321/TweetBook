const info_div = document.querySelector(".info");
const update_div = document.querySelector(".update");
let item = {};
const comments = document.querySelector(".comments");
const form = document.querySelector("#commentCreateForm")

function getData() {
  const xhr = new XMLHttpRequest();
  const method = "GET";
  const url = "/api/posts/" + info_div.id + "/";
  const responseType = "json";
  xhr.response = responseType;
  xhr.open(method, url);
  xhr.onload = () => {
    const serverResponse = xhr.response;
    var listedItem = serverResponse;
    item = listedItem;
    if (xhr.status === 200) {
      listedItem = JSON.parse(listedItem);
      insertToRoot(listedItem);
    } else if (xhr.status === 404) {
      alert("Post does not exist");
      window.location.href = "/";
    } else {
      alert("An error occured");
    }
  };

  xhr.send();
}

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

function UpdateOnChange(post) {
  info_div.innerHTML = `
    <h2><a href="/profile/${post.user.username}/">@${post.user.username}</a> (${
    post.user.first_name
  } ${post.user.last_name})</h2>
    <p class="content">${post.content}</p>
    <div class="btn-group">
    <button class="btn btn-primary" onclick="likeUnlike(${post.id}, 'like');">${
    post.likes
  } Likes</button>
    <button class="btn btn-primary" onclick="likeUnlike(${
      post.id
    }, 'unlike');">Unlike</button>
   </div>
   <p class="my-3" style="font-size : 18px;">On ${post.date}</p>  
   ${
     post.is_owner === true
       ? " <div class='btn-group my-3'><button class='btn btn-danger' onclick='Delete()'>Delete</button><button class='btn btn-secondary' onclick='Update();'>Update</button></div>"
       : "<div></div>"
   }  
    `;
}

function Delete() {
  const method = "DELETE";
  const endpoint = `/api/posts/${info_div.id}/`;
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
      window.location.href = "/";
    } else if (xhr.status === 404) {
      alert("Post does not exist");
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

function Update() {
  const post = JSON.parse(item);
  update_div.innerHTML = `
    
    <form id="update-form">
    <textarea class="form-control" name="content">${post.content}</textarea>
    <button class="btn btn-secondary my-2">Save</button>
    </form>
     
    `;

  const form = document.querySelector("#update-form");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const content = e.srcElement[0].value;
    const data = {
      content: content,
    };
    const method = "POST";
    const endpoint = `/api/posts/${post.id}/`;
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
        UpdateOnChange(response);
      } else if (xhr.status === 404) {
        alert("Post does not exist");
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

    xhr.send(JSON.stringify(data));
  });
}

function likeUnlike(id, action) {
  const endpoint = "/api/posts/action/";
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
      UpdateOnChange(responseData);
    } else if (xhr.status === 404) {
      alert("Post does not exist");
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

function insertToRoot(post) {
  info_div.innerHTML = `
 <h2><a href="/profile/${post.user.username}/">@${post.user.username}</a> (${
    post.user.first_name
  } ${post.user.last_name})</h2>
  <p class="content">${post.content}</p>
  <div class="btn-group">
  <button class="btn btn-primary" onclick="likeUnlike(${post.id}, 'like');">${
    post.likes
  } Likes</button>
  <button class="btn btn-primary" onclick="likeUnlike(${
    post.id
  }, 'unlike');">Unlike</button>
 </div>
 <p class="my-3" style="font-size : 18px;">On ${post.date}</p>  
 ${
   post.is_owner === true
     ? ` <div class="btn-group my-3"><button class="btn btn-danger" onClick="Delete()">Delete</button><button class="btn btn-secondary" onclick="Update();">Update</button></div>`
     : "<div></div>"
 }

 `;
}

function likeUnlikeComment(action, id) {
  const endpoint = "/api/comments/like-unlike/";
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
      UpdateCommentOnChange(responseData);
    } else if (xhr.status === 404) {
      alert("Comment does not exist");
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

function getComments() {
  const xhr = new XMLHttpRequest();
  const method = "GET";
  const url = `/api/comments/post/${info_div.id}/`
  const responseType = "json"
  xhr.response = responseType
  xhr.open(method, url)
  xhr.onload = () => {
     const serverResponse = xhr.response;
     var listedItems = serverResponse;
     if (xhr.status === 200) {
         listedItems = JSON.parse(listedItems)
         insertComments(listedItems);
     } else {
         alert("An error occured")
     }
  }
 
  xhr.send();
}

function DeleteComment(id) {
  const method = "DELETE";
  const endpoint = `/api/comments/${id}/`;
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
      alert("Comment does not exist");
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


function UpdateCommentOnChange(item) {
  const commentEl = document.querySelector(`#comment-${item.id}`)
  commentEl.innerHTML = `
  <p>${item.user.first_name} ${item.user.last_name} (<a href="/profile/${item.user.username}">@${item.user.username}</a>)</p>
  <p style="font-size : 20px;">${item.content}</p>
  <p class="text-muted small">On ${item.date}</p>
  <div class="btn-group">
  ${
    item.is_owner === true
    ? 
    `
    <button class="btn btn-danger" onclick="DeleteComment(${item.id})">Delete</button>
    <button class="btn btn-primary" onclick="likeUnlikeComment('like', ${item.id})"> ${item.likes} Likes</button>
    <button class="btn btn-primary" onclick="likeUnlikeComment('unlike', ${item.id})">Unlike</button>
    <a href="/comment/${item.id}/replies/" class="btn btn-outline-primary">Replies</a>
    `
    :
    `
    <button class="btn btn-primary" onclick="likeUnlikeComment('like', ${item.id})">Like</button>
    <button class="btn btn-primary" onclick="likeUnlikeComment('unlike', ${item.id})">Unlike</button>
    <a href="/comment/${item.id}/replies/" class="btn btn-outline-primary">Replies</a>
    `
  }
  </div>
  `
 }

function addNewPost(item) {
  const card = document.createElement("div")
  const card_correct = document.createElement("div")
  const card_body = document.createElement("div")
  card_correct.className += "card mb-3"
  card_body.id  = `comment-${item.id}`
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
    <button class="btn btn-danger" onclick="DeleteComment(${item.id})">Delete</button>
    <button class="btn btn-primary" onclick="likeUnlikeComment('like', ${item.id})"> ${item.likes} Likes</button>
    <button class="btn btn-primary" onclick="likeUnlikeComment('unlike', ${item.id})">Unlike</button>
    <a href="/comment/${item.id}/replies/" class="btn btn-outline-primary">Replies</a>
    `
    :
    `
    <button class="btn btn-primary" onclick="likeUnlikeComment('like', ${item.id})">Like</button>
    <button class="btn btn-primary" onclick="likeUnlikeComment('unlike', ${item.id})">Unlike</button>
    <a href="/comment/${item.id}/replies/" class="btn btn-outline-primary">Replies</a>
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
  const endpoint = "/api/comments/create/"
  const method = "POST"
  const xhr = new XMLHttpRequest();
  xhr.open(method, endpoint)
  xhr.onload = () => {
    if (xhr.status === 201) {
      const responseData = JSON.parse(xhr.response)
      comments.innerHTML = addNewPost(responseData) + comments.innerHTML
    } else if(xhr.status === 400) {
      alert("Input empty or Post too long")
    } else if (xhr.status === 401 || xhr.status === 403) {
      alert("Authentication error");
      window.location.href = "/accounts/login/?next=/";
    } else if (xhr.status === 500) {
      alert("Please try again");
    } else if(xhr.status === 404) {
      alert("Post not found")
    }
    myForm.reset();
  }
  xhr.onerror = () => {
    alert("An error occured. Please try again");
  };
  xhr.send(myformdata)
})

function insertComments(items) {
  items.forEach((item) => {
    const commentEl = document.createElement('div')
    commentEl.className += "card mb-3"
    const commentContentEl = document.createElement('div')
    commentContentEl.className += "card-body"
    commentContentEl.id += `comment-${item.id}`
    commentContentEl.innerHTML =  `
    <p>${item.user.first_name} ${item.user.last_name} (<a href="/profile/${item.user.username}">@${item.user.username}</a>)</p>
    <p style="font-size : 20px;">${item.content}</p>
    <p class="text-muted small">On ${item.date}</p>
    <div class="btn-group">
    ${
      item.is_owner === true
      ? 
      `
      <button class="btn btn-danger" onclick="DeleteComment(${item.id})">Delete</button>
      <button class="btn btn-primary" onclick="likeUnlikeComment('like', ${item.id})"> ${item.likes} Likes</button>
      <button class="btn btn-primary" onclick="likeUnlikeComment('unlike', ${item.id})">Unlike</button>
      <a href="/comment/${item.id}/replies/" class="btn btn-outline-primary">Replies</a>
      `
      :
      `
      <button class="btn btn-primary" onclick="likeUnlikeComment('like', ${item.id})">Like</button>
      <button class="btn btn-primary" onclick="likeUnlikeComment('unlike', ${item.id})">Unlike</button>
      <a href="/comment/${item.id}/replies/" class="btn btn-outline-primary">Replies</a>
      `
    }
    </div>
    `
    commentEl.appendChild(commentContentEl)
    comments.appendChild(commentEl)

  })
}

getComments();
getData();
