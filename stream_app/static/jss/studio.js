function copyUrl() {
    var copyText = document.getElementById("pull_url");
    copyText.select();
    navigator.clipboard.writeText(copyText.value);
}

function copyKey(){
    var copyText = document.getElementById("stream_key");
    copyText.select();
    navigator.clipboard.writeText(copyText.value);
}