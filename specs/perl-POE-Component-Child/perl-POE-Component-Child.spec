# $Id$
# Authority: dag
# Upstream: Erick Calder <ecalder$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Child

Summary: Perl module that implements a child management component
Name: perl-POE-Component-Child
Version: 1.39
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Child/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Child-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-POE-Component-Child is a Perl module that implements
a child management component.

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/POE::Component::Child.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
#%{perl_vendorlib}/POE/Component/Child/
%{perl_vendorlib}/POE/Component/Child.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.39-1
- Initial package. (using DAR)
