# $Id$
# Authority: dries
# Upstream: Mikael BERTHE
# ScreenshotURL: http://www.lilotux.net/~mikael/mcabber/screenshots/mcabber_sample.png

Summary: Console jabber client
Name: mcabber
Version: 0.6.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.lilotux.net/~mikael/mcabber/

Source: http://www.lilotux.net/~mikael/mcabber/files/mcabber-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, ncurses-devel, glib2-devel, openssl-devel, pkgconfig

%description
Mcabber is a small jabber console client which supports SSL support, history 
logging, external actions and more.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man?/mcabber*
%{_bindir}/mcabber

%changelog
* Tue Feb 12 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.2-1
- Initial package.
