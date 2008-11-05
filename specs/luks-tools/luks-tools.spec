# $Id$
# Authority: dag

Summary: Utilities for working with LUKS-protected filesystems
Name: luks-tools
Version: 0.0.12
Release: 1
License: GPL
Group: Applications/System
URL: http://www.flyn.org/

Source: http://www.flyn.org/projects/luks-tools/luks-tools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: check-devel
BuildRequires: cryptsetup-luks
BuildRequires: e2fsprogs-devel
BuildRequires: glib2-devel
Requires: dbus-python
Requires: pygtk2
Requires: python

%description
The luks-tools package contains various utilities for working with 
LUKS-protected filesystems. HAL uses these utilities to automatically 
mount encrypted volumes when they are attached to a system, provided 
the user can produce the correct passphrase. These utilities are 
written as separate programs to allow MAC systems like SELinux to 
have fine-grained control over them.

It contains luks-format, luks-is-encrypted, luks-setup and gnome-luks-format.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README FAQ
%doc %{_mandir}/man1/gnome-luks-format.1*
%doc %{_mandir}/man1/luks-format.1*
%doc %{_mandir}/man1/luks-is-encrypted.1*
%doc %{_mandir}/man1/luks-setup.1*
%doc %{_mandir}/man1/luks-tools.1*
%{_sysconfdir}/pam.d/gnome-luks-format
%{_sysconfdir}/security/console.apps/gnome-luks-format
%{_bindir}/gnome-luks-format
%{_datadir}/luks-tools/
%{_sbindir}/luks-format
%{_sbindir}/luks-is-encrypted
%{_sbindir}/luks-setup

%changelog
* Wed Nov 05 2008 Dag Wieers <dag@wieers.com> - 0.0.12-1
- Initial package. (using DAR)
