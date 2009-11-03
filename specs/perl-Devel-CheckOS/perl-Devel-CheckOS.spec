# $Id$
# Authority: dag
# Upstream: David Cantrell <pause$barnyard,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-CheckOS

Summary: Check what OS we are running on
Name: perl-Devel-CheckOS
Version: 1.61
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-CheckOS/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-CheckOS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Check what OS we are running on.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc CHANGES MANIFEST META.yml README TODO
%doc %{_mandir}/man1/use-devel-assertos.1*
%doc %{_mandir}/man3/Devel::AssertOS.3pm*
%doc %{_mandir}/man3/Devel::AssertOS::*.3pm*
%doc %{_mandir}/man3/Devel::CheckOS.3pm*
%doc %{_mandir}/man3/Devel::CheckOS::Families.3pm*
%{_bindir}/use-devel-assertos
%dir %{perl_vendorlib}/Devel/
%{perl_vendorlib}/Devel/AssertOS/
%{perl_vendorlib}/Devel/AssertOS.pm
#%{perl_vendorlib}/Devel/CheckOS/
%{perl_vendorlib}/Devel/CheckOS.pm
%{perl_vendorlib}/Devel/CheckOS/Families.pod

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.61-1
- Updated to version 1.61.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.44-1
- Updated to release 1.44.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.43-1
- Updated to release 1.43.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 1.42-1
- Initial package. (using DAR)
