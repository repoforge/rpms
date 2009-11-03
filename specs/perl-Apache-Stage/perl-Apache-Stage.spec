# $Id$
# Authority: dag
# Upstream: Andreas J. König <andreas,koenig$anima,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Stage

Summary: Perl module to manage a staging directory
Name: perl-Apache-Stage
Version: 1.20
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Stage/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-Stage-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Apache-Stage is a Perl module to manage a staging directory.

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
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man3/Apache::Stage.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/Stage.pm

%changelog
* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 1.20-1
- Initial package. (using DAR)
