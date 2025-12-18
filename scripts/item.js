const form = document.getElementById("commentForm");
const commentsDiv = document.getElementById("comments");
const comment_section=document.getElementById("comments-section")

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const stars = document.getElementById("stars");
  const comment = document.getElementById("comment");

  const data = {
    user_id: 1,
    food_id: 1,
    vendor_id: 1,
    rating: Number(stars.value),
    review_text: comment.value
  };

  console.log("Sending:", data);

  const response = await fetch("http://127.0.0.1:8000/reviews", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  const result = await response.json();

  // backend returns single object, so wrap in array
  displayComments([result]);
  
  form.reset();
});

async function loadComments() {
  try {
    const response = await fetch("http://127.0.0.1:8000/reviews");
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    displayComments(data);
    console.log(data);
  } catch (error) {
    console.error("Error fetching comments:", error);
    commentsDiv.innerHTML = "<p>Failed to load comments.</p>";
  }
}

function displayComments(data) {
  commentsDiv.innerHTML = ""; // Clear previous comments

  if (data.length === 0) {
    commentsDiv.innerHTML = "<p>No comments yet.</p>";
    return;
  }
 
  data.forEach((item) => {
    const commentItem = document.createElement("div");
    commentItem.className = "comment";

    commentItem.innerHTML = `
    <div><h3 class="userName">User_id: Customer${item.user_id}</h3><h3 class="userComments"><strong>comment: ${item.review_text}</strong></h3></div><h3 class="userStar"> Star Rating (${item.rating}⭐)</h3
    >
    `;

    comment_section.appendChild(commentItem);
  });
}

// Call the function to load comments when the page loads
loadComments();

