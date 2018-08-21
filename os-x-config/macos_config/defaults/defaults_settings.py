

defaults_settings = [
    defaults("Always show the full URL in the search/url field",
             ["app", "safari"],
             "com.apple.Safari",
             "ShowFullURLInSmartSearchField",
             ["-bool", "true"]),

    defaults("Disable shadow in screenshots",
             ["preference", "screenshot"],
             "com.apple.screencapture",
             "disable-shadow",
             ["-bool", "true"]),

    defaults("Don’t show Dashboard as a Space",
             ["preference", "dock"],
            "com.apple.dock",
             "dashboard-in-overlay",
             ["-bool", "true"]),

    defaults("Show file path in title of finder window",
             ["preference", "finder"],
             "com.apple.finder",
             "_FXShowPosixPathInTitle",
             ["-bool", "true"]),

    defaults("Enable AirDrop feature for ethernet connected Macs",
             ["network", "utility"],
             "com.apple.NetworkBrowser",
             "BrowseAllInterfaces",
             ["-bool", "true"]),

    defaults("Show Recovery partition & EFI Boot partition",
             ["disk", "utility"],
             "com.apple.DiskUtility",
             "DUDebugMenuEnabled",
             ["-bool", "true"],
             "10.11"),

    defaults("Always show scroll bars",
            ["global", "windows"],
             "NSGlobalDomain",
             "AppleShowScrollBars",
             ["-string", "Always"]),

    defaults("Expand Save panel by default",
             ["misc", "global"],
            "NSGlobalDomain",
             "NSNavPanelExpandedStateForSaveMode",
             ["-bool", "true"]),

    defaults("Expand Save panel by default",
             ["misc", "global"],
            "NSGlobalDomain",
             "NSNavPanelExpandedStateForSaveMode2",
             ["-bool", "true"]),

    defaults("Expand Print menu by default",
             ["misc", "global"],
            "NSGlobalDomain",
             "PMPrintingExpandedStateforPrint",
             ["-bool", "true"]),

    defaults("Expand Print menu by default",
             ["misc", "global"],
             "NSGlobalDomain",
             "PMPrintingExpandedStateforPrint2",
             ["-bool", "true"])

]

# Turn on/off mouse driver (use keyboard for mouse control)
# Add defaults write com.apple.universalaccess mouseDriver <value>

# Add pmset for energy saver settings (AC & Battery power). Needs sudo
# pmset -g to display current settings.
