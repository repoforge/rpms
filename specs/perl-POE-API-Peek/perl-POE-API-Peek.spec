# $Id$
# Authority: dries
# Upstream: Matt Cashner <sungo$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-API-Peek

Summary: Peek into the internals of a running POE environment
Name: perl-POE-API-Peek
Version: 1.34
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-API-Peek/

Source: http://www.cpan.org/modules/by-module/POE/POE-API-Peek-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(Module::Signature)
BuildRequires: perl(Test::Distribution)
BuildRequires: perl(Test::Pod::Coverage)
Requires: perl >= 1:5.6.1

%description
POE::API::Peek extends the POE::Kernel interface to provide clean access
to Kernel internals in a cross-version compatible manner. Other
calculated data is also available.

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
%doc LICENSE MANIFEST MANIFEST.SKIP META.yml README VERSION
%doc %{_mandir}/man3/POE::API::Peek.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/API/
#%{perl_vendorlib}/POE/API/Peek/
%{perl_vendorlib}/POE/API/Peek.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.34-1
- Updated to version 1.34.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.0802-1
- Updated to release 1.0802.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Initial package.

