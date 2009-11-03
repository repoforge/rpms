# $Id$
# Authority: dag
# Upstream: Kevin C. Krinke <kckrinke$opendoorsoftware,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UI-Dialog

Summary: Perl module named UI-Dialog
Name: perl-UI-Dialog
Version: 1.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UI-Dialog/

Source: http://www.cpan.org/authors/id/K/KC/KCK/UI-Dialog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-UI-Dialog is a Perl module.

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
%doc COPYRIGHT Changes MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/UI/
%{perl_vendorlib}/UI/Dialog/
%{perl_vendorlib}/UI/Dialog.pm
%{perl_vendorlib}/UI/Dialog.pod

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.08-1
- Initial package. (using DAR)
