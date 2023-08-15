function copyUrl() {
    var copyText = document.getElementById("pull_url");
    copyText.select();
    navigator.clipboard.writeText(copyText.value);
}

function copyKey(){
    var copyText = document.getElementById("id_stream_key");
    copyText.select();
    navigator.clipboard.writeText(copyText.value);
}

async function startStream(){
    var url=output_url
    fetch(url)
    .then(function() {
        fetch(location.origin+"/api/v1/studio/status_change");
        location.reload()
    })
    .catch(function() {
        alert("Сначала запустите видеокодер")
    });
}

async function stopStream(){
    fetch(location.origin+"/api/v1/studio/status_change")
    .then(function() {
        location.reload()
    })
    .catch(function() {
        
    });
}