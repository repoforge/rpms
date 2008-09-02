# $Id$
# Authority: dries
# Upstream: Terrence Brannon <metaperl$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Eroot

Summary: Eternal root to handle persistent objects
Name: perl-Class-Eroot
Version: 2.1
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Eroot/

Source: http://search.cpan.org/CPAN/authors/id/T/TB/TBONE/Class-Eroot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
An eternal root to handle persistent objects.

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
%doc Changes MANIFEST
%doc %{_mandir}/man3/Class::Eroot.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Eroot.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 2.1-2
- Improved package.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Initial package.
