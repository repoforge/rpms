# $Id$
# Authority: shuff
# ExcludeDist: el3 el4
# Rationale: 2.12.0 requires gfortran

%{?el5:%define _with_cairo 1}
%{?el5:%define _with_gcc4 1}
%{?el5:%define _optimization 1}

%{?el4:%define _with_g77 1}
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
Version: 2.12.1
Release: 1%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://www.r-project.org/

Source: ftp://cran.r-project.org/pub/R/src/base/R-2/R-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: blas-devel >= 3.0
BuildRequires: bzip2-devel
BuildRequires: make
BuildRequires: gcc-objc
BuildRequires: java >= 1.6.0
BuildRequires: lapack-devel >= 3.0
BuildRequires: libicu-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtermcap-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: pcre-devel
BuildRequires: perl >= 5.8.0
BuildRequires: readline-devel
BuildRequires: tcl-devel
BuildRequires: tetex-latex
BuildRequires: texinfo-tex
BuildRequires: tk-devel
BuildRequires: zlib-devel
BuildRequires: rpm-macros-rpmforge
%{?_with_cairo:BuildRequires: cairo-devel}
%{!?_without_modxorg:BuildRequires: libICE-devel}
%{!?_without_modxorg:BuildRequires: libSM-devel}
%{!?_without_modxorg:BuildRequires: libXmu-devel}
%{!?_without_modxorg:BuildRequires: libXt-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{?_with_gcc4:BuildRequires: gcc-gfortran}
%{?_with_g77:BuildRequires: gcc4-gfortran}
Requires: blas >= 3.0
Requires: cups
Requires: firefox
Requires: lapack >= 3.0
Requires: xdg-utils
%{?_with_cairo:Requires: evince}
%{!?_with_cairo:Requires: ggv}

### These are the submodules that R provides. Sometimes R modules say they
### depend on one of these submodules rather than just R. These are 
### provided for packager convenience. (taken from Fedora)
Provides: R-base = %{version}
Provides: R-boot = 1.2
Provides: R-class = 7.3
Provides: R-cluster = 1.13.2
Provides: R-codetools = 0.2
Provides: R-datasets = %{version}
Provides: R-foreign = 0.8
Provides: R-graphics = %{version}
Provides: R-grDevices = %{version}
Provides: R-grid = %{version}
Provides: R-KernSmooth = 2.23
Provides: R-lattice = 0.19
Provides: R-MASS = 7.3
Provides: R-Matrix = 0.999375
Provides: R-methods = %{version}
Provides: R-mgcv = 1.7
Provides: R-nlme = 3.1
Provides: R-nnet = 7.3
Provides: R-rpart = 3.1
Provides: R-spatial = 7.3
Provides: R-splines = %{version}
Provides: R-stats = %{version}
Provides: R-stats4 = %{version}
Provides: R-survival = 2.36
Provides: R-tcltk = %{version}
Provides: R-tools = %{version}
Provides: R-utils = %{version}

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

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

echo "%{_libdir}/R/lib/" >R.ld.conf

%build
export F77="gfortran"
export R_BROWSER="%{_bindir}/firefox"
export R_PDFVIEWER="%{_bindir}/xdg-open"
export R_PRINTCMD="lpr"
export CFLAGS=%{CFLAGS}
export CXXFLAGS=%{CXXFLAGS}
export FFLAGS=%{FFLAGS}
export LDFLAGS=%{LDFLAGS}
%configure \
    --enable-R-shlib \
    --with-blas \
    --with-lapack \
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
* Mon Dec 20 2010 Steve Huff <shuff@vecna.org> - 2.12.1-1
- Updated to release 2.12.1.

* Mon Oct 25 2010 Steve Huff <shuff@vecna.org> - 2.12.0-1
- Updated to release 2.12.0.
- 2.12.0 requires gfortran rather than g77.
- Build using Java 1.6.0 or newer.
- Added dependency on LAPACK.
- Captured dependency on libicu.
- Captured dependency on texinfo-tex.

* Thu Sep 30 2010 Steve Huff <shuff@vecna.org> - 2.11.1-1
- Updated to release 2.11.1.
- Needless duplication of BuildRequires: in subpackage was breaking the build.

* Fri Apr 30 2010 Steve Huff <shuff@vecna.org> - 2.11.0-1
- Updated to release 2.11.0.
- Added some additional uncaptured dependencies.
- Added optimization flags for el5.

* Fri Feb 08 2008 Dag Wieers <dag@wieers.com> - 2.6.2-1
- Updated to release 2.6.2.

* Thu Jun 28 2007 Dag Wieers <dag@wieers.com> - 2.5.1-1
- Updated to release 2.5.1.

* Sat Feb 17 2007 Dag Wieers <dag@wieers.com> - 2.4.1-1
- Initial package. (using DAR)
