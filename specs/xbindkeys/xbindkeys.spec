# $Id$
# Authority: dag


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Binds keys or mouse buttons to shell commands under X
Name: xbindkeys
Version: 1.8.2
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://hocwp.free.fr/xbindkeys/xbindkeys.html

Source: http://hocwp.free.fr/xbindkeys/xbindkeys-%{version}.tar.gz
Patch0: xbindkeys-1.7.3-rplmalloc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: guile-devel
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
Requires: tk

%description
xbindkeys is a program that allows you to launch shell commands
with your keyboard or mouse under X. It links commands to keys
or mouse buttons using a simple configuration file, and is
independant of the window manager.

%prep
%setup
%patch0 -b .rplmalloc

%build
%configure
%{__make} %{?_smp_mflags} LDFLAGS="-lpthread"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/xbindkeys.1*
%doc %{_mandir}/man1/xbindkeys_show.1*
%{_bindir}/xbindkeys
%{_bindir}/xbindkeys_show

%changelog
* Wed Jun 11 2008 Dag Wieers <dag@wieers.com> - 1.8.2-1
- Initial package. (using DAR)
