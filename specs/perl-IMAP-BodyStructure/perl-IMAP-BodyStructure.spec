# $Id$
# Authority: dries
# Upstream: Alex Kapranoff <alex%20at%20kapranoff%20dot%20ru>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IMAP-BodyStructure

Summary: Interface to parse the output of an IMAP4 MIME-parser
Name: perl-IMAP-BodyStructure
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IMAP-BodyStructure/

Source: http://www.cpan.org/modules/by-module/IMAP/IMAP-BodyStructure-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
An IMAP4-compatible IMAP server MUST include a full MIME-parser which
parses the messages inside IMAP mailboxes and is accessible via
BODYSTRUCTURE fetch item. This module provides a perl interface to
parse the output of IMAP4 MIME-parser. Hope no one will have problems
with parsing previous sentence.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/IMAP/BodyStructure.pm

%changelog
* Fri Sep 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.96-1
- Initial package.
