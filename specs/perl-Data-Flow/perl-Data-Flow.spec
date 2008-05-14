# $Id$
# Authority: dries
# Upstream: Ilya Zakharevich <cpan$ilyaz,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Flow

Summary: Simple-minded recipe-controlled build of data
Name: perl-Data-Flow
Version: 1.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Flow/

Source: http://www.cpan.org/modules/by-module/Data/Data-Flow-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl extension for simple-minded recipe-controlled build of data.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Data::Flow.3pm*
%dir %{perl_vendorlib}/auto/Data/
%{perl_vendorlib}/auto/Data/Flow/
%dir %{perl_vendorlib}/Data/
#%{perl_vendorlib}/Data/Flow/
%{perl_vendorlib}/Data/Flow.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
