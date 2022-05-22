#!/usr/bin/env python3
"""
Errors
20220123
"""
import os,sys,pwd,stat,platform

os.system("cls" if os.name=="nt" else "clear")


if __name__ == "__main__":
	if os.name == "posix":
		target = platform.machine()
		if target in ('aarch64', 'armv8l', 'arm64'):
			target = 'aarch64'
		bins_path = "local/bin/{}/".format(target)
		username = pwd.getpwuid(os.getuid()).pw_name
		myUsersId = pwd.getpwnam(username).pw_uid
		myGroupId = pwd.getpwnam(username).pw_gid

		if os.access(bins_path, os.F_OK):
			if os.geteuid():
				args = [sys.executable] + sys.argv
				os.execlp('sudo', 'sudo', *args)
			if not os.access("{}mke2fs".format(bins_path), os.X_OK):
				print(myUsersId, myGroupId)
				os.chmod(bins_path, 0o777)
				os.chown(bins_path, myUsersId, myGroupId)
				os.system("chmod -R 777 {}*".format(bins_path))
			# 启动脚本
			if os.path.isfile("./{}dna".format(bins_path)):
				os.system("./{}dna {}".format(bins_path, username))
			else:
				sys.exit('Not found bin: dna')
		else:
			sys.exit('Invalid bin: {}'.format(platform.machine()))
	else:
		sys.exit('Invalid OS: {}'.format(os.name))