# $Id$
# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}
%{?rh6:%define _without_tcltk_devel 1}

Summary: Objective Caml
Name: ocaml
Version: 3.10.1
Release: 1
License: QPL/LGPL
Group: Development/Languages
URL: http://caml.inria.fr/

Source0: http://caml.inria.fr/distrib/ocaml-3.10/ocaml-%{version}.tar.bz2
Source1: http://caml.inria.fr/distrib/ocaml-3.10/ocaml-3.10-refman.html.tar.gz
Source2: http://caml.inria.fr/distrib/ocaml-3.10/ocaml-3.10-refman.ps.gz
Source3: http://caml.inria.fr/distrib/ocaml-3.10/ocaml-3.10-refman.info.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, gdbm-devel, emacs
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3, tk-devel}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.3, tk}
Obsoletes: ocaml-ocamldoc <= %{version}-%{release}

%description
Objective Caml is the latest implementation of the Caml dialect of ML. It
has full support for objects and classes combined with ML-style type
reconstruction, a powerful module calculus in the style of Standard ML (but
retaining separate compilation), a high-performance native code compiler (in
addition to a Caml Light-style bytecode compiler), and labeled arguments
with possible default value.

%package labltk
Summary: Tk bindings for Objective Caml
Group: Development/Languages
Requires: ocaml = %{version}-%{release}
Obsoletes: labltk <= %{version}-%{release}

%description labltk
A library for interfacing Objective Caml with the scripting language
Tcl/Tk. It include the OCamlBrowser code editor / library browser.

%package camlp4
Group: Development/Languages
Summary: Pre-Processor-Pretty-Printer for OCaml
Requires: ocaml = %{version}-%{release}
Obsoletes: camlp4 <= %{version}-%{release}

%description camlp4
Camlp4 is a Pre-Processor-Pretty-Printer for OCaml, parsing a source
file and printing some result on standard output.

%package -n emacs-ocaml
Summary: Emacs mode for Objective Caml
Group: Applications/Editors
Requires: ocaml = %{version}-%{release}
Obsoletes: ocaml-emacs <= %{version}

%description -n emacs-ocaml
Emacs mode for Objective Caml.

%prep
%setup -T -b 0
%setup -T -D -a 1
%setup -T -D -a 3
%{__cp} -v %{SOURCE2} refman.ps.gz

%build
./configure \
    -cc "%{__cc} %{optflags}" \
    -bindir "%{_bindir}" \
    -libdir "%{_libdir}/ocaml" \
    -mandir "%{_mandir}" \
    -prefix "%{_prefix}" \
    -verbose \
    -with-pthread \
%{!?_without_modxorg:-x11lib "%{_libdir}"} \
%{?_without_modxorg:-x11lib "%{_prefix}/X11/%{_lib}"}
#%{__make} %{?_smp_mflags} world bootstrap opt opt.opt
%{__make} world bootstrap opt opt.opt
%{__make} -C emacs ocamltags

%install
%{__rm} -rf %{buildroot}
%{__make} install BINDIR="%{buildroot}%{_bindir}" LIBDIR="%{buildroot}%{_libdir}/ocaml" MANDIR="%{buildroot}%{_mandir}"
%{__perl} -pi.orig -e 's|^%{buildroot}||' %{buildroot}%{_libdir}/ocaml/ld.conf

%{__make} -C emacs install install-ocamltags BINDIR="%{buildroot}%{_bindir}" EMACSDIR="%{buildroot}%{_datadir}/emacs/site-lisp"

%{__install} -d %{buildroot}%{_infodir}
%{__install} -p -m0644 infoman/ocaml*.gz %{buildroot}%{_infodir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes htmlman/ INSTALL LICENSE README refman.ps.gz
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man3/*.3*
%doc %{_infodir}/ocaml*
%{_bindir}/*
%{_libdir}/ocaml/

### in ocaml-camlp4
%exclude %{_bindir}/camlp4*
%exclude %{_bindir}/mkcamlp4
%exclude %{_libdir}/ocaml/camlp4/

### in ocaml-labltk
%exclude %{_bindir}/labltk
%exclude %{_bindir}/ocamlbrowser
%exclude %{_libdir}/ocaml/labltk/
%exclude %{_libdir}/ocaml/stublibs/dlllabltk.so
%exclude %{_libdir}/ocaml/stublibs/dlltkanim.so

### in emacs-ocaml
%exclude %{_bindir}/ocamltags

%files camlp4
%defattr(-, root, root, 0755)
%{_bindir}/camlp4*
%{_bindir}/mkcamlp4
%dir %{_libdir}/ocaml/
%{_libdir}/ocaml/camlp4/

%files labltk
%defattr(-, root, root, 0755)
%doc otherlibs/labltk/examples_*tk
%{_bindir}/labltk
%{_bindir}/ocamlbrowser
%dir %{_libdir}/ocaml/
%dir %{_libdir}/ocaml/stublibs/
%{_libdir}/ocaml/labltk/
%{_libdir}/ocaml/stublibs/dlllabltk.so
%{_libdir}/ocaml/stublibs/dlltkanim.so

%files -n emacs-ocaml
%defattr(-, root, root, 0755)
%doc emacs/README
%{_bindir}/ocamltags
%dir %{_datadir}/emacs/
%dir %{_datadir}/emacs/site-lisp/
%{_datadir}/emacs/site-lisp/*.el
%{_datadir}/emacs/site-lisp/*.elc

%changelog
* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 3.10-1
- Updated to release 3.10.

* Wed Jan 04 2006 Dries Verachtert <dries@ulyssis.org> - 3.09.1-1
- Updated to release 3.09.1.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> - 3.08.4-1
- Updated to release 3.08.4.

* Tue Aug 09 2005 Dag Wieers <dag@wieers.com> - 3.08.3-2
- Cleanup and fixes to build on x86_64.
- Added subpackages and obsoletes for FE.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 3.08.3-1
- Update to release 3.08.3.

* Thu Mar 03 2005 Dries Verachtert <dries@ulyssis.org> - 3.08.2-2
- Added the documentation, thanks to David Aspinall for informing me
  about the missing documentation.

* Thu Dec 09 2004 Dries Verachtert <dries@ulyssis.org> - 3.08.2
- Initial package.
