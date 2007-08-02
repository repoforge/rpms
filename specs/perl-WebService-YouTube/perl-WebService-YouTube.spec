# $Id$
# Authority: dries
# Upstream: Hironori Yoshida <yoshida$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

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

%description
An interface to YouTube.

%prep
%setup -n %{real_name}-%{version}

%build
export PERL_EXTUTILS_AUTOINSTALL="--skipdeps --skip"
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export PERL_EXTUTILS_AUTOINSTALL="--skipdeps --skip"
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/WebService/
%{perl_vendorlib}/WebService/YouTube.pm
%{perl_vendorlib}/WebService/YouTube/

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
