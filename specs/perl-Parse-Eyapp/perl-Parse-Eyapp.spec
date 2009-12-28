# $Id$
# Authority: dag
# Upstream: Casiano Rodriguez-Leon <casiano$ull,es>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-Eyapp

Summary: Extensions for Parse::Yapp
Name: perl-Parse-Eyapp
Version: 1.153
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-Eyapp/

Source: http://search.cpan.org/CPAN/authors/id/C/CA/CASIANO/Parse-Eyapp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Data::Dumper) >= 1.0
BuildRequires: perl(List::Util) >= 1.0
BuildRequires: perl(Pod::Usage) >= 1.0
Requires: perl(Data::Dumper) >= 1.0
Requires: perl(List::Util) >= 1.0
Requires: perl(Pod::Usage) >= 1.0

%filter_from_requires /^perl*/d
%filter_setup

%description
Extensions for Parse::Yapp.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man1/eyapp.1*
%doc %{_mandir}/man1/treereg.1*
%doc %{_mandir}/man1/vgg.1*
%doc %{_mandir}/man3/Parse::Eyapp.3pm*
%doc %{_mandir}/man3/Parse::Eyapp::*.3pm*
%{_bindir}/eyapp
%{_bindir}/treereg
%{_bindir}/vgg
%dir %{perl_vendorlib}/Parse/
%{perl_vendorlib}/Parse/Eyapp/
%{perl_vendorlib}/Parse/Eyapp.pm
%{perl_vendorlib}/Parse/Eyapp.pod

%changelog
* Mon Dec 28 2009 Christoph Maser <cmr@financial.com> - 1.153-1
- Updated to version 1.153.

* Tue Dec 22 2009 Christoph Maser <cmr@financial.com> - 1.151-1
- Updated to version 1.151.

* Tue Dec 15 2009 Christoph Maser <cmr@financial.com> - 1.149-1
- Updated to version 1.149.

* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 1.148-1
- Updated to version 1.148.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.147-1
- Updated to version 1.147.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.115-1
- Updated to release 1.115.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.109-1
- Updated to release 1.109.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 1.107-1
- Updated to release 1.107.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.106-1
- Updated to release 1.106.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 1.098-1
- Initial package. (using DAR)
