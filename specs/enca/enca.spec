# $Id$

# Authority: dries

Summary: charset and encoding analyser
Name: enca
Version: 1.3
Release: 2
License: GPL
Group: Applications/Text
URL: http://trific.ath.cx/software/enca/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://trific.ath.cx/Ftp//enca/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: recode, recode-devel
Requires: recode

%description
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
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
/usr/include/enca.h
/usr/lib/libenca.a
/usr/lib/libenca.la
/usr/lib/libenca.so.0.4.0
/usr/lib/pkgconfig/enca.pc
/usr/libexec/enca/extconv/cstocs
/usr/libexec/enca/extconv/map
/usr/libexec/enca/extconv/piconv
/usr/libexec/enca/extconv/recode
/usr/libexec/enca/extconv/umap
/usr/share/man/man1/enca.1.gz

%changelog
* Sun Feb 29 2004 Dries Verachtert <dries@ulyssis.org> 1.3-2
- cleanup of spec file

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 1.3-1
- first packaging for Fedora Core 1
