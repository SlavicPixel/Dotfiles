#   ██████  ██▓    ▄▄▄    ██▒   █▓ ██▓ ▄████▄      ██▓███   ██▓▒██   ██▒▓█████  ██▓    
# ▒██    ▒ ▓██▒   ▒████▄ ▓██░   █▒▓██▒▒██▀ ▀█     ▓██░  ██▒▓██▒▒▒ █ █ ▒░▓█   ▀ ▓██▒    
# ░ ▓██▄   ▒██░   ▒██  ▀█▄▓██  █▒░▒██▒▒▓█    ▄    ▓██░ ██▓▒▒██▒░░  █   ░▒███   ▒██░    
#   ▒   ██▒▒██░   ░██▄▄▄▄██▒██ █░░░██░▒▓▓▄ ▄██▒   ▒██▄█▓▒ ▒░██░ ░ █ █ ▒ ▒▓█  ▄ ▒██░    
# ▒██████▒▒░██████▒▓█   ▓██▒▒▀█░  ░██░▒ ▓███▀ ░   ▒██▒ ░  ░░██░▒██▒ ▒██▒░▒████▒░██████▒
# ▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░░ ▐░  ░▓  ░ ░▒ ▒  ░   ▒▓▒░ ░  ░░▓  ▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒░▓  ░
# ░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ▒ ░  ░  ▒      ░▒ ░      ▒ ░░░   ░▒ ░ ░ ░  ░░ ░ ▒  ░
# ░  ░  ░    ░ ░    ░   ▒     ░░   ▒ ░░           ░░        ▒ ░ ░    ░     ░     ░ ░   
#       ░      ░  ░     ░  ░   ░   ░  ░ ░                   ░   ░    ░     ░  ░    ░  ░
#                             ░       ░                                                

import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401
from libqtile.widget import Spacer
from libqtile.utils import guess_terminal
from nic import get_nic_name
from datetime import datetime

mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')
terminal = guess_terminal()
myTerm="alacritty"
interface_name = get_nic_name() # set get_nic_name('wired') if using a wired connection
current_year = datetime.now().year

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [

# SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "x", lazy.spawn('archlinux-logout')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn(myTerm)),

# SUPER + SHIFT KEYS

    Key([mod, "shift"], "Return", lazy.spawn('thunar')),
    #Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -l 20 -h 38 -fn 'UbuntuMono:bold:pixelsize=22'")),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),

# CONTROL + ALT KEYS

    # Key(["mod1", "control"], "e", lazy.spawn('arcolinux-tweak-tool')),
    Key(["mod1", "control"], "e", lazy.spawn("emacsclient -c -a 'emacs'")),
    Key(["mod1", "control"], "f", lazy.spawn('firefox')),
    Key(["mod1", "control"], "c", lazy.spawn('vscodium')),
    Key(["mod1", "control"], "p", lazy.spawn('pavucontrol')),
    Key(["mod1", "control"], "v", lazy.spawn('virt-manager')),
    Key(["mod1", "control"], "b", lazy.spawn('brave')),
    Key(["mod1", "control"], "s", lazy.spawn('steam')),
    Key(["mod1", "control"], "t", lazy.spawn('thunderbird')),
    Key(["mod1", "control"], "q", lazy.spawn('qbittorrent')), # SEED YOUR LINUX ISOs

# SCREENSHOTS

    #Key([], "Print", lazy.spawn("scrot 'ArcoLinux-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key([], "Print", lazy.spawn('xfce4-screenshooter')),
    Key([mod], "Print", lazy.spawn('thunar /home/pixel/Pictures/Screenshots')),

# MULTIMEDIA KEYS
    Key([], "XF86Calculator", lazy.spawn("qalculate-gtk")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    # Key([mod, "comma"], lazy.to_screen(0), desc='Next monitor'),
    # Key([mod, "period"], lazy.to_screen(1), desc='Next monitor'),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

group_names = [("1  ", {'layout': 'monadtall'}),
               ("2 ", {'layout': 'monadtall', 'matches':[Match(wm_class='qbittorrent')]}),
               ("3 ", {'layout': 'monadtall'}),
               ("4 ", {'layout': 'monadtall'}),
               ("5 ", {'layout': 'monadtall'}),
               ("6 ", {'layout': 'monadtall'}),
               ("7 ", {'layout': 'monadtall'}),
               ("8 λ", {'layout': 'monadtall', 'matches':[Match(wm_class='origin.exe')]}),
               ("9 ", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group


layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330",
                "single_border_width": 0
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.TreeTab(
    #      font = "Ubuntu",
    #      fontsize = 10,
    #      sections = ["FIRST", "SECOND"],
    #      section_fontsize = 11,
    #      bg_color = "141414",
    #      active_bg = "90C435",
    #      active_fg = "000000",
    #      inactive_bg = "384323",
    #      inactive_fg = "a0a0a0",
    #      padding_y = 5,
    #      section_top = 10,
    #      panel_width = 320
    #      ),
    layout.Floating(**layout_theme)
]

colors = [["#282a36", "#282a36"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#808080", "#808080"]] # vertical line color

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize = 17,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
             widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/tux.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
                       background = colors[0]
                       ),
             widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[7],
                       fontsize = 20
                       ),
             widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "FiraCode Nerd Font",
                       fontsize = 16,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = "#ff71ce",
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[0],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1],
                       fontsize = 16
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[7],
                       fontsize = 20
                       ),
              widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "⟳{updates} Updates",
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       background = colors[0]
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[7],
                       fontsize = 20
                       ),
              widget.CPU(
                       format = ' cpu: {load_percent}% {freq_current}GHz',
                       foreground = '#01cdfe',
                       background = colors[0]
              ),
              widget.ThermalSensor(
                       foreground = '#01cdfe',
                       background = colors[0],
                       threshold = 90,
                       padding = 5,
                       tag_sensor = "Package id 0"
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[7],
                       fontsize = 20
                       ),
              widget.TextBox(
                       text = " 🌡",
                       padding = 2,
                       foreground = '#05ffa1',
                       background = colors[0],
                       fontsize = 16
                       ),
              widget.NvidiaSensors(
                      foreground = '#05ffa1',
                      background = colors[0],
                      format = 'gpu: {temp}°C'
                      ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[7],
                       fontsize = 20
                       ),
              widget.Memory(
                       foreground = '#ff6c6b',
                       background = colors[0],
                       format = '\uf233 {MemUsed: .0f}M/{MemTotal: .0f}M',
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[7],
                       fontsize = 20
                       ),
             widget.Net(
                       interface = interface_name,
                       format = '\uf0ab {down}  \uf0aa {up}',
                       foreground = '#fffb96',
                       background = colors[0],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[7],
                       fontsize = 20
                       ),
               widget.TextBox(
                       text="",
                       foreground='#ff71ce',
                       background=colors[0],
                       font="Font Awesome 6 Free Solid",
                       # fontsize=38,
                       ),
              widget.Volume(
                       #foreground = '#828CF6',
                       foreground='#ff71ce',
                       background = colors[0],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[7],
                       fontsize = 20
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = '#c678dd',
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = '#c678dd',
                       background = colors[0],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[7],
                       fontsize = 20
                       ),
              widget.TextBox(
                       text="",
                       # text="\uF551",
                       foreground='#46d9ff',
                       background=colors[0],
                       font="Font Awesome 6 Free Solid",
                       # fontsize=38,
                       ),
              widget.Clock(
                       foreground = '#46d9ff',
                       background = colors[0],
                       format = "%A, %B %d - %H:%M:%S",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + f" --hold -e cal {current_year}")}
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[7],
                       fontsize = 20
                       ),
               widget.Systray(
                        background = colors[0],
                        icon_size=21,
                        padding = 4
                        ),
              widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[10:12]
    del widgets_screen2[29:31]
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))]
screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
  *layout.Floating.default_float_rules,
  Match(wm_class='Arcolinux-welcome-app.py'),
  Match(wm_class='Arcolinux-tweak-tool.py'),
  Match(wm_class='confirm'),
  Match(wm_class='dialog'),
  Match(wm_class='download'),
  Match(wm_class='error'),
  Match(wm_class='file_progress'),
  Match(wm_class='notification'),
  Match(wm_class='splash'),
  Match(wm_class='toolbar'),
  Match(wm_class='confirmreset'),
  Match(wm_class='makebranch'),
  Match(wm_class='maketag'),
  Match(wm_class='Arandr'),
  Match(wm_class='feh'),
  Match(wm_class='Galculator'),
  Match(wm_class='arcolinux-logout'),
  Match(wm_class='xfce4-terminal'),
  Match(wm_class='ssh-askpass'),
  Match(wm_class='mullvad vpn'),
  Match(wm_class='origin.exe'),
  Match(wm_class='Origin.exe'),
  Match(title='branchdialog'),
  Match(title='Open File'),
  Match(title='pinentry'),
  Match(title='Qalculate!'),
  Match(title='Connman System Tray'),

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
