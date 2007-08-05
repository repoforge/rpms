# $Id$
# Authority: dag
# Upstream: Marcel GrE<uuml>nauer <marcel$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Distribution

Summary: perform tests on all modules of a distribution
Name: perl-Test-Distribution
Version: 1.26
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Distribution/

Source: http://www.cpan.org/modules/by-module/Test/Test-Distribution-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Module::Build)

%description
perform tests on all modules of a distribution.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Test::Distribution.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Distribution/
%{perl_vendorlib}/Test/Distribution.pm

%changelog
* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 1.26-1
- Initial package. (using DAR)
