# $Id$
# Authority: matthias

Summary: Planet image rendering into the X root window
Name: xplanet
Version: 1.1.1
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://xplanet.sourceforge.net/
Source: http://dl.sf.net/xplanet/xplanet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xplanet-maps
BuildRequires: XFree86-devel, gcc-c++, zlib-devel
BuildRequires: libungif-devel, libjpeg-devel, libpng-devel
BuildRequires: netpbm-devel, libtiff-devel, pango-devel

%description
Xplanet was inspired by Xearth, which renders an image of the earth into the
X root window. All of the major planets and most satellites can be drawn,
similar to the Solar System Simulator. A number of different map projections
are also supported, including azimuthal, Lambert, Mercator, Mollweide,
orthographic, and rectangular.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS NEWS README* TODO
%{_bindir}/xplanet
%{_datadir}/xplanet
%{_mandir}/man1/xplanet.1.gz


%changelog
* Mon Jul 26 2004 Matthias Saou <http://freshrpms.net> 1.1.1-1
- Update to 1.1.1.

* Mon Jun 21 2004 Matthias Saou <http://freshrpms.net> 1.1.0-1
- Update to 1.1.0.

* Mon May 24 2004 Matthias Saou <http://freshrpms.net> 1.0.8-1
- Update to 1.0.8.

* Thu May 20 2004 Matthias Saou <http://freshrpms.net> 1.0.7-1
- Update to 1.0.7.
- Add xplanets-maps as a dependency as requested by users.

* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net> 1.0.3-2
- Spec file cleanup.
- Split off the extra maps.

* Wed Jan 28 2004 Dries Verachtert <dries@ulyssis.org> 1.0.3-1
- first packaging for Fedora Core 1

