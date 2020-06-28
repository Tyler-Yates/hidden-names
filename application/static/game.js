$(document).ready(function () {
    const socket = io.connect('http://' + document.domain + ':' + location.port);

    const roomName = document.getElementById('game-name').innerHTML;

    socket.on('connection', function (socket) {
        console.log('Websocket connected!');
        socket.join('some room');
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
