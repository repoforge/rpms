# $Id$
# Authority: dag
# Upstream: Gisle Aas <gisle$ActiveState,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-Base64-Perl

Summary: Perl module for encoding and decoding of base64 strings
Name: perl-MIME-Base64-Perl
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-Base64-Perl/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-Base64-Perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-MIME-Base64-Perl is a Perl module for encoding and decoding
of base64 strings.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/MIME::Base64::Perl.3pm*
%doc %{_mandir}/man3/MIME::QuotedPrint::Perl.3pm*
%dir %{perl_vendorlib}/MIME/
%dir %{perl_vendorlib}/MIME/Base64/
%{perl_vendorlib}/MIME/Base64/Perl.pm
%dir %{perl_vendorlib}/MIME/QuotedPrint/
%{perl_vendorlib}/MIME/QuotedPrint/Perl.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
