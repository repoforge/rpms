# $Id$
# Authority: shuff

%{?el5:%define _with_cairo 1}
%{?el5:%define _with_compat_gcc34 1}
%{?el5:%define _optimization 1}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%if 0%{?_optimization}
#Optimization flags for recent linux systems: see appendix B.3.3 of R-admin
   %define CFLAGS '-O3 -g -std=gnu99'
   %define CXXFLAGS '-O3 -g'
   %define FFLAGS '-O2 -g' 
   %define LDFLAGS '-Bdirect,--hash-stype=both,-Wl,-O1'
%else
#Standard optimization flags for linux: see appendix A.1 of R-admin
   %define CFLAGS '-O2 -g -std=gnu99'
   %define CXXFLAGS '-O2 -g'
   %define FFLAGS '-O2 -g'
   %define LDFLAGS '-Wl,-O1'
%endif

Summary: Language for data analysis and graphics
Name: R
Version: 2.11.0
Release: 1%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://www.r-project.org/

Source: ftp://cran.r-project.org/pub/R/src/base/R-2/R-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gcc-objc, tetex-latex, texinfo 
BuildRequires: libpng-devel, libjpeg-devel, readline-devel, libtermcap-devel
BuildRequires: tcl-devel, tk-devel, ncurses-devel
BuildRequires: blas >= 3.0, pcre-devel, zlib-devel, bzip2-devel
BuildRequires: java-1.4.2-gcj-compat
%{?_with_cairo:BuildRequires: cairo-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{?_with_compat_gcc34:BuildRequires: compat-gcc-34-g77}
%{!?_with_compat_gcc34:BuildRequires: gcc-g77}
BuildRequires: rpm-macros-rpmforge
Requires: cups, firefox, xdg-utils
%{?_with_cairo:Requires: evince}
%{!?_with_cairo:Requires: ggv}

### These are the submodules that R provides. Sometimes R modules say they
### depend on one of these submodules rather than just R. These are 
### provided for packager convenience. (taken from Fedora)
Provides: R-base = %{version}
Provides: R-boot = 1.2
Provides: R-class = %{version}
Provides: R-cluster = 1.11.11
Provides: R-codetools = 0.2
Provides: R-datasets = %{version}
Provides: R-foreign = 0.8
Provides: R-graphics = %{version}
Provides: R-grDevices = %{version}
Provides: R-grid = %{version}
Provides: R-KernSmooth = 2.22
Provides: R-lattice = 0.17
Provides: R-MASS = %{version}
Provides: R-methods = %{version}
Provides: R-mgcv = 1.4
Provides: R-nlme = 3.1
Provides: R-nnet = %{version}
Provides: R-rpart = 3.1
Provides: R-spatial = %{version}
Provides: R-splines = %{version}
Provides: R-stats = %{version}
Provides: R-stats4 = %{version}
Provides: R-survival = 2.34
Provides: R-tcltk = %{version}
Provides: R-tools = %{version}
Provides: R-utils = %{version}
Provides: R-VR = 7.2

# we do not provide any Perl modules outside the R:: tree
%filter_from_provides /^perl.*File::Copy/d
%filter_setup

%description
A language and environment for statistical computing and graphics. 
R is similar to the award-winning S system, which was developed at 
Bell Laboratories by John Chambers et al. It provides a wide 
variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

R is designed as a true computer language with control-flow
constructions for iteration and alternation, and it allows users to
add additional functionality by defining new functions. For
computationally intensive tasks, C, C++ and Fortran code can be linked
and called at run time.

%package -n libRmath
Summary: standalone math library from the R project
Group: Development/Libraries

%description -n libRmath
A standalone library of mathematical and statistical functions derived
from the R project.  This packages provides the shared libRmath library.

%package -n libRmath-devel
Summary: standalone math library from the R project
Group: Development/Libraries
Requires: libRmath = %{version}-%{release}
Requires: pkgconfig

%description -n libRmath-devel
A standalone library of mathematical and statistical functions derived
from the R project.  This packages provides the static libRmath library
and header files.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gcc-c++, gcc-objc, tetex-latex, texinfo 
Requires: libpng-devel, libjpeg-devel, readline-devel, libtermcap-devel
Requires: tcl-devel, tk-devel, pkgconfig
%{?_with_cairo:BuildRequires: cairo-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{?_with_compat_gcc34:BuildRequires: compat-gcc-34-g77}
%{!?_with_compat_gcc34:BuildRequires: gcc-g77}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

echo "%{_libdir}/R/lib/" >R.ld.conf

%build
export F77="g77"
export R_BROWSER="%{_bindir}/firefox"
export R_PDFVIEWER="%{_bindir}/xdg-open"
export R_PRINTCMD="lpr"
export CFLAGS=%{CFLAGS}
export CXXFLAGS=%{CXXFLAGS}
export FFLAGS=%{FFLAGS}
export LDFLAGS=%{LDFLAGS}
%configure \
	--enable-R-shlib \
	--with-system-bzlib \
	--with-system-pcre \
	--with-system-zlib \
	--with-tcl-config="%{_libdir}/tclConfig.sh" \
	--with-tk-config="%{_libdir}/tkConfig.sh"
%{__make}
%{__make} -C src/nmath/standalone
#make check-all
%{__make} pdf info

%install
%{__rm} -rf %{buildroot}
%makeinstall install-info
%makeinstall -C src/nmath/standalone

%{__perl} -pi -e 's|R_HOME_DIR=.*|R_HOME_DIR=%{_libdir}/R|' bin/R
%{__install} -Dp -m0755 bin/R %{buildroot}%{_libdir}/R/bin/R
%{__install} -Dp -m0755 bin/R %{buildroot}%{_bindir}/R

%{__install} -Dp -m0644 R.ld.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/R-%{_target}.conf

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/R/{AUTHORS,COPYING*,COPYRIGHTS,FAQ,NEWS,ONEWS,RESOURCES,THANKS}

%post 
/sbin/install-info %{_infodir}/R-FAQ.info.gz %{_infodir}/dir 2>/dev/null
/sbin/install-info %{_infodir}/R-admin.info.gz %{_infodir}/dir 2>/dev/null
/sbin/install-info %{_infodir}/R-exts.info.gz %{_infodir}/dir 2>/dev/null
/sbin/install-info %{_infodir}/R-intro.info.gz %{_infodir}/dir 2>/dev/null
/sbin/install-info %{_infodir}/R-lang.info.gz %{_infodir}/dir 2>/dev/null
/sbin/ldconfig

%preun 
/sbin/install-info --delete R-FAQ %{_infodir}/dir 2>/dev/null
/sbin/install-info --delete R-admin %{_infodir}/dir 2>/dev/null
/sbin/install-info --delete R-exts %{_infodir}/dir 2>/dev/null
/sbin/install-info --delete R-intro %{_infodir}/dir 2>/dev/null
/sbin/install-info --delete R-lang %{_infodir}/dir 2>/dev/null

%postun -p /sbin/ldconfig

%post -n libRmath -p /sbin/ldconfig
%postun -n libRmath -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL *NEWS README VERSION
%doc doc/AUTHORS doc/COPYING* doc/COPYRIGHTS 
%doc doc/CRAN_mirrors.csv doc/FAQ doc/KEYWORDS
%doc doc/RESOURCES doc/THANKS doc/manual/
%doc %{_mandir}/man?/*
%doc %{_infodir}/R-*.info*
%config %{_sysconfdir}/ld.so.conf.d/R-%{_target}.conf
%{_bindir}/R
%{_bindir}/Rscript

%{_libdir}/R/
%exclude %{_datadir}/info/dir*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/pkgconfig/libR.pc
%{_libdir}/pkgconfig/libRmath.pc

%files -n libRmath
%defattr(-, root, root, 0755)
%{_libdir}/libRmath.so

%files -n libRmath-devel
%defattr(-, root, root, 0755)
%{_includedir}/Rmath.h
%{_libdir}/libRmath.a

%changelog
* Fri Apr 30 2010 Steve Huff <shuff@vecna.org> - 2.11.0-1
- Updated to release 2.11.0.
- Added some additional uncaptured dependencies.
- Added optimization flags for el5.

* Thu Jun 28 2007 Dag Wieers <dag@wieers.com> - 2.5.1-1
- Updated to release 2.5.1.

* Sat Feb 17 2007 Dag Wieers <dag@wieers.com> - 2.4.1-1
- Initial package. (using DAR)
