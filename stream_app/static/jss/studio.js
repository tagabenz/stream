function copyUrl() {
    // const isIos = navigator.userAgent.match(/ipad|iphone/i);
    var copyText = document.getElementById("pull_url");
    
    // if (isIos) {
    //     const range = document.createRange();
    //     range.selectNodeContents(textarea);
    
    //     const selection = window.getSelection();
    //     selection.removeAllRanges();
    //     selection.addRange(range);
    //     textarea.setSelectionRange(0, 999999);
    //   } else {
    //     textarea.select();
    //   }
    
    //   // copy selection
    //   document.execCommand('copy');
    
    //   // cleanup
    //   document.body.removeChild(textarea);
      
    copyText.select();
    navigator.clipboard.writeText(copyText.value);
}

function copyKey(){
    const isIos = navigator.userAgent.match(/ipad|iphone/i);
    var copyText = document.getElementById("id_stream_key");
    copyText.select();
    navigator.clipboard.writeText(copyText.value);
}