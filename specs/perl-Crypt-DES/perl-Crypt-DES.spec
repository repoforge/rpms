# $Id$
# Authority: axel

%define rname Crypt-DES

Summary: Crypt-DES module for perl 
Name: perl-Crypt-DES
Version: 2.03
Release: 2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-DES/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-DES-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Crypt-DES module for perl

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
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 2.03-0
- Initial package. (using DAR)
