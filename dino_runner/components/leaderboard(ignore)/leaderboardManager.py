import json

LEADERBOARD_FILE = "dino_runner/components/leaderboard/leaderboard_file.json"


class LeaderboardManager:
    def __init__(self):
        self.leaderboard = LEADERBOARD_FILE

    def read_scores(self):
        with open(self.leaderboard, "r") as f:
            scores = json.load(f)
        return scores["scores"]
    
    def update_score(self, name, score):
        scores = self.read_scores()
        scores.append({"name": name, "score": score})
        scores.sort(key=lambda dic: dic["score"], reverse=True)
        scores = scores[:5]
        with open(LEADERBOARD_FILE, "w") as f:
            json.dump({"scores": scores}, f)