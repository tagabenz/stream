// Subscribe to user
async function subscribe(user_id, subscribe_to) {
    url = document.location.origin + "/api/v1/subscribe/" + user_id
    
    let response = await fetch(url, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json; charset=UTF-8',
            'X-CSRFToken': Cookies.get('csrftoken')
        },
        mode: 'same-origin', // Do not send CSRF token to another domain.
        body: JSON.stringify({"following": [subscribe_to]})
    });

    if (response.ok) {
        let json = await response.json();
        console.log(json.text)
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}