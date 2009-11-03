# $Id$

# Authority: dries

Summary: Advanced object-oriented programming language
Name: Nice
Version: 0.9.6
Release: 1.2%{?dist}
License: GPL
Group: Development/Languages
URL: http://nice.sourceforge.net

Source: http://dl.sf.net/nice/Nice-%{version}-source.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# to fix: buildrequires: j2se sdk

%description
New object-oriented programming language based on Java, with the following
advanced features: parametric types, anonymous functions, multi-methods,
tuples, optional parameters. Nice also detects more errors during
compilation (null pointers, casts).

%prep
%setup -n nice-0.9.6.orig

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} PREFIX=%{buildroot}/usr install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE NEWS
%{_bindir}/nicec
%{_bindir}/niceunit
%{_datadir}/java/nice.jar
%{_mandir}/man1/nicec.1.gz
%{_mandir}/man1/niceunit.1.gz
%{_datadir}/emacs/site-lisp/nice/nice-mode.el
%{_datadir}/emacs/site-lisp/nice/nice-startup.el
%{_datadir}/doc/nice/nicec.html

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1.2
- Rebuild for Fedora Core 5.

* Wed Feb 25 2004 Dries Verachtert <dries@ulyssis.org> 0.9.6-1
- updated to version 0.9.6

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.9.5-1
- first packaging for Fedora Core 1
