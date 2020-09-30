import json

class Player:
    def __init__(self, player_name, peer_id):
        self.player_name = player_name;
        self.peer_id = peer_id;

    def serialize(self):
        data_to_serialize = {
            "player_name": self.player_name,
            "peer_id": self.peer_id
        }
        return json.dumps(data_to_serialize);