output_url = JSON.parse(document.getElementById('output_url').textContent);
const player = OvenPlayer.create('player_id', {
    autoStart: true,
    autoFallback: true,
    showBigPlayButton: false,
    sources: [
        {   
            type: 'll-hls',
            file: output_url,
        }
    ]
});
player.play()