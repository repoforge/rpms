# $Id$
# Authority: dries
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME

Summary: Easy MIME message parsing
Name: perl-Email-MIME
Version: 1.863
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME/

Source: http://www.cpan.org/modules/by-module/Email/Email-MIME-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Email::Simple)

%description
This is an extension of the Email::Simple module, to handle MIME encoded
messages. It takes a message as a string, splits it up into its
constituent parts, and allows you access to various parts of the
message. Headers are decoded from MIME encoding.

This package contains the following Perl module:

    Email::MIME

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
%doc %{_mandir}/man3/Email::MIME.3pm*
%doc %{_mandir}/man3/Email::MIME::Header.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/MIME/Header.pm
%{perl_vendorlib}/Email/MIME.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.863-1
- Updated to version 1.863.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.861-1
- Updated to release 1.861.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 1.860-1
- Updated to release 1.860.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.859-1
- Updated to release 1.859.

* Tue Nov 21 2006 Dries Verachtert <dries@ulyssis.org> - 1.854-1
- Updated to release 1.854.
- perl(Email::Simple) added to requirements, thanks to Max Kanat-Alexander.

* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.82-1
- Initial package.

