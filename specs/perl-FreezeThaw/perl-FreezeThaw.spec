# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name FreezeThaw

Summary: FreezeThaw module for perl
Name: perl-FreezeThaw
Version: 0.43
Release: 1.2
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FreezeThaw/

Source: http://www.cpan.org/modules/by-module/FreezeThaw/FreezeThaw-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.8.0, perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.8.0

%description
FreezeThaw module for perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/FreezeThaw.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.43-1.2
- Rebuild for Fedora Core 5.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 0.43-1
- Cosmetic cleanup.

* Fri Jul 18 2003 Dag Wieers <dag@wieers.com> - 0.43-0
- Initial package. (using DAR)
