# $Id$
# Authority: dries
# Upstream: Paul H Alfille <paul,alfille$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name OWNet

Summary: Light weight access to owserver
Name: perl-OWNet
Version: 1.8
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/OWNet/

Source: http://www.cpan.org/authors/id/A/AL/ALFILLE/OWNet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Light weight access to owserver.

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
%doc %{_mandir}/man3/OWNet.3pm*
#%{perl_vendorlib}/OWNet/
%{perl_vendorlib}/OWNet.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.8-1
- Updated to release 1.8.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
