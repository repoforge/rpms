# $Id$

# Authority: dag

%define real_name diacanvas

Summary: Full featured diagramming canvas for GNOME
Name: diacanvas2
Version: 0.9.2
Release: 0.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://diacanvas.sourceforge.net/

Source: http://dl.sf.net/diacanvas/diacanvas2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.0, libart_lgpl-devel >= 2.0, pango-devel >= 1.2
BuildRequires: libgnomecanvas-devel >= 2.0, libgnomeprintui-devel >= 1.116
BuildRequires: perl, pygtk2-devel >= 1.99.10, python-devel >= 2.2, gettext

%description
DiaCanvas2 is providing you with a full featured diagramming canvas for GNOME.

%package devel
Summary: Static library and API documentation of DiaCanvas
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Static library and API documentation of DiaCanvas.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking \
	--enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{real_name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/diacanvas2/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/diacanvas/
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.2-0.2
- Rebuild for Fedora Core 5.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Initial package. (using DAR)
