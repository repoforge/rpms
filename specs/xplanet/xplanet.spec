# $Id$
# Authority: matthias

Summary: Planet image rendering into the X root window
Name: xplanet
Version: 1.0.3
Release: 2
License: GPL
Group: Amusements/Graphics
URL: http://xplanet.sourceforge.net/
Source: http://dl.sf.net/xplanet/xplanet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
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
%{__make} install-strip DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc README AUTHORS README.config NEWS TODO
%{_bindir}/xplanet
%{_datadir}/xplanet
%{_mandir}/man1/xplanet.1.gz


%changelog
* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net> 1.0.3-2.fr
- Spec file cleanup.
- Split off the extra maps.

* Wed Jan 28 2004 Dries Verachtert <dries@ulyssis.org> 1.0.3-1
- first packaging for Fedora Core 1

