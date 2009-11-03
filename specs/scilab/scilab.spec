# $Id$
# Authority: dries
# Upstream: scilab@inria.fr

# Screenshot: http://scilabsoft.inria.fr/images/session_27.png

Summary: Scientific software package
Name: scilab
Version: 4.0
Release: 1%{?dist}
License: Other
Group: Applications/Engineering
URL: http://scilabsoft.inria.fr/

Source: http://scilabsoft.inria.fr/download/stable/scilab-%{version}-src.tar.gz
Patch: scilab-4.0.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gcc-g77
#%{!?_without_gfortran:BuildRequires: gcc4-gfortran}
BuildRequires: tcl-devel >= 8.4, tk-devel >= 8.4, Xaw3d-devel, libpng10-devel
BuildRequires: readline-devel, gtk2-devel, gtkhtml2-devel, vte-devel
BuildRequires: libxslt

%description
Scilab a numerical computation system similiar to matlab or simulink. Scilab
includes hundreds of mathematical functions, and programs from various
languages (such as C or Fortran) can be added interactively. It has
sophisticated data structures (including lists, polynomials, rational
functions, and linear systems), an interpreter, and a high-level programming
language. Scilab has been designed to be an open system where the user can
define new data types and operations on these data types by using
overloading. A number of toolboxes are available with the system.

%prep
%setup
%patch -p1

%build
%{__perl} -pi.orig -e 's|-fwritable-strings||g;' configure
%configure \
	--with-gcc \
	--with-gfortran \
	--with-gtk2 \
	--with-tcl-library="%{_libdir}" \
	--without-java
#%{!?_without_gfortran:--with-gfortran} \
# ../include/pvmtev.h nodig in pvm3/src/global.h
#(echo '#include "../include/pvmtev.h"'; cat pvm3/src/global.h) > pvm3/src/global.h.temp
#%{__mv} pvm3/src/global.h.temp pvm3/src/global.h
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_libdir}
%{__perl} -pi.orig -e '
		s|/usr/bin|%{buildroot}%{_bindir}|g;
		s|/usr/lib|%{buildroot}%{_libdir}|g;
		s|ln -fs \$\(PREFIX\)/lib|ln -fs %{_libdir}|g;
	' Makefile

%{__perl} -pi -e 's|/bin/sh5|/bin/sh|g;' bin/dold
%{__make} install PREFIX="%{buildroot}%{_prefix}" LIBPREFIX="%{buildroot}%{_libdir}"

%{__perl} -pi -e ' s|%{buildroot}||g;' %{buildroot}%{_libdir}/scilab-%{version}/bin/*

#%{__perl} -pi -e '
#		s|SCI="/scilab-4.0"|SCI="%{_libdir}/scilab-4.0"|g;
#		s|\$SCI/bin/zterm|%{_bindir}/xterm|g;
#	' %{buildroot}%{_libdir}/scilab-%{version}/bin/scilab

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS CHANGES licence.txt README_Unix Version.incl
%{_bindir}/intersci
%{_bindir}/intersci-n
%{_bindir}/scilab
%{_libdir}/scilab-%{version}/
%exclude %{_libdir}/scilab-%{version}/examples/mex-examples/mexglx

%changelog
* Fri Apr 14 2006 Rene van Paassen <repa@lrcslap2.lr.tudelft.nl> - 4.0-1
- Updated to release 4.0.
- Using gtk2 instead of athena widgets.
- Created a patch for periGtk.c; sent patch upstream too.
- Removed gtk+ / gnome build dependencies. 

* Mon Aug 01 2005 Dries Verachtert <dries@ulyssis.org> - 3.1.1-2
- Rebuild.

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> - 3.1.1-1
- Updated to release 3.1.1.

* Wed Jul 14 2004 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Initial package.
