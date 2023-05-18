new Vue({
    el: "#player_id",
    data: {
        player:[]
    },
    mounted: function () { 
        const vm = this;
        const username = JSON.parse(document.getElementById('username').textContent);
        const player = OvenPlayer.create('player_id', {
            sources: [
                {   
                    autoStart: true,
                    type: 'll-hls',
                    file: "http://192.168.1.198:3333/input/"+username+"/llhls.m3u8",
                }
            ]
        });
        vm.player=player
    },
})
