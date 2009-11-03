# $Id$
# Authority: dries
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Abstract

Summary: Unified interface to mail representations
Name: perl-Email-Abstract
Version: 3.001
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Abstract/

Source: http://www.cpan.org/modules/by-module/Email/Email-Abstract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
"Email::Abstract" provides module writers with the ability to write
representation-independent mail handling code. For instance, in the
cases of "Mail::Thread" or "Mail::ListDetector", a key part of the code
involves reading the headers from a mail object. Where previously one
would either have to specify the mail class required, or to build a new
object from scratch, "Email::Abstract" can be used to perform certain
simple operations on an object regardless of its underlying
representation.

This package contains the following Perl module:

    Email::Abstract

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
%doc %{_mandir}/man3/Email::Abstract.3pm*
%doc %{_mandir}/man3/Email::Abstract::*.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/Abstract/
%{perl_vendorlib}/Email/Abstract.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 3.001-1
- Updated to version 3.001.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.134-1
- Updated to release 2.134.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.132-1
- Updated to release 2.132.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 2.131-1
- Initial package.
