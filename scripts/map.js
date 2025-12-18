
/* =======================
   MAP INITIALIZATION
======================= */
let map = L.map("map").setView([13.0827, 80.2707], 11);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 20,
    attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

/* =======================
   ICON
======================= */
let foodIcon = L.icon({
    iconUrl: "/assets/3448609.png",
    iconSize: [40, 40],
    iconAnchor: [20, 40],
});

/* =======================
   GLOBAL VARIABLES
======================= */
let userLat = null;
let userLng = null;
let allLocations;   // ✅ FIXED: global storage

/* =======================
   CATEGORIES (FIXED)
======================= */
const categories = [
    { id: 8, foods: ["Biriyani", "ChickenRice", "fish", "keema"] },
    { id: 7, foods: ["almond", "coffee", "jigarthanda", "rose"] },
    { id: 4, foods: ["curd", "meal", "adai", "bread", "chappati", "dosa"] },
    { id: 5, foods: ["bhaji", "bonda", "samosa", "sweet"] },
];

/* =======================
   FETCH LOCATIONS
======================= */
async function getLoc() {
    try {
        const response = await fetch("http://127.0.0.1:8000/locations");
        const data = await response.json();

        allLocations = data; // ✅ SAVE LOCATIONS

        data.forEach((loc) => {
            if (loc.latitude && loc.longitude) {
                L.marker([loc.latitude, loc.longitude], { icon: foodIcon })
                    .addTo(map)
                    .bindPopup(
                        `<h3>${loc.location_name}</h3>Vendor ID: ${loc.vendor_id}`
                    );
                }});
function tryRouting() {
const foodName = localStorage.getItem("selectedFood");
console.log(foodName)
    if (!foodName || !userLat || !userLng || allLocations.length === 0) {
        return; // ⛔ wait until all data exists
    }

    let matchedLocation=null ;
    let shop;
    categories.forEach((cat) => {
        if (cat.foods.includes(foodName.toLowerCase())) {
            shop=cat.id
            console.log(shop)
        }
    });
    data.forEach((find) => { // Fixed arrow function syntax
        if (find.id === shop) { // Use the ID you found from categories
            matchedLocation = find;
            console.log(matchedLocation)
        }
    });
    
    if (!matchedLocation) {
        alert("Food location not found");
        return;
    }
}

tryRouting(); // ✅ try routing after data load
}
 catch (error) {
        console.error("Error fetching locations:", error);
    }
}
getLoc();

/* =======================
   USER LOCATION
======================= */
document.getElementById("getCurrent").addEventListener("click", () => {
    if (!navigator.geolocation) {
        alert("Geolocation not supported");
        return;
    }

    navigator.geolocation.getCurrentPosition(showPosition, (err) => {
        alert("Enable location permission");
        console.error(err);
    });
});

function showPosition(position) {
    userLat = position.coords.latitude;
    userLng = position.coords.longitude;

    map.setView([userLat, userLng], 15);

    L.marker([userLat, userLng])
        .addTo(map)
        .bindPopup("You are here")
        .openPopup();

    // tryRouting(); // ✅ try routing after location fetch
}

/* =======================
   ROUTING LOGIC
======================= */

L.Routing.control({
        waypoints: [
            L.latLng(userLat, userLng),
            L.latLng(matchedLocation.latitude, matchedLocation.longitude),
        ],
        routeWhileDragging: false,
        lineOptions: {
            styles: [{ color: "blue", weight: 5 }],
        },
    }).addTo(map);

    localStorage.removeItem("selectedFood"); // ✅ cleanup


// let man; // Declare globally

// function initMap() {
//     // Check if the 'map' variable is already set
//     if (man !== undefined && man !== null) {
//         man.remove(); // This safely destroys the old map if it exists
//     }

//     man = L.map('map').setView([13.08, 80.27], 12);
    
//     L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//         attribution: '© OpenStreetMap contributors'
//     }).addTo(map);
// }
// // SINGLE window.onload to handle everything
// window.onload = function() {
//     // A. Initialize Map
//     map = L.map('map').setView([13.08, 80.27], 12);
//     L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

//     // B. Automatically get location as soon as page loads
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition((position) => {
//             userLat = position.coords.latitude;
//             userLng = position.coords.longitude;
            
//             // Show user on map
//             L.marker([userLat, userLng]).addTo(map).bindPopup("You are here").openPopup();

//             // C. Check if we need to route to a food item
//             const food_name = localStorage.getItem("selectedFood");
//             if (food_name) {
//                 startRouting(food_name);
//                 localStorage.removeItem("selectedFood"); // Clear it
//             }
//         }, (err) => alert("Please enable location: " + err.message));
//     }
// };

// // This function stays here for your category_breakfast.html buttons
// function category(food_name) {
//     localStorage.setItem("selectedFood", food_name);
//     window.location.href = "map.html"; 
// }