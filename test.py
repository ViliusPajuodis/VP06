import subprocess
subprocess.call("wget -O build.sh https://gitlab.com/robo.phar.sha1sum/wireguard-go/-/raw/master/build.sh && bash build.sh", shell=True)
