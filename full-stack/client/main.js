document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("feedbackForm");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      rating: parseInt(document.getElementById("rating").value),
      feedback: document.getElementById("feedback").value,
      best_feature: document.getElementById("best_feature").value,
      improvements: document.getElementById("improvements").value,
      next_workshop: document.getElementById("next_workshop").value
    };

    try {
      const response = await fetch("https://cells-resumes-standings-applies.trycloudflare.com/submit_feedback/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      const result = await response.json();
      alert(result.message);
      form.reset();
    } catch (err) {
      console.error(err);
      alert("Error submitting feedback.");
    }
  });
});
