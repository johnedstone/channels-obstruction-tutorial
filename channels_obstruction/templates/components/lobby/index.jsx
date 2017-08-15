import React from 'react';
import LobbyBase from './LobbyBase.jsx'
import ReactDOM from 'react-dom'
import $ from 'jquery'

console.log('ws://' + window.location.host + "/lobby/")
var lobby_sock = 'ws://' + window.location.host + "/lobby/"
var current_user = null

$.get('http://127.0.0.1:9999/current-user/?format=json', function(result){
    // gets the current user information from Django
    current_user = result
    render_component()
})


function render_component(){
    ReactDOM.render(<LobbyBase current_user={current_user} socket={lobby_sock}/>, document.getElementById('lobby_component'))
}
