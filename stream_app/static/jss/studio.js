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