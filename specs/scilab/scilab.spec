# $Id: $

# Authority: dries
# Upstream: scilab@inria.fr
# Screenshot: http://scilabsoft.inria.fr/images/session_27.png

# ExcludeDist: el3 fc1

Summary: Scientific software package
Name: scilab
Version: 3.1.1
Release: 1
License: Other
Group: Applications/Engineering
URL: http://scilabsoft.inria.fr/

Source: http://scilabsoft.inria.fr/download/stable/scilab-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tcl tk Xaw3d-devel, libpng10-devel, tcl-devel, tk-devel
BuildRequires: perl gtkhtml2-devel, gcc-c++, gtk+-devel
Requires: libpng10
%{?fc4:BuildRequires: gcc-gfortran}
%{!?fc4:BuildRequires: gcc-g77}


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

%build
%configure \
	--with-gcc \
	--with-g77 \
	--with-gnu \
	--with-xaw3d \
	--with-gtk \
	--with-x
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_libdir} \
	%{buildroot}%{_bindir}
%{__perl} -pi.orig -e '
	s|/usr/bin|%{buildroot}%{_bindir}|g;
	s|ln -fs \$\{LIBPREFIX\}|ln -fs %{_libdir}|g;
	' Makefile

%{__perl} -pi -e '
	s|/bin/sh5|/bin/sh|g;
	' bin/dold
%makeinstall LIBPREFIX=%{buildroot}%{_libdir}

%{__perl} -pi -e '
	s|%{buildroot}||g;
	' %{buildroot}%{_libdir}/scilab-%{version}/bin/* \
	config/configuration \
	util/Blatdoc* Makefile* Path.incl


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_libdir}/scilab-%{version}
%exclude %{_libdir}/scilab-%{version}/examples/mex-examples/mexglx

%changelog
* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> - 3.1.1
- Update to release 3.1.1.

* Wed Jul 14 2004 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Initial package.
