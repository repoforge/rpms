# $Id: $

# Authority: dries
# Upstream:

%define real_name Apache-Session

Summary: Session data persistence
Name: perl-Apache-Session
Version: 1.6
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Session/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/J/JB/JBAKER/Apache-Session-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Requires: perl-DBI

%description
These modules provide persistent storage for arbitrary data, in arbitrary
backing stores.  The details of interacting with the backing store are
abstracted to make all backing stores behave alike.  The programmer simply
interacts with a tied hash.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO CHANGES
%{_mandir}/man3/*
%{_libdir}/perl5/vendor_perl/*/Apache/Session.pm
%{_libdir}/perl5/vendor_perl/*/Apache/Session/*
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%exclude %{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
