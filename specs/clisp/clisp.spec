# $Id$
# Authority: dries

Summary: ANSI Common Lisp implementation
Name: clisp
Version: 2.41
Release: 1
License: GPL
Group: Development/Languages
URL: http://clisp.cons.org

Source: http://dl.sf.net/clisp/clisp-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel, libsigsegv-devel, ncurses-devel

%description
GNU CLISP is an ANSI Common Lisp implementation with an interpreter, 
compiler, debugger, object system (CLOS, MOP), sockets, fast bignums, 
and foreign language interface

%prep
%setup

%build
./configure --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib --mandir=/usr/share/man
cd src
./makemake --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib --mandir=/usr/share/man --with-dynamic-ffi > Makefile
%{__make} %{?_smp_mflags} config.lisp
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd src
%makeinstall
cd -
%{__mv} %{buildroot}%{_docdir}/clisp rpmdocs
%find_lang clisp
%find_lang clisplow
%{__cat} clisplow.lang >> clisp.lang

%clean
%{__rm} -rf %{buildroot}

%files -f clisp.lang
%defattr(-, root, root, 0755)
%doc rpmdocs/*
%doc %{_mandir}/man1/clisp*
%{_bindir}/clisp
%{_libdir}/clisp/
%{_datadir}/emacs/site-lisp/clhs.el
%{_datadir}/emacs/site-lisp/clisp-*

%changelog
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.41-1
- Updated to release 2.41.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 2.38-1
- Updated to release 2.38.

* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 2.36-1
- Initial package.
