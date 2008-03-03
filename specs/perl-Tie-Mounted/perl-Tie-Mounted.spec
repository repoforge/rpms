# $Id$
# Authority: dries
# Upstream: Steven Schubiger <schubiger$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-Mounted

Summary: Tie a mounted node to an array
Name: perl-Tie-Mounted
Version: 0.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-Mounted/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-Mounted-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%description
Tie a mounted node to an array.

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
%doc %{_mandir}/man3/Tie::Mounted.3pm*
%dir %{perl_vendorlib}/Tie/
#%{perl_vendorlib}/Tie/Mounted/
%{perl_vendorlib}/Tie/Mounted.pm

%changelog
* Mon Mar 03 2008 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Initial package.
