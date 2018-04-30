#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# Definition of OS X/MacOS tweaks
# group, description, set, get, os_v_min, os_ver_max

tweaks = [
    {'group': 'test',
     'description': 'Test exception handling',
     'get': "foobar",
     'set': "set-foobar",
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'animation',
     'description': 'Disable animations when opening and closing windows.',
     'get': "defaults read NSGlobalDomain NSAutomaticWindowAnimationsEnabled",
     'set': "defaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false",
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'animation',
     'description': 'Disable animations when opening a Quick Look window.',
     'set': "defaults write -g QLPanelAnimationDuration -float 0",
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'animation',
     'description': 'Disable animation when opening the Info window in OS X Finder (cmd⌘ + i).',
     'set': 'defaults write com.apple.finder DisableAllAnimations -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'animation',
     'description': 'Accelerated playback when adjusting the window size (Cocoa applications).',
     'set': 'defaults write NSGlobalDomain NSWindowResizeTime -float 0.001',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'animation',
     'description': 'Disable animations when you open an application from the Dock.',
     'set': 'defaults write com.apple.dock launchanim -bool false',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'app',
     'description': 'Always show the full URL in the search/url field',
     'get': 'defaults read com.apple.Safari ShowFullURLInSmartSearchField',
     'set': 'defaults write com.apple.Safari ShowFullURLInSmartSearchField -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'admin',
     'description': 'Show Recovery partition & EFI Boot partition',
     'set': 'defaults write com.apple.DiskUtility DUDebugMenuEnabled -bool true',
     'os_v_min': '10.09', 'os_v_max': '10.10'
     },
    {'group': 'general',
     'description': 'Disable shadow in screenshots',
     'set': 'defaults write com.apple.screencapture disable-shadow -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'sudo',
     'description': 'Disable Bonjour multicast advertisements.\n  See https://www.trustwave.com/Resources/SpiderLabs-Blog/mDNS---Telling-the-world-about-you-(and-your-device)/',
     'get': 'sudo defaults read /Library/Preferences/com.apple.mDNSResponder.plist NoMulticastAdvertisements',
     'set': 'sudo defaults write /Library/Preferences/com.apple.mDNSResponder.plist NoMulticastAdvertisements -bool YES',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'sudo',
     'description': 'Disable WiFi hotspot screen',
     'get': 'sudo defaults read /Library/Preferences/SystemConfiguration/com.apple.captive.control Active',
     'set': 'sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.captive.control Active -boolean false',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'general',
     'description': 'Don’t show Dashboard as a Space',
     'get': 'defaults read com.apple.dock dashboard-in-overlay',
     'set': 'defaults write com.apple.dock dashboard-in-overlay -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'Finder',
     'description': 'Show file path in title of finder window',
     'set': 'defaults write com.apple.finder _FXShowPosixPathInTitle -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'general',
     'description': 'Enable AirDrop feature for ethernet connected Macs',
     'set': 'defaults write com.apple.NetworkBrowser BrowseAllInterfaces -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'general',
     'description': 'Always show scroll bars',
     'set': 'defaults write NSGlobalDomain AppleShowScrollBars -string "Always"',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'general',
     'description': 'Expand Save panel by default (1/2)',
     'set': 'defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'general',
     'description': 'Expand Save panel by default (2/2)',
     'set': 'defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode2 -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'general', 'description': 'Expand Print menu by default (1/2)',
     'set': 'defaults write NSGlobalDomain PMPrintingExpandedStateforPrint -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'general', 'description': 'Expand Print menu by default (2/2)',
     'set': 'defaults write NSGlobalDomain PMPrintingExpandedStateforPrint2 -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'general',
     'description': 'Make all animations faster that are used by Mission Control.',
     'set': 'defaults write com.apple.dock expose-animation-duration -float 0.1',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'Finder',
     'description': 'Disable the delay when you hide the Dock',
     'set': 'defaults write com.apple.Dock autohide-delay -float 0',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'Finder',
     'description': 'Remove the animation when hiding/showing the Dock',
     'set': 'defaults write com.apple.dock autohide-time-modifier -float 0',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'app',
     'description': 'Disable the animation when you replying to an e-mail',
     'set': 'defaults write com.apple.mail DisableReplyAnimations -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'app',
     'description': 'Disable the animation when you sending an e-mail',
     'set': 'defaults write com.apple.mail DisableSendAnimations -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'app',
     'description': 'Disable the standard delay in rendering a Web page.',
     'set': 'defaults write com.apple.Safari WebKitInitialTimedLayoutDelay 0.25',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'general',
     'description': 'The keyboard react faster to keystrokes (not equally useful for everyone)',
     'set': 'defaults write NSGlobalDomain KeyRepeat -int 0',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'general',
     'description': 'Disable smooth scrolling for paging (space bar)',
     'set': 'defaults write -g NSScrollAnimationEnabled -bool false',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'Finder',
     'description': 'Avoid creating .DS_Store files on network volumes',
     'set': 'defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },
    {'group': 'Finder',
     'description': 'Avoid creating .DS_Store files on USB volumes',
     'set': 'defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'Finder',
     'description': 'Show the ~/Library folder',
     'set': 'chflags nohidden ~/Library',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'Finder',
     'description': 'Save to disk (not to iCloud) by default',
     'set': 'defaults write NSGlobalDomain NSDocumentSaveNewDocumentsToCloud -bool false',
     'os_v_min': '10.09', 'os_v_max': None
     },

    {'group': 'Finder',
     'description': 'Disable the warning when changing a file extension',
     'set': 'defaults write com.apple.finder FXEnableExtensionChangeWarning -bool false',
     'os_v_min': '10.09', 'os_v_max': None
     }
]
