# $Id$
# Authority: dries
# Upstream: Yves <yves$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Simple

Summary: Simple date object
Name: perl-Date-Simple
Version: 3.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Simple/

Source: http://search.cpan.org/CPAN/authors/id/Y/YV/YVES/Date-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Dates are complex enough without times and timezones. This module may be
used to create simple date objects.

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
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Date/Simple.pm
%{perl_vendorarch}/Date/Simple/
%{perl_vendorarch}/auto/Date/Simple/

%changelog
* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 3.02-1
- Initial package.
