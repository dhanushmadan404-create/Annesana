index page js with css{}

blur image should be change

logo+title
\

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 30px;
  background: #ffb347; /* spicy orange-yellow */
  box-shadow: 0 2px 10px rgba(255, 140, 0, 0.3);
  border-bottom: 3px solid #e85d04;
  flex-wrap: wrap;
}
header h1 {
  font-size: 28px;
  font-weight: 800;
  color: #3b1f00;
  text-shadow: 1px 1px 4px rgba(255, 255, 255, 0.5);
  letter-spacing: 2px;
}
.logo-align{
  display: flex;
  
}
/* Search Bar */
.search-bar ,.right-align{
  display: flex;
  align-items: center;
  
}
.right{
  gap: 20px;
}

.search-bar input {
  padding: 8px 10px;
  width: 250px;
  border: 2px solid #e85d04;
  border-radius: 4px 0 0 4px;
  outline: none;
  background: #fff;
  color: #3b1f00;
}
.right-align a{
  color: #3f3f3e;
}
.right-align a:hover{
  color: #090908;
}

.search-bar button {
  background: #e85d04;
  color: #fff;
  border: none;
  padding: 8px 12px;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
  font-weight: bold;
  transition: 0.3s;
}

.search-bar button:hover {
  background: #d9480f;
}

/* Navigation */
nav {
  display: flex;
  justify-content: center;
  /* background: #ffedd8; */
  padding: 12px 0;
  /* border-top: 2px solid #e85d04; */
  /* border-bottom: 2px solid #e85d04; */
  gap: 20px;
  flex-wrap: wrap;
}

nav a {
  color: #3b1f00;
  text-decoration: none;
  font-weight: bold;
  /* border: 2px solid #e85d04; */
  padding: 10px 20px;
  border-radius: 10px;
  transition: 0.3s;
  /* background: #fffaf2; */
}

nav a:hover {
  background: #e85d04;
  color: #fff;
  box-shadow: 0 0 10px rgba(232, 93, 4, 0.6);
}


   <header>
      <div class="logo-align">
      <img class="logo" src="/assets/logo.png" alt="not able to see" />
      <h1>Annesana</h1>
      </div>
      <nav>
        <a href="#">Home</a>
        <a href="/pages/map.html">Track</a>
        <a href="/pages/profile.html">Profile</a>
      </nav>
    
      <div class="search-bar">
        <input type="text" placeholder="Search..." />
        <button>🔍</button>
      </div>
   
    </header>