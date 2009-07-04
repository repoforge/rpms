# $Id$
# Authority: dries
# Upstream: Satoshi Konno <skonno$cybergarage,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-UPnP

Summary: Extension for UPnP
Name: perl-Net-UPnP
Version: 1.41
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-UPnP/

Source: http://www.cpan.org/modules/by-module/Net/Net-UPnP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl extension for UPnP.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/UPnP.pm
%{perl_vendorlib}/Net/UPnP/

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.41-1
- Updated to version 1.41.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.1-1
- Updated to release 1.2.1.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.2-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.2-1
- Updated to release 1.1.2.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Initial package.
