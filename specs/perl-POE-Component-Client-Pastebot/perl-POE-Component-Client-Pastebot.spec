# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-Pastebot

Summary: Interact with Bot::Pastebot web services from POE
Name: perl-POE-Component-Client-Pastebot
Version: 1.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-Pastebot/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Client-Pastebot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
Interact with Bot::Pastebot web services.

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
%doc %{_mandir}/man3/POE::Component::Client::Pastebot.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Client/
#%{perl_vendorlib}/POE/Component/Client/Pastebot/
%{perl_vendorlib}/POE/Component/Client/Pastebot.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
