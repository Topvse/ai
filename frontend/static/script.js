async function sendEvent(eventType, elementName) {
  const payload = {
    event: eventType,
    element: elementName
  };

  try {
    const response = await fetch("http://localhost:8000/say", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    console.log("Ответ от сервера:", data);

    if (data.audio_file) {
      const player = document.getElementById("player");
      player.src = `http://localhost:8000${data.audio_file}`;
      player.play();
    }

  } catch (error) {
    console.error("Ошибка:", error);
    alert("Ошибка соединения с API");
  }
}

