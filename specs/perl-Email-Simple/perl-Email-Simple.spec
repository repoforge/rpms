# $Id$
# Authority: dries
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Simple

Summary: Simple parsing of RFC2822 message format and headers
Name: perl-Email-Simple
Version: 2.100
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Simple/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Email-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Email::Date::Format)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47
Requires: perl(Email::Date::Format)
Requires: perl(Test::More) >= 0.47

# as of version 2.100, this includes Email::Simple::Creator
Obsoletes: perl-Email-Simple-Creator

%filter_from_requires /^perl*/d
%filter_setup


%description
With this module you can parse RFC2822 message format and headers.

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
%doc %{_mandir}/man3/Email::Simple.3pm*
%doc %{_mandir}/man3/Email::Simple::Header.3pm*
%doc %{_mandir}/man3/Email::Simple::Creator.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/Simple/
%{perl_vendorlib}/Email/Simple.pm

%changelog
* Tue Jan 05 2010 Steve Huff <shuff@vecna.org> - 2.100-2
- Obsoletes perl-Email-Simple-Creator.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 2.100-1
- Updated to version 2.100.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 2.005-1
- Updated to version 2.005.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 2.004-1
- Updated to release 2.004.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 2.003-1
- Updated to release 2.003.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.999-1
- Updated to release 1.999.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.995-1
- Initial package.
