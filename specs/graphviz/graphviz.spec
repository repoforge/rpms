# $Id$

# Authority: dag

##DarSoapbox: 0
##DarDistcc: 0

Summary: Graph Visualization Tools
Name: graphviz
Version: 1.16
Release: 1
Group: Applications/Multimedia
License: AT&T open source (see COPYING)
URL: http://www.graphviz.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.graphviz.org/pub/graphviz/ARCHIVE/graphviz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: XFree86-devel, tcl-devel, tk-devel, freetype-devel >= 2.0
BuildRequires: libjpeg-devel, libpng-devel, zlib-devel, gcc-c++
# needs version 2.0.29 of gdlib but fc3 contains 2.0.28
# BuildRequires: gd-progs, gd-devel

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

%prep
%setup

%build
%ifarch i386
%define optflags -O2 -ffast-math
%endif
%configure \
	--with-x
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	includedir="%{buildroot}%{_includedir}/graphviz"
%{__mv} %{buildroot}%{_datadir}/graphviz/doc rpmdoc

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/%{name}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ.txt MINTERMS.txt NEWS README
%doc rpmdoc/*
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/%{name}/libagraph.so.*
%{_libdir}/%{name}/libcdt.so.*
%{_libdir}/%{name}/libexpr.so.*
%{_libdir}/%{name}/libgraph.so.*
#%{_libdir}/%{name}/libgd.so.*
%{_libdir}/%{name}/libpack.so.*
%{_libdir}/%{name}/libpathplan.so.*
%{_libdir}/%{name}/libcircogen.so.*
%{_libdir}/%{name}/libcommon.so.*
%{_libdir}/%{name}/libdotgen.so.*
%{_libdir}/%{name}/libdotneato.so.*
%{_libdir}/%{name}/libfdpgen.so.*
%{_libdir}/%{name}/libgvgd.so.*
%{_libdir}/%{name}/libgvrender.so.*
%{_libdir}/%{name}/libneatogen.so.*
%{_libdir}/%{name}/libtwopigen.so.*
%{_datadir}/%{name}/lefty/
%{_datadir}/%{name}/graphs/

%files tcl
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ.txt MINTERMS.txt NEWS README
#%doc doc/tcldot.html
%doc %{_mandir}/mann/*
%{_libdir}/%{name}/libgdtclft.so.*
%{_libdir}/%{name}/libtcl*.so.*
%{_libdir}/%{name}/libtkspline.so.*
%{_libdir}/%{name}/pkgIndex.tcl
%{_datadir}/%{name}/demo/

%files devel
%defattr(-, root, root, 0755)
%doc LICENSE.html
%doc %{_mandir}/man3/*
%{_includedir}/graphviz/
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/pkgconfig
#exclude %{_libdir}/%{name}/*.la

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> 1.16-1
- Updated to release 1.16.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 1.8.10-6
- Fixed includedir. (Reported by Thomas Moschny)

* Sun Jan 04 2003 Dag Wieers <dag@wieers.com> - 1.8.10-0
- Initial package. (using DAR)
