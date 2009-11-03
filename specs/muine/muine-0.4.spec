# $Id$

# Authority: dag
# Soapbox: 0

Summary: Simple music player
Name: muine
Version: 0.4.0
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://muine.gooeylinux.org/

Source: http://muine.gooeylinux.org/muine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: glib2-devel, mono-devel, gtk-sharp-devel >= 0.17, gstreamer-devel
BuildRequires: gstreamer-plugins-devel, libvorbis-devel, libid3tag-devel, flac-devel
Requires: mono, gtk-sharp

%description
Muine is an innovative music player. It is much easier and comfortable to
use than the iTunes model, which is used by both Rhythmbox and Jamboree.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/muine/*.{a,la}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/muine/
%{_datadir}/pixmaps/*.png
%{_datadir}/application-registry/*.applications
%{_datadir}/applications/*.desktop

%changelog
* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Rebuild against gtk-sharp 0.17.

* Fri Feb 13 2004 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Updated to release 0.4.0.

* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 0.3.2-0
- Updated to release 0.3.2.

* Sun Feb 01 2004 Dag Wieers <dag@wieers.com> - 0.3.1.1-0
- Added a new covers patch.
- Updated to release 0.3.1.1.

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 0.3.1-0
- Updated to release 0.3.1.
- Updated to release 0.3.0.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Initial package. (using DAR)
