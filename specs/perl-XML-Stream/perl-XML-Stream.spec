# $Id$
# Authority: dries
# Upstream: Darian Anthony Patrick <dapatrick@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Stream

Summary: XML Stream connection support
Name: perl-XML-Stream
Version: 1.23
Release: 1%{?dist}
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Stream/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAPATRICK/XML-Stream-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Authen::SASL)
BuildRequires: perl(Carp)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FileHandle)
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(POSIX)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl >= 5.008
BuildRequires: perl(utf8)
Requires: perl(Authen::SASL)
Requires: perl(Carp)
Requires: perl(Encode)
Requires: perl(FileHandle)
Requires: perl(IO::Select)
Requires: perl(IO::Socket)
Requires: perl(MIME::Base64)
Requires: perl(POSIX)
Requires: perl(Sys::Hostname)
Requires: perl >= 5.008
Requires: perl(utf8)

%filter_from_requires /^perl*/d
%filter_setup


%description
This module contains support for XML stream connections.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INFO LICENSE.LGPL README
%{_mandir}/man3/*
%{perl_vendorlib}/XML/Stream.pm
%{perl_vendorlib}/XML/Stream/*

%changelog
* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 1.23-1
- Updated to version 1.23.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.22-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Initial package.
