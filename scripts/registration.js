const API_URL = window.location.hostname === "127.0.0.1" || window.location.hostname === "localhost" ? "http://127.0.0.1:8000" : "";
// ---------------- PAGE LOAD ----------------
/* document.addEventListener("DOMContentLoaded", () => {
   getCurrentLocation(); 
}); */

// ---------------- MENU LIST ----------------
let list = []; // store menu items

let menu = document.querySelector(".menu-list"); // menu container
let inputList = document.getElementById("list"); // input box

document.getElementById("send").addEventListener("click", () => {
  const value = inputList.value.trim();

  if (value === "") return; // avoid empty input

  list.push(value); // store item

  let food = document.createElement("b"); // create UI element
  food.innerHTML = `${value}<br/>`;
  menu.appendChild(food); // add to UI

  inputList.value = ""; // clear input
});

// ---------------- MAP OPEN / CLOSE ----------------
let mapCon = document.getElementById("mapContainer");

document.querySelector(".location-group").addEventListener("click", () => {
  mapCon.style.display = "block"; // show map
});

document.getElementById("back").addEventListener("click", () => {
  mapCon.style.display = "none"; // hide map
});

document.getElementById("save").addEventListener("click", () => {
  mapCon.style.display = "none"; // hide map
});

// ---------------- MAP INIT ----------------
const map = L.map("map").setView([13.0827, 80.2707], 11);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 20,
}).addTo(map);

// ---------------- CURRENT LOCATION ----------------
document.getElementById("location").addEventListener("click", () => {
  navigator.geolocation.getCurrentPosition((position) => {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;

    map.setView([lat, lon], 15); // center map
  });
});

// ---------------- MAP ICON ----------------
const foodIcon = L.icon({
  iconUrl: "/assets/3448609.png",
  iconSize: [40, 40],
  iconAnchor: [20, 40],
});

// ---------------- LOCATION SELECT ----------------
let marker = null;
let latitude = null;   // ❗ was const (fixed)
let longitude = null;  // ❗ was const (fixed)

map.on("click", (e) => {
  if (marker) map.removeLayer(marker); // remove old marker

  marker = L.marker([e.latlng.lat, e.latlng.lng], { icon: foodIcon }).addTo(map);

  latitude = e.latlng.lat;   // save lat
  longitude = e.latlng.lng;  // save lng
});

// ---------------- VENDOR REGISTRATION ----------------
document.getElementById("vendorRegistration").addEventListener("submit", async (e) => {
  e.preventDefault(); // stop refresh

  const foodType = document.querySelector("select");
  if (foodType.value === "") return alert("Select food type");

  const phone = document.getElementById("number");
  if (!/^\d{10}$/.test(phone.value)) return alert("Invalid phone");

  const image = document.getElementById("image");
  if (!image.files.length) return alert("Upload image");

  const menuContainer = document.querySelector(".menu-list");
  if (menuContainer.children.length === 0)
    return alert("Add at least one food");

  // convert menu UI → array
  let menuList = [...menuContainer.children].map(item =>
    item.textContent.trim()
  );

  // location check
  if (latitude === null || longitude === null)
    return alert("Select shop location");

  // time validation
  const timeInputs = document.querySelectorAll('input[type="time"]');
  const openTime = timeInputs[0].value;
  const closeTime = timeInputs[1].value;

  if (!openTime || !closeTime)
    return alert("Select opening & closing time");

  const [openH, openM] = openTime.split(":").map(Number);
  const [closeH, closeM] = closeTime.split(":").map(Number);

  const openMinutes = openH * 60 + openM;
  const closeMinutes = closeH * 60 + closeM;

  if (closeMinutes <= openMinutes)
    return alert("Closing must be after opening");

  if (closeMinutes - openMinutes < 60)
    return alert("Minimum 1 hour required");

  // ---------------- SEND VENDOR DATA ----------------
  const user = JSON.parse(localStorage.getItem("user"));
  if (!user || !user.user_id) return alert("Please login first");
  const vendorId = user.user_id; // actually user_id, backend maps it

  const formData = new FormData();
  formData.append("phone_number", phone.value);
  formData.append("cart_image_url", image.files[0]);
  formData.append("opening_time", openTime);
  formData.append("closing_time", closeTime);
  formData.append("user_id", vendorId);

  try {
    const res = await fetch(`${API_URL}/vendors`, {
      method: "POST",
      body: formData
    });

    if (!res.ok) {
      const err = await res.json();
      return alert(err.detail || "Registration failed");
    }

    const data = await res.json();

    const foodDataList = menuList.map(food => ({
      food_name: food,
      category: foodType.value,
      latitude,
      longitude,
      vendor_id: data.vendor_id,   // ✅ now correct
      cart_image_url: null
    }));

    // Create foods backend
    for (const food of foodDataList) {
      const fd = new FormData();
      fd.append("food_name", food.food_name);
      fd.append("category", food.category);
      fd.append("latitude", food.latitude);
      fd.append("longitude", food.longitude);
      fd.append("vendor_id", food.vendor_id);

      // Dummy image or handle file upload properly?
      // Since registration form has only one image (for cart/vendor), 
      // we might not have images for individual foods yet.
      // BUT backend requires image. We can reuse vendor image or a default.
      // For now, let's reuse the vendor image file object if possible, or skip image if backend allows optional (it doesn't).
      // We will re-append the same image file for now.
      fd.append("image", image.files[0]);

      await fetch(`${API_URL}/foods`, {
        method: "POST",
        body: fd
      });
    }

    // Update localStorage user/vendor status if needed
    // Maybe redirect to login or vendor profile
    alert("Vendor Registered Successfully! ✅");
    window.location.href = "/pages/vendor-profile.html";

  } catch (err) {
    alert("Upload failed ❌");
  }
});

