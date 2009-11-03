# $Id$
# Authority: dag

Summary: Security and Privacy plugin for Pidgin
Name: pidgin-privacy-please
Version: 0.5.3
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://code.google.com/p/pidgin-privacy-please/

Source: http://pidgin-privacy-please.googlecode.com/files/pidgin-privacy-please-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pidgin-devel
Requires: pidgin

%description
pidgin-privacy-please is a pidgin plugin to stop spammers from annoying you.
It allows to block certain users (with an optional auto-reply), it blocks
messages from people who are not on your contact list (with an optional
auto-reply and it suppress repeated authorization requests.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
    INSTALL="install -p"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%dir %{_libdir}/pidgin/
%{_libdir}/pidgin/libpidgin_pp.so
%exclude %{_libdir}/pidgin/libpidgin_pp.la

%changelog
* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Initial package. (using DAR)
