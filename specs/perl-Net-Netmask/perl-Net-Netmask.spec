# $Id$

# Authority: dries
# Upstream: David Muir Sharnoff <muir$idiom,com>


%define real_name Net-Netmask
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Parse, manipulate and lookup IP network blocks
Name: perl-Net-Netmask
Version: 1.9015
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Netmask/

Source: http://www.cpan.org/modules/by-module/Net/Net-Netmask-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can parse, manipulate and
lookup IP network blocks.

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
%doc CHANGELOG README
%{_mandir}/man3/*
%{perl_vendorlib}/Net/Netmask.pm
%{perl_vendorlib}/Net/Netmask.pod

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.9015-1
- Updated to release 1.9015.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.9014-1
- Updated to release 1.9014.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.9013-1
Updated to release 1.9013.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.9012-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.9012-1
- Updated to release 1.9012.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.9011-1
- Initial package.
