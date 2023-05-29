function copyUrl() {
    var copyText = document.getElementById("stream_url");
    copyText.select();
    navigator.clipboard.writeText(copyText.value);
}

function copyKey(){
    var copyText = document.getElementById("id_stream_key");
    copyText.select();
    navigator.clipboard.writeText(copyText.value);
}

function startStreaming(){
    url='http://192.168.1.198:3333/input/tagabenz3/llhls.m3u8';
    let response = fetch(url);
    if (response.ok) { 
    // если HTTP-статус в диапазоне 200-299
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}