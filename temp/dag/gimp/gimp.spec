# Authority: dag

%define aversion 1.3

Summary: The GNU Image Manipulation Program.
Name: gimp
Version: 1.3.12
Release: 0
License: GPL, LGPL
Group: Applications/Multimedia
URL: http://www.gimp.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.gimp.org/pub/gimp/v%{aversion}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk2-devel >= 2.0.0, gtkhtml2-devel, pkgconfig, aalib-devel

%description
The GIMP (GNU Image Manipulation Program) is a powerful image
composition and editing program, which can be extremely useful for
creating logos and other graphics for Web pages.  The GIMP has many of
the tools and filters you would expect to find in similar commercial
offerings, and some interesting extras as well. The GIMP provides a
large image manipulation toolbox, including channel operations and
layers, effects, sub-pixel imaging and anti-aliasing, and conversions,
all with multi-level undo.

%package devel
Summary: GIMP plugin and extension development kit.
Group: Applications/Multimedia
Requires: %{name} = %{version}

%description devel
The gimp-devel package contains the static libraries and header files
for writing GNU Image Manipulation Program (GIMP) plug-ins and
extensions.

Install gimp-devel if you're going to create plug-ins and/or
extensions for the GIMP.

%prep
%setup

%build
%configure \
	--enable-default-binary \
	--disable-print
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --delete-original --vendor "gnome" \
	--add-category X-Red-Hat-Base                   \
	--add-category Application                      \
	--add-category Graphics                         \
	--dir %{buildroot}%{_datadir}/applications      \
	%{buildroot}%{_datadir}/gimp/%{aversion}/misc/%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr (-, root, root, 0755)
%doc AUTHORS ChangeLog* COPYING MAINTAINERS NEWS README README.i18n
%doc docs/*.txt
%doc %{_datadir}/gtk-doc/html/*
%doc %{_mandir}/man1/*
%config %{_sysconfdir}/gimp/%{aversion}/
%dir %{_libdir}/gimp/
%dir %{_libdir}/gimp/%{aversion}
%dir %{_libdir}/gimp/%{aversion}/modules
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/gimp/%{aversion}/environ
%{_libdir}/gimp/%{aversion}/modules/*.so
%{_libdir}/gimp/%{aversion}/plug-ins
%{_datadir}/applications/*
%{_datadir}/gimp/
%{_datadir}/locale/*/LC_MESSAGES/*

%files devel
%defattr (-, root, root, 0755)
%doc HACKING PLUGIN_MAINTAINERS
%doc %{_mandir}/man5/*
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/gimp/%{aversion}/modules/*.a
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/gimp/%{aversion}/modules/*.la

%changelog
* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 1.3.12-0
- Initial package. (using DAR)
