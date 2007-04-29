# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Dispatch

Summary: OO modules for logging
Name: perl-Log-Dispatch
Version: 2.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Dispatch/

Source: http://www.cpan.org/modules/by-module/Log/Log-Dispatch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE README
%{_mandir}/man3/*
%dir %{perl_vendorlib}/Log/
%dir %{perl_vendorlib}/Log/Dispatch/
%dir %{perl_vendorlib}/Log/Dispatch/Email/
%dir %{perl_vendorlib}/Log/Dispatch/File/
%{perl_vendorlib}/Log/Dispatch.pm
%{perl_vendorlib}/Log/Dispatch/*.pm
%{perl_vendorlib}/Log/Dispatch/Email/*.pm
%{perl_vendorlib}/Log/Dispatch/File/*.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.17-1
- Updated to release 2.17.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.11-1
- Updated to release 2.11.

* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Initial package.
