from GameServers.Counter import Counter;
from GameServers.Player import Player;
from flask import jsonify
import json

class GameServer:

    def __init__(self, server_name, address, max_players, max_count, port = 7171):
        self.server_name = server_name;
        self.address = address;
        self.max_players = max_players;
        self.port = port;
        self.counter = Counter(max_count);
        self.players = []

    def tick(self):
        self.counter.tick();

    def get_basic_data(self):
        data_to_serialize = {
            "server_name": self.server_name,
            "address": self.address,
            "max_players": self.max_players,
            "port": self.port,
            "player_count": len(self.players)
        }
        return json.dumps(data_to_serialize);

    def get_detailed_data(self):
        serialized_players = [];
        for player in self.players:
            serialized_players.append(player.serialize());

        server_info = {
            "server": self.get_basic_data(),
            "players": serialized_players
        }
        return server_info;

    def update(self, players):
        self.players.clear();
        for player in players:
            _player = Player(player['player_name'], player['id']);
            self.players.append(_player);
        self.counter.signal();

    def is_destroyable(self):
        return self.counter.can_be_destroyed;
