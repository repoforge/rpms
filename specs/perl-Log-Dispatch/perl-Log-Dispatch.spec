# $Id$

# Authority: dries
# Upstream:

%define real_name Log-Dispatch

Summary: OO modules for logging
Name: perl-Log-Dispatch
Version: 2.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Dispatch/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Log-Dispatch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-Params-Validate, perl-Module-Build
Requires: perl-Params-Validate, perl-Mail-Sender, perl-Mail-Sendmail

%description
Log::Dispatch is a suite of OO modules for logging messages to
multiple outputs, each of which can have a minimum and maximum log
level.  It is designed to be easily subclassed, both for creating a
new dispatcher object and particularly for creating new outputs.

It also allows both global (dispatcher level) and local (logging
object) message formatting callbacks which allows greater flexibility
and should reduce the need for subclassing.

Subclassing is only needed to send a message to a different output,
not to change the message format.

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
%doc LICENSE README Changes
%{_mandir}/man3/*
%{_libdir}/perl5/vendor_perl/*/Log/Dispatch.pm
%{_libdir}/perl5/vendor_perl/*/Log/Dispatch

%changelog
* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Initial package.
