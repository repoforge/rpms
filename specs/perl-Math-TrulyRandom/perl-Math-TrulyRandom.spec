# $Id: perl-Archive-Tar.spec 120 2004-03-15 17:26:20Z dag $

# Authority: dag

%define rname Math-TrulyRandom

Summary: Perl interface to a truly random number generator function
Name: perl-Math-TrulyRandom
Version: 1.0
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-TrulyRandom/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GARY/Math-TrulyRandom-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Perl interface to a truly random number generator function.

%prep
%setup -n %{rname}-%{version} 

### FIXME: Change to real perl. (Please fix upstream)
%{__perl} -pi -e 's|^#!\s+/.*bin/perl|#!%{__perl}|i' *.pm

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
%doc MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/*

%changelog
* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
