# $Id$
# Authority: dries
# Upstream: Joshua Nathaniel Pritikin <jpritikin$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Event

Summary: Generic Perl Event Loop
Name: perl-Event
Version: 1.08
Release: 1
License: Artistic/GPL
Group: Development/Libraries
URL: http://search.cpan.org/dist/Event/

Source: http://search.cpan.org/CPAN/authors/id/J/JP/JPRIT/Event-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This extension aims to provide an simple and optimized event loop for
a broad class of applications.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Event/
%{perl_vendorarch}/Event.pm
%{perl_vendorarch}/Event.pod
%{perl_vendorarch}/auto/Event

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.0.6-2
- Release bump to drop the disttag number in FC5 build.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
