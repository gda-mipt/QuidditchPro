def team_changed(window, text):
    from src.gui.GUI import MainWindow
    if not text:
        return
    window.current_team = text
    window.choose_team_widget.choose_player_combobox.setup()


def player_changed(window, text):
    from src.gui.GUI import MainWindow
    if not text:
        return
    window.current_player = text
    window.choose_team_widget.player_info.update_text()
