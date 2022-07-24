from masonite.routes import Route

ROUTES = [
    Route.get('/results', 'GameController@show_results'),
    Route.get('/reset', 'GameController@reset_game'),
    Route.post('/play', 'GameController@play')
]