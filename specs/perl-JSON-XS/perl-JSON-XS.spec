# $Id$
# Authority: dag
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON-XS

Summary: Perl module that implements JSON serialising/deserialising
Name: perl-JSON-XS
Version: 1.43
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JSON-XS/

Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/JSON-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/JSON::XS.3pm*
%doc %{_mandir}/man3/JSON::XS::Boolean.3pm*
%dir %{perl_vendorarch}/JSON/
%{perl_vendorarch}/JSON/XS.pm
%{perl_vendorarch}/JSON/XS/
%dir %{perl_vendorarch}/auto/JSON/
%{perl_vendorarch}/auto/JSON/XS/

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.43-1
- Initial package. (using DAR)
