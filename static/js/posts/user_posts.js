const root = document.querySelector(".posts")

console.log(root.id)

function getPosts() {
 const xhr = new XMLHttpRequest();
 const method = "GET";
 const url = `/api/posts/?username=${root.id}`
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

function UpdateOnlike(post) {
  const postdiv = document.getElementById(post.id)
  postdiv.innerHTML = `
  <p class="post-content">${post.content}</p>
  <p class="post-username"><a href="/profile/${post.user.username}/">@${post.user.username}</a></p>
  <div class="btn-group">
   <button class="btn btn-primary" onclick="likeUnlike(${post.id}, 'like');">${post.likes} Likes</button>
   <button class="btn btn-primary" onclick="likeUnlike(${post.id}, 'unlike');">Unlike</button>
   <a href="/${post.id}/" class="btn btn-outline-primary">View</a>
  </div>
  <p class="my-3" style="font-size : 18px;">On ${post.date}</p>   
  
  `
}

function likeUnlike(id, action) {
  const endpoint = "/api/posts/action/"
  const data = {id : id, action : action}
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
      UpdateOnlike(responseData);
    } else if(xhr.status === 404) {
      alert("Post does not exist")
    } else if (xhr.status === 401 || xhr.status === 403) {
      alert("You must login");
      window.location.href = "/accounts/login/?next=/";
    } else if (xhr.status === 500) {
      alert("Please try again");
    }    
  }

  xhr.onerror = () => {
    alert("An error occured. Please try again");
  };

  xhr.send(JSON.stringify(data))

}


function insertToRoot(posts) {
     posts.forEach((post) => {
       const card = document.createElement("div")
       const card_body = document.createElement("div")
       card_body.id = post.id
       card.className += "card my-3"
       card_body.className += "card-body py-2"
       card_body.innerHTML = `
       <p class="post-content">${post.content}</p>
       <p class="post-username"><a href="/profile/${post.user.username}/">@${post.user.username}</a></p>
       <div class="btn-group">
       <button class="btn btn-primary" onclick="likeUnlike(${post.id}, 'like');">${post.likes} Likes</button>
       <button class="btn btn-primary" onclick="likeUnlike(${post.id}, 'unlike');">Unlike</button>
       <a href="/${post.id}/" class="btn btn-outline-primary">View</a>
      </div>
      <p class="my-3" style="font-size : 18px;">On ${post.date}</p>  
       `
       card.appendChild(card_body)
       root.appendChild(card)
     })
}

getPosts();