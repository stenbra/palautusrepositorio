class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def advantage_status(self):
        status_text=["Advantage ","Win for "]
        text_index = max(0,min(abs(self.player1_score - self.player2_score)-1,1))
    
        if self. player2_score> self.player1_score:
            return status_text[text_index] + self.player2_name
        else:
            return status_text[text_index] + self.player1_name

    def get_score(self):
        score_texts =["Love","Fifteen","Thirty","Forty","Deuce"]

        if self.player1_score == self.player2_score:
            return score_texts[self.player1_score]+"-All" if self.player1_score < 4 else "Deuce"

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.advantage_status()
        else:
            return score_texts[self.player1_score]+"-"+score_texts[self.player2_score]

