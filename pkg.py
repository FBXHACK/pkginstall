import subprocess

packages = ['python', 'python2', 'python2-dev', 'python3', 'java', 'fish', 'ruby', 'help', 'git', 'host', 'php', 'perl', 'nmap', 'bash', 'clang', 'nano', 'w3m', 'havij', 'hydra', 'figlet', 'cowsay', 'curl', 'tar', 'zip', 'unzip', 'tor', 'google', 'sudo', 'wget', 'wireshark', 'wgetrc', 'wcalc', 'bmon', 'vpn', 'unrar', 'toilet', 'proot', 'net-tools', 'golang', 'chroot', 'termux-chroot', 'macchanger', 'openssl', 'cmatrix', 'openssh', 'wireshark', 'termux-setup-storage']

for package in packages:
  subprocess.call(['pkg', 'install', package, '-y'])