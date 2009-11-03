# $Id$
# Authority: dries
# Upstream: Jesse Vincent <jesse$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Quoted

Summary: Extract the structure of a quoted mail message
Name: perl-Text-Quoted
Version: 2.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Quoted/

Source: http://www.cpan.org/modules/by-module/Text/Text-Quoted-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.6.0

%description
Extract the structure of a quoted mail message.

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
%doc %{_mandir}/man3/Text::Quoted.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/Quoted/
%{perl_vendorlib}/Text/Quoted.pm

%changelog
* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release 2.05.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Sat Aug 25 2007 Dag Wieers <dag@wieers.com> - 2.02-1
- Updated to release 2.02.

* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 1.8-1
- Initial package.
