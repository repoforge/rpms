# $Id$
# Authority: dag
# Upstream: Andy Armstrong <andy$hexten,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Harness

Summary: Run Perl standard test scripts with statistics
Name: perl-Test-Harness
Version: 3.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Harness/

Source: http://www.cpan.org/modules/by-module/Test/Test-Harness-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Run Perl standard test scripts with statistics.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes Changes-2.64 HACKING.pod MANIFEST META.yml README examples/
%doc %{_mandir}/man1/prove.1*
%doc %{_mandir}/man3/App::Prove.3pm*
%doc %{_mandir}/man3/App::Prove::*.3pm*
%doc %{_mandir}/man3/Test::HACKING.3pm*
%doc %{_mandir}/man3/Test::Harness.3pm*
%doc %{_mandir}/man3/TAP::*.3pm*
%{_bindir}/prove
%dir %{perl_vendorlib}/App/
%{perl_vendorlib}/App/Prove/
%{perl_vendorlib}/App/Prove.pm
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Harness/
%{perl_vendorlib}/Test/HACKING.pod
%{perl_vendorlib}/Test/Harness.pm
%{perl_vendorlib}/TAP/

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 3.06-1
- Updated to release 3.06.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 3.05-1
- Updated to release 3.05.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 3.04-1
- Updated to release 3.04.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 3.03-1
- Updated to release 3.03.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 3.00-1
- Updated to release 3.00.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 2.64-1
- Initial package. (using DAR)
