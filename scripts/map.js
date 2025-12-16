let map=L.map("map").setView([0,0],1)
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{
    MaxZoom:20,
    Attributes: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map)
