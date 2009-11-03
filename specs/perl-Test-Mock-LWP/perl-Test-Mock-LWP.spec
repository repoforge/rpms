# $Id$
# Authority: dag
# Upstream: Luke Closs <test-mock-lwp@awesnob.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Mock-LWP

Summary: Perl module named Test-Mock-LWP
Name: perl-Test-Mock-LWP
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Mock-LWP/

Source: http://www.cpan.org/modules/by-module/Test/Test-Mock-LWP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(Test::MockObject) >= 1.08

%description
perl-Test-Mock-LWP is a Perl module.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Test::Mock::HTTP::Request.3pm*
%doc %{_mandir}/man3/Test::Mock::HTTP::Response.3pm*
%doc %{_mandir}/man3/Test::Mock::LWP.3pm*
%doc %{_mandir}/man3/Test::Mock::LWP::UserAgent.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/Mock/
%{perl_vendorlib}/Test/Mock/HTTP/
%{perl_vendorlib}/Test/Mock/LWP/
%{perl_vendorlib}/Test/Mock/LWP.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
