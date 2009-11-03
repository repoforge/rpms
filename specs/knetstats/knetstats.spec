# $Id$
# Authority: dries

Summary: Network monitor
Name: knetstats
Version: 1.5
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://knetstats.sourceforge.net/

Source: http://dl.sf.net/knetstats/knetstats-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gettext, scons

%description
A simple KDE network monitor that show rx/tx LEDs or numeric information about
the transfer rate of any network interface in a system tray icon.

%prep
%setup

%build
scons

%install
%{__rm} -rf %{buildroot}
scons install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/knetstats
%{_datadir}/applnk/Internet/knetstats.desktop
%{_datadir}/apps/knetstats/
%{_datadir}/doc/HTML/*/knetstats/
%{_datadir}/icons/*/*/apps/knetstats.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1.2
- Rebuild for Fedora Core 5.

* Mon Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Initial package.
