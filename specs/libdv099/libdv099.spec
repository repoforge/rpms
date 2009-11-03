# $Id$
# Authority: dag
# Upstream: <libdv-dev$lists,sf,net>

%define real_name libdv

Summary: Software codec for DV video, used by most digital camcorders
Name: libdv099
Version: 0.99
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://libdv.sourceforge.net/

Source: http://dl.sf.net/libdv/libdv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig >= 0.9.0, glib-devel, gtk+-devel

%description
The Quasar DV codec (libdv) is a software codec for DV video, the encoding
format used by most digital camcorders, typically those that support the
IEEE 1394 (a.k.a. FireWire or i.Link) interface. Libdv was developed
according to the official standards for DV video: IEC 61834 and SMPTE 314M.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPY* NEWS README* TODO
%{_libdir}/*.so.*
%exclude %{_bindir}/*
%exclude %{_mandir}/man?/*
%exclude %{_includedir}/*
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.so
%exclude %{_libdir}/pkgconfig/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.99-1.2
- Rebuild for Fedora Core 5.

* Wed Apr 14 2004 Dag Wieers <dag@wieers.com> - 0.99-1
- Renamed to libdv099 as compat package.

* Thu Jan 23 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.99.

* Thu Sep 26 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0.

* Thu Aug  1 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Spec file rewrite from the one included with the sources.

