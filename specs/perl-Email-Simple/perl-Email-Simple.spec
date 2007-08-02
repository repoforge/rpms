# $Id$
# Authority: dries
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Simple

Summary: Simple parsing of RFC2822 message format and headers
Name: perl-Email-Simple
Version: 1.999
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Simple/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Email-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
With this module you can parse RFC2822 message format and headers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Email/Simple.pm
%{perl_vendorlib}/Email/Simple/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.999-1
- Updated to release 1.999.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.995-1
- Initial package.
