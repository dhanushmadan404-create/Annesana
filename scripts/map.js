/* =======================
   MAP INITIALIZATION
======================= */
const map = L.map("map").setView([13.0827, 80.2707], 11);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 20,
    attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

/* =======================
   ICON
======================= */
const foodIcon = L.icon({
    iconUrl: "/assets/3448609.png",
    iconSize: [40, 40],
    iconAnchor: [20, 40],
});

/* =======================
   GLOBAL VARIABLES
======================= */
let userLat = null;
let userLng = null;
let allLocations = [];
let matchedLocation = null;
let routingControl = null;

/* =======================
   FOOD CATEGORIES
======================= */
const categories = [
    { id: 8, foods: ["biriyani", "chickenrice", "fish", "keema", "rice"] },
    { id: 7, foods: ["almond", "coffee", "jigarthanda", "rose"] },
    { id: 4, foods: ["curd", "meal", "adai", "bread", "chappati", "dosa"] },
    { id: 5, foods: ["bhaji", "bonda", "samosa", "sweet"] },
];

/* =======================
   FETCH LOCATIONS
======================= */
async function getLocations() {
    const API_URL = window.location.hostname === "127.0.0.1" || window.location.hostname === "localhost" ? "http://127.0.0.1:8000" : "";
    try {
        const res = await fetch(`${API_URL}/foods/locations`);
        allLocations = await res.json();

        console.log("Locations loaded:", allLocations);

        allLocations.forEach(loc => {
            if (loc.latitude && loc.longitude) {
                L.marker([loc.latitude, loc.longitude], { icon: foodIcon })
                    .addTo(map)
                    .bindPopup(
                        `<b>${loc.location_name}</b><br>Vendor ID: ${loc.vendor_id}`
                    );
            }
        });

        tryRouting(); // attempt after locations load
    } catch (err) {
        console.error("Location fetch error:", err);
    }
}
getLocations();

/* =======================
   USER LOCATION
======================= */
document.getElementById("getCurrent")?.addEventListener("click", () => {
    if (!navigator.geolocation) {
        alert("Geolocation not supported");
        return;
    }

    navigator.geolocation.getCurrentPosition(
        showPosition,
        err => alert("Enable location access")
    );
});

function showPosition(position) {
    userLat = position.coords.latitude;
    userLng = position.coords.longitude;

    map.setView([userLat, userLng], 15);

    L.marker([userLat, userLng])
        .addTo(map)
        .bindPopup("You are here")
        .openPopup();

    tryRouting(); // attempt after location load
}

/* =======================
   ROUTING LOGIC
======================= */
function tryRouting() {
    // NEW ROUTING LOGIC
    const targetJSON = localStorage.getItem("targetCoords");

    if (targetJSON && userLat && userLng) {
        const target = JSON.parse(targetJSON);

        // Remove existing route
        if (routingControl) {
            map.removeControl(routingControl);
        }

        routingControl = L.Routing.control({
            waypoints: [
                L.latLng(userLat, userLng),
                L.latLng(target.lat, target.lng),
            ],
            routeWhileDragging: false,
            lineOptions: {
                styles: [{ color: "blue", weight: 5 }],
            },
            createMarker: function () { return null; } // Optional: suppress default markers
        }).addTo(map);

        // Optional: clear it after arrival or keep it
        // localStorage.removeItem("targetCoords");
        return;
    }

    // FALLBACK (Old Logic) - Optional to keep or remove.
    // I'll keep it simple: if no precise target, do nothing or just show all locations (which getLocations does).
}

/* =======================
   FOOD BUTTON HANDLER (Global)
======================= */
function findLocation(lat, lng) {
    localStorage.setItem("targetCoords", JSON.stringify({ lat, lng }));
    window.location.href = "/pages/map.html";
}

/* =======================
   FOOD BUTTON HANDLER
======================= */
function category(food_name) {
    localStorage.setItem("selectedFood", food_name.toLowerCase());
    window.location.href = "map.html";
}

// Vendor Find location
