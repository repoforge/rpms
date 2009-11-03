# $Id$
# Authority: dag
# Upstream: <gtk-sharp-list$ximian,com>


%{?el3:%define _without_croco 1}
%{?rh9:%define _without_croco 1}
%{?rh9:%define _without_gtkhtml3 1}
%{?rh7:%define _without_croco 1}
%{?rh7:%define _without_gtkhtml3 1}
%{?el2:%define _without_croco 1}
%{?el2:%define _without_gtkhtml3 1}

Summary: .Net language bindings for Gtk+ and GNOME
Name: gtk-sharp
Version: 1.0.4
Release: 1.2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://gtk-sharp.sourceforge.net/

Source: http://dl.sf.net/gtk-sharp/gtk-sharp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mono-core, mono-devel
BuildRequires: libgnomeui-devel >= 2.0, libgnomecanvas-devel >= 2.0, libglade2-devel, gtk2-devel >= 2.2.0
BuildRequires: libgnomedb-devel, libgda-devel, librsvg2-devel, glib2-devel, libart_lgpl-devel, libgsf-devel
#BuildRequires: vte-devel >= 0.11.10
BuildRequires: vte-devel
%{!?_without_croco:BuildRequires: libcroco-devel}
%{!?_without_gtkhtml3:BuildRequires: gtkhtml3-devel}
Requires: librsvg2
%{!?_without_croco:Requires: libcroco}
%{!?_without_gtkhtml3:Requires: gtkhtml3}
#Requires: libgnomeui >= 2.0, libgnomecanvas >= 2.0, libglade2

%description
A C source parser and C# code generator to produce .Net assemblies
which bind to GObject based libraries.  The Gtk+-2.0 libraries are
included along with several GNOME platform libraries.

%package gapi
Summary: C source parser and C generator
Group: Development/Libraries
Requires: perl-XML-LibXML-Common, perl-XML-LibXML, perl-XML-NamespaceSupport
Requires: perl-XML-SAX, gtk-sharp = %{version}-%{release}

%description gapi
The gtk-sharp-gapi package includes the parser and code
generator used by the Gtk if you want to bind
GObject-based libraries, or need to compile a project that
uses it to bind such a library.

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

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}" \
	GACUTIL_FLAGS="/package gtk-sharp /root %{buildroot}%{_libdir}"

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%{_bindir}/*
%exclude %{_bindir}/gapi*
%{_libdir}/mono/
%{_libdir}/*.so

%files gapi
%defattr(-, root, root, 0755)
%{_bindir}/gapi*
%{_libdir}/pkgconfig/gapi.pc
%{_datadir}/gapi/

%files devel
%defattr(-, root, root, 0755)
%doc README.generator sample/
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/pkgconfig/gapi.pc
#%{_datadir}/perl5/GAPI/
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

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
