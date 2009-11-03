# $Id$
# Authority: dries
# Upstream: Johannes Mesa Pascasio <frosla$sourceforge,net>

Summary: Go board, SGF editor and client for the Internet Go Server
Name: qgo
Version: 1.5.4
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://qgo.sourceforge.net/

Source: http://dl.sf.net/qgo/qgo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gettext, gcc-c++

%description
qGo is a Go board, SGF editor, and client for the Internet Go Server. You can
review and edit games, connect to IGS, and play against a computer program
supporting GTP (like GnuGo). Go is an ancient board game which is very common
in Japan, China, and Korea.

%prep
%setup

%build
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__ln_s} normaltools_gui.h src/normaltools.h
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/qgo
%{_datadir}/applnk/Games/qgo.desktop
%{_datadir}/mimelnk/text/sgf.desktop
%{_datadir}/qGo/

%changelog
* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 1.5.4-1
- Updated to release 1.5.4.

* Tue Jan 09 2007 Dries Verachtert <dries@ulyssis.org> - 1.5.3-1
- Updated to release 1.5.3.

* Mon Nov 13 2006 Dries Verachtert <dries@ulyssis.org> - 1.5.2-1
- Updated to release 1.5.2.

* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to release 1.5.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1.2
- Rebuild for Fedora Core 5.

* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1
- Initial package.
