# $Id$

# Authority: dag

### FIXME: frontline triggers a strange bug in Distcc 2.2 (RH9 maybe others)
# Distcc: 0

Summary: GUI frontend program and library for autotrace.
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
%{__install} -d -m0755 %{buildroot}%{_libdir}/gimp/1.2/plug-ins/
mv %{buildroot}/usr/libexec/trace %{buildroot}%{_libdir}/gimp/1.2/plug-ins/

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
%{_libdir}/gimp/1.2/plug-ins/trace

%changelog
* Tue Nov 26 2002 Dag Wieers <dag@wieers.com> - 0.5.4
- Updated to 0.5.4

* Sun Sep  8 2002 Masatake YAMATO <jet@gyve.org>
- Initial build.
