# $Id$
# Authority: dries
# Upstream: Petr Cimprich <petr$gingerall,cz>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-STX

Summary: Implementation of an STX processor
Name: perl-XML-STX
Version: 0.43
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-STX/

Source: http://search.cpan.org/CPAN/authors/id/P/PC/PCIMPRICH/XML-STX-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-XML-SAX, perl-Clone, perl-XML-NamespaceSupport

%description
XML::STX is a pure Perl implementation of STX processor. Streaming 
Transformations for XML (STX) is a one-pass transformation language for 
XML documents that builds on the Simple API for XML (SAX). See 
http://stx.sourceforge.net/ for more details.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%{_bindir}/stx*.pl
%{perl_vendorlib}/XML/STX.pm
%{perl_vendorlib}/XML/STX/
%{perl_vendorlib}/XML/stx*.pl

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.43-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.43-1
- Initial package.
