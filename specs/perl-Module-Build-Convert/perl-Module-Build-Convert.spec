# $Id$
# Authority: dries
# Upstream: Steven Schubiger <schubiger$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Build-Convert

Summary: Makefile.PL to Build.PL converter
Name: perl-Module-Build-Convert
Version: 0.49
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Build-Convert/

Source: http://www.cpan.org/modules/by-module/Module/Module-Build-Convert-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%description
Makefile.PL to Build.PL converter.

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
%doc Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man1/make2build.1*
%doc %{_mandir}/man3/Module::Build::Convert.3pm*
%{_bindir}/make2build
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Build/
#%{perl_vendorlib}/Module/Build/Convert/
%{perl_vendorlib}/Module/Build/Convert.pm

%changelog
* Wed Nov 14 2007 Dag Wieers <dag@wieers.com> - 0.49-1
- Updated to release 0.49.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.44-1
- Initial package.
