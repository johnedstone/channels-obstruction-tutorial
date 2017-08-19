import React from 'react';
import GameBoard from './GameBoard.jsx'
import ReactDOM from 'react-dom'
import $ from 'jquery'

const game = $("#game_component").data("game")
const game_sock = 'ws://' + window.location.host + "/game/" + game + "/"
console.log(window.location.host)
let current_user = null

$.get('http://' + window.location.host + '/current-user/?format=json', function(result){
    // gets the current user information from Django
    current_user = result
    render_component()
})


function render_component(){
    ReactDOM.render(<GameBoard current_user={current_user} game_id={game} socket={game_sock}/>, document.getElementById("game_component"))
}
