# $Id$
# Authority: dries
# Upstream: Apocalypse <APOCAL$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-SimpleDBI

Summary: Asynchronous non-blocking DBI calls in POE made simple
Name: perl-POE-Component-SimpleDBI
Version: 1.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-SimpleDBI/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-SimpleDBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Asynchronous non-blocking DBI calls in POE made simple.

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
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/POE::Component::SimpleDBI.3pm*
%doc %{_mandir}/man3/POE::Component::SimpleDBI::SubProcess.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%{perl_vendorlib}/POE/Component/SimpleDBI/
%{perl_vendorlib}/POE/Component/SimpleDBI.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.18-1
- Updated to release 1.18.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.17-1
- Updated to release 1.17.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Sat Sep 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Updated to release 1.15.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Initial package.
