# $Id$
# Authority: dag
# Upstream: Makamaka Hannyaharamitu <makamaka$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON-PC

Summary: Perl module that implements a fast JSON Parser and Converter
Name: perl-JSON-PC
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JSON-PC/

Source: http://www.cpan.org/authors/id/M/MA/MAKAMAKA/JSON-PC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.0

%description
perl-JSON-PC is a Perl module that implements a fast JSON Parser and Converter.

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
%doc %{_mandir}/man3/JSON::PC.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/JSON/
%{perl_vendorarch}/JSON/PC.pm
%dir %{perl_vendorarch}/auto/JSON/
%{perl_vendorarch}/auto/JSON/PC/

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
