# $Id$
# Authority: dag
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON-XS

Summary: Perl module that implements JSON serialising/deserialising
Name: perl-JSON-XS
Version: 2.2
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JSON-XS/

Source: http://www.cpan.org/modules/by-module/JSON/JSON-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-JSON-XS is a Perl module that implements JSON serialising/deserialising,
done correctly and fast.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man1/json_xs.1*
%doc %{_mandir}/man3/JSON::XS.3pm*
%doc %{_mandir}/man3/JSON::XS::Boolean.3pm*
%{_bindir}/json_xs
%dir %{perl_vendorarch}/auto/JSON/
%{perl_vendorarch}/auto/JSON/XS/
%dir %{perl_vendorarch}/JSON/
%{perl_vendorarch}/JSON/XS/
%{perl_vendorarch}/JSON/XS.pm

%changelog
* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 2.01-1
- Updated to release 2.01.

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.53-1
- Updated to release 1.53.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.52-1
- Updated to release 1.52.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.43-2
- Disabled auto-requires for eg/.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.43-1
- Initial package. (using DAR)
