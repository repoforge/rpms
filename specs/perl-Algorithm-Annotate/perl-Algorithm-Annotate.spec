# $Id$
# Authority: dag
# Upstream: Chia-liang Kao <clkao$clkao,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Annotate

Summary: Perl module to represent a series of changes in annotate form 
Name: perl-Algorithm-Annotate
Version: 0.10
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Annotate/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Annotate-%{version}.tar.gz
#Source: http://www.cpan.org/authors/id/C/CL/CLKAO/Algorithm-Annotate-0.10.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Algorithm-Annotate is a Perl module to represent a series of changes
in annotate form.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST
%doc %{_mandir}/man3/Algorithm::Annotate.3pm*
%dir %{perl_vendorlib}/Algorithm/
#%{perl_vendorlib}/Algorithm/Annotate/
%{perl_vendorlib}/Algorithm/Annotate.pm

%changelog
* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
