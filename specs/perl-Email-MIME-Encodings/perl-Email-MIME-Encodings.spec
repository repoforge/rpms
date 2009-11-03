# $Id$
# Authority: dries
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME-Encodings

Summary: Unified interface to MIME encoding and decoding
Name: perl-Email-MIME-Encodings
Version: 1.313
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME-Encodings/

Source: http://www.cpan.org/modules/by-module/Email/Email-MIME-Encodings-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module simply wraps "MIME::Base64" and "MIME::QuotedPrint" so that
you can throw the contents of a "Content-Transfer-Encoding" header at
some text and have the right thing happen.

This package contains the following Perl module:

    Email::MIME::Encodings

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Email::MIME::Encodings.3pm*
%dir %{perl_vendorlib}/Email/
%dir %{perl_vendorlib}/Email/MIME/
#%{perl_vendorlib}/Email/MIME/Encodings/
%{perl_vendorlib}/Email/MIME/Encodings.pm

%changelog
* Fri Apr 24 2009 Christoph Maser <cmr@financial.com> - 1.313-1
- Updated to release 1.313.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.311-1
- Updated to release 1.311.

* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
