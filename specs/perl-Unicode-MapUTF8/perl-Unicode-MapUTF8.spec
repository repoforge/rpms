# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-MapUTF8

Summary: Unicode-MapUTF8 (Conversions to and from arbitrary character sets and UTF8) module for perl
Name: perl-Unicode-MapUTF8
Version: 1.11
Release: 1.2%{?dist}
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-MapUTF8/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-MapUTF8-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker) >= 2:5.8.0
Requires: perl >= 2:5.8.0

%description
Unicode-MapUTF8 (Conversions to and from arbitrary character sets and UTF8) module for perl.

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
%doc MANIFEST README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Unicode/
%{perl_vendorlib}/Unicode/MapUTF8.p*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1.2
- Rebuild for Fedora Core 5.

* Sat Oct 15 2005 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Tue May 31 2005 Dag Wieers <dag@wieers.com> - 1.09-1
- Fixed package. (Kovacs Janos)

* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 1.09-0
- Initial package. (using DAR)
