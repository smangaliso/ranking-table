from main import rankings

CONTENT = "Lions 3 ,Snakes 3\nTarantulas 1 ,FC Awesome 0\nLions 1 ,FC Awesome 1\nTarantulas 3 ,Snakes 1\n" \
              "Lions 4 ,Grouches 0"


def test_rankings(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input.txt"
    p.write_text(CONTENT)
    assert rankings(p) == {'Tarantulas ': 6, 'Lions ': 5, 'FC Awesome ': 1, 'Snakes ': 1, 'Grouches ': 0}


