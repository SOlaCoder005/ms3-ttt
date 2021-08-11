terminal.js 



var socket = null;
var term = null;
var buffer = '';

function init_socket() {
    socket = io(window.location.protocol + '//' + window.location.host, {
        path: '/socket.io'
    });

    socket.on('connect', function () {
        socket.emit('connection_establish', 'ok');
        console.log("connected")
    });

    socket.on('console_output', function (msg, cb) {
        console.log("output:", msg)
        term.writeln(msg);
        term_short_prompt(term);
        if (cb)
            cb();
    });

}

function term_prompt(term) {
    buffer = '';
    term.write('\r\n$ ');
}

function term_short_prompt(term) {
    buffer = '';
    term.write('\r$ ');
}

function init_terminal() {
    term = new window.Terminal();
    term.open(document.getElementById('terminal'));

    function runFakeTerminal() {
        if (term._initialized) {
            return;
        }

        term._initialized = true;


        term.writeln('');
        term_prompt(term);

        term.onData(e => {
            switch (e) {
                case '\r': // Enter
                    console.log("command entered: ", buffer)
                    socket.emit('command_entered', buffer);
                    term_prompt(term);
                    break;
                case '\u007F': // Backspace (DEL)
                    // Do not delete the prompt
                    if (term._core.buffer.x > 2) {
                        term.write('\b \b');
                        buffer = buffer.slice(0, buffer.length - 1);
                    }
                    break;
                default: // Print all other characters for demo
                    buffer = buffer + e;
                    term.write(e);
            }
        });
    }

    runFakeTerminal();
}

document.addEventListener("DOMContentLoaded", function () {
    init_socket();
    init_terminal();
});