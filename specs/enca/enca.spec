# $Id$

# Authority: dries

Summary: charset and encoding analyser
Name: enca
Version: 1.4
Release: 1
License: GPL
Group: Applications/Text
URL: http://trific.ath.cx/software/enca/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://kf.fyz.fce.vutbr.cz/~yeti/Ftp/enca/enca-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: recode, recode-devel, gcc-c++
Requires: recode

%description
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings.

%prep
%{__rm} -rf %{buildroot}
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
%{__make}  install-strip
mv ${RPM_BUILD_ROOT}/usr/share/gtk-doc/html ./html

%files
%defattr(-,root,root,0755)
%doc README html AUTHORS ChangeLog COPYING FAQ INSTALL NEWS THANKS TODO
%{_bindir}/enca
%{_includedir}/enca.h
%{_libdir}/libenca.a
%{_libdir}/libenca.la
%{_libdir}/libenca.so.0.4.0
%{_libdir}/pkgconfig/enca.pc
/usr/libexec/enca/extconv/cstocs
/usr/libexec/enca/extconv/map
/usr/libexec/enca/extconv/piconv
/usr/libexec/enca/extconv/recode
/usr/libexec/enca/extconv/umap
%{_datadir}/man/man1/enca.1.gz

%changelog
* Thu May 20 2004 Dries Verachtert <dries@ulyssis.org> 1.4-1
- update to 1.4

* Sun Feb 29 2004 Dries Verachtert <dries@ulyssis.org> 1.3-2
- cleanup of spec file

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 1.3-1
- first packaging for Fedora Core 1
