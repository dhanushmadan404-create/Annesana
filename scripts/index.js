// localStorage.clear(); // or remove specific key
// localStorage.removeItem("token");
// localStorage.removeItem("role");
// localStorage.setItem("user", JSON.strconst userData = JSON.parse(localStorage.getItem("user"));
// console.log(userData.role); // user / admin / vendoringify(user));

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
document.addEventListener("DOMContentLoaded", () => {
    checkLoginStatus();
});

function checkLoginStatus() {
  let user = localStorage.getItem("user");

  let loginBtn = document.getElementById("login");
  let profileBtn = document.getElementById("profile");

  if (user) {
    // user logged in
    loginBtn.style.display = "none";
    profileBtn.style.display = "inline-block";
  } else {
    // user not logged in
    loginBtn.style.display = "inline-block";
    profileBtn.style.display = "none";
  }
}