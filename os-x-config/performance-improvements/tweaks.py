#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# Definition of OS X/MacOS tweaks
# group, description, command, os_v_min, os_ver_max

tweaks = [
  {'group': 'test',
   'description': 'Test exception handling',
   'command': "foobar",
   'os_v_min': '10.09', 'os_v_max': None
   },
  {'group': 'animation',
   'description': 'Disable animations when opening and closing windows.',
   'command': "defaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false",
   'os_v_min': '10.09', 'os_v_max': None
   },
  {'group': 'animation',
   'description': 'Disable animations when opening a Quick Look window.',
   'command': "defaults write -g QLPanelAnimationDuration -float 0",
   'os_v_min': '10.09', 'os_v_max': None
   },
  {'group': 'animation',
   'description': 'Disable animation when opening the Info window in OS X Finder (cmd⌘ + i).',
   'command': 'defaults write com.apple.finder DisableAllAnimations -bool true',
   'os_v_min': '10.09', 'os_v_max': None
   },
  {'group': 'animation',
   'description': 'Accelerated playback when adjusting the window size (Cocoa applications).',
   'command': 'defaults write NSGlobalDomain NSWindowResizeTime -float 0.001',
   'os_v_min': '10.09', 'os_v_max': None
   },
  {'group': 'animation',
   'description': 'Disable animations when you open an application from the Dock.',
   'command': 'defaults write com.apple.dock launchanim -bool false',
   'os_v_min': '10.09', 'os_v_max': None
   }
]
