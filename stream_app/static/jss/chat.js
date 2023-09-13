async function chatApi(url = "", data = {}) {
    const response = await fetch(url, {
      method: "POST", 
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
        "X-API-Key": "api-key"
      },
      body: JSON.stringify(data),
    });
    return response.json();
}