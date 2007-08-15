# $Id$
# Authority: dries
# Upstream: Mark Morgan <makk384$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-XML-Parser

Summary: Parse an XML message into a user-defined class structure
Name: perl-Class-XML-Parser
Version: 0.9
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-XML-Parser/

Source: http://search.cpan.org//CPAN/authors/id/M/MM/MMORGAN/Class-XML-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Parse an XML message into a user-defined class structure.

%prep
%setup -n %{real_name}-%{version}

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
%doc README
%doc %{_mandir}/man3/Class::XML::Parser*
%{perl_vendorlib}/Class/XML/Parser.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Initial package.
