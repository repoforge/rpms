# $Id$
# Authority: dag
# Upstream: Dan Sully <daniel@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Cracklib

Summary: Perl interface to Alec Muffett's Cracklib
Name: perl-Crypt-Cracklib
Version: 1.2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Cracklib/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Cracklib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.004
Requires: perl >= 0:5.004

%description
Perl interface to Alec Muffett's Cracklib.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man3/Crypt::Cracklib.3pm*
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/Cracklib/
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/Cracklib.pm

%changelog
* Sun Feb 24 2008 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.1-1
- Initial package. (using DAR)
