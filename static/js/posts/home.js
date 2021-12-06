const root = document.getElementById("root")

function getPost() {

}

function updatePost() {

}

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

function CreatePost() {

}

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