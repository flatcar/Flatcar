# CIS review

## Level 1

### Level 1 benchmark feedback

* 1.1.1.1   - cramfs: is not disabled, because it is not even provided
* 1.1.1.2   - freevxfs: is not disabled, because it is not even provided
* 1.1.1.3   - jffs2: is not disabled, because it is not even provided
* 1.1.1.4   - hfs: is not disabled, because it is not even provided
* 1.1.1.5   - hfsplus: is not disabled, because it is not even provided
* 1.1.1.6   - squashfs: we provide hardening to remediate
* 1.1.1.7   - udf: we provide hardening to remediate
* 1.1.5     - /tmp "noexec": remediation provided
* 1.1.17    - /dev/shm "noexec": remediation provided
* 1.1.23    - usb_storage: we provide hardening to remediate
* 1.3.1     - aide: available to be run in a container (even the system `toolbox`)
* 1.3.2     - scheduled aide checks: available through container
* 1.4.1     - grub config is stored in the cryptographically immutable /usr partition (/usr/boot/syslinux/root.A.cfg and /usr/boot/syslinux/root.B.cfg), though it is readable 0644.
* 1.4.2     - grub password: remediation provided
* 1.4.3     - root password: remediation provided (/etc/inittab nor /etc/sysconfig/init will exist or matter)
* 1.4.4     - core dump restriction: remediation provided
* 1.7.1.6   - /etc/issue.net does not exist
* 2.2.1.2   - ntpd: is ready, but not enabled by default. And will run as non-root user "ntp"
* 3.1.1     - sysctl ip_forward: remediation provided
* 3.1.2     - sysctl send_redirects: remediation provided
* 3.2.2     - sysctl accept_redirects: remediation provided
* 3.2.3     - sysctl secure_redirects: remediation provided
* 3.2.4     - sysctl log_martians: remediation provided
* 3.2.9     - sysctl accept_ra: remediation provided
* 3.3.1     - tcp_wrappers (libwrap0): this package is not provided, as it only works for TCP traffic, and unless an application links to libwrap, then the /etc/hosts.{allow,deny} do not apply anyways. Modern applications require iptables, nftables, ipset, and/or BPF rules for network policy.
* 3.3.2     - see 3.3.1 answer
* 3.3.3     - see 3.3.1 answer
* 3.3.4     - see 3.3.1 answer
* 3.3.5     - see 3.3.1 answer
* 3.5.1.1   - ip6tables: our default policy is clean slate. remediation provided.
* 3.5.1.2   - ip6tables: remediation provided
* 3.5.1.3   - ip6tables: remediation provided
* 3.5.1.4   - ip6tables ports: remediation provided
* 3.5.2.1   - iptables: remediation provided
* 3.5.2.2   - iptables: remediation provided
* 3.5.2.3   - iptables: remediation provided
* 3.5.2.4   - iptables: remediation provided
* 4.2.1.2   - rsyslog: available via container
* 4.2.1.3   - rsyslog: remediation provided
* 4.2.1.4   - rsyslog: remediation provided
* 4.2.1.5   - rsyslog: remediation provided
* 4.2.2.1   - journald to syslog: remediation provided
* 4.2.3     - log permissions (faillog and btmp): remediation provided
* 5.1.1     - cron: this is not provided. Use systemd.timer instead
* 5.1.2     - cron: this is not provided. Use systemd.timer instead
* 5.1.3     - cron: this is not provided. Use systemd.timer instead
* 5.1.4     - cron: this is not provided. Use systemd.timer instead
* 5.1.5     - cron: this is not provided. Use systemd.timer instead
* 5.1.6     - cron: this is not provided. Use systemd.timer instead
* 5.1.7     - cron: this is not provided. Use systemd.timer instead
* 5.1.8     - cron.allow/cron.deny: concept does not translate to systemd.timer
* 5.2.4     - sshd protocol: 2 has been the default, and the field is a noop
* 5.2.5     - sshd: remediation provided
* 5.2.6     - sshd: remediation provided
* 5.2.7     - sshd: remediation provided
* 5.2.8     - sshd: remediation provided
* 5.2.9     - sshd: remediation provided
* 5.2.10    - sshd: remediation provided
* 5.2.11    - sshd: remediation provided
* 5.2.12    - sshd: remediation provided
* 5.2.13    - sshd: remediation provided
* 5.2.14    - sshd: remediation provided
* 5.2.15    - sshd: remediation provided
* 5.2.16    - sshd: remediation provided
* 5.2.17    - sshd: remediation provided
* 5.2.18    - sshd: remediation provided
* 5.2.19    - sshd: remediation provided
* 5.2.22    - sshd: remediation provided
* 5.2.23    - sshd: remediation provided
* 5.3.3     - pam: TODO testing needed, as /usr/lib64/pam.d/ is readonly
* 5.3.4     - pam: TODO testing needed, as /usr/lib64/pam.d/ is readonly
* 5.4.1.1   - login.defs: remediation provided
* 5.4.1.2   - login.defs: remediation provided
* 5.4.1.4   - useradd: remediation provided
* 5.4.2     - system accounts: TODO not sure about making "core" as a UID >=1000 and `/sbin/nologin` for all other accounts
* 5.4.4     - umask: remediation provided
* 5.6       - su: su is unusable by any user but root by default (/usr/lib64/pam.d/su is the location)
* 6.1.6     - /etc/passwd- permission: remediation provided
* 6.1.11    - unowned files (UID): the config filesystem (i.e. cloud-init, or qemu config) are UID 1000, which is not mapped. Also, this is largely irrelevant for UIDs that are not mapped by the host, as this is a container host, and files on the disk will be owned the full range of the 128 bit integer UIDs.
* 6.1.12    - unowned files (GID): see 6.1.11 explanation
* 6.2.15    - accounted for groups: TODO determine why this 236 GID is there (it's not in the qemu image)

### Level 1 hardening notes

* /etc/modprobe.d/blacklist-1.1.1.conf to blacklist modules

```shell
blacklist cramfs
blacklist freevxfs
blacklist jffs2
blacklist hfs
blacklist hfsplus
blacklist squashfs
blacklist udf
```

* /tmp with "noexec"

```ini
# /etc/systemd/system/tmp.mount.d/noexec.conf
[Mount]
Options=mode=1777,strictatime,nosuid,nodev,size=50%,nr_inodes=400k,noexec
```

* /dev/shm with "noexec" (could figure this out in a systemd drop-in...)

```shell
echo "none /dev/shm tmpfs rw,nosuid,nodev,seclabel,noexec 0 0" >> /etc/fstab
```

* /etc/modprobe.d/blacklist-1.1.23.conf to blacklist modules

```shell
blacklist usb_storage
```

* install aide (NOTE: this will require an updated toolbox:/etc/aide.conf for looking into /media/root/)

```shell
toolbox
dnf install -y aide
aide --init
mv /var/lib/aide/aide.db{.new,}.gz
aide --check
```

* check with aide (NOTE: see prior)

```shell
toolbox aide --check
```

* grub/menu.list permissions:

```shell
chmod 0600 /boot/boot/grub/menu.lst
# BUG permissions are 0755, and the chmod does not persist on reboot...
# https://github.com/kinvolk/Flatcar/issues/296
```

* grub password: /usr/share/oem/grub.cfg

```shell
set superusers="user1"
password user1 password1
```

* root password: `passwd` to set a root password; or hash in cloud-init/ignition
* core dump restriction:

```shell
# /etc/security/limits.d/restrict.conf
*               hard    core          0
```

* sysctl (currently there is a bug for persistence of these settings https://github.com/kinvolk/Flatcar/issues/297)
  * IP forwarding

```sysclt
# /etc/sysctl.d/forward.conf
net.ipv4.ip_forward=0
```

  * send_redirects; accept_redirects; secure_redirects

```sysctl
# /etc/sysctl.d/redirects.conf
net.ipv4.conf.all.send_redirects=0
net.ipv4.conf.default.send_redirects=0
net.ipv4.conf.default.accept_redirects=0
net.ipv6.conf.all.accept_redirects=0
net.ipv6.conf.default.accept_redirects=0
net.ipv4.conf.all.secure_redirect=0
net.ipv4.conf.default.secure_redirects=0
```

  * log_martians

```sysctl
# /etc/sysctl.d/martians.conf
net.ipv4.conf.all.log_martians=1
net.ipv4.conf.default.log_martians=1
```

  * accept_ra (router advertisements)

```sysctl
net.ipv6.conf.all.accept_ra=0
net.ipv6.conf.default.accept_ra=0
```

  * lastly, after all that;

```shell
sysctl --system
# OR
systemctl restart systemd-sysctl # this ought to pick this up on reboot...
```

* ip6tables

```shell
ip6tables -P INPUT DROP
ip6tables -P OUTPUT DROP
ip6tables -P FORWARD DROP
ip6tables -I INPUT 1 -i lo -j ACCEPT
ip6tables -I FORWARD 1 -i lo -j ACCEPT # needs to be validated
ip6tables -I FORWARD 2 -o lo -j ACCEPT # needs to be validated
ip6tables -I FORWARD 3 -i lo -o lo -j ACCEPT # needs to be validated
ip6tables -I OUTPUT 1 -o lo -j ACCEPT
ip6tables -A INPUT -s ::1 -j DROP
ip6tables -A OUTPUT -p tcp -m state --state NEW,ESTABLISHED -j ACCEPT
ip6tables -A INPUT -p tcp -m state --state NEW,ESTABLISHED -j ACCEPT
ip6tables -A INPUT -p tcp -m state --state ESTABLISHED -j ACCEPT
ip6tables -A OUTPUT -p udp -m state --state NEW,ESTABLISHED -j ACCEPT
ip6tables -A INPUT -p udp -m state --state NEW,ESTABLISHED -j ACCEPT
ip6tables -A INPUT -p udp -m state --state ESTABLISHED -j ACCEPT
ip6tables -A OUTPUT -p icmp -m state --state NEW,ESTABLISHED -j ACCEPT
ip6tables -A INPUT -p icmp -m state --state NEW,ESTABLISHED -j ACCEPT
ip6tables -A INPUT -p icmp -m state --state ESTABLISHED -j ACCEPT
ip6tables -A INPUT -p udp --dport 68 -j ACCEPT
ip6tables -A INPUT -p tcp --dport 22 -j ACCEPT

# Persist with something like (which may screw up container networking tools):
systemctl enable --now ip6tables-store.service ip6tables-restore.service
```

* iptables:

```shell
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP
iptables -I INPUT 1 -i lo -j ACCEPT
iptables -I FORWARD 1 -i lo -j ACCEPT # needs to be validated
iptables -I FORWARD 2 -o lo -j ACCEPT # needs to be validated
iptables -I FORWARD 3 -i lo -o lo -j ACCEPT # needs to be validated
iptables -I OUTPUT 1 -o lo -j ACCEPT
iptables -A INPUT -s 127.0.0.0/8 -j DROP
iptables -A OUTPUT -p tcp -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp -m state --state ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p udp -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p udp -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p udp -m state --state ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p icmp -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p icmp -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p icmp -m state --state ESTABLISHED -j ACCEPT
iptables -A INPUT -p udp --dport 68 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Persist with something like (which may screw up container networking tools):
systemctl enable --now iptables-store.service iptables-restore.service
```

* rsyslog, configured like a host service

```Dockerfile
# https://github.com/voxxit/dockerfiles/blob/master/rsyslog/Dockerfile

FROM alpine:latest

#FROM voxxit/base:alpine
#MAINTAINER Joshua Delsman <j (at) srv.im>

RUN  apk add --update rsyslog \
  && rm -rf /var/cache/apk/*

EXPOSE 514 514/udp

VOLUME [ "/var/log", "/etc/rsyslog.d" ]

# for some reason, the apk comes built with a v5
# config file. using this one for v8:
COPY ./etc/rsyslog.conf /etc/rsyslog.conf

ENTRYPOINT [ "rsyslogd", "-n" ]
```

```rsyslog
# rsyslog.conf
#
# if you experience problems, check:
# http://www.rsyslog.com/troubleshoot

$FileCreateMode 0640

#### MODULES ####

module(load="imuxsock")    # local system logging support (e.g. via logger command)
#module(load="imklog")     # kernel logging support (previously done by rklogd)
module(load="immark")      # --MARK-- message support
module(load="imudp")       # UDP listener support
module(load="imtcp")       # TCP listener support

input(type="imudp" port="514")
input(type="imtcp" port="514")

# Log all kernel messages to the console.
# Logging much else clutters up the screen.
kern.*                                                 action(type="omfile" file="/dev/console")

# Log anything (except mail) of level info or higher.
# Don't log private authentication messages!
*.info;mail.none;authpriv.none;cron.none                action(type="omfile" file="/var/log/messages")

# The authpriv file has restricted access.
authpriv.*                                              action(type="omfile" file="/var/log/secure")

# Log all the mail messages in one place.
mail.*                                                  action(type="omfile" file="/var/log/maillog")

# Log cron stuff
cron.*                                                  action(type="omfile" file="/var/log/cron")

# Everybody gets emergency messages
*.emerg                                                 action(type="omusrmsg" users="*")

# Save news errors of level crit and higher in a special file.
uucp,news.crit                                          action(type="omfile" file="/var/log/spooler")

# Save boot messages also to boot.log
local7.*                                                action(type="omfile" file="/var/log/boot.log")

#*.*          @@loghost.example.com

# Include all .conf files in /etc/rsyslog.d
$IncludeConfig /etc/rsyslog.d/*.conf
```

```shell
docker run -it --rm --entrypoint="" rsyslog cat /etc/rsyslog.conf > /etc/rsyslog.conf
docker run -d -it --name rsyslog --restart=always --env TZ=UTC --cap-add SYSLOG -v /etc/rsyslog.conf:/etc/rsyslog.conf -v /var/log/:/var/log -v /etc/rsyslog.d:/etc/rsyslog.d -p 514:514/udp -p 514:514 rsyslog
```

* journald

```shell
sed -i 's/^#*ForwardToSyslog=.*$/ForwardToSyslog=yes/' /etc/systemd/journald.conf
sed -i 's/^#*Compress=.*$/Compress=yes/' /etc/systemd/journald.conf
sed -i 's/^#*Storage=.*$/Storage=persistent/' /etc/systemd/journald.conf
systemctl restart systemd-journald
```

* permissions of faillog and btmp

```shell
chmod 0600 /var/log/faillog
chmod 0600 /var/log/btmp

# if they're wanting to be sure, then make a systemd unit that sets it on boot
```

* sshd configs

```shell
cat /etc/ssh/sshd_config > /tmp/sshd_config
rm /etc/ssh/sshd_config
mv /tmp/sshd_config
chmod 0600 /etc/ssh/sshd_config

# maybe sed -i 'd/...' to clean the file first?
echo "Protocol 2" >> /etc/ssh/sshd_config
echo "LogLevel VERBOSE" >> /etc/ssh/sshd_config
echo "X11Forwarding no" >> /etc/ssh/sshd_config
echo "MaxAuthTries 4" >> /etc/ssh/sshd_config
echo "IgnoreRhosts yes" >> /etc/ssh/sshd_config
echo "HostbasedAuthentication no" >> /etc/ssh/sshd_config
echo "PermitRootLogin no" >> /etc/ssh/sshd_config
echo "PermitEmptyPasswords no" >> /etc/ssh/sshd_config
echo "PermitUserEnvironment no" >> /etc/ssh/sshd_config
echo "Ciphers chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr,aes128-gcm@openssh.com,aes256-gcm@openssh.com" >> /etc/ssh/sshd_config
echo "MACs hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512,umac-128-etm@openssh.com,umac-128@openssh.com" >> /etc/ssh/sshd_config
echo "KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256" >> /etc/ssh/sshd_config
echo "ClientAliveCountMax 0" >> /etc/ssh/sshd_config
echo "LoginGraceTime 60" >> /etc/ssh/sshd_config
echo "AllowGroups core" >> /etc/ssh/sshd_config
cat > /etc/ssh/banner.txt <<EOF
 ____________________________________
< This machine is under surveillance >
 ------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
EOF
echo "Banner /etc/ssh/banner.txt" >> /etc/ssh/sshd_config
echo "MaxStartups 10:30:60" >> /etc/ssh/sshd_config
echo "MaxSessions 4" >> /etc/ssh/sshd_config

systemctl restart sshd.service
```

* pam

```shell
```

* login.defs

```shell
cat /etc/login.defs > /tmp/login.defs
rm /etc/login.defs
mv /tmp/login.defs /etc/login.defs
chmod 0644 /etc/login.defs

sed -i 's/^PASS_MAX_DAYS.*$/PASS_MAX_DAYS  365/' /etc/login.defs
sed -i 's/^PASS_MIN_DAYS.*$/PASS_MIN_DAYS  7/' /etc/login.defs
```

* useradd defaults

```shell
cat /etc/default/useradd > /tmp/useradd
rm /etc/default/useradd
mv /tmp/useradd /etc/default/useradd
chmod 0644 /etc/default/useradd

sed -i 's/^INACTIVE.*$/INACTIVE=30/' /etc/default/useradd
```

* umask for logins

```shell
cat /etc/profile > /tmp/profile
rm /etc/profile
mv /tmp/profile /etc/profile
chmod 0644 /etc/profile

sed -i 's/^umask.*$/umask 027/' /etc/profile
```

* passwd- permission

```shell
chmod 0600 /etc/passwd-
```
