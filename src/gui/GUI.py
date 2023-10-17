import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from src.gui import actions, styles
from src.backend import converter, loader


class MainWindow(QMainWindow):  # главное окно
    size = (1200, 720)
    start_pos = (300, 200)

    teams: list = []
    current_team: str = ''
    current_player: str = ''

    def __init__(self):
        super().__init__()
        self.setup_UI()

    def setup_UI(self):
        self.setWindowTitle("QuidditchPro")
        self.move(*self.start_pos)
        self.setFixedSize(*self.size)

        self.choose_team_widget = ChooseTeamWidget(self, self)
        self.choose_team_widget.move(self.size[0] // 4 - self.choose_team_widget.size[0] // 2, self.size[1] // 100)


class ChooseTeamWidget(QWidget):
    size = (300, 400)

    def __init__(self, window, parent=None):
        super().__init__(parent)
        self.window = window
        self.setup()

    def setup(self):
        self.resize(*self.size)

        layot = QVBoxLayout(self)

        title_lbl = QLabel('Choose team:', self)
        title_lbl.setFont(styles.H2)
        title_lbl.setAlignment(Qt.AlignCenter)

        layot.addWidget(title_lbl)

        self.team_combo_box = self.TeamComboBox(self.window, self)
        self.team_combo_box.currentTextChanged.connect(lambda x: actions.team_changed(self.window, x))
        layot.addWidget(self.team_combo_box)

        self.choose_player_lbl = QLabel('Choose player:', self)
        self.choose_player_lbl.setFont(styles.H3)
        layot.addWidget(self.choose_player_lbl)

        self.choose_player_combobox = self.PlayerComboBox(self.window, self)
        self.choose_player_combobox.currentTextChanged.connect(
            lambda x: actions.player_changed(self.window, x))
        layot.addWidget(self.choose_player_combobox)

        self.player_info = self.PlayerInfo(self.window, self)
        layot.addWidget(self.player_info)

        self.setLayout(layot)
        self.setStyleSheet("border: 2px solid black;")
        layot.setAlignment(Qt.AlignCenter)

    class TeamComboBox(QComboBox):
        size = (200, 200)

        def __init__(self, window, parent=None):
            super().__init__(parent)
            self.window = window
            self.setup()

        def setup(self):
            self.resize(*self.size)
            self.setFont(styles.TextFont)

            teams = loader.ExcelLoader().load_teams()

            self.clear()

            if not self.window.current_team:
                self.window.current_team = teams[0].name
            for team in teams:
                self.addItem(team.name)

    class PlayerComboBox(QComboBox):
        def __init__(self, window, parent=None):
            super().__init__(parent)
            self.window = window
            self.setup()

        def setup(self):
            window = self.window
            self.setFont(styles.TextFont)

            teams = loader.ExcelLoader().load_teams()
            for t in teams:
                if t.name == window.current_team:
                    team = t
                    break
            self.clear()

            for player_name in t.positions:
                if not self.window.current_player:
                    self.window.current_player = player_name
                self.addItem(player_name)

    class PlayerInfo(QWidget):
        def __init__(self, window, parent=None):
            super().__init__(parent)
            self.window = window
            self.setup()

        def setup(self):
            layot = QVBoxLayout(self)

            title_lbl = QLabel('Player Info:', self)
            title_lbl.setFont(styles.H2)
            title_lbl.setAlignment(Qt.AlignCenter)
            layot.addWidget(title_lbl)

            self.namel = QLabel('', self)
            self.namel.setFont(styles.TextFont)
            self.rolel = QLabel('', self)
            self.rolel.setFont(styles.TextFont)
            self.statel = QLabel('', self)
            self.statel.setFont(styles.TextFont)
            self.diseasel = QLabel('', self)
            self.diseasel.setFont(styles.TextFont)
            self.treatsl = QLabel('', self)
            self.treatsl.setFont(styles.TextFont)

            layot.addWidget(self.namel)
            layot.addWidget(self.rolel)
            layot.addWidget(self.statel)
            layot.addWidget(self.diseasel)
            layot.addWidget(self.treatsl)

            self.update_text()

            self.setLayout(layot)
            self.setStyleSheet("border: 2px solid black;")
            layot.setAlignment(Qt.AlignRight)

        def update_text(self):
            teams = loader.ExcelLoader().load_teams()
            for t in teams:
                if t.name == self.window.current_team:
                    team = t
                    break
            for name, pos in team.positions.items():
                if name == self.window.current_player:
                    position = pos
                    break

            name = position.player.name
            role = converter.convert_role_to_str(position.role)
            state = converter.convert_state_to_str(position.state)
            disease = str(pos.player.current_disease)
            treats = '\n->'.join([str(t) for t in pos.player.treats])

            self.namel.setText(f'Name: {name}')
            self.rolel.setText(f'Role: {role}')
            self.statel.setText(f'Status: {state}')
            self.diseasel.setText(f'Current disease: {disease}')
            self.treatsl.setText(f'Treats:\n->{treats}')


def launch():
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    launch()
