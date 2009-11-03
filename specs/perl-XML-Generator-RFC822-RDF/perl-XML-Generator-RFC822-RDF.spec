# $Id$
# Authority: dries
# Upstream: Aaron Straup Cope <ascope$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Generator-RFC822-RDF

Summary: Generate RDF/XML SAX2 events for RFC822 messages
Name: perl-XML-Generator-RFC822-RDF
Version: 1.1
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Generator-RFC822-RDF/

Source: http://www.cpan.org/modules/by-module/XML/XML-Generator-RFC822-RDF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
Generate RDF/XML SAX2 events for RFC822 messages.

Messages are keyed using SHA1 digests of Message-IDs and email
addresses. In the case of the latter this makes it easier to merge
messages with contact data that has been serialized using
XML::Generator::vCard::RDF (version 1.3+)

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
%{perl_vendorlib}/XML/Generator/RFC822/RDF.pm

%changelog
* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Initial package.
