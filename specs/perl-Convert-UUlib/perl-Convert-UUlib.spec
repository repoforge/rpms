# $Id$

# Authority: dag

%define rname Convert-UUlib

Summary: Convert-UUlib module for perl
Name: perl-Convert-UUlib
Version: 1.01
Release: 0
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-UUlib/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/Convert-UUlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
Convert-UUlib module for perl.

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes COPYING* MANIFEST README doc/*
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*/*

%changelog
* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.01-0
- Updated to release 1.01.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.31-0
- Updated to release 0.31.
- Initial package. (using DAR)
