# $Id$
# Authority: dries
# Upstream: Andy Lester <andy$petdance,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Next

Summary: File-finding iterator
Name: perl-File-Next
Version: 1.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Next/

Source: http://www.cpan.org/modules/by-module/File/File-Next-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
File-finding iterator.

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
%doc %{_mandir}/man3/File::Next.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/Next.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Initial package.
