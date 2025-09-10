document.getElementById("animeForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const title = document.getElementById("title").value;
    const status = document.getElementById("status").value;
  
    const response = await fetch("/add", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ title, status })
    });
  
    const result = await response.json();
    alert(result.message);
    window.location.reload();
  });