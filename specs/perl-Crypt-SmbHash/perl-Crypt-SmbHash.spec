# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define rname Crypt-SmbHash

Summary: Crypt-SmbHash module for perl 
Name: perl-Crypt-SmbHash
Version: 0.02
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-SmbHash/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-SmbHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Crypt-SmbHash module for perl

%prep
%setup -n %{rname}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/*

%changelog
* Mon Jun 21 2004 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
