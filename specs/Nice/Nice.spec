# $Id: Nice.spec,v 1.2 2004/02/27 17:08:23 driesve Exp $

# Authority: dries

Summary: An advanced object-oriented programming language.
Name: Nice
Version: 0.9.6
Release: 1
License: GPL
Group: Development/Languages
URL: http://nice.sourceforge.net

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://prdownloads.sourceforge.net/nice/Nice-%{version}-source.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
# to fix: buildrequires: j2se sdk

%description
New object-oriented programming language based on Java, with the following
advanced features: parametric types, anonymous functions, multi-methods,
tuples, optional parameters. Nice also detects more errors during
compilation (null pointers, casts).

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n nice-0.9.6.orig

%build
%{__make} %{?_smp_mflags}

%install
%{__make} PREFIX=$RPM_BUILD_ROOT/usr install

%files
%defattr(-,root,root,0755)
%doc LICENSE NEWS
%{_bindir}/nicec
%{_bindir}/niceunit
/usr/share/java/nice.jar
%{_mandir}/man1/nicec.1.gz
%{_mandir}/man1/niceunit.1.gz
/usr/share/emacs/site-lisp/nice/nice-mode.el
/usr/share/emacs/site-lisp/nice/nice-startup.el
/usr/share/doc/nice/nicec.html

%changelog
* Wed Feb 25 2004 Dries Verachtert <dries@ulyssis.org> 0.9.6-1
- updated to version 0.9.6

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.9.5-1
- first packaging for Fedora Core 1
