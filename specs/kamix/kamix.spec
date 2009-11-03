# $Id$
# Authority: dries
# Upstream: Stefano Rivoir <s,rivoir$gts,it>

Summary: Mixer for kde and alsa
Name: kamix
Version: 0.6.6
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://kamix.sourceforge.net

Source: http://dl.sf.net/kamix/kamix-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gettext, autoconf, automake

%description
kamix is a mixer for KDE and ALSA, with more features than kmix (or at least
with more features than kmix had when kamix was started). It supports
channel splitting, levels storing/restoring, sync with external ALSA events,
correct handling of "enumerated" elements, and selective item hiding/showing.

%prep
%setup -n kamix

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
%{_bindir}/kamix
%{_datadir}/applnk/Utilities/kamix.desktop
%{_datadir}/apps/kamix/
%{_datadir}/doc/HTML/*/kamix/
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/128x128/apps/kamix/

%changelog
* Fri Apr 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.6.6-1
- Updated to release 0.6.6.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.5-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.5-1
- Initial package.
