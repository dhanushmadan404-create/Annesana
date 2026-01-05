// ---------------- SHOW / HIDE FORMS ----------------
function visible(showForm, hideForm) {
  
  document.getElementById(showForm).classList.add("visible");
  document.getElementById(hideForm).classList.remove("visible");
}

// ---------------- REGISTER ----------------
document.getElementById("registerForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("registrationEmail").value.trim();
  const password = document.getElementById("registrationPassword").value.trim();
  const role = document.getElementById("role").value;
  const image = document.getElementById("image").files[0];

  if (name.length < 3) return alert("Name too short");
  if (!email.includes("@gmail.com")) return alert("Invalid email");
  if (password.length < 6) return alert("Weak password");
  if (!role) return alert("Select role");
  if (!image) return alert("Upload image");

  const formData = new FormData();
  formData.append("name", name);
  formData.append("email", email);
  formData.append("password", password);
  formData.append("role", role);
  formData.append("image", image);

  const res = await fetch("http://127.0.0.1:8000/users/", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  if (!res.ok) return alert(data.detail);

  alert("Registration successful ✅");
});

// ---------------- LOGIN ----------------
document.getElementById("check").addEventListener("click", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();

  if (!email.includes("@gmail.com")) return alert("Invalid email");
  if (password.length < 6) return alert("Invalid password");

  const res = await fetch("http://127.0.0.1:8000/users/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const data = await res.json();
  if (!res.ok) return alert(data.detail);

  localStorage.setItem(data.role, JSON.stringify(data));

  if (data.role === "vendor") {
    const res = await fetch(`http://127.0.0.1:8000/vendors/users/${data.user_id}`);
    const vendor = await res.json();
    if(vendor){
        location.href="/pages/vendor-profile.html"
    }
    else{
    location.href = "/pages/registration.html"
    };
  } else if (data.role === "admin") {
    location.href = "/pages/admin.html";
  } else {
    location.href = "/index.html";
  }
});
