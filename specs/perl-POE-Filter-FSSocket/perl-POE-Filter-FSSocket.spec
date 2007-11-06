# $Id$
# Authority: dries
# Upstream: Paul David Tinsley <pdt$jackhammer,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Filter-FSSocket

Summary: POE filter that parses FreeSWITCH events into hashes
Name: perl-POE-Filter-FSSocket
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Filter-FSSocket/

Source: http://search.cpan.org/CPAN/authors/id/P/PT/PTINSLEY/POE-Filter-FSSocket-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
A POE filter for FreeSWITCH (http://www.freeswitch.org) that parses 
event/log/etc... messages for you.  You must ask for events in plain mode.

%prep
%setup -n %{real_name}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Filter/
%{perl_vendorlib}/POE/Filter/FSSocket.pm

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Updated to release 0.03.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
