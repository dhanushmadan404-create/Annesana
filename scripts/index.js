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



const form = document.getElementById("UserData");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const formObject = Object.fromEntries(formData.entries());

  // Extra validation (optional)
  if (!formObject.email || !formObject.password || !formObject.role) {
    alert("All fields are required");
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formObject),
    });

    const data = await response.json();

    if (!response.ok) {
      console.error("Backend error:", data);
      alert(data.detail || "Submission failed");
      return;
    }

    console.log("Success:", data);
    alert("User created successfully!");
    form.reset();

  } catch (error) {
    console.error("Network Error:", error);
    alert("Server not reachable");
  }
});


// PROFILE
document.getElementById("profile").addEventListener("click", async (event) => {
     event.preventDefault();  // <-- Prevent page jump
    try {
        document.getElementById("profileDetails").style.visibility = "visible";

        const profile = document.getElementById("details");

        const response = await fetch("http://127.0.0.1:8000/users", {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        
        
        const data = await response.json();  // <-- data is now defined here
        console.log(data)
        profile.innerHTML = `
            <h1>Profile</h1>
            <label>Email:</label>
            <h3>${data[(data.length)-1].email}</h3>
            <br/>
            <label>Role:</label>
            <h3>${data[0].role}</h3>
        `;
    } catch (error) {
        console.error("Error:", error);
    }
});


    
            // if (!response.ok) {
            //     throw new Error("Failed to fetch profile");
            // }
