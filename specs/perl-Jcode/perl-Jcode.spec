# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>
 
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jcode

Summary: Japanese Charset Handler
Name: perl-Jcode
Version: 2.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jcode/

Source: http://www.cpan.org/modules/by-module/Jcode/Jcode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
Jcode (Japanese Charset Handler) module for perl.

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
%doc Changes Changes.ver0X MANIFEST META.yml README
%doc %{_mandir}/man3/Jcode.3pm*
%doc %{_mandir}/man3/Jcode::*.3pm*
%{perl_vendorlib}/Jcode/
%{perl_vendorlib}/Jcode.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.07-1
- Updated to release 2.07.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.06-1
- Updated to release 2.06.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release 2.05.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Updated to release 2.03.

* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 0.83-0
- Initial package. (using DAR)
