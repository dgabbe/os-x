#! /usr/bin/env bash

# Always show the full URL in the search/url field
defaults write  com.apple.Safari ShowFullURLInSmartSearchField -bool true

# Disable shadow in screenshots
defaults write com.apple.screencapture disable-shadow -bool true

# Don’t show Dashboard as a Space
defaults write com.apple.dock dashboard-in-overlay -bool true

# Show file path in title of finder window
defaults write com.apple.finder _FXShowPosixPathInTitle -bool true

# Enable AirDrop feature for ethernet connected Macs
defaults write com.apple.NetworkBrowser BrowseAllInterfaces -bool true

# Show Recovery partition & EFI Boot partition
defaults write com.apple.DiskUtility DUDebugMenuEnabled -bool true

# Always show scroll bars
defaults write NSGlobalDomain AppleShowScrollBars -string "Always"

# Expand Save panel by default
defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode -bool true
defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode2 -bool true

# Expand Print menu by default
defaults write NSGlobalDomain PMPrintingExpandedStateforPrint -bool true
defaults write NSGlobalDomain PMPrintingExpandedStateforPrint2 -bool true


