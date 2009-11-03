# $Id$
# Authority: dries
# Upstream: <harpin_floh$yahoo,de>

Summary: Guitar and other instruments tuner
Name: k3guitune
Version: 0.5.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://home.planet.nl/~lamer024/k3guitune.html

Source: http://home.planet.nl/~lamer024/files/k3guitune-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, kdelibs-devel, gettext

%description
KGuitune is a guitar-and-other-instruments tuner. It takes a signal from the
microphone, calculates its frequency, and displays it on a note scale
graphic and an oscilloscope. It supports normal, Wien, and physical tuning.

%prep
%setup
%{__perl} -pi -e "s|^\.#|#|g;" k3guitune/k3guitune.desktop

%build
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/k3guitune
%{_datadir}/applnk/Multimedia/k3guitune.desktop
%{_datadir}/apps/k3guitune/
%{_datadir}/doc/HTML/*/k3guitune/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.2-1.2
- Rebuild for Fedora Core 5.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.2-1
- Updated to release 0.5.2.

* Fri Dec 16 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.1-2
- Fix the desktop file, thanks to Stephen Biggs.

* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.1-1
- Initial package.
