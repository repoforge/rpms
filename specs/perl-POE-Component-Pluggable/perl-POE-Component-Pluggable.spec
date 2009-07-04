# $Id$
# Authority: dag
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Pluggable

Summary: Base class for creating plugin enabled POE Components
Name: perl-POE-Component-Pluggable
Version: 1.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Pluggable/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Pluggable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More) >= 0.47

%description
A base class for creating plugin enabled POE Components.

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
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/POE::Component::Pluggable.3pm*
%doc %{_mandir}/man3/POE::Component::Pluggable::Constants.3pm*
%doc %{_mandir}/man3/POE::Component::Pluggable::Pipeline.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%{perl_vendorlib}/POE/Component/Pluggable/
%{perl_vendorlib}/POE/Component/Pluggable.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.20-1
- Updated to version 1.20.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
