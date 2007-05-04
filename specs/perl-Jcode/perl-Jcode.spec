# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>
 
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jcode

Summary: Jcode (Japanese Charset Handler) module for perl
Name: perl-Jcode
Version: 2.06
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jcode/

Source: http://www.cpan.org/modules/by-module/Jcode/Jcode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0

%description
Jcode (Japanese Charset Handler) module for perl.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3*
%{perl_vendorlib}/Jcode.pm
%{perl_vendorlib}/Jcode/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.06-1
- Updated to release 2.06.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.06-1
- Updated to release 2.06.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release 2.05.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Updated to release 2.03.

* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 0.83-0
- Initial package. (using DAR)
