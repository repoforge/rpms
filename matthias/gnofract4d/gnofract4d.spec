# Authority: dag

# Upstream: Edwin Young <edwin@sourceforge.net>

Summary: A GNOME-based program to generate and view fractals.
Name: gnofract4d
Version: 1.9
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://gnofract4d.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/gnofract4d/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/gnome/apps/Graphics/%{name}.desktop

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_datadir}/gnome/help/gnofract4d/
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.so.*
%{_datadir}/gnofract4d/
%dir %{_datadir}/maps/
%{_datadir}/maps/gnofract4d/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/gnofract4d/
%{_datadir}/omf/gnofract4d/

%changelog
* Sat Dec 13 2003 Dag Wieers <dag@wieers.com> - 1.9-0
- Updated to release 1.9.

* Sun Nov 02 2003 Dag Wieers <dag@wieers.com> - 1.8-0
- Updated to release 1.8.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 1.7-0
- Initial package. (using DAR)
