# $Id$

# Authority: dag
# Upstream: Peter Andreasen <pandr$pandr,dk>

Summary: Markup-language based presentation tool
Name: pointless
Version: 0.5
Release: 3
License: GPL
Group: Applications/Productivity
URL: http://pointless.dk/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/pointless/pointless-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: XFree86-devel, libpng-devel, zlib-devel, python >= 2.2
%{?fc2:BuildRequires: xorg-x11-Mesa-libGL}
%{?fc1:BuildRequires: XFree86-Mesa-libGL}
%{?el3:BuildRequires: XFree86-Mesa-libGL}
%{?rh9:BuildRequires: XFree86-Mesa-libGL}
%{?rh8:BuildRequires: XFree86-Mesa-libGL}
Requires: python >= 2.2

%description
Pointless is a presentation tool primarily targeted at the un*x world.
Presentations are made using a simple markup-language (best described
as a mix between TeX and Pod, and affectionately known as "The
Pointless Language").

The resulting slideshow is rendered using FreeType and OpenGL for
optimal visual quality. Hardware accelerated OpenGL is highly
recommended but not required in order to run pointless.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking \
	--enable-html
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	libdir="%{buildroot}%{_datadir}/pointless/lib/python/pointless"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/libpointless.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS PLANS README TODO
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/pointless/

%changelog
* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 0.5-3
- Fixed the libdir problem. (Jacob Weismann Poulsen)

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.5-2
- Fixed the libdir problem. (Stéphane Lentz)

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Thu Jan 08 2004 Dag Wieers <dag@wieers.com> - 0.5-0.pre1
- Updated to release 0.5-pre1.

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 0.4-0
- Initial package. (using DAR)
