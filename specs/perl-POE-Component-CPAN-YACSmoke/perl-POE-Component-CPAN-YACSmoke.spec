# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-CPAN-YACSmoke

Summary: Bringing the power of POE to CPAN smoke testing
Name: perl-POE-Component-CPAN-YACSmoke
Version: 1.36
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-CPAN-YACSmoke/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-CPAN-YACSmoke-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
Smoke testing with POE.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man1/minismoker.1*
%doc %{_mandir}/man3/POE::Component::CPAN::YACSmoke.3pm*
%{_bindir}/minismoker
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/CPAN/
#%{perl_vendorlib}/POE/Component/CPAN/YACSmoke/
%{perl_vendorlib}/POE/Component/CPAN/YACSmoke.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.36-1
- Updated to version 1.36.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.18-1
- Updated to release 1.18.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.09-1
- Updated to release 1.09.

* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
