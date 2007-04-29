# $Id$
# Authority: dries
# Upstream: Ricardo Signes <rjbs$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Abstract

Summary: Unified interface to mail representations
Name: perl-Email-Abstract
Version: 2.132
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Abstract/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Email-Abstract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Email::Abstract*
%{perl_vendorlib}/Email/Abstract.pm
%{perl_vendorlib}/Email/Abstract/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.132-1
- Updated to release 2.132.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 2.131-1
- Initial package.
