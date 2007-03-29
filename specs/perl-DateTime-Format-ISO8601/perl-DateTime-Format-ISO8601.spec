# $Id$
# Authority: dries
# Upstream: Joshua Hoblitt <jhoblitt$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-ISO8601

Summary: Parses almost all ISO8601 date and time formats
Name: perl-DateTime-Format-ISO8601
Version: 0.0403
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-ISO8601/

Source: http://search.cpan.org/CPAN/authors/id/J/JH/JHOBLITT/DateTime-Format-ISO8601-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
This module parses almost all ISO8601 date and time formats.
ISO8601 time-intervals will be supported in a later release.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DateTime/Format/ISO8601.p*

%changelog
* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.0403-1
- Initial package.
