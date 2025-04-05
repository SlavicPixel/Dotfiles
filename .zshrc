ZSH=/usr/share/oh-my-zsh/
export SSH_AUTH_SOCK=$XDG_RUNTIME_DIR/gcr/ssh 
# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

plugins=(
	git
	zsh-autosuggestions
	zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh

# zsh edit or update
alias zshedit='nvim ~/.zshrc'
alias zshup='source ~/.zshrc'
alias zshgit='cp ~/.zshrc ~/Dotfiles/.zshrc'

# navigation
alias ..='cd ..'
alias ...='cd ../..'

# list files
alias ls="lsd -l"
alias lss="lsd -la"

# vim & emacs
alias vim="nvim"
alias svim="sudo nvim"

# the terminal rickroll
alias rr='curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash'

# pacman
alias pacsyu='sudo pacman -Syu'
alias pacsyyu='sudo pacman -Syyu'
alias pacs='sudo pacman -S'
alias pacr='sudo pacman -R'
alias paconfig='sudo vim /etc/pacman.conf'

# shutdown or reboot 
alias ssn="sudo shutdown now"
alias sr="sudo reboot"

# git config
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

# yay
alias yays='yay -S'
alias yaysyu='yay -Syu'

# fan speed control
alias fsl='sudo fsload'
alias fsi='sudo fsidle'

# picom
alias pik='killall picom'
alias pis='picom --config $HOME/.config/picom/picom.conf & disown'

# turn off external drive
alias driveoff='udisksctl power-off -b'

# yt-dlp
alias ytd='yt-dlp'

# xrandr
alias mon='xrandr --output DP-0 --auto --left-of DP-2'
alias moff='xrandr --output DP-0 --off'

neofetch
colorscript random

eval "$(starship init zsh)"
