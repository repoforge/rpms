# $Id$
# Authority: dag
# Upstream: Jos Boumans <kane$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Loaded

Summary: Perl module to mark modules as loaded or unloaded
Name: perl-Module-Loaded
Version: 0.06
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Loaded/

Source: http://www.cpan.org/modules/by-module/Module/Module-Loaded-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Module-Loaded is a Perl module to mark modules as loaded or unloaded.

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
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/Module::Loaded.3pm*
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/Loaded.pm

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 0.06-1
- Updated to version 0.06.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.02-1
- Updated to version 0.02.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
