# $Id$

# Authority: dag

%define real_name ExtUtils-PkgConfig

Summary: ExtUtils-PkgConfig module for perl
Name: perl-ExtUtils-PkgConfig
Version: 1.07
Release: 1
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-PkgConfig/

Source: http://dl.sf.net/gtk2-perl/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
This module is a simplistic Perl interface to the pkg-config command-line
utility, for use in the Makefile.PLs used to build Perl modules which wrap
the libraries about which pkg-config knows.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/ \
                %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/ \
                %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.03-0
- Updated to release 1.03.

* Sat Oct 11 2003 Dag Wieers <dag@wieers.com> - 1.01-0
- Initial package. (using DAR)
