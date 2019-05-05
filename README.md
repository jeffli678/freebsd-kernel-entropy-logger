# freebsd-kernel-entropy-logger
Slightly modify the freebsd kernel to output the entropy source information using printf. User space program can retrieve this information using dmesg. 

This is based on FreeBSD 12.0. See https://www.vultr.com/docs/how-to-build-and-install-a-custom-kernel-on-freebsd-11 for FreeBSD kernel build instructions. 

1. Edits are in freebsd/sys/dev/random/hash.c and hash.h. 

2. Use kern.msgbufsize="128M" in /boot/loader.conf to enlarge the kernel buffer size. No kernel rebuild required. 

3. log1.txt is dumped using "dmesg >> log1.txt".

4. convert.py converts it to a format that can be processed by the neural network. split-data.py splits them into 10 folds.
