# $Id$
# Authority: dag
# Upstream: Edwin Young <edwin$sourceforge,net>

%define desktop_vendor rpmforge

Summary: Program to generate and view fractals
Name: gnofract4d
Version: 2.5
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://gnofract4d.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gnofract4d/gnofract4d-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: scrollkeeper

Requires(post): scrollkeeper
Requires: gcc-c++

%description
Gnofract 4D is a GNOME-based program to draw fractals. What sets it
apart from other fractal programs (and makes it "4D") is the way that
it treats the Mandelbrot and Julia sets as different views of the
same four-dimensional fractal object. 

%prep
%setup

%build
python2 setup.py build

%install
%{__rm} -rf %{buildroot}
python2 setup.py install \
        --root="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --delete-original             \
	--vendor %{desktop_vendor}                 \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/gnome/apps/Graphics/gnofract4d.desktop

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_datadir}/gnome/help/gnofract4d/
%{_bindir}/gnofract4d
%dir %{_datadir}/maps/
%{_datadir}/maps/gnofract4d/
%{_datadir}/applications/%{desktop_vendor}-gnofract4d.desktop
%{_datadir}/pixmaps/gnofract4d/
%{_prefix}/lib/gnofract4d-%{version}/
%{_datadir}/formulas/gnofract4d/

%changelog
* Fri Dec 24 2004 Dag Wieers <dag@wieers.com> - 2.5-1
- Updated to release 2.5.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Mon Jun 28 2004 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Sat Dec 13 2003 Dag Wieers <dag@wieers.com> - 1.9-0
- Updated to release 1.9.

* Sun Nov 02 2003 Dag Wieers <dag@wieers.com> - 1.8-0
- Updated to release 1.8.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 1.7-0
- Initial package. (using DAR)
