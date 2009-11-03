# $Id$
# Authority: dries
# Upstream: David Muir Sharnoff <muir$idiom,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-modules

Summary: Date and time objects
Name: perl-Time-modules
Version: 2006.0814
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-modules/

Source: http://www.cpan.org/modules/by-module/Time/Time-modules-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Date and time objects.

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
%doc CHANGELOG MANIFEST META.yml README
%doc %{_mandir}/man3/Time::*.3pm*
%{perl_vendorlib}/Time/

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 2006.0814-1
- Updated to release 2006.0814.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2003.1126-1
- Initial package.
