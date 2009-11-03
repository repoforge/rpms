# $Id$
# Authority: dag

Summary: Gaim plugin to forward messages.
Name: gaim-assistant
Version: 0.1.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gaim-assistant.tulg.org/

Source: http://dl.sf.net/gaim-assistant/gaim-assistant-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gaim-devel
Requires: gaim >= 0.82

%description
GAIM Assistant is a plugin to GAIM that will allow you to forward messages
to a different screen name should you become away. It's quite handy for
those of you out there that use AIM over mobile devices as well as at home.

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
%doc AUTHORS CHANGELOG COPYING README TODO
%{_libdir}/gaim/gaim-assistant.so

%changelog
* Mon Mar 20 2006 Dag Wieers <dag@wieers.com> - 0.1.0-1
- Initial package. (using DAR)
