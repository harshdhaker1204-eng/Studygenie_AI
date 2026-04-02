const BASE_URL = "http://127.0.0.1:5000";

// Add message
function addMessage(text, sender) {
    const chatBox = document.getElementById("chat-box");

    const msg = document.createElement("div");
    msg.className = `message ${sender}`;
    msg.innerText = text;

    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;

    return msg;
}

// Ask AI
async function askAI() {
    const input = document.getElementById("input");
    const question = input.value.trim();

    if (!question) return;

    addMessage(question, "user");
    input.value = "";

    const loading = addMessage("Typing...", "bot");

    try {
        const res = await fetch(`${BASE_URL}/ask`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ question })
        });

        if (!res.ok) throw new Error();

        const data = await res.json();

        loading.remove();
        addMessage(data.response || "No response", "bot");

    } catch (err) {
        loading.remove();
        addMessage("⚠️ Server error. Try again.", "bot");
    }
}

// Enter key
function handleKey(e) {
    if (e.key === "Enter") {
        askAI();
    }
}