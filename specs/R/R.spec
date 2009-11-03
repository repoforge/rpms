# $Id$
# Authority: dag


%{?el5:%define _with_compat_gcc34 1}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: Language for data analysis and graphics
Name: R
Version: 2.5.1
Release: 1%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://www.r-project.org/

Source: ftp://cran.r-project.org/pub/R/src/base/R-2/R-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, tetex-latex, texinfo 
BuildRequires: libpng-devel, libjpeg-devel, readline-devel, libtermcap-devel
BuildRequires: tcl-devel, tk-devel
BuildRequires: blas >= 3.0, pcre-devel, zlib-devel
BuildRequires: java-1.4.2-gcj-compat
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{?_with_compat_gcc34:BuildRequires: compat-gcc-34-g77}
%{!?_with_compat_gcc34:BuildRequires: gcc-g77}
Requires: ggv, cups, firefox

### These are the submodules that R provides. Sometimes R modules say they
### depend on one of these submodules rather than just R. These are 
### provided for packager convenience. (taken from Fedora)
Provides: R-base = %{version}
Provides: R-boot = 1.2
Provides: R-class = %{version}
Provides: R-cluster = 1.10.5
Provides: R-datasets = %{version}
Provides: R-foreign = 0.8
Provides: R-graphics = %{version}
Provides: R-grDevices = %{version}
Provides: R-grid = %{version}
Provides: R-KernSmooth = 2.22
Provides: R-lattice = 0.13
Provides: R-MASS = %{version}
Provides: R-methods = %{version}
Provides: R-mgcv = 1.3
Provides: R-nlme = 3.1
Provides: R-nnet = %{version}
Provides: R-rpart = 3.1
Provides: R-spatial = %{version}
Provides: R-splines = %{version}
Provides: R-stats = %{version}
Provides: R-stats4 = %{version}
Provides: R-survival = 2.24
Provides: R-tcltk = %{version}
Provides: R-tools = %{version}
Provides: R-utils = %{version}
Provides: R-VR = 7.2

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

%description -n libRmath-devel
A standalone library of mathematical and statistical functions derived
from the R project.  This packages provides the static libRmath library
and header files.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gcc-c++, gcc-g77, tetex-latex, texinfo 
Requires: libpng-devel, libjpeg-devel, readline-devel, libtermcap-devel
Requires: XFree86-devel, tcl-devel, tk-devel

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
export R_PDFVIEWER="%{_bindir}/ggv"
export R_PRINTCMD="lpr"
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
%doc NEWS ONEWS README VERSION doc/AUTHORS doc/COPYING* doc/COPYRIGHTS doc/FAQ
%doc doc/RESOURCES doc/THANKS doc/manual/R-admin.pdf doc/manual/R-data.pdf
%doc doc/manual/R-FAQ.pdf doc/manual/R-intro.pdf doc/manual/R-lang.pdf
%doc %{_mandir}/man1/*.1*
%doc %{_infodir}/R-*.info*
%config %{_sysconfdir}/ld.so.conf.d/R-%{_target}.conf
%{_bindir}/R
%{_bindir}/Rscript

%{_libdir}/R/
%exclude %{_datadir}/info/dir*

%files devel
%defattr(-, root, root, 0755)
%doc doc/manual/R-exts.pdf
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
* Thu Jun 28 2007 Dag Wieers <dag@wieers.com> - 2.5.1-1
- Updated to release 2.5.1.

* Sat Feb 17 2007 Dag Wieers <dag@wieers.com> - 2.4.1-1
- Initial package. (using DAR)
