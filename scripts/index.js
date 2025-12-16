let loginForm=document.getElementById("loginForm")

document.getElementById("login").addEventListener("click",()=>{
loginForm.style.visibility="visible"
})
let collection = [
    "assets/food_image/Categories/break_fast.jpg",
    "assets/food_image/Categories/dinner.webp",
    "assets/food_image/Categories/drinking.JPG",
    "assets/food_image/Categories/lunch.avif",
    "assets/food_image/Categories/snacks.jpg",
    "assets/food_image/Categories/soup.jpg"
];

let collection_link = [
    "pages/categories/category_breakFast.html",
    "pages/categories/categories_dinner.html",
    "pages/categories/categories_drinking.html",
    "pages/categories/categories_lunch.html",
    "pages/categories/categories_snacks.html",
    "pages/categories/categories_drinking.html"
];

let img = document.getElementById("book");
let moveBtn = document.getElementById("move");

let i = 0;

// Set initial image + click
img.src = collection[i];
img.onclick = () => window.location.href = collection_link[i];

moveBtn.addEventListener("click", () => {
    // Advance index
    i++;
    if (i >= collection.length) {i = 0};

    // Update image
    img.src = collection[i];

    // Update click action
    img.onclick = () => {
        window.location.href = collection_link[i];
    };
});



// userData validation 
const form=document.getElementById("UserData")
document.getElementById("get").addEventListener("submit",async (event)=>{
    event.preventDefault()
    const formData=FormData(event.target)
    const formObject=Object.fromEntries(formData.entries())
    alert(formObject)
    fetch("/backend/app/router/user.py/users",{
        method:"POST",
        headers:{"content-type":"application/json"},
        body:JSON.stringify(formObject)
    })
    .then((Response)=>(Response.json()))
    .then((data)=>console.log("success:",data))
    .catch((error)=>{
        console.error("Error:",error)
    });

})
document.getElementById("profile").addEventListener("click",async ()=>{
    document.getElementById("profileDetails").style.visibility="visible"

let profile=document.getElementById("details")
const Response=await fetch("/backend/app/router/user.py/users/1")
const data=(await Response).json()
profile.innerHTML=`<h1>Profile</h1>
<label for="dataEmail"><h3 id="dataEmail">${data.email}</h3><br/>
<label for="Role"<h3 id="Role">${data.role}</h3>`
})

    
