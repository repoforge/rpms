# $Id$
# Authority: dries
# Upstream: Tels <nospam-abuse$bloodgate,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-Morse

Summary: Convert between ASCII and MORSE code
Name: perl-Convert-Morse
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-Morse/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-Morse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::More)
Requires: perl >= 2:5.8.1

%description
A package to convert between ASCII and MORSE code.

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
%doc CHANGES LICENSE MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Convert::Morse.3pm*
%dir %{perl_vendorlib}/Convert/
#%{perl_vendorlib}/Convert/Morse/
%{perl_vendorlib}/Convert/Morse.pm

%changelog
* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 0.06-1
- Updated to release 0.06.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Updated to release 0.05.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
