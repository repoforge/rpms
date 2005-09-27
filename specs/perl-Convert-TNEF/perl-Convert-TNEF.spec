# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-TNEF

Summary: Convert-TNEF module for perl
Name: perl-Convert-TNEF
Version: 0.17
Release: 3
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-TNEF/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-TNEF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503, perl-MIME-tools

%description
Convert-TNEF module for perl

%prep
%setup -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
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
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Convert/
%{perl_vendorlib}/Convert/TNEF.pm

%changelog
* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 0.17-3
- Cosmetic changes.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
