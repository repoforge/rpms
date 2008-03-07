# $Id$
# Authority: dries
# Upstream: Andreas J. K&#246;nig <andreas,koenig$anima,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-UU

Summary: Module for uuencode and uudecode
Name: perl-Convert-UU
Version: 0.5201
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-UU/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-UU-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
UUencode and UUDecode strings and files.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man1/puudecode.1*
%doc %{_mandir}/man1/puuencode.1*
%doc %{_mandir}/man3/Convert::UU.3pm*
%{_bindir}/puudecode
%{_bindir}/puuencode
%dir %{perl_vendorlib}/Convert/
#%{perl_vendorlib}/Convert/UU/
%{perl_vendorlib}/Convert/UU.pm

%changelog
* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 0.5201-1
- Updated to release 0.5201.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Initial package.
