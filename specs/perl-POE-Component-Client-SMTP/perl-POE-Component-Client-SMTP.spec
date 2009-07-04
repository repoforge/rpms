# $Id$
# Authority: dries
# Upstream: George Nistorica <ultadm$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-SMTP

Summary: Asynchronous mail sending with POE
Name: perl-POE-Component-Client-SMTP
Version: 0.21
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-SMTP/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Client-SMTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
Asynchronous mail sending with POE.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes LICENSE MANIFEST META.yml README TODO eg/
%doc %{_mandir}/man3/POE::Component::Client::SMTP.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Client/
#%{perl_vendorlib}/POE/Component/Client/SMTP/
%{perl_vendorlib}/POE/Component/Client/SMTP.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.21-1
- Updated to version 0.21.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
