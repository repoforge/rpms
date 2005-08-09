# $Id$
# Authority: dag

%define logmsg logger -t %{name}/rpm

Summary: Local and remote filesystem snapshot utility
Name: rsnapshot
Version: 1.2.1
Release: 2
License: GPL
Group: Applications/System
URL: http://www.rsnapshot.org/

Source: http://www.rsnapshot.org/downloads/rsnapshot-%{version}.tar.gz
Patch: rsnapshot-1.2.1.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: rsync, openssh, autoconf, automake, openssh-clients
Requires: perl, rsync, openssh-clients

%description
rsnapshot is a remote backup program that uses rsync to take backup snapshots
of filesystems. rnsapshot uses hard links to save space on disk.

%prep
%setup 
%patch

%build
%configure \
	--with-perl="%{__perl}" \
	--with-rsync="%{_bindir}/rsync" \
	--with-ssh="%{_bindir}/ssh" \
	--with-logger="%{_bindir}/logger" \
	--with-du="%{_bindir}/du"

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__install} -Dp -m0755 rsnapshot %{buildroot}%{_bindir}/rsnapshot
%{__install} -Dp -m0644 rsnapshot.1 %{buildroot}%{_mandir}/man1/rsnapshot.1
%{__install} -Dp -m0644 rsnapshot.conf.default %{buildroot}%{_sysconfdir}/rsnapshot.conf

%post
VERSION="$(%{_bindir}/rsnapshot check-config-version &>/dev/null)"
if [ $1 -gt 0 ]; then
	%logmsg "Error upgrading %{_sysconfdir}/rsnapshot.conf."
fi

VERSION="$(%{_bindir}/rsnapshot check-config-version &>/dev/null)"
if [ "$VERSION" == "unknown" ]; then
	%{_bindir}/rsnapshot upgrade-config-file
	exit $?
fi

if [ "$VERSION" != "1.2" ]; then
	%logmsg "Error upgrading %{_sysconfdir}/rsnapshot.conf. Config format unknown!"
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc rsnapshot.conf.default utils/
%doc %{_mandir}/man1/rsnapshot.1*
%config %{_sysconfdir}/rsnapshot.conf
%{_bindir}/rsnapshot

%changelog
* Sat Aug 06 2005 Dag Wieers <dag@wieers.com> - 1.2.1-2
- Fixed bug in %post script. (John Hinton)

* Sat May 07 2005 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Initial package. (using DAR)
