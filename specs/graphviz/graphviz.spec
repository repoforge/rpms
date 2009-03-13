# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el5:%define _without_lua 1}
%{?el5:%define _without_ocaml 1}
%{?el5:%define _without_php 1}

%{?fc5:%define _without_lua 1}
%{?fc5:%define _without_pangocairo 1}
%{?fc5:%define _without_rsvg 1}

%{?fc4:%define _without_java 1}
%{?fc4:%define _without_lua 1}
%{?fc4:%define _without_modxorg 1}
%{?fc4:%define _without_ocaml 1}
%{?fc4:%define _without_pangocairo 1}
%{?fc4:%define _without_php 1}
%{?fc4:%define _without_rsvg 1}

%{?el4:%define _without_java 1}
%{?el4:%define _without_ltdl_devel 1}
%{?el4:%define _without_lua 1}
%{?el4:%define _without_modxorg 1}
%{?el4:%define _without_ocaml 1}
%{?el4:%define _without_pangocairo 1}
%{?el4:%define _without_php 1}
%{?el4:%define _without_rsvg 1}

%{?fc3:%define _without_guile 1}
%{?fc3:%define _without_java 1}
%{?fc3:%define _without_ltdl_devel 1}
%{?fc3:%define _without_lua 1}
%{?fc3:%define _without_modxorg 1}
%{?fc3:%define _without_ocaml 1}
%{?fc3:%define _without_pangocairo 1}
%{?fc3:%define _without_php 1}
%{?fc3:%define _without_python 1}
%{?fc3:%define _without_rsvg 1}
%{?fc3:%define _without_ruby 1}

%{?fc2:%define _without_guile 1}
%{?fc2:%define _without_ipsepcola 1}
%{?fc2:%define _without_java 1}
%{?fc2:%define _without_ltdl_devel 1}
%{?fc2:%define _without_lua 1}
%{?fc2:%define _without_modxorg 1}
%{?fc2:%define _without_ocaml 1}
%{?fc2:%define _without_pangocairo 1}
%{?fc2:%define _without_php 1}
%{?fc2:%define _without_python 1}
%{?fc2:%define _without_rsvg 1}
%{?fc2:%define _without_ruby 1}

%{?fc1:%define _without_guile 1}
%{?fc1:%define _without_ipsepcola 1}
%{?fc1:%define _without_java 1}
%{?fc1:%define _without_ltdl_devel 1}
%{?fc1:%define _without_lua 1}
%{?fc1:%define _without_modxorg 1}
%{?fc1:%define _without_ocaml 1}
%{?fc1:%define _without_pangocairo 1}
%{?fc1:%define _without_php 1}
%{?fc1:%define _without_python 1}
%{?fc1:%define _without_rsvg 1}
%{?fc1:%define _without_ruby 1}

%{?el3:%define _without_guile 1}
%{?el3:%define _without_java 1}
%{?el3:%define _without_ltdl_devel 1}
%{?el3:%define _without_lua 1}
%{?el3:%define _without_modxorg 1}
%{?el3:%define _without_ocaml 1}
%{?el3:%define _without_pangocairo 1}
%{?el3:%define _without_perl 1}
%{?el3:%define _without_php 1}
%{?el3:%define _without_python 1}
%{?el3:%define _without_rsvg 1}
%{?el3:%define _without_ruby 1}

%{?rh9:%define _without_fontconfig 1}
%{?rh9:%define _without_guile 1}
%{?rh9:%define _without_ipsepcola 1}
%{?rh9:%define _without_java 1}
%{?rh9:%define _without_ltdl_devel 1}
%{?rh9:%define _without_lua 1}
%{?rh9:%define _without_modxorg 1}
%{?rh9:%define _without_ocaml 1}
%{?rh9:%define _without_pangocairo 1}
%{?rh9:%define _without_php 1}
%{?rh9:%define _without_python 1}
%{?rh9:%define _without_rsvg 1}
%{?rh9:%define _without_ruby 1}
%{?rh9:%define _without_tcltk_devel 1}

%{?rh8:%define _without_fontconfig 1}
%{?rh8:%define _without_guile 1}
%{?rh8:%define _without_ipsepcola 1}
%{?rh8:%define _without_java 1}
%{?rh8:%define _without_ltdl_devel 1}
%{?rh8:%define _without_lua 1}
%{?rh8:%define _without_modxorg 1}
%{?rh8:%define _without_ocaml 1}
%{?rh8:%define _without_pangocairo 1}
%{?rh8:%define _without_php 1}
%{?rh8:%define _without_python 1}
%{?rh8:%define _without_rsvg 1}
%{?rh8:%define _without_ruby 1}
%{?rh8:%define _without_tcltk_devel 1}

%{?rh7:%define _without_fontconfig 1}
%{?rh7:%define _without_guile 1}
%{?rh7:%define _without_ipsepcola 1}
%{?rh7:%define _without_java 1}
%{?rh7:%define _without_ltdl_devel 1}
%{?rh7:%define _without_lua 1}
%{?rh7:%define _without_modxorg 1}
%{?rh7:%define _without_ocaml 1}
%{?rh7:%define _without_pangocairo 1}
%{?rh7:%define _without_php 1}
%{?rh7:%define _without_python 1}
%{?rh7:%define _without_rsvg 1}
%{?rh7:%define _without_ruby 1}
%{?rh7:%define _without_tcltk_devel 1}

%{?el2:%define _without_fontconfig 1}
%{?el2:%define _without_freetype 1}
%{?el2:%define _without_guile 1}
%{?el2:%define _without_ipsepcola 1}
%{?el2:%define _without_java 1}
%{?el2:%define _without_ltdl_devel 1}
%{?el2:%define _without_lua 1}
%{?el2:%define _without_modxorg 1}
%{?el2:%define _without_ocaml 1}
%{?el2:%define _without_pangocairo 1}
%{?el2:%define _without_perl 1}
%{?el2:%define _without_php 1}
%{?el2:%define _without_python 1}
%{?el2:%define _without_rsvg 1}
%{?el2:%define _without_ruby 1}
%{?el2:%define _without_tcltk_devel 1}

Summary: Graph Visualization Tools
Name: graphviz
Version: 2.22.0
Release: 4
License: CPL
Group: Applications/Multimedia
URL: http://www.graphviz.org/

Source: http://www.graphviz.org/pub/graphviz/ARCHIVE/graphviz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, m4, flex, swig, tcl >= 8.3, tk
BuildRequires: libjpeg-devel, libpng-devel, zlib-devel, expat-devel, gcc-c++
BuildRequires: perl
%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3, tk-devel}
# needs version 2.0.34 of gdlib
# BuildRequires: gd-progs, gd-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXext-devel, libXt-devel, libXaw-devel}
%{!?_without_java:BuildRequires: java-devel libgcj-devel}
%{!?_without_ltdl_devel:BuildRequires: libtool-ltdl-devel}
%{?_without_ltdl_devel:BuildRequires: libtool}
%{!?_without_guile:BuildRequires: guile-devel}
%{!?_without_lua:BuildRequires: lua-devel}
%{!?_without_ocaml:BuildRequires: ocaml}
%{!?_without_python:BuildRequires: python python-devel}
%{!?_without_ruby:BuildRequires: ruby, ruby-devel}
%{!?_without_php:BuildRequires: php-devel}
%{!?_without_fontconfig:BuildRequires: fontconfig-devel}
%{!?_without_freetype:BuildRequires: freetype-devel >= 2.0}
%{!?_without_rsvg:BuildRequires: librsvg2-devel}
%{!?_without_pangocairo:BuildRequires: cairo-devel pango-devel gmp-devel gtk2-devel}

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

# Make sure we get the system ltdl.h and not the one in libltdl
%{__perl} -pi -e 's/INCLTDL=.*/INCLTDL=/' configure

%build
%{expand: %%define optflags %{optflags} -ffast-math}
%configure \
	--with-mylibgd \
	--with-x \
	%{?_without_java:--disable-java} \
	%{?_without_ruby:--disable-ruby} \
	%{?_without_ocaml:--disable-ocaml} \
	%{?_without_python:--disable-python} \
	%{?_without_lua:--disable-lua} \
	%{?_without_php:--disable-php} \
	%{?_without_perl:--disable-perl} \
	%{?_without_pangocairo:--without-pangocairo} \
	%{?_without_rsvg:--without-rsvg} \
	%{?_without_freetype:--without-freetype2} \
	%{?_without_fontconfig:--without-fontconfig} \
	%{!?_without_ipsepcola:--with-ipsepcola} \
	%{!?_with_gdk_pixbuf:--without-gdk-pixbuf}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
	pkgconfigdir=%{_libdir}/pkgconfig \
	transform='s,x,x,'
%{__mv} %{buildroot}%{_datadir}/graphviz/doc rpmdoc
%{__chmod} -x %{buildroot}%{_datadir}/graphviz/lefty/*

#check || :
#{__make} -C rtest rtest

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig
%{_bindir}/dot -c

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc *.txt AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man7/graphviz.7*
%{_bindir}/*
%dir %{_datadir}/graphviz/
%{_datadir}/graphviz/lefty/
%{_libdir}/graphviz/*.so.*
%{_libdir}/*.so.*

%files tcl
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3tcl*
%doc %{_mandir}/man3/*3tk*
%{_libdir}/graphviz/tcl/
%{_libdir}/tcl*/*
%{_datadir}/graphviz/demo/*.tcl*
%{_datadir}/graphviz/demo/*_data

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3.*
%{_includedir}/graphviz/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/graphviz/*.la
%exclude %{_libdir}/*.la
%exclude %{_libdir}/graphviz/libgvplugin*
%exclude %{_libdir}/graphviz/*.so

%if %{!?_without_ruby:1}0
%files ruby
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3ruby*
%{_libdir}/graphviz/ruby/
%{_libdir}/*ruby*/*
%{_datadir}/graphviz/demo/*.rb*
%endif

%if %{!?_without_python:1}0
%files python
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3python*
%{_libdir}/graphviz/python/
%{_libdir}/python*/*
%{_datadir}/graphviz/demo/*.py*
%endif

%if %{!?_without_php:1}0
%files php
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3php*
%{_libdir}/graphviz/php/
%{_libdir}/php*/*
%{_datadir}/graphviz/demo/*.php*
%{_datadir}/php/gv.php
%endif

%if %{!?_without_ocaml:1}0
%files ocaml
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3ocaml*
%{_libdir}/graphviz/ocaml/
%endif

%if %{!?_without_guile:1}0
%files guile
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3guile*
%{_libdir}/graphviz/guile/
%endif

%if %{!?_without_java:1}0
%files java
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3java*
%{_libdir}/graphviz/java/
%endif

%if %{!?_without_lua:1}0
%files lua
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3lua*
%{_libdir}/graphviz/lua/
%{_libdir}/lua*/*
%{_datadir}/graphviz/demo/*.lua*
%endif

%if %{!?_without_perl:1}0
%files perl
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3perl*
%{_libdir}/graphviz/perl/
%{_libdir}/perl*/*
%{_datadir}/graphviz/demo/*.pl*
%endif

%files graphs
%defattr(-, root, root, 0755)
%dir %{_datadir}/graphviz/
%{_datadir}/graphviz/graphs/

%files doc
%defattr(-, root, root, 0755)
%doc rpmdoc/*

%changelog
* Thu Mar 13 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 2.22.0-4
- Fix BR for rh7-9
- Explicitly disable freetype/fontconfig when requested to build without

* Thu Mar  5 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 2.22.0-3
- Updated to release 2.22.0.

* Fri Feb 27 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 2.20.3-2
- Fix BR so that language bindings are actually built correctly
- Make subpackages match upstream more closely

* Wed Feb 25 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 2.20.3-1
- BR libtool where libtool-ltdl-devel is not available
- Updated to release 2.20.3.

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
