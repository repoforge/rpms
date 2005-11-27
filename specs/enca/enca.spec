# $Id$

# Authority: dries

Summary: Charset and encoding analyser
Name: enca
Version: 1.8
Release: 1
License: GPL
Group: Applications/Text
URL: http://trific.ath.cx/software/enca/

Source: http://trific.ath.cx/Ftp//enca/enca-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: recode, recode-devel, gcc-c++
Requires: recode

%description
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot} _html
%{__make} install DESTDIR=%{buildroot}
%{__mv} %{buildroot}%{_datadir}/gtk-doc/html _html

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README THANKS TODO
%{_bindir}/enca
%{_bindir}/enconv
%{_includedir}/enca.h
%{_libdir}/libenca.*
%{_libdir}/pkgconfig/enca.pc
%{_libexecdir}/enca/extconv/cstocs
%{_libexecdir}/enca/extconv/map
%{_libexecdir}/enca/extconv/piconv
%{_libexecdir}/enca/extconv/recode
%{_libexecdir}/enca/extconv/umap
%{_datadir}/man/man1/enca.1*
%{_datadir}/man/man1/enconv.1*


%changelog
* Sun Nov 27 2005 Dries Verachtert <dries@ulyssis.org> 1.8-1
- Update to release 1.8.

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> 1.7-1
- Update to release 1.7.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> 1.6-1
- update to 1.6

* Thu May 20 2004 Dries Verachtert <dries@ulyssis.org> 1.4-1
- update to 1.4

* Sun Feb 29 2004 Dries Verachtert <dries@ulyssis.org> 1.3-2
- cleanup of spec file

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 1.3-1
- first packaging for Fedora Core 1
