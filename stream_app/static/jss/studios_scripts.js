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

async function startStreaming(){
    var url=output_url
    let response = await fetch(url);
    if (response.ok) { 
        // если HTTP-статус в диапазоне 200-299
        
       
    } else {
        alert("Сначала запустите видеокодер");
    }
}

