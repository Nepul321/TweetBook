const root = document.getElementById("root")
const form = document.getElementById('post-create-form')

function getPosts() {
 const xhr = new XMLHttpRequest();
 const method = "GET";
 const url = '/api/posts/'
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

function addNewPost(post) {
  const card = document.createElement("div")
  const card_correct = document.createElement("div")
  const card_body = document.createElement("div")
  card_correct.className += "card my-3"
  card_body.className += "card-body py-2"
  card_body.innerHTML = `
  <p class="post-content">${post.content}</p>
  <p class="post-username">@${post.user.username}</p>
  <div class="btn-group">
   <button class="btn btn-primary">${post.likes} Likes</button>
   <button class="btn btn-primary">Unlike</button>
   <a href="" class="btn btn-outline-primary">View</a>
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
  const endpoint = "/api/posts/create/"
  const method = "POST"
  const xhr = new XMLHttpRequest();
  xhr.open(method, endpoint)
  xhr.onload = () => {
    if (xhr.status === 201) {
      const responseData = JSON.parse(xhr.response)
      root.innerHTML = addNewPost(responseData) + root.innerHTML
    } else if(xhr.status === 400) {
      alert("Input empty or Post too long")
    } else if (xhr.status === 401 || xhr.status === 403) {
      alert("You must login");
      window.location.href = "/admin/login/?next=/";
    } else if (xhr.status === 500) {
      alert("Please try again");
    }
    myForm.reset();
  }
  xhr.onerror = () => {
    alert("An error occured. Please try again");
  };
  xhr.send(myformdata)
})


function insertToRoot(posts) {
     posts.forEach((post) => {
       const card = document.createElement("div")
       const card_body = document.createElement("div")
       card.className += "card my-3"
       card_body.className += "card-body py-2"
       card_body.innerHTML = `
       <p class="post-content">${post.content}</p>
       <p class="post-username">@${post.user.username}</p>
       <div class="btn-group">
        <button class="btn btn-primary">${post.likes} Likes</button>
        <button class="btn btn-primary">Unlike</button>
        <a href="" class="btn btn-outline-primary">View</a>
       </div>
       `
       card.appendChild(card_body)
       root.appendChild(card)
     })
}

getPosts();