# $Id: $
# Authority: dries

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
# %{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Objective Caml
Name: ocaml
Version: 3.08.2
Release: 2
License: QPL
Group: Development/Languages
URL: http://caml.inria.fr/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://caml.inria.fr/distrib/ocaml-3.08/ocaml-%{version}.tar.bz2
Source1: http://caml.inria.fr/distrib/ocaml-3.08/ocaml-3.08-refman.html.tar.gz
Source2: http://caml.inria.fr/distrib/ocaml-3.08/ocaml-3.08-refman.ps.gz
Source3: http://caml.inria.fr/distrib/ocaml-3.08/ocaml-3.08-refman.info.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gdbm-devel, tcl-devel, tk-devel
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Objective Caml is the latest implementation of the Caml dialect of ML. It
has full support for objects and classes combined with ML-style type
reconstruction, a powerful module calculus in the style of Standard ML (but
retaining separate compilation), a high-performance native code compiler (in
addition to a Caml Light-style bytecode compiler), and labeled arguments
with possible default value. 

%prep
%setup
%setup -T -q -D -a 1
%setup -T -q -D -a 3
cp %{SOURCE2} refman.ps.gz

%build
./configure -prefix %{_prefix} -bindir %{_bindir} -libdir %{_libdir}/ocaml -mandir %{_mandir} -verbose
%{__make} %{?_smp_mflags} world
%{__make} %{?_smp_mflags} bootstrap
%{__make} %{?_smp_mflags} opt
%{__make} %{?_smp_mflags} opt.opt

%install
%{__rm} -rf %{buildroot}
%{__perl} -pi -e 's|^PREFIX=.*|PREFIX=%{buildroot}%{_prefix}|g;' config/Makefile camlp4/config/Makefile
%{__perl} -pi -e 's|^BINDIR=.*|BINDIR=%{buildroot}%{_bindir}|g;' config/Makefile camlp4/config/Makefile
%{__perl} -pi -e 's|^LIBDIR=.*|LIBDIR=%{buildroot}%{_libdir}/ocaml|g;' config/Makefile camlp4/config/Makefile
%{__perl} -pi -e 's|^MANDIR=.*|MANDIR=%{buildroot}%{_mandir}|g;' config/Makefile camlp4/config/Makefile
%makeinstall
%{__install} -d %{buildroot}%{_infodir}
%{__cp} infoman/ocaml*.gz %{buildroot}%{_infodir}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL LICENSE README refman.ps.gz htmlman
%doc %{_mandir}/man1/*
%doc %{_mandir}/man3/*
%{_bindir}/camlp4o.opt
%{_bindir}/ocamlprof
%{_bindir}/ocamllex
%{_bindir}/camlp4
%{_bindir}/ocamlmktop
%{_bindir}/ocamllex.opt
%{_bindir}/ocamlc.opt
%{_bindir}/ocamlbrowser
%{_bindir}/mkcamlp4
%{_bindir}/ocamlyacc
%{_bindir}/ocaml
%{_bindir}/ocamlmklib
%{_bindir}/camlp4o
%{_bindir}/ocpp
%{_bindir}/ocamldep.opt
%{_bindir}/ocamlcp
%{_bindir}/ocamldoc
%{_bindir}/ocamlc
%{_bindir}/ocamldebug
%{_bindir}/ocamlrun
%{_bindir}/ocamlopt.opt
%{_bindir}/labltk
%{_bindir}/camlp4r.opt
%{_bindir}/camlp4r
%{_bindir}/ocamldep
%{_bindir}/ocamldoc.opt
%{_bindir}/ocamlopt
%{_libdir}/ocaml/*.mli
%{_libdir}/ocaml/*.ml
%{_libdir}/ocaml/*.cm?
%{_libdir}/ocaml/*.cmxa
%{_libdir}/ocaml/*.a
%{_libdir}/ocaml/*.o
%{_libdir}/ocaml/addlabels
%{_libdir}/ocaml/camlheader
%{_libdir}/ocaml/camlheader_ur
%{_libdir}/ocaml/expunge
%{_libdir}/ocaml/extract_crc
%{_libdir}/ocaml/ld.conf
%{_libdir}/ocaml/scrapelabels
# directories
%{_libdir}/ocaml/caml
%{_libdir}/ocaml/camlp4
%{_libdir}/ocaml/labltk
%{_libdir}/ocaml/ocamldoc
%{_libdir}/ocaml/stublibs
%{_libdir}/ocaml/threads
%{_libdir}/ocaml/vmthreads
%{_infodir}/*

%changelog
* Thu Mar 03 2005 Dries Verachtert <dries@ulyssis.org> - 3.08.2-2
- Added the documentation, thanks to David Aspinall for informing me 
  about the missing documentation.

* Thu Dec 09 2004 Dries Verachtert <dries@ulyssis.org> - 3.08.2
- Initial package.
