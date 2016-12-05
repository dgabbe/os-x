#! /usr/bin/env bash

# Always show the full URL in the search/url field
defaults write  com.apple.Safari ShowFullURLInSmartSearchField true

# Disable shadow in screenshots
defaults write com.apple.screencapture disable-shadow -bool true

# Don’t show Dashboard as a Space
defaults write com.apple.dock dashboard-in-overlay -bool true

# Show file path in title of finder window
defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES

# Enable AirDrop feature for ethernet connected Macs
defaults write com.apple.NetworkBrowser BrowseAllInterfaces -bool true

# Show Recovery partition
defaults write com.apple.DiskUtility DUDebugMenuEnabled -bool true

