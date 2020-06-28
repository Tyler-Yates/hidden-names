$(document).ready(function () {
    const socket = io.connect('http://' + document.domain + ':' + location.port);

    const roomName = document.getElementById('game-name').innerHTML;

    socket.on('connect', function () {
        console.log('Webhook initiated');
        socket.emit('join', {'room': roomName});
    });

    socket.on('game_update', function (data) {
        console.log(data);

        update_team_information(data.game_state);

        data.game_state.tiles.forEach(function (item, index) {
            update_tile(item.word, item.hidden_value, item.guessed);
        });
    });

    add_button_event_listener(socket, roomName);
});

// Function that sets up the logic for emitting a socket message when clicking on a button.
function add_button_event_listener(socket, roomName) {
    // Add an event wrapper to the entire button div but filter clicks only for button elements.
    const wrapper = document.getElementById('button-container');
    wrapper.addEventListener('click', (event) => {
        const isButton = event.target.nodeName === 'BUTTON';
        if (!isButton) {
            return;
        }

        const inputId = `${event.target.id}-input`;
        const inputElement = document.getElementById(inputId);

        socket.emit('guess', {'room': roomName, 'guess': inputElement.value});
    });
}

// Handle updates related to teams.
function update_team_information(game_state) {
    const blue_team_tiles_remaining = game_state.blue_team_tiles_remaining;
    document.getElementById('blue-team-tiles-remaining').innerText = `${blue_team_tiles_remaining}`;

    const red_team_tiles_remaining = game_state.red_team_tiles_remaining;
    document.getElementById('red-team-tiles-remaining').innerText = `${red_team_tiles_remaining}`;
}

// Handle an update to a particular tile.
function update_tile(word, hidden_value, guessed) {
    const tile = document.getElementById(`button-${word}`);

    let category = "btn-light";

    if (guessed) {
        // Make button unclickable
        const disabledAttribute = document.createAttribute("disabled");
        tile.setAttributeNode(disabledAttribute);

        if (hidden_value === 3) {
            category = "btn-dark";
        } else if (hidden_value === 2) {
            category = "btn-danger";
        } else if (hidden_value === 1) {
            category = "btn-primary";
        } else {
            category = "btn-secondary";
        }
    }


    tile.setAttribute("class", `btn btn-block shadow-none rounded-0 ${category}`);
}