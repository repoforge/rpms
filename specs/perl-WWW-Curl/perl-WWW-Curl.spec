# $Id$
# Authority: dag
# Upstream: Cris Bailiff <c,bailiff+curl$devsecure,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Curl

Summary: Perl extension interface for libcurl
Name: perl-WWW-Curl
Version: 4.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Curl/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Curl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.6.1 curl-devel
Requires: perl >= 1:5.6.1

%description
Perl extension interface for libcurl.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/WWW::Curl.3pm*
%dir %{perl_vendorarch}/auto/WWW/
%{perl_vendorarch}/auto/WWW/Curl/
%dir %{perl_vendorarch}/WWW/
%{perl_vendorarch}/WWW/Curl/
%{perl_vendorarch}/WWW/Curl.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 4.07-1
- Updated to version 4.07.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 4.04-1
- Initial package. (using DAR)
