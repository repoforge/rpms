# $Id$

# Authority: dries
# Upstream: Grant McLean <grantm$cpan,org>


%define real_name XML-Simple
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Easy API to XML files
Name: perl-XML-Simple
Version: 2.14
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Simple/

Source: http://search.cpan.org/CPAN/authors/id/G/GR/GRANTM/XML-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains an easy API to XML files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/XML/Simple.pm
%{perl_vendorlib}/XML/Simple/*

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 2.14-1
- Updated to release 2.14.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 2.13-2
- Fixed the license tag (Thanks to David Necas !)

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 2.13-1
- Updated to release 2.13.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Initial package.
