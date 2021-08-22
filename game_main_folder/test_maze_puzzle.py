from unittest.mock import patch
import pytest
import maze_puzzle


# check that state of game to changes to game when this function is called
def test_state_of_game():
    play = maze_puzzle.Game()  # arrange
    play.state_of_game()  # act
    assert play.game_state == "game"  # assert


# mock input of is_detective_near_crumbs() to True
# check that cookie crumbs changes to True when <20 pixels from cookie crumbs position
@patch('maze_puzzle.Game.is_detective_near_crumbs')
@pytest.mark.me
def test_find_crumbs(mockis_detective_near_crumbs):
    crumbs = maze_puzzle.Game()
    crumbs.game_state = "game"
    crumbs.init_game_state()
    mockis_detective_near_crumbs.return_value = True
    crumbs.find_crumbs()
    assert crumbs.cookie_crumbs is True


# mock input of is_detective_near_fountain() to True
# check that found_fountain changes to True when <20 pixels from fountain position
@patch('maze_puzzle.Game.is_detective_near_fountain')
@pytest.mark.me
def test_find_fountain(mockis_detective_near_fountain):
    crumbs = maze_puzzle.Game()
    crumbs.game_state = "game"
    crumbs.init_game_state()
    mockis_detective_near_fountain.return_value = True
    crumbs.find_fountain()
    assert crumbs.found_fountain is True


# mock inputs of winning position and cookie crumbs to True
# test that the game state changes to "win" if all win variables are True
@patch('maze_puzzle.Game.is_detective_near_winning_position')
@patch('maze_puzzle.Game.true_cookie_crumbs')
@pytest.mark.me
def test_win_is_true(mockis_detective_near_winning_position, mocktrue_cookie_crumbs):
    win = maze_puzzle.Game()
    win.game_state = "game"
    win.init_game_state()
    mockis_detective_near_winning_position.return_value = True
    mocktrue_cookie_crumbs.return_value = True
    win.win()
    assert win.game_state == "win"


# mocks input of winning position, cookie crumbs and that the false_no_win() function is false
# tests that the game continues when no_win is True
@patch('maze_puzzle.Game.is_detective_near_winning_position')
@patch('maze_puzzle.Game.true_cookie_crumbs')
@patch('maze_puzzle.Game.false_no_win')
@pytest.mark.me
def test_win_is_false(mockis_detective_near_winning_position, mocktrue_cookie_crumbs, mockfalse_no_win):
    win = maze_puzzle.Game()
    win.game_state = "game"
    win.init_game_state()
    win.true_no_win()
    mockis_detective_near_winning_position.return_value = True
    mocktrue_cookie_crumbs.return_value = False
    mockfalse_no_win.return_value = False
    win.win()
    assert win.no_win is True


