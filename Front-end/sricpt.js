function summarize() {
    let videoUrl = document.getElementById("videoUrl").value;

    fetch("http://127.0.0.1:5000/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: videoUrl })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("summary").innerText = data.summary;
    })
    .catch(error => console.error("Error:", error));
}
