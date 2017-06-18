import network, badge, ugfx

sta_if = network.WLAN(network.STA_IF);
sta_if.active(True)
sta_if.connect("revspace-pub-2.4ghz")
sta_if.isconnected()

badge.init()
ugfx.init()

# loading screen
ugfx.clear();
ugfx.string(5, 5, "the quick brown fox jumps over the lazy dog", "DejaVuSansMono12", 0)
ugfx.string(5, 20, "the quick brown fox jumps over the lazy dog", "DejaVuSansMono14", 0)
ugfx.string(5, 40, "the quick brown fox jumps over the lazy dog", "DejaVuSansMono16", 0)
ugfx.string(5, 60, "the quick brown fox jumps over the lazy dog", "DejaVuSansMono18", 0)
ugfx.string(5, 80, "the quick brown fox jumps over the lazy dog", "DejaVuSansMono20", 0)
ugfx.string(5, 100, "the quick brown fox jumps over the lazy dog", "DejaVuSansMono22", 0)

ugfx.flush()
