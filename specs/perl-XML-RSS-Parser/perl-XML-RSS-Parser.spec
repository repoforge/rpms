# $Id$

# Authority: dries
# Upstream: Timothy Appnel <cpan$timeaoutloud,org>

%define real_name XML-RSS-Parser
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Parser for RSS formats
Name: perl-XML-RSS-Parser
Version: 2.15
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSS-Parser/

Source: http://www.cpan.org/modules/by-module/XML/XML-RSS-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
XML::RSS::Parser is an objected-oriented liberal parser for handling 
the morass of RSS formats in use.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/RSS/Parser.pm
%{perl_vendorlib}/XML/RSS/Parser/*

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Initial package.
