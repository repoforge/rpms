# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}

Summary: Graph Visualization Tools
Name: graphviz
Version: 2.6
Release: 2.2
License: CPL
Group: Applications/Multimedia
URL: http://www.graphviz.org/

Source: http://www.graphviz.org/pub/graphviz/ARCHIVE/graphviz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: freetype-devel >= 2.0, bison, m4, flex, ruby-devel, libtool-ltdl-devel
BuildRequires: libjpeg-devel, libpng-devel, zlib-devel, expat-devel, gcc-c++
#BuildRequires: /bin/ksh
%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3, tk-devel}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.3, tk}
# needs version 2.0.29 of gdlib but fc3 contains 2.0.28
# BuildRequires: gd-progs, gd-devel
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%package tcl
Group: Applications/Multimedia
Summary: Tcl extension tools for version %{version} of %{name}
Requires: %{name} = %{version}-%{release}, tk

%description tcl
The %{name}-tcl package contains the various tcl packages (extensions)
for version %{version} of the %{name} tools.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}.

%package doc
Summary: PDF and HTML documents for %{name}
Group: Documentation

%description doc
Provides some additional PDF and HTML documentation for %{name}.

%package graphs
Summary: Demo graphs for %{name}
Group: Applications/Multimedia

%description graphs
Some demo graphs for %{name}.

%prep
%setup

%build
%{expand: %%define optflags %{optflags} -ffast-math}
%configure \
	--with-mylibgd \
	--with-x
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
	pkgconfigdir=%{_libdir}/pkgconfig \
	transform='s,x,x,'
%{__mv} %{buildroot}%{_datadir}/graphviz/doc rpmdoc
%{__chmod} -x %{buildroot}%{_datadir}/graphviz/lefty/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/*
%{_bindir}/*
%dir %{_datadir}/graphviz/
%{_datadir}/graphviz/lefty/
%{_libdir}/graphviz/*.so.*
%exclude %{_libdir}/graphviz/lib*tcl*.so.*
%exclude %{_libdir}/graphviz/libtk*.so.*
#%exclude %{_bindir}/dotneato-config
#%exclude %{_mandir}/man1/dotneato-config.1*

%files tcl
%defattr(-, root, root, 0755)
#%doc doc/tcldot.html
%doc %{_mandir}/mann/*
%{_datadir}/graphviz/demo/
%{_libdir}/graphviz/lib*tcl*.so.*
%{_libdir}/graphviz/libtk*.so.*
%{_libdir}/graphviz/pkgIndex.tcl
%exclude %{_libdir}/%{name}/lib*tcl*.so.?
%exclude %{_libdir}/%{name}/libtk*.so.?

%files devel
%defattr(-, root, root, 0755)
#%doc %{_mandir}/man1/dotneato-config.1*
%doc %{_mandir}/man3/*
#%{_bindir}/dotneato-config
%{_includedir}/graphviz/
%{_libdir}/graphviz/*.so
%{_libdir}/graphviz/*.a
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/graphviz/*.la

%files graphs
%defattr(-, root, root, 0755)
%dir %{_datadir}/graphviz/
%{_datadir}/graphviz/graphs/

%files doc
%defattr(-, root, root, 0755)
%doc rpmdoc/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.6-2.2
- Rebuild for Fedora Core 5.

* Sat Nov 12 2005 Dries Verachtert <dries@ulyssis.org> - 2.6-2
- Changes in files section: dotneato* removed, static libs added.

* Mon Nov 07 2005 Dries Verachtert <dries@ulyssis.org> - 2.6-1
- Updated to release 2.6.

* Fri Mar 11 2005 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> 1.16-1
- Updated to release 1.16.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 1.8.10-6
- Fixed includedir. (Reported by Thomas Moschny)

* Sun Jan 04 2003 Dag Wieers <dag@wieers.com> - 1.8.10-0
- Initial package. (using DAR)
