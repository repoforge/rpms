# $Id$

# Authority: dries
# Upstream:Flávio Soibelmann Glock <fglock$pucrs,br>

%define real_name DateTime-Set
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Datetime sets and set math
Name: perl-DateTime-Set
Version: 0.20
Release: 2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Set/

Source: http://search.cpan.org/CPAN/authors/id/F/FG/FGLOCK/DateTime-Set-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: perl

%description
The DateTime::Set module provides a date/time sets implementation.  

It allows, for example, the generation of groups of dates, 
like "every wednesday", and then find all the dates matching that 
pattern, within a time range.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} -pi -e 's|use Set::Infinite 0.5502;|use Set::Infinite;|g;' lib/Set/Infinite/_recurrence.pm
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DateTime/*.pm
%{perl_vendorlib}/Set/Infinite/_recurrence.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.19-2
- Requirements fixes.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Initial package.
