const API_URL = window.location.hostname === "127.0.0.1" || window.location.hostname === "localhost" ? "http://127.0.0.1:8000" : "";
const category = "drinking";
document.addEventListener("DOMContentLoaded", async () => {
  let card = document.getElementById("cardContainer")
  try {
    const res = await fetch(`${API_URL}/foods/category/${category}`);
    const vendor = await res.json();
    if (!vendor) {
      alert("Food data empty")
    }

    console.log(vendor)
    vendor.forEach(food => {
      const div = document.createElement("div");
      div.innerHTML = `
         <div class="card">
            <div class="image_container">
              <h2 class="food_name">${food.food_name}</h2>
              <img
                src="${API_URL}/uploads/${food.food_image_url}"
                class="card-image"
              />
            </div>
            <div class="card-buttons">
              <button class="find-btn" onclick="findLocation(${food.latitude}, ${food.longitude})">
                FIND
              </button>
            </div>
          </div>
      `;
      card.appendChild(div);
    });
  } catch (err) {
    alert(" failed ❌");
  }
})

function findLocation(lat, lng) {
  if (!lat || !lng) {
    alert("Location not available for this item.");
    return;
  }
  localStorage.setItem("targetCoords", JSON.stringify({ lat, lng }));
  window.location.href = "/pages/map.html";
}