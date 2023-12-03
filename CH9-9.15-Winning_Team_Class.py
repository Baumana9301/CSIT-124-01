# 11.29.23 - LAB 9.15 - Winning Team (Classes)

# Andrew Bauman

# Class

class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def set_wins(self, win_count):
        self.wins = win_count

    def set_losses(self, loss_count):
        self.losses = loss_count

    def get_win_percentage(self):
        win_percentage = self.wins / (self.wins + self.losses)
        return win_percentage

    def print_standing(self):
        print(f'Win percentage: {self.get_win_percentage():.2f}')
        if self.get_win_percentage() >= 0.5:
            print(f'Congratulations, Team {self.name} has a winning average!')
        else:
            print(f'Team {self.name} has a losing average.')

team = Team()

team_name = input('Please enter a team: ')
team_wins = int(input('Please enter the amount of wins earned by the team: '))
team_losses = int(input('Please enter the amount of losses accrued by the team: '))

team.name = team_name
team.wins = team_wins
team.losses = team_losses

team.print_standing()
