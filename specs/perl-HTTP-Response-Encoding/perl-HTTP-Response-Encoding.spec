# $Id$
# Authority: cmr
# Upstream: Dan Kogai <dankogai$dan,co,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Response-Encoding

Summary: Adds encoding() to HTTP::Response
Name: perl-HTTP-Response-Encoding
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Response-Encoding/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Response-Encoding-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Adds encoding() to HTTP::Response.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/HTTP::Response::Encoding.3pm*
%dir %{perl_vendorlib}/HTTP/
%dir %{perl_vendorlib}/HTTP/Response/
#%{perl_vendorlib}/HTTP/Response/Encoding/
%{perl_vendorlib}/HTTP/Response/Encoding.pm

%changelog
* Mon Jun 29 2009 Unknown - 0.05-1
- Initial package. (using DAR)
