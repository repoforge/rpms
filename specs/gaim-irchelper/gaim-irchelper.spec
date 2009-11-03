# $Id$
# Authority: dag

Summary: Gaim plugin to assist with IRC networks
Name: gaim-irchelper
Version: 0.12
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gaim-irchelper.sourceforge.net/

Source: http://dl.sf.net/gaim-irchelper/gaim-irchelper-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, glib2-devel, gaim-devel
Requires: gaim >= 1:1.2.0, gaim < 1:2.0.0

%description
IRC Helper is a plugin for Gaim which seeks to handle the rough
edges of the IRC protocol through network-specific code.

%prep
%setup

%build
%{__make} all

%install
%{__rm} -rf %{buildroot}
%makeinstall PLUGINDIR="%{buildroot}%{_libdir}/gaim/"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING COPYRIGHT IDEAS INSTALL PHILOSOPHY README
%dir %{_libdir}/gaim/
%{_libdir}/gaim/irchelper.so

%changelog
* Mon Mar 13 2006 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
