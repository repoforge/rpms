# $Id$
# Authority: dries
# Upstream: Hironori Yoshida <yoshida$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-YouTube

Summary: Interface to YouTube
Name: perl-WebService-YouTube
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-YouTube/

Source: http://search.cpan.org//CPAN/authors/id/Y/YO/YOSHIDA/WebService-YouTube-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
An interface to YouTube.

%prep
%setup -n %{real_name}-%{version}

%build
export PERL_EXTUTILS_AUTOINSTALL="--skipdeps --skip"
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
export PERL_EXTUTILS_AUTOINSTALL="--skipdeps --skip"
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/WebService/
%{perl_vendorlib}/WebService/YouTube.pm
%{perl_vendorlib}/WebService/YouTube/

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
