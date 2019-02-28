#! /usr/bin/env python3

# Definition of OS X/MacOS settings
# group, description, command_line, os_v_min, os_ver_max
#
# Check for min version of OS X 10.9!!

# Sources:
#    - https://github.com/mathiasbynens/dotfiles/blob/master/.macos
#    - https://github.com/pawelgrzybek/dotfiles/blob/master/setup-macos.sh

settings = [
    {'group': 'animation',
     'description': 'Disable animations when opening and closing windows.',
     'command_line': "defaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false"
     },

    {'group': 'animation',
     'description': 'Disable animations when opening a Quick Look window.',
     'command_line': "defaults write -g QLPanelAnimationDuration -float 0"
     },

    {'group': 'animation',
     'description': 'Disable animation when opening the Info window in OS X Finder (cmd⌘ + i).',
     'command_line': 'defaults write com.apple.finder DisableAllAnimations -bool true'
     },

    {'group': 'animation',
     'description': 'Accelerated playback when adjusting the window size (Cocoa applications).',
     'command_line': 'defaults write NSGlobalDomain NSWindowResizeTime -float 0.001'
     },

    {'group': 'animation',
     'description': 'Disable animations when you open an application from the Dock.',
     'command_line': 'defaults write com.apple.dock launchanim -bool false'
     },

    {'group': 'Safari',
     'description': 'Always show the full URL in the search/url field',
     'command_line': 'defaults write com.apple.Safari ShowFullURLInSmartSearchField -bool true'
     },

    {'group': 'admin',
     'description': 'Show Recovery partition & EFI Boot partition',
     'command_line': 'defaults write com.apple.DiskUtility DUDebugMenuEnabled -bool true',
     'os_v_max': '10.10'
     },

    {'group': 'general',
     'description': 'Disable shadow in screenshots',
     'command_line': 'defaults write com.apple.screencapture disable-shadow -bool true'
     },

    {'group': 'need-user-input',
     'description': 'Change the location for saving screenshots',
     'command_line': 'defaults write com.apple.screencapture location <new path>/; killall SystemUIServer'
     },

    {'group': 'sudo',
     'description': 'Disable Bonjour multicast advertisements.\n  See https://www.trustwave.com/Resources/SpiderLabs-Blog/mDNS---Telling-the-world-about-you-(and-your-device)/',
     'command_line': 'sudo defaults write /Library/Preferences/com.apple.mDNSResponder.plist NoMulticastAdvertisements -bool YES'
     },

    {'group': 'sudo',
     'description': 'Disable WiFi hotspot screen',
     'command_line': 'sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.captive.control Active -boolean false'
     },

    {'group': 'general',
     'description': 'Don’t show Dashboard as a Space',
     'command_line': 'defaults write com.apple.dock dashboard-in-overlay -bool true'
     },

    {'group': 'Finder',
     'description': 'Show file path in title of finder window',
     'command_line': 'defaults write com.apple.finder _FXShowPosixPathInTitle -bool true'
     },

    {'group': 'sharing',
     'description': 'Enable AirDrop feature for ethernet connected Macs',
     'command_line': 'defaults write com.apple.NetworkBrowser BrowseAllInterfaces -bool true'
     },

    {'group': 'general',
     'description': 'Always show scroll bars',
     'command_line': 'defaults write NSGlobalDomain AppleShowScrollBars -string "Always"'
     },

    {'group': 'general',
     'description': 'Expand Save panel by default (1/2)',
     'command_line': 'defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode -bool true'
     },

    {'group': 'general',
     'description': 'Expand Save panel by default (2/2)',
     'command_line': 'defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode2 -bool true'
     },

    {'group': 'general',
     'description': 'Expand Print menu by default (1/2)',
     'command_line': 'defaults write NSGlobalDomain PMPrintingExpandedStateforPrint -bool true'
     },

    {'group': 'general',
     'description': 'Expand Print menu by default (2/2)',
     'command_line': 'defaults write NSGlobalDomain PMPrintingExpandedStateforPrint2 -bool true'
     },

    {'group': 'general',
     'description': 'Make all animations faster that are used by Mission Control.',
     'command_line': 'defaults write com.apple.dock expose-animation-duration -float 0.1'
     },

    {'group': 'Finder',
     'description': 'Disable the delay when you hide the Dock',
     'command_line': 'defaults write com.apple.Dock autohide-delay -float 0'
     },

    {'group': 'Finder',
     'description': 'Remove the animation when hiding/showing the Dock',
     'command_line': 'defaults write com.apple.dock autohide-time-modifier -float 0'
     },

    {'group': 'app',
     'description': 'Disable the animation when you replying to an e-mail',
     'command_line': 'defaults write com.apple.mail DisableReplyAnimations -bool true'
     },

    {'group': 'app',
     'description': 'Disable the animation when you sending an e-mail',
     'command_line': 'defaults write com.apple.mail DisableSendAnimations -bool true'
     },

    {'group': 'Safari',
     'description': 'Disable the standard delay in rendering a Web page.',
     'command_line': 'defaults write com.apple.Safari WebKitInitialTimedLayoutDelay 0.25'
     },

    {'group': 'general',
     'description': 'The keyboard react faster to keystrokes (not equally useful for everyone)',
     'command_line': 'defaults write NSGlobalDomain KeyRepeat -int 0'
     },

    {'group': 'general',
     'description': 'Disable smooth scrolling for paging (space bar)',
     'command_line': 'defaults write -g NSScrollAnimationEnabled -bool false'
     },

    {'group': 'Finder',
     'description': 'Avoid creating .DS_Store files on network volumes',
     'command_line': 'defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true'
     },

    {'group': 'Finder',
     'description': 'Avoid creating .DS_Store files on USB volumes',
     'command_line': 'defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true'
     },

    {'group': 'Finder',
     'description': 'Show the ~/Library folder',
     'command_line': 'chflags nohidden ~/Library'
     },

    {'group': 'Finder',
     'description': 'Save to disk (not to iCloud) by default',
     'command_line': 'defaults write NSGlobalDomain NSDocumentSaveNewDocumentsToCloud -bool false'
     },

    {'group': 'Finder',
     'description': 'Disable the warning when changing a file extension',
     'command_line': 'defaults write com.apple.finder FXEnableExtensionChangeWarning -bool false'
     },

    {'group': 'Finder',
     'description': 'Shows hidden files',
     'command_line': 'defaults write com.apple.finder AppleShowAllFiles -bool true'
     },

    {'group': 'Finder',
     'description': 'Always display file extensions (.jpg, .txt, .pdf, etc)',
     'command_line': 'defaults write NSGlobalDomain AppleShowAllExtensions -bool true'
     }
]
