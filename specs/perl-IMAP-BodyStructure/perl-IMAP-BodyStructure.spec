# $Id$
# Authority: dries
# Upstream: Alex Kapranoff <alex%20at%20kapranoff%20dot%20ru>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IMAP-BodyStructure

Summary: Interface to parse the output of an IMAP4 MIME-parser
Name: perl-IMAP-BodyStructure
Version: 0.96
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IMAP-BodyStructure/

Source: http://search.cpan.org/CPAN/authors/id/K/KA/KAPPA/IMAP-BodyStructure-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
An IMAP4-compatible IMAP server MUST include a full MIME-parser which
parses the messages inside IMAP mailboxes and is accessible via
BODYSTRUCTURE fetch item. This module provides a perl interface to
parse the output of IMAP4 MIME-parser. Hope no one will have problems
with parsing previous sentence.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/IMAP/BodyStructure.pm

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.96-1
- Initial package.
