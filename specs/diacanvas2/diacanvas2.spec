# Authority: dag

%define rname diacanvas

Summary: A full featured diagramming canvas for GNOME.
Name: diacanvas2
Version: 0.9.2
Release: 0
Group: System Environment/Libraries
License: GPL
URL: http://diacanvas.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/diacanvas/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: glib2-devel >= 2.0, libart_lgpl-devel >= 2.0, pango-devel >= 1.2
BuildRequires: libgnomecanvas-devel >= 2.0, libgnomeprintui-devel >= 1.116
BuildRequires: perl, pygtk2-devel >= 1.99.10, python-devel >= 2.2

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
%find_lang %{rname}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{rname}.lang
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
* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Initial package. (using DAR)
