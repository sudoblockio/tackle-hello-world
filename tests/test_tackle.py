from tackle import tackle


def test_all(change_base_dir):
    o = tackle(no_input=True)
    assert o
