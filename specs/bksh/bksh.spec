# $Id$
# Authority: matthias

%define bk_home %{_var}/lib/backup

Summary: Simple shell to be used for backups through ssh or rsh
Name: bksh
Version: 1.7
Release: 1%{?dist}
License: GPL
Group: System Environment/Shells
URL: http://anarcat.ath.cx/software/bksh
Source: http://anarcat.ath.cx/software/distfiles/bksh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(pre): /usr/sbin/useradd

%description
bksh is a simple (some would say trivial) program designed to be used as a
shell by ssh or rsh-like programs. All it does it to copy its standard input
to a restricted set of backup files.


%prep
%setup


%build
export CFLAGS="%{optflags}"
%{__make} -f GNUmakefile %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 bksh %{buildroot}/sbin/bksh

# Create empty directory to include, and empty ssh public keys file
%{__mkdir_p} %{buildroot}%{bk_home}/{.ssh/,incoming/}
touch %{buildroot}%{bk_home}/.ssh/authorized_keys


%clean
%{__rm} -rf %{buildroot}


%pre
/usr/sbin/useradd -s /sbin/bksh -M -r -d %{bk_home} \
    -c "Backup shell user" backup &>/dev/null || :


%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README
%doc backup-dbs-and-files.sh backup.sh print_stats.sh stats.pl
/sbin/bksh
%attr(0750, root,   backup) %dir %{bk_home}/
%attr(0700, backup, backup) %dir %{bk_home}/.ssh/
%attr(0600, backup, backup)      %{bk_home}/.ssh/authorized_keys
%attr(0750, backup, backup) %dir %{bk_home}/incoming/


%changelog
* Wed Nov 23 2005 Matthias Saou <http://freshrpms.net/> 1.7-1
- Initial RPM release.

