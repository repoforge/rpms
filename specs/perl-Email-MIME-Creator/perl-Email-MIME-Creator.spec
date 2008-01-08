# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME-Creator

Summary: Constructor for Email::MIME
Name: perl-Email-MIME-Creator
Version: 1.454
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME-Creator/

Source: http://www.cpan.org/modules/by-module/Email/Email-MIME-Creator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
### Pull in perl-Email-Simple because this packages provides it as well !!
Requires: perl-Email-MIME

%description
This package contains a constructor for Email::MIME.

This package contains the following Perl module:

    Email::MIME::Creator

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
%doc %{_mandir}/man3/Email::MIME::Creator.3pm*
%dir %{perl_vendorlib}/Email/
%dir %{perl_vendorlib}/Email/MIME/
#%{perl_vendorlib}/Email/MIME/Creator/
%{perl_vendorlib}/Email/MIME/Creator.pm

%changelog
* Mon Jan  7 2008 Dries Verachtert <dries@ulyssis.org> - 1.454-2
- Fix: perl-Email-MIME requirement added, thanks to Tom G. Christensen.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 1.454-1
- Updated to release 1.454.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.453-1
- Updated to release 1.453.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.451
- Initial package.
