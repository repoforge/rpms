# $Id$
# Authority: dag

%define gimp %(rpm -q gimp-devel | grep -q 1\.2; echo $?)

Summary: GUI frontend program and library for autotrace
Name: frontline
Version: 0.5.4
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://autotrace.sf.net/frontline/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/autotrace/frontline-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libart_lgpl-devel >= 2.0, gimp-devel, autotrace-devel
BuildRequires: gnome-libs-devel

%description
Frontline provides a Gtk+/GNOME based GUI frontend for 
autotrace.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{gimp}0
%else
%{__install} -d -m0755 %{buildroot}%{_libdir}/gimp/1.2/plug-ins/
%{__mv} -f %{buildroot}/usr/libexec/trace %{buildroot}%{_libdir}/gimp/1.2/plug-ins/
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_libdir}/*.a
%{_includedir}/gundo/
%{_includedir}/frontline/
%{_datadir}/gnome/apps/Graphics/frontline.desktop
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_datadir}/aclocal/frontline.m4
%{_libdir}/pkgconfig/frontline.pc
%if %{gimp}0
%else
%{_libdir}/gimp/1.2/plug-ins/trace
%endif

%changelog
* Tue Nov 26 2002 Dag Wieers <dag@wieers.com> - 0.5.4
- Updated to 0.5.4

* Sun Sep  8 2002 Masatake YAMATO <jet@gyve.org>
- Initial build.
