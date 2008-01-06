# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Filter-Bzip2

Summary: POE filter wrapped around Compress::Bzip2
Name: perl-POE-Filter-Bzip2
Version: 1.54
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Filter-Bzip2/

Source: http://www.cpan.org/modules/by-module/POE/POE-Filter-Bzip2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
POE filter wrapped around Compress::Bzip2.

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
%doc %{_mandir}/man3/POE::Filter::Bzip2.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Filter/
#%{perl_vendorlib}/POE/Filter/Bzip2/
%{perl_vendorlib}/POE/Filter/Bzip2.pm

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 1.54-1
- Updated to release 1.54.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.53-1
- Updated to release 1.53.

* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 1.52-1
- Updated to release 1.52.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
