const info_div = document.querySelector('.info')


function getData() {
    const xhr = new XMLHttpRequest();
    const method = "GET";
    const url = '/api/posts/' + info_div.id + "/"
    const responseType = "json"
    xhr.response = responseType
    xhr.open(method, url)
    xhr.onload = () => {
       const serverResponse = xhr.response;
       var listedItem = serverResponse;
       if (xhr.status === 200) {
           listedItem = JSON.parse(listedItem)
           insertToRoot(listedItem);
       } else if (xhr.status === 404) {
           alert("Post does not exist")
           window.location.href = "/"
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

function UpdateOnChange(post) {
    info_div.innerHTML = `
    <h2>@${post.user.username} (${post.user.first_name} ${post.user.last_name})</h2>
    <p class="content">${post.content}</p>
    <div class="btn-group">
    <button class="btn btn-primary" onclick="likeUnlike(${post.id}, 'like');">${post.likes} Likes</button>
    <button class="btn btn-primary" onclick="likeUnlike(${post.id}, 'unlike');">Unlike</button>
   </div>
   <br />
   ${post.is_owner === true ? ` <div class="btn-group my-3"><button class="btn btn-danger" onClick="Delete()">Delete</button><button class="btn btn-secondary">Update</button></div>` : "<div></div>"}  
    `
}

function Delete() {
   const method = "DELETE";
   const endpoint = `/api/posts/${info_div.id}/`
   const xhr = new XMLHttpRequest();
   const csrftoken = getCookie("csrftoken");
   xhr.open(method, endpoint)
   xhr.setRequestHeader("Content-Type", "application/json");
   if (csrftoken) {
     xhr.setRequestHeader("X-CSRFToken", csrftoken);
   }   
   xhr.onload = () => { 
    if (xhr.status === 200) {
        const response = JSON.parse(xhr.response)
        alert(response.message)
        window.location.href = "/"
    }
    else if(xhr.status === 404) {
      alert("Post does not exist")
    } else if (xhr.status === 401 || xhr.status === 403) {
      alert("An authentication error, you are not logged in or this is not your post");
      window.location.href = "/admin/login/?next=/" + info_div.id +  "/";
    } else if (xhr.status === 500) {
      alert("Please try again");
    }    
  }
  xhr.onerror = () => {
    alert("An error occured. Please try again");
  };

  xhr.send();
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
        UpdateOnChange(responseData);
      } else if(xhr.status === 404) {
        alert("Post does not exist")
      } else if (xhr.status === 401 || xhr.status === 403) {
        alert("You must login");
        window.location.href = "/admin/login/?next=/";
      } else if (xhr.status === 500) {
        alert("Please try again");
      }    
    }
  
    xhr.onerror = () => {
      alert("An error occured. Please try again");
    };
  
    xhr.send(JSON.stringify(data))
  
  }

function insertToRoot(post) {
 info_div.innerHTML = `
  <h2>@${post.user.username} (${post.user.first_name} ${post.user.last_name})</h2>
  <p class="content">${post.content}</p>
  <div class="btn-group">
  <button class="btn btn-primary" onclick="likeUnlike(${post.id}, 'like');">${post.likes} Likes</button>
  <button class="btn btn-primary" onclick="likeUnlike(${post.id}, 'unlike');">Unlike</button>
 </div> 
 <br />
 ${post.is_owner === true ? ` <div class="btn-group my-3"><button class="btn btn-danger" onClick="Delete()">Delete</button><button class="btn btn-secondary">Update</button></div>` : "<div></div>"}

 `
}

getData();