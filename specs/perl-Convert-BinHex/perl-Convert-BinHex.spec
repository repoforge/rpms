# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-BinHex

Summary: Extract data from Macintosh BinHex files
Name: perl-Convert-BinHex
Version: 1.119
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-BinHex/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-BinHex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Convert-BinHex is a set of Perl classes to extract data from Macintosh
BinHex files.

%prep
%setup -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL \
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
%doc COPYING MANIFEST README*
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Convert/

%changelog
* Sun Mar 06 2005 Dag Wieers <dag@wieers.com> - 1.119-1
- Initial package. (using DAR)
