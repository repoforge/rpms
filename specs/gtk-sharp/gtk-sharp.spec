# $Id$
# Authority: dag
# Upstream: <gtk-sharp-list@ximian.com>

Summary: .Net language bindings for Gtk+ and GNOME
Name: gtk-sharp
Version: 0.18
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://gtk-sharp.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gtk-sharp/gtk-sharp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mono-devel
BuildRequires: libgnomeui-devel >= 2.0, libgnomecanvas-devel >= 2.0, libglade2-devel, gtk2-devel >= 2.2.0
BuildRequires: libgnomedb-devel, libgda-devel
Requires: libgnomeui >= 2.0, libgnomecanvas >= 2.0, libglade2

%description
A C source parser and C# code generator to produce .Net assemblies
which bind to GObject based libraries.  The Gtk+-2.0 libraries are
included along with several GNOME platform libraries.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%{__perl} -pi.orig -e 's|\@prefix\@/lib|\$(libdir)|g;' Makefile.in

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
%doc ChangeLog COPYING README
%{_bindir}/gconfsharp-schemagen*
%{_libdir}/*.dll
%{_libdir}/*.so

%files devel
%defattr(-, root, root, 0755)
%doc README.generator sample/
%{_bindir}/gapi*
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gapi/
%{_datadir}/perl5/GAPI/
%exclude %{_libdir}/*.la

%changelog
* Thu Apr 01 2004 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.17-0
- Updated to release 0.17.

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 0.15-1
- Symlinked gtk-sharp.pc to gapi.pc.

* Mon Jan 05 2004 Dag Wieers <dag@wieers.com> - 0.15-0
- Updated to release 0.15.

* Thu Nov 20 2003 Dag Wieers <dag@wieers.com> - 0.14-0
- Updated to release 0.14.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 0.13-0
- Updated to release 0.13.

* Wed Oct 29 2003 Dag Wieers <dag@wieers.com> - 0.12-0
- Updated to release 0.12.

* Fri Sep 19 2003 Dag Wieers <dag@wieers.com> - 0.11-0
- Updated to release 0.11.

* Sun Jun 15 2003 Dag Wieers <dag@wieers.com> - 0.10-0
- Updated to release 0.10.

* Sun May 25 2003 Dag Wieers <dag@wieers.com> - 0.9-0
- Initial package. (using DAR)
