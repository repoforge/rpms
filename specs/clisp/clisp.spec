# $Id$
# Authority: dries

# the name of the dir in _libdir contains the following (wrong?) version
%define real_version 2.46

Summary: ANSI Common Lisp implementation
Name: clisp
Version: 2.46
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
./configure --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} --mandir=%{_mandir}
cd src
./makemake --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} --mandir=%{_mandir} --with-dynamic-ffi > Makefile
%{__make} %{?_smp_mflags} config.lisp
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd src
%{__perl} -pi -e "s|destdir=..localedir.|destdir=%{buildroot}%{_datadir}/locale|g;" po/Makefile*
%{__make} install DESTDIR=%{buildroot}
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
%{_libdir}/clisp-%{real_version}/
%{_datadir}/emacs/site-lisp/clhs.el
%{_datadir}/emacs/site-lisp/clisp-*
%dir %{_datadir}/vim/vimfiles/
%dir %{_datadir}/vim/vimfiles/after/
%dir %{_datadir}/vim/vimfiles/after/syntax/
%{_datadir}/vim/vimfiles/after/syntax/lisp.vim

%changelog
* Sun Jul  6 2008 Dries Verachtert <dries@ulyssis.org> - 2.46-1
- Updated to release 2.46.

* Sun Feb  3 2008 Dries Verachtert <dries@ulyssis.org> - 2.44-1
- Updated to release 2.44.

* Tue Nov 20 2007 Dries Verachtert <dries@ulyssis.org> - 2.43-1
- Updated to release 2.43.

* Wed Oct 17 2007 Dries Verachtert <dries@ulyssis.org> - 2.42-1
- Updated to release 2.42.

* Wed Nov 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.41-2
- Fix links to buildroot, thanks to Scott Dowdle.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.41-1
- Updated to release 2.41.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 2.38-1
- Updated to release 2.38.

* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 2.36-1
- Initial package.
