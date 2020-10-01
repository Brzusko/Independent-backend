from flask import  Flask, request, jsonify, session;
from GameServers.GameServer import GameServer;
from GameServers.superview import game_service_view;
from GameServers.ServerHandler import ServerHandler;

import globals
import os
# data.server_name, data.address, data.max_players, data.max_count, data.port
# TOKEN, SECRET_KEY

master_servers = {};

app = Flask(__name__);
app.register_blueprint(game_service_view)

def register_master_servers():
    globals.master_servers['QuickHand'] = ServerHandler(10);

    for key, master_server in globals.master_servers.items():
        master_server.start();

def run():
    globals.init();
    register_master_servers();
    app.run(threaded=True, host='0.0.0.0', port=80);


if __name__ == "__main__":
    run();

