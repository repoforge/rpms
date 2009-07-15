# $Id$
# Authority: dries
# Upstream: Salvador Fandiño García <salva$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Properties

Summary: Read and write property files
Name: perl-Config-Properties
Version: 1.70
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Properties/

Source: http://www.cpan.org/modules/by-module/Config/Config-Properties-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Wrap) >= 2001.0929       


%description
Read and write property files.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Config::Properties.3pm*
%dir %{perl_vendorlib}/Config/
#%{perl_vendorlib}/Config/Properties/
%{perl_vendorlib}/Config/Properties.pm

%changelog
* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 1.70-1
- Updated to version 1.70.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.68-1
- Updated to release 1.68.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.65-1
- Initial package.
