# $Id$
# Authority: dag

%define real_name BerkeleyDB

Summary: Perl extension for Berkeley DB version 2, 3 or 4
Name: perl-BerkeleyDB
Version: 0.25
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/BerkeleyDB/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/BerkeleyDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Perl extension for Berkeley DB version 2, 3 or 4.

%prep
%setup -n %{real_name}-%{version} 

%build
FLAGS="%{optflags}" %{__perl} Makefile.PL \
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
%doc Changes MANIFEST README Todo
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 0.25-0
- Initial package. (using DAR)
