# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME-Modifier

Summary: Modify Email::MIME Objects Easily
Name: perl-Email-MIME-Modifier
Version: 1.444
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME-Modifier/

Source: http://www.cpan.org/modules/by-module/Email/Email-MIME-Modifier-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

### FIXME: Get rid of perl(Email::MIME) provides (please fix upstream)
AutoProv: 0
Provides: perl(Email::MIME::Modifier) = %{version}

%description
Provides a number of useful methods for manipulating MIME messages.

These method are declared in the "Email::MIME" namespace, and are used
with "Email::MIME" objects.

This package contains the following Perl module:

    Email::MIME::Modifier

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
%doc %{_mandir}/man3/Email::MIME::Modifier.3pm*
%dir %{perl_vendorlib}/Email/
%dir %{perl_vendorlib}/Email/MIME/
#%{perl_vendorlib}/Email/MIME/Modifier/
%{perl_vendorlib}/Email/MIME/Modifier.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.444-1
- Updated to version 1.444.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 1.442-1
- Updated to release 1.442.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.441-2
- Correctly provide perl(Email::MIME::Modifier).

* Sun Dec 10 2006 Dries Verachtert <dries@ulyssis.org> - 1.441-1
- Updated to release 1.441.
- Disabled automatic provides to make sure it doesn't provide perl(Email::MIME)
  anymore, thanks to Max Kanat-Alexander.

* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.42-1
- Initial package.

