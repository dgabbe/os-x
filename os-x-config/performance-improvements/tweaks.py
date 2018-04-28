#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# Definition of OS X/MacOS tweaks
# group, description, command, os_v_min, os_ver_max

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
   }
]
