# $Id$
# Authority: dries
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME

Summary: Easy MIME message parsing
Name: perl-Email-MIME
Version: 1.903
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Email-MIME-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Email::MIME::ContentType) >= 1.011
BuildRequires: perl(Email::MIME::Encodings) >= 1.313
BuildRequires: perl(Email::MessageID)
BuildRequires: perl(Email::Simple) >= 2.004
BuildRequires: perl(Email::Simple::Creator)
BuildRequires: perl(Encode) >= 1.9801
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MIME::Types) >= 1.13
BuildRequires: perl(Test::More) >= 0.47
Requires: perl(Email::MIME::ContentType) >= 1.011
Requires: perl(Email::MIME::Encodings) >= 1.313
Requires: perl(Email::MessageID)
Requires: perl(Email::Simple) >= 2.004
Requires: perl(Email::Simple::Creator)
Requires: perl(Encode) >= 1.9801
Requires: perl(MIME::Types) >= 1.13
Requires: perl(Test::More) >= 0.47

# as of version 1.903, this includes Email::MIME::Creator
Obsoletes: perl-Email-MIME-Creator

%filter_from_requires /^perl*/d
%filter_setup


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
%doc %{_mandir}/man3/Email::MIME::Creator.3pm*
%doc %{_mandir}/man3/Email::MIME::Header.3pm*
%doc %{_mandir}/man3/Email::MIME::Modifier.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/MIME/Creator.pm
%{perl_vendorlib}/Email/MIME/Header.pm
%{perl_vendorlib}/Email/MIME/Modifier.pm
%{perl_vendorlib}/Email/MIME.pm

%changelog
* Tue Jan 05 2010 Steve Huff <shuff@vecna.org> - 1.903-2
- This package obsoletes our perl-Email-MIME-Creator package, 
  which is in the vault as of 2009-12-30.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 1.903-1
- Updated to version 1.903.

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

