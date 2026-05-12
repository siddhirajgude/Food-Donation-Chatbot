function sendMessage() {
    let userInput = document.getElementById("message").value;

    fetch("/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Bot reply:", data);  // Debug
        document.getElementById("chatbox").innerHTML += 
            "<p><b>You:</b> " + userInput + "</p>" +
            "<p><b>Bot:</b> " + data.reply + "</p>";
    });
}