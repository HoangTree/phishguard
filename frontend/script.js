const API_BASE = "http://127.0.0.1:5000";

const btn = document.getElementById("checkBtn");
const textarea = document.getElementById("emailText");
const result = document.getElementById("result");
const badge = document.getElementById("badge");
const confidence = document.getElementById("confidence");

btn.addEventListener("click", async () => {
  const text = textarea.value.trim();
  if (!text) {
    alert("Please paste an email or message.");
    return;
  }
  btn.disabled = true;
  btn.textContent = "Checking...";

  try {
    const res = await fetch(`${API_BASE}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });
    const data = await res.json();
    if (data.error) throw new Error(data.error);

    result.classList.remove("hidden");
    const pred = (data.prediction || "").toLowerCase();
    const conf = data.confidence !== null && data.confidence !== undefined ? (data.confidence * 100).toFixed(1) : null;

    if (pred === "phishing") {
      badge.innerHTML = `<span class="badge phish">⚠️ Phishing</span>`;
    } else {
      badge.innerHTML = `<span class="badge safe">✅ Safe</span>`;
    }
    confidence.textContent = conf ? `Confidence: ${conf}%` : "Confidence: N/A";
  } catch (e) {
    result.classList.remove("hidden");
    badge.innerHTML = `<span class="badge phish">Error</span>`;
    confidence.textContent = e.message;
  } finally {
    btn.disabled = false;
    btn.textContent = "Check Now";
  }
});
