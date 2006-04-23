# $Id: $
# Authority: dries
# Upstream: scilab@inria.fr

# Screenshot: http://scilabsoft.inria.fr/images/session_27.png

### (dag) Is there a reason to exclude these ?
##ExcludeDist: el3 fc1

Summary: Scientific software package
Name: scilab
Version: 4.0
Release: 1
License: Other
Group: Applications/Engineering
URL: http://scilabsoft.inria.fr/

Source: http://scilabsoft.inria.fr/download/stable/scilab-%{version}-src.tar.gz
Patch: scilab-4.0.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tcl, tk, Xaw3d-devel, libpng10-devel, tcl-devel, tk-devel
BuildRequires: perl, gtkhtml2-devel, gcc-c++, gtk2-devel
BuildRequires: libxslt, vte-devel
BuildRequires: readline-devel
BuildRequires: gcc-gfortran

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
	--without-java \
	--with-tcl-library="%{_libdir}"
# ../include/pvmtev.h nodig in pvm3/src/global.h
#(echo '#include "../include/pvmtev.h"'; cat pvm3/src/global.h) > pvm3/src/global.h.temp
#%{__mv} pvm3/src/global.h.temp pvm3/src/global.h
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_libdir} \
	%{buildroot}%{_bindir}
%{__perl} -pi.orig -e '
	s|/usr/bin|%{buildroot}%{_bindir}|g;
	s|ln -fs \$\(PREFIX\)/lib|ln -fs %{_libdir}|g;
	' Makefile

%{__perl} -pi -e '
	s|/bin/sh5|/bin/sh|g;
	' bin/dold
%makeinstall PREFIX=%{buildroot}%{_prefix} LIBPREFIX=%{buildroot}%{_libdir}

%{__perl} -pi -e '
	s|%{buildroot}||g;
	' %{buildroot}%{_libdir}/scilab-%{version}/bin/* \
	config/configuration \
	util/Blatdoc* Makefile* Path.incl


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS CHANGES README_Unix Version.incl licence.txt
%{_bindir}/*
%{_libdir}/scilab-%{version}/
%exclude %{_libdir}/scilab-%{version}/examples/mex-examples/mexglx

%changelog
* Fri Apr 14 2006 Rene van Paassen <repa@lrcslap2.lr.tudelft.nl> - 4.0-2
- Updated to release 4.0.
- Using gtk2 instead of athena widgets.
- Created a patch for periGtk.c; sent patch upstream too.
- Removed gtk+ / gnome build dependencies. 

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.1.1-2.2
- Rebuild for Fedora Core 5.

* Mon Aug 01 2005 Dries Verachtert <dries@ulyssis.org> - 3.1.1-2
- Rebuild.

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> - 3.1.1-1
- Update to release 3.1.1.

* Wed Jul 14 2004 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Initial package.
