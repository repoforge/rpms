# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el5:%define _without_java 1}
%{?fc6:%define _without_java 1}
%{?fc5:%define _without_java 1}

%{?fc4:%define _without_java 1}
%{?fc4:%define _without_modxorg 1}

%{?el4:%define _without_java 1}
%{?el4:%define _without_modxorg 1}

%{?fc3:%define _without_java 1}
%{?fc3:%define _without_modxorg 1}

%{?fc2:%define _without_java 1}
%{?fc2:%define _without_modxorg 1}

%{?fc1:%define _without_java 1}
%{?fc1:%define _without_modxorg 1}

%{?el3:%define _without_java 1}
%{?el3:%define _without_modxorg 1}

%{?rh9:%define _without_java 1}
%{?rh9:%define _without_tcltk_devel 1}

%{?rh8:%define _without_java 1}
%{?rh8:%define _without_tcltk_devel 1}

%{?rh7:%define _without_java 1}
%{?rh7:%define _without_tcltk_devel 1}

%{?el2:%define _without_java 1}
%{?el2:%define _without_modxorg 1}
%{?el2:%define _without_tcltk_devel 1}

Summary: Graph Visualization Tools
Name: graphviz
Version: 2.14.1
Release: 2
License: CPL
Group: Applications/Multimedia
URL: http://www.graphviz.org/

Source: http://www.graphviz.org/pub/graphviz/ARCHIVE/graphviz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: freetype-devel >= 2.0, bison, m4, flex, ruby-devel, libtool-ltdl-devel
BuildRequires: libjpeg-devel, libpng-devel, zlib-devel, expat-devel, gcc-c++
BuildRequires: python-devel, php-devel, guile-devel, perl
#BuildRequires: /bin/ksh
%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3, tk-devel}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.3, tk}
# needs version 2.0.29 of gdlib but fc3 contains 2.0.28
# BuildRequires: gd-progs, gd-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXext-devel, libXt-devel, libXaw-devel}
%{!?_without_java:BuildRequires: java}

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%post
/sbin/ldconfig
%{_bindir}/dot -c

%postun -p /sbin/ldconfig

%package tcl
Group: Applications/Multimedia
Summary: Tcl extension tools for version %{version} of %{name}
Requires: %{name} = %{version}-%{release}, tk

%description tcl
The %{name}-tcl package contains the various tcl packages (extensions)
for version %{version} of the %{name} tools.

%package ruby
Group: Applications/Multimedia
Summary: Ruby extension tools for version %{version} of %{name}
Requires: %{name} = %{version}-%{release}

%description ruby
The %{name}-ruby package contains the various ruby packages (extensions)
for version %{version} of the %{name} tools.

%package python
Group: Applications/Multimedia
Summary: Python extension tools for version %{version} of %{name}
Requires: %{name} = %{version}-%{release}

%description python
The %{name}-python package contains the various python packages (extensions)
for version %{version} of the %{name} tools.

%package php
Group: Applications/Multimedia
Summary: Php extension tools for version %{version} of %{name}
Requires: %{name} = %{version}-%{release}

%description php
The %{name}-php package contains the various php packages (extensions)
for version %{version} of the %{name} tools.

%package ocaml
Group: Applications/Multimedia
Summary: Ocaml extension tools for version %{version} of %{name}
Requires: %{name} = %{version}-%{release}

%description ocaml
The %{name}-ocaml package contains the various ocaml packages (extensions)
for version %{version} of the %{name} tools.

%package guile
Group: Applications/Multimedia
Summary: Guile extension tools for version %{version} of %{name}
Requires: %{name} = %{version}-%{release}

%description guile
The %{name}-guile package contains the various guile packages (extensions)
for version %{version} of the %{name} tools.

%package java
Group: Applications/Multimedia
Summary: Java extension tools for version %{version} of %{name}
Requires: %{name} = %{version}-%{release}

%description java
The %{name}-java package contains the various java packages (extensions)
for version %{version} of the %{name} tools.

%package lua
Group: Applications/Multimedia
Summary: Lua extension tools for version %{version} of %{name}
Requires: %{name} = %{version}-%{release}

%description lua
The %{name}-lua package contains the various lua packages (extensions)
for version %{version} of the %{name} tools.

%package perl
Group: Applications/Multimedia
Summary: Perl extension tools for version %{version} of %{name}
Requires: %{name} = %{version}-%{release}

%description perl
The %{name}-perl package contains the various perl packages (extensions)
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
	--with-x \
	%{?_without_java:--disable-java}
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
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man7/graphviz.7*
%{_bindir}/*
%dir %{_datadir}/graphviz/
%{_datadir}/graphviz/lefty/
%{_libdir}/graphviz/*.so.*
#exclude %{_libdir}/graphviz/lib*tcl*.so.*
#exclude %{_libdir}/graphviz/libtk*.so.*
#exclude %{_bindir}/dotneato-config
#exclude %{_mandir}/man1/dotneato-config.1*
%{_libdir}/lib*.so.*

%files tcl
%defattr(-, root, root, 0755)
#%doc doc/tcldot.html
%doc %{_mandir}/mann/*.n*
%{_libdir}/graphviz/tcl/
%{_datadir}/graphviz/demo/
#{_libdir}/graphviz/lib*tcl*.so.*
#{_libdir}/graphviz/libtk*.so.*
%{_libdir}/graphviz/pkgIndex.tcl
#exclude %{_libdir}/%{name}/lib*tcl*.so.?
#exclude %{_libdir}/%{name}/libtk*.so.?

%files devel
%defattr(-, root, root, 0755)
#%doc %{_mandir}/man1/dotneato-config.1*
%doc %{_mandir}/man3/*
#%{_bindir}/dotneato-config
%{_includedir}/graphviz/
%{_libdir}/graphviz/*.so
%{_libdir}/lib*.so
# %{_libdir}/graphviz/*.a
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/graphviz/*.la
%exclude %{_libdir}/*.la

%files ruby
%defattr(-, root, root, 0755)
%{_libdir}/graphviz/ruby/

%files python
%defattr(-, root, root, 0755)
%{_libdir}/graphviz/python/

%files php
%defattr(-, root, root, 0755)
%{_libdir}/graphviz/php/

%files ocaml
%defattr(-, root, root, 0755)
%{_libdir}/graphviz/ocaml/

%files guile
%defattr(-, root, root, 0755)
%{_libdir}/graphviz/guile/

%if %{!?_without_java:1}0
%files java
%defattr(-, root, root, 0755)
%{_libdir}/graphviz/java/
%endif

%files lua
%defattr(-, root, root, 0755)
%{_libdir}/graphviz/lua/

%files perl
%defattr(-, root, root, 0755)
%{_libdir}/graphviz/perl/

%files graphs
%defattr(-, root, root, 0755)
%dir %{_datadir}/graphviz/
%{_datadir}/graphviz/graphs/

%files doc
%defattr(-, root, root, 0755)
%doc rpmdoc/*

%changelog
* Sun Apr 20 2008 Dries Verachtert <dries@ulyssis.org> - 2.14.1-2
- Added --disable-java to configure when _without_java is set.

* Mon Sep  3 2007 Dries Verachtert <dries@ulyssis.org> - 2.14.1-1
- Updated to release 2.14.1.
- Generate config file in post script, thanks to Stefan Radman.

* Sun Oct 15 2006 Dries Verachtert <dries@ulyssis.org> - 2.8-1
- Updated to release 2.8.
- Made some more subpackages.

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
