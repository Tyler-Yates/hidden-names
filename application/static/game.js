$(document).ready(function () {
    const socket = io.connect('http://' + document.domain + ':' + location.port);

    const roomName = document.getElementById('game-name').innerHTML;
    socket.emit('join', {'room': roomName});

    socket.on('connect', function () {
        console.log('Webhook initiated');
    });

    socket.on('reload', function (data) {
        console.log(data);

        data.game_state.forEach(function (item, index) {
            update_tile(item.word, item.hidden_value, item.guessed);
        });
        //window.location.reload(false);
    });

    const wrapper = document.getElementById('button-container');
    console.info('Initialized event listener');

    wrapper.addEventListener('click', (event) => {
        const isButton = event.target.nodeName === 'BUTTON';
        if (!isButton) {
            return;
        }

        const inputId = `${event.target.id}-input`;
        const inputElement = document.getElementById(inputId);

        console.info(inputElement.value);

        socket.emit('guess', {'room': roomName, 'guess': inputElement.value});
    });
});

function update_tile(word, hidden_value, guessed) {
    const tile = document.getElementById(`button-${word}`);

    let category = "btn-light";

    if (guessed) {
        // Make button unclickable
        const disabledAttribute = document.createAttribute("disabled");
        tile.setAttributeNode(disabledAttribute);

        if (hidden_value === 3) {
            category = "btn-dark";
        } else if(hidden_value === 2) {
            category = "btn-danger";
        } else if(hidden_value === 1) {
            category = "btn-primary";
        } else {
            category = "btn-secondary";
        }
    }


    tile.setAttribute("class", `btn btn-block shadow-none rounded-0 ${category}`);
}